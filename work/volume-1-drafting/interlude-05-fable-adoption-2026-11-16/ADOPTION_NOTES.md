# Interlude 5 — Fable adoption and author chapter edits

**16 November 2026.** Canonical target: `manuscripts/volume-1/05-interlude.md`. Incoming: `/Users/samseatt/projects/book_poma/sam/claude/fable/interlude-5.md`, with the two SVGs under `assets/05-interlude/`. Incoming sources remain read-only. No publication.

Adopted the substantial revision in one pass. The former canonical interlude was an approximately 3,200-word draft with no source notes; Fable supplies roughly 7,100 words of main material, 42 notes and two figures. This is a substantive upgrade, not merely a few alterations to an already integrated version. The edited main text is about 7,220 words including captions and markers, a roughly 2% increase over incoming. Most of the larger total file is the incoming expansion, not this editorial pass.

## Preserved and recovered

The USC course sequence, visiting professor/exam/grade story, imagined ISI outpost, Marina joke, Arbib and Kosko accounts, brief parallel-computer class, three-part multimedia proposal, deferred implementation and departures remain. The entire class story is byte-for-byte preserved; the proposal section changes only the technical interpretation of the end-to-end principle. The ending and Maggie/Alex meditation are exact. All twelve incoming comments and all 42 reference identities survive. No personal episode was invented or shortened.

Recovered the older sentence about layers creating power, blindness and hiding places for bugs. Also recovered the Web/arrival coincidence in two sentences: browser and server working by the end of 1990, the year of arrival at USC. The old conflation with the 1992 riots does not return. The more substantial civic argument supersedes the older generic society/network parallels; optional old humor remains in `RECOVERY_NOTES.md` rather than being forced into the new account.

## Necessary technical repairs

- TCP numbers bytes; DNS follows delegation/referrals and caching; HOSTS.TXT was redistributed by FTP. OSI protocols were implemented, even though TCP/IP prevailed. F-16 redundancy refers to control channels, with variants distinguished in the note.
- Corrected 32,000/40 to an 800-fold throughput collapse. Qualified the simplified AIMD phase, random-walk model and wireless behavior without discarding their social analogies.
- Lamport's clocks respect a partial causal order. The Byzantine one-third threshold has model assumptions. FLP limits guaranteed termination, not the possibility of exact agreement; Paxos can maintain safety while awaiting progress. The Gödel flavor remains explicitly analogical.
- Distinguished tensor/pipeline parallelism and corrected ZeRO's state ownership. The full 16-byte partitioning belongs to the full-sharding stage; fetching another rank's optimizer state is not the mechanism.
- Ring traffic is `2(N−1)S/N` per rank: `1.5S` at four ranks and `1.75S` at eight, approaching `2S`. Total traffic and latency still grow. NVLink arithmetic uses aggregate outgoing bandwidth as an optimistic bound, not a promised ring-edge rate. Tail probability requires independent events.
- RDMA bypasses normal per-transfer CPU/kernel handling after memory/permissions setup. Flow control prevents buffer overflow, not all packet loss. Qualified fat-tree bandwidth, current hardware examples and tensor-parallel serving; included queueing in first-token latency.
- Kept the author's extreme endpoint-computation wager while distinguishing it from the end-to-end correctness principle. Kept Bob's proposal, adding that consensus itself need not be centralized and tightening the Ostrom/reciprocity support. S025 records open obligations rather than converting the wager into settled science.

`change-log.json` contains exact local changes and reasons. `reference-alignment.json` records incoming and updated notes. Study authors with direct conceptual, temporal or personal roles remain; Sam's mechanism-first preference is flexible, not a prohibition on names.

## Figures and references

Installed both supplied grayscale SVGs. Ring labels and alternative text now agree with the finite-rank formula. In the cluster figure, the 1.8 TB/s figure is explicitly bidirectional, the internet comparison says classic TCP, and the lower GPU row connects directly to NVLink switches instead of appearing to be daisy-chained through upper GPUs. Layout and overall graphic style are retained. Edited SVG derivatives omit stale embedded source signatures; the original signed source files remain untouched, with original and installed hashes recorded.

Both figures were rendered and inspected. Ring intermediate/final states and bandwidth, Amdahl and tail arithmetic were checked. The accompanying PNGs record the visual review. No third figure was needed.

Reviewed all 42 incoming source definitions, replaced vague or pending citations with specific sources, and added F-16 and Web notes for a total of 44. `SOURCE_AUDIT.md` distinguishes technical verification, metadata checks, reported quotations and personal testimony. Inherited “from memory” provenance comments stay, with a new audit comment explaining the completed checking. This is not a claim to have read every cited book in full or independently authenticated private memories.

## Reader value and later choices

This interlude now gives the reader an actual path from packets and congestion through causal ordering, consensus, distributed training and serving. It supplies prerequisites for Interlude 11 rather than only decorating networks with social analogies. The class account doubles as a memorable model of congestion, retransmission and directories; the proposal explains why meaning, bandwidth and endpoint computation matter. Bob offers a consequential design question: which shared commitments enable pluralism rather than merely suppress it?

No essential old personal account was lost. The draft is long because it adds substantial mechanisms and autobiography; a future length pass can assess the long parallelism/fabric section against Interlude 11, without automatically cutting the proposal or reverting to superficial coverage. No major cut or speculative-topic replacement was made here. An optional new Dijkstra/Fokker connection is saved in the recovery drawer, not inserted.

## Chapters 3 and 4

Reviewed and included Sam's existing uncommitted changes exactly as supplied. Chapter 3 refines first sensation/registration and the poetic entry into the brain's domain, while retaining the explicit prenatal-wiring qualification. Chapter 4 refines the room arrival and restores the wolf poster/dartboard recollection and silicon-chip wording. These are author testimony and voice refinements; no new scientific correction was necessary. Neither file was rewritten. Both active checksums were refreshed.

The separate dirty `04-interlude.md` is outside this request and remains unchanged and uncommitted. Publishing files and the read-only source tree are untouched.
