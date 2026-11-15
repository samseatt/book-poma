import importlib.util
import unittest
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "scripts" / "build-print.py"
SPEC = importlib.util.spec_from_file_location("build_print", SCRIPT)
build_print = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(build_print)


class ProloguePrintTransformTests(unittest.TestCase):
    def generated(self, body):
        return (
            build_print.MARKER
            + "\n\n# Prologue {.unnumbered}\n\n"
            + "::: {.chapter-opening}\n\n![](assets/prologue/image-01.png)\n\n:::\n\n"
            + body
        )

    def test_current_single_blockquote_epigraph(self):
        source = self.generated(
            "> *Wo aber Gefahr ist.*\n"
            "> *(Yet where danger is.)*\n"
            "> --- Holderlin\n\n"
            "Opening scene.\n\n{{< pagebreak >}}\n\nReveal."
        )
        result = build_print.transform_prologue(source, Path("prologue.qmd"))
        self.assertIn("\\begin{pomaepigraph}", result)
        self.assertIn("{{< pagebreak >}}", result)
        self.assertLess(result.index("Opening scene."), result.index("{{< pagebreak >}}"))
        self.assertLess(result.index("{{< pagebreak >}}"), result.index("Reveal."))

    def test_incoming_comment_and_three_block_epigraph(self):
        comment = "<!-- AI-assisted: invisible provenance -->"
        source = self.generated(
            comment
            + "\n\n*Wo aber Gefahr ist.*\n\n"
            + "*(Yet where danger is.)*\n\n"
            + "> --- Holderlin\n\n"
            + "The basket was still there.\n\n"
            + "{{< pagebreak >}}\n\n"
            + "That boy was me."
        )
        result = build_print.transform_prologue(source, Path("prologue.qmd"))
        self.assertIn(comment, result)
        self.assertIn("*Wo aber Gefahr ist.*", result)
        self.assertIn("*(Yet where danger is.)*", result)
        self.assertIn("--- Holderlin", result)
        self.assertEqual(result.count("\\begin{pomaepigraph}"), 1)
        self.assertIn("The basket was still there.\n\n{{< pagebreak >}}\n\nThat boy was me.", result)

    def test_missing_epigraph_still_fails_clearly(self):
        with self.assertRaisesRegex(SystemExit, "Print Prologue epigraph not recognized"):
            build_print.transform_prologue(
                self.generated("Ordinary body without an epigraph."), Path("prologue.qmd")
            )


if __name__ == "__main__":
    unittest.main()
