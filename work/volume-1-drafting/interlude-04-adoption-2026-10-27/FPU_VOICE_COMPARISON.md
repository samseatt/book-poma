# FPU prose: author source, editorial condensation and local repair

27 October 2026. The text in the `claude` folder is **author material with drafting assistance**, not a reliable attribution of individual sentences to Claude. Its filename does not establish authorship. This comparison does not use an AI detector or infer who wrote which line.

## Editorial judgment

The author's preference has concrete textual support. The incoming scene supplies an embodied narrator, a small dramatic sequence and humor that changes the meaning of technical words. The editorial condensation gives a lucid summary of the facts and lessons but removes much of the encounter through which the reader would discover them. This is a mismatch with the vignette's job, not evidence that technical precision itself is bland or that every original sentence is better.

| Aspect | Original author source | Editorial condensation | Effect |
|---|---|---|---|
| The narrator enters | Battery/tongue image; the transcript laminated, framed and hung above the bench | “I enrolled…”; a roster; “and me” | The shorter version reports the setup but removes the physical comic image and the narrator's disproportionate self-consciousness. |
| The demonstration | “But for reasons historians will never explain…” followed by the remembered compliance speech | “I opened with its departure from the standard.” | A performed scene becomes a summary. The joke admits mixed motives instead of explaining them all in advance. |
| Technical vocabulary as humor | “round off the rounding error itself” | “someone else's unexamined assumption” | Both convey a concern, but only the first makes the domain language perform the joke. The second belongs naturally in technical explanation. |
| Movement into software | “cheap cosmic expansion in time”; the softer basket of loops and recursion | Registers/control/latency tradeoff followed by a direct explanation of processor reuse | The technical account is useful, but the full replacement spends the vignette's emotional momentum on instruction. A small repair or note can supply that precision. |

The condensation has a usable new line—“Four months of wiring, and I led with the asterisk”—and makes latency easier to understand. Those successes do not compensate for replacing the original's dramatic structure. That line remains optional, not reinserted in this pass.

The original still has issues: the opening's double-colon construction is awkward; a few judgments overstate what tests establish; the professor's “trivial issue” framing contradicts the author's later clarification; and the hardware/software distinction needs a literal boundary. These are local repair targets. They do not justify erasing the scene, its self-deprecation or its wordplay. The public-speaking interpretation remains tentative (“Perhaps”); the author may later decide whether it belongs beside his stated professional reason for disclosure.

## Local corrections now applied

- Correct course name and add **Engineering Precision Computer (EPC)**.
- Explain the four ticks as CPU waiting for one FPU pass, without adding a circuit-design lesson.
- Present IEEE compliance as the author's aim, not externally established certification; acknowledge that the assignment did not require it.
- Replace test cases as proof with the observed results of those cases.
- Replace the “trivial issue” characterization with the author's stated respect for the professor's interest and his own obligation to qualify the claim.
- Preserve the entire hardware/software comic passage and closing. A single note distinguishes revisable software, sequential hardware and the metaphorical “symmetry breakings.”

Seven bounded replacements, including the note anchor. No paragraph was reordered or replaced wholesale. The display speech, transcript joke, rounding wordplay, lawyers, cosmic expansion, basket and final cadence remain. No new memoir incident or dialogue was invented. The factual repairs rely on the author's corrections and sources already checked during adoption; this is not new research or a claim to have recovered the original circuit report.

## Full original from the author’s holding-pen draft

Source: `/Users/samseatt/projects/book_poma/sam/claude/interlude-4.md`.

### Will It Float?

Against the advice of my undergraduate peers, I marched into Professor Kime's digital engineering lab, the way any ten-year-old engineer sticks his tongue on a battery: a room of five people: three terrifyingly smart graduate students, one undergraduate with one of those faces stamped with the word *genius*, and one defiant undergraduate who still believed sleep was optional.

If imposter syndrome were a transcript, I had it laminated, framed and hung above my lab bench. The course had a single project that semester (most students at that large university knew better than to attempt it), and the five of us spent four months building a processor on a huge breadboard. The project split in two. One half was everything a processor needs: the arithmetic unit, pipeline, registers, memory, and a custom instruction set with its own little assembler. The other half was the machine's signature feature, its floating-point unit. That was mine, shared with a graduate student who split his time between the two halves. Everything custom-wired. Everything powered by stubbornness, caffeine and the belief that youth is permanent.

The design ran in a single pass: no multi-step routines, just four lightning-fast ticks for even the worst-case operation. It was even compliant with the standard for floating-point arithmetic, IEEE 754, except for one microscopic rounding detail I implemented "differently," because I stubbornly wanted it to fit in that single pass. Given the constraint, it was the only card I could play, and it was elegant: unlike anything else. I had the test cases to prove the output was correct.

Demo day arrived. The FPU was formally my baby, so I was the one asked to present it. I had custom-wired a single-pass, four-tick computing monster, a feat that should have earned a victory lap. But for reasons historians will never explain, I stood before the room and opened with: "This FPU fully complies with IEEE 754... except for a rounding corner."

Perhaps a safe, reductionist debate over an edge case was psychologically soothing compared with the terrifying theater of public speaking. My subconscious apparently decided that defending one minor flaw was infinitely easier than listing my accomplishments. I was genuinely surprised by the professor's interest in that single, trivial issue. But the moment he left the room, my FPU partner was livid. He would simply have built a working unit and never mentioned the standard at all. The problem wasn't the rounding error; it was my unwillingness to round off the rounding error itself. There is a limit even to a detail. Reductionism of any kind will eventually circle back behind your face.

That day I learned two truths. First, psychology always matters: never volunteer your sins unless a lawyer advises it. Even the most rational of minds needs psychology to flow. Second, software matters even more. Hardware is a stubborn, brittle animal. It does exactly what you told it to, even when what you told it to do was stupid. Software can apologize. A hardwired circuit admits a mistake once; a program can say, "Let me try that again," and actually mean it. Better still, software buys you a cheap cosmic expansion in time, cycling through the same hardware again and again: the same circuit, with little symmetry breakings the size of an instruction set.

My engineering eggs deserved a softer basket, one made of loops, recursion, revisions and second chances. I chose software. Not because it was easier, but because it could forgive.

## Full editorial condensation being compared

Source: canonical I4 at commit `10a8824`. This version is retained only for comparison and is not the current manuscript.

### Will It Float?

Against the advice of my undergraduate peers, I enrolled in Professor Kime's Digital Design Lab. There were five of us: three terrifyingly smart graduate students, one undergraduate whose face seemed stamped with *genius*, and me.

Over four months, we built the Engineering Precision Computer, or EPC, across a joined expanse of breadboards. The name was a little more generous than the register width. I took on its floating-point unit (FPU), sharing the work with a graduate student who also helped with the rest of the processor. We used chips, erasable programmable logic devices (EPLDs) and physical wires. Lots of wires.

My FPU did its arithmetic in one pass. As I remember it, the CPU waited about four clock ticks for the slowest operation to settle. Those ticks were latency, not four trips through the arithmetic. Single pass was the feature. I had put considerable wiring behind that adjective.

Floating-point arithmetic has to squeeze results into a finite number of digits. IEEE 754, first published in that same year as Windows and the C++ book, specified how that rounding should work. I had handled one part differently.

Compliance wasn't required for the assignment, and the examples I'd checked came out correctly. Still, when the professor asked me to present my FPU, I opened with its departure from the standard. He was interested in what I had built; I wanted him to know exactly what I was claiming. My partner thought I could have started with the achievement. Four months of wiring, and I led with the asterisk.

Even a teaching machine was enough to show me how a small exception could become someone else's unexamined assumption. But the more useful discovery was what another step might have bought. Reusing a smaller arithmetic path across several cycles could have spared wiring and left room for the awkward rounding logic, at the cost of registers, control and possibly more waiting. A different bargain, with its own engineering bill.

Software takes that bargain much further. A processor reuses its arithmetic unit, stores a result, and returns with new operands. A loop gives a finite patch of circuitry a succession of jobs. Instead of stretching the wiring to contain the entire calculation at once, we stretch the execution through time. Hardware already has clocks, state and sequential circuits; software lets us organize their repeated use into computations far larger than any one pass.

My engineering eggs deserved a softer basket, one made of loops, recursion, revisions and second chances. I chose software. I would soon discover how effectively it could refuse to forgive.

Footnote markers are omitted from the displayed passages. Their source records remain in the canonical interlude and adoption audit; this working comparison is outside publication.
