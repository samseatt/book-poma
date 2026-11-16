# Interlude 4 — preservation notes

No author decision is pending. The FPU and closing are unchanged. The old automatic-differentiation explanation and calculus joke, and the shared-address-space distinction, are restored in the merged manuscript. Other condensation is accepted without rewriting the personal material.

Fable’s protected comment names `04-interlude-before-2026-11-15.md`, which was not found in the incoming folder. Rather than silently change the comment, the complete previous Bob section is preserved below, also recoverable from baseline commit `adb85e7511d52669f6aa77a53926352023f04709`. Its longer thermodynamic explanation is now chiefly carried by Interlude 1; no claim has been discarded solely for being speculative.

## Previous canonical Bob section

## Bob, Through the Looking-Glass: A Past the Machine Must Live With

*The twist, in one line: perhaps a silicon psychology would depend on how a system carries, spends and revises its past, as much as on what its next calculation can accomplish.*

<!-- AI draft: author-authorized replacement of Bob, with thermodynamic footing and an open temporal-organization conjecture. -->
My FPU used time to let a calculation settle. Patrick's assignment used time to let several calculations cooperate. An agent uses time to return to a world its previous action may have changed. There is something worth separating here: the time that passes through a machine, and the history the machine can carry forward.

The clock keeps ticking through a deadlock. A processor can become very warm while achieving absolutely nothing, a condition I had already met in higher education. So elapsed time, energy consumption and meaningful progress cannot be the same quantity. Nor does adding more code automatically add thermodynamic entropy. A software project's complexity and a physical system's entropy require different accounts.

There is nevertheless a physical bill. Landauer's principle connects the loss of information in a physical memory to heat: resetting an initially unknown, equally likely bit to a standard value, in the usual isothermal setting, has a minimum average heat cost of $k_{\mathrm B}T\ln 2$. Here $T$ is the reservoir's absolute temperature. The memory loses one bit of uncertainty; the surroundings receive compensating entropy. Actual computers usually dissipate much more. This is not a fee charged for every clock tick or every logical operation.[^v1-i4-landauer]

Bennett showed how computation can, in principle, preserve the information needed to reverse its logical steps, copy out a result, and uncompute the temporary work. Calculation need not continually destroy its own trail.[^v1-i4-bennett] A real machine's running costs remain; logical reversibility is not a promise that an ordinary processor runs without heat. Nor is the heat exported during ideal erasure identical to net entropy production of the whole apparatus and reservoir, which can approach zero in the reversible limit.[^v1-i4-thermo]

That makes the biological comparison more interesting to me. A living system maintains organization through physical exchanges; an operating computer does too. But a program needn't become more ordered, more intelligent or more conscious merely because its power supply pays the bill. To ask about a silicon psychology, I would start with a different accounting: what must the system retain so that its future actions remain answerable to its past?

I wonder whether the important boundary is a *managed continuity*: a system that must decide which observations survive, which commitments remain binding and which old interpretation deserves revision, while the consequences of earlier actions keep arriving. A fixed model called afresh for every request can be immensely capable. A persistent system using the same model may have a different problem altogether: it has to live with the sequence. Memory capacity alone doesn't settle how that sequence acquires authority over its next move.

We could investigate that without declaring a machine conscious. Hold the model and computational budget fixed, then vary how its surrounding software preserves history, orders actions and permits revision. Interrupt it, delay consequences, restore an earlier state, or give it evidence that contradicts its own record. Look for sustained commitments that remain corrigible, rather than mere repetition or persuasive explanations after the fact. The hypothesis worth pursuing is whether coherent agency depends on this organization of time in ways that a stronger model, queried without that organization, cannot cheaply substitute for. Context and memory already affect performance; the harder question is what arrangement lets a system govern the continuity itself.

Nothing here establishes felt experience. It does give the builder something more demanding to attempt than attaching a personality prompt. Patrick's last lock returns with a less comfortable question: which parts of the past are keeping the machine coherent, and which are simply keeping it waiting?

## Author clarification — deliberate condensation, 15 November 2026

The author confirms that the forward/backward walkthrough was removed intentionally because Interlude 2 already covers it. The editor’s restoration of automatic differentiation and the calculus joke has therefore been removed. The preceding recommendation to recover that passage is superseded. The incoming cross-reference and training-cost discussion are joined again, and the autograd marker returns to the incoming backpropagation/optimizer sentence. No reference definition, figure, personal scene, Bob conjecture or closing changes. Compiler/OS condensation and the shorter thermodynamics callback remain as intended. B-054 records the standing merge lesson. See `trim-followup.json` and `trim-followup-validation.json` for this correction; the original audit and validation remain historical.
