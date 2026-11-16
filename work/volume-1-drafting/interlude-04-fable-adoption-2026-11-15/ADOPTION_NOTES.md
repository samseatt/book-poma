# Interlude 4 — Fable adoption, 15 November 2026

Adopted `fable/04-interlude.md` as canonical *Soft Logic — The Art of Software*. The source folder remains read-only. No publication.

## What changed and why it matters

Fable’s larger revision moves beyond “software is code” to the machinery that makes ML possible: data preparation and leakage, CPU/GPU dispatch, kernel fusion, automatic differentiation and training cost, optimizer/activation memory, checkpointing, reproducibility, lifecycle/drift, feedback, serving and speculative decoding. It builds usefully on Interludes 2–3 and prepares Interlude 11 without taking over its account of intelligence and model architecture. The increased length carries mechanisms and examples; no broad compression pass was imposed.

Both supplied diagrams were rendered, visually inspected and checked against their arithmetic. They are copied unchanged. The captions distinguish weight storage from whole-process memory and ideal roofline ceilings from measured throughput. The earlier semaphore and training/serving diagrams remain unchanged: four instructional figures total.

## Protected writing and recovery

The FPU scene is byte-for-byte unchanged, as are “Lines of Flight,” the boombox instruction and the Maggie/Alex closing. Personal narration, humor, Windows/C++ timing, signature terms, headings and every comment from both versions survive. Fable’s small opening edits remain. No new private detail was introduced.

Recovered the old automatic-differentiation mechanism and its calculus joke before training-cost arithmetic; restored the shared-address-space distinction for threads. No other essential old passage needs reinstating. The longer prior thermodynamics/Bob section is retained in RECOVERY_NOTES.md, resolving the provenance behind Fable’s comment naming an unavailable local backup. Bob’s managed-continuity proposal remains fully alive, with S023 recording the research obligations rather than replacing the wager with settled doctrine.

## Local repairs

The exact before/after record is in change-log.json (A: factual errors; B: precision/recovery; preservation: marker retention). No wholesale style or thesis rewrite was applied. Important repairs:

- Self-hosting is not asserted of most compilers; the hair-pulling story is sourced to Bürger’s actual passage.
- Shuffling does not guarantee a fair sample, pinning alone does not guarantee transfer overlap, CUDA execution presumes an NVIDIA device, and fusion speedups depend on workload.
- The 6ND formula is scoped to the dominant dense-transformer work. MFU counts useful model arithmetic, not hardware busy time. Adam’s statistics, the 16-byte configuration and 54-day reliability window are stated accurately.
- Inference memory includes activations/cache/metadata beyond weights. KV cache means earlier keys and values. Single-user decode arithmetic is explicitly an ideal ceiling under stated assumptions.
- Speculative decoding preserves a distribution through acceptance ratios and corrected rejection sampling, not by comparing with a hypothetical token the large model “would have” sampled.
- Drift can be abrupt; a frozen model does not automatically acquire later events but can still infer or receive new information. Recursive-data experiments are not all pure replacement. The informational-gravity reading remains.
- The Landauer bound retains its already documented equiprobable-bit condition in the sentence itself.

## References and validation

Verified the 19 incoming new source notes and checked the three expanded older notes. Added one primary-source roofline/bandwidth note at the numerical claim. Inherited references retain their previous verification scope; source-audit.json identifies abstracts, full-text passages, same-day reused evidence and access limitations honestly. No verification placeholder remains. The chapter now has 49 footnotes.

The active manuscript checksum is updated. The manuscript validator checks footnotes/backlinks, local assets, headings, math and the manifest; results are in validation.json after installation. Figure/arithmetic checks and protected-text hashes are recorded alongside it. No source artifact, publisher file or unrelated manuscript was changed.

## Author clarification — deliberate condensation, 15 November 2026

The author confirms that the forward/backward walkthrough was removed intentionally because Interlude 2 already covers it. The editor’s restoration of automatic differentiation and the calculus joke has therefore been removed. The preceding recommendation to recover that passage is superseded. The incoming cross-reference and training-cost discussion are joined again, and the autograd marker returns to the incoming backpropagation/optimizer sentence. No reference definition, figure, personal scene, Bob conjecture or closing changes. Compiler/OS condensation and the shorter thermodynamics callback remain as intended. B-054 records the standing merge lesson. See `trim-followup.json` and `trim-followup-validation.json` for this correction; the original audit and validation remain historical.
