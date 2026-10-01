import hashlib
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "scripts" / "sync-manuscripts.py"
SPEC = importlib.util.spec_from_file_location("sync_manuscripts", SCRIPT)
sync_manuscripts = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(sync_manuscripts)


class AnnotationOmissionTests(unittest.TestCase):
    def clean(self, text):
        return sync_manuscripts.omit_annotations(text, "fixture.md")

    def test_inline_spacing_and_punctuation(self):
        self.assertEqual(self.clean("one [[NOTE: x]] two"), ("one two", 1))
        self.assertEqual(self.clean("one [[x]], two"), ("one, two", 1))
        self.assertEqual(self.clean("one[[x]]two"), ("one two", 1))

    def test_standalone_and_multiline_paragraphs(self):
        source = "before\n\n[[NOTE: first\n\nsecond]]\n\nafter\n"
        self.assertEqual(self.clean(source), ("before\n\nafter\n", 1))

    def test_adjacent_escaped_legacy_and_unknown_forms(self):
        source = r"one [[ADD: a]][[<legacy>]] \[\[FUTURE: c\]\] two"
        self.assertEqual(self.clean(source), ("one two", 3))

    def test_unrelated_markdown_structure_is_preserved(self):
        source = (
            "- item [[NOTE: omit]] here  \n"
            "  continuation\n\n"
            "| A | B |\n| - | - |\n| 1 | [[omit]]2 |\n"
        )
        expected = (
            "- item here  \n"
            "  continuation\n\n"
            "| A | B |\n| - | - |\n| 1 | 2 |\n"
        )
        self.assertEqual(self.clean(source), (expected, 2))

    def test_hard_break_and_paragraph_boundary_spacing(self):
        self.assertEqual(
            self.clean("one [[NOTE: x]]  \nnext\n"),
            ("one  \nnext\n", 1),
        )
        self.assertEqual(
            self.clean("one [[NOTE: x]]\n\nnext\n"),
            ("one\n\nnext\n", 1),
        )

    def test_note_only_structural_lines_are_removed(self):
        source = (
            "- first\n"
            "- [[NOTE: remove this item]]\n"
            "- third\n\n"
            "## [[NOTE: remove this heading]]\n\n"
            "> [[NOTE: remove this quote]]\n"
        )
        self.assertEqual(self.clean(source), ("- first\n- third\n", 3))

    def test_malformed_annotations_report_source_and_location(self):
        cases = {
            "unclosed": "text [[NOTE: x",
            "unmatched": "text ]] end",
            "nested": "text [[NOTE: [[inner]] outer]]",
            "mismatched": r"text [[NOTE: x\]\]",
        }
        for label, source in cases.items():
            with self.subTest(label=label):
                with self.assertRaisesRegex(
                    sync_manuscripts.AnnotationError, r"fixture\.md:1:\d+:"
                ):
                    self.clean(source)

    def test_bad_preflight_preserves_existing_generated_output(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "source.md"
            source.write_text("text [[unclosed")
            manifest = root / "manifest.json"
            manifest.write_text(
                json.dumps(
                    {
                        "documents": [
                            {
                                "unit_id": "fixture",
                                "kind": "front-matter",
                                "active_source": {"path": str(source)},
                            }
                        ]
                    }
                )
            )
            content = root / "content"
            content.mkdir()
            sentinel = content / "existing.txt"
            sentinel.write_text("keep this build")
            output_manifest = root / "content-manifest.json"
            output_manifest.write_text("keep this manifest")
            before = hashlib.sha256(sentinel.read_bytes()).hexdigest()

            with self.assertRaises(sync_manuscripts.AnnotationError):
                sync_manuscripts.sync(
                    manifest_path=manifest,
                    content_dir=content,
                    manifest_output=output_manifest,
                    expected_count=1,
                    asset_root=root / "assets",
                )

            self.assertEqual(hashlib.sha256(sentinel.read_bytes()).hexdigest(), before)
            self.assertEqual(output_manifest.read_text(), "keep this manifest")


if __name__ == "__main__":
    unittest.main()
