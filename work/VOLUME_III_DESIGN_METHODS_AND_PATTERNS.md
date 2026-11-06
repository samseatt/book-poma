# Volume III: design methods and builder patterns

> **Status update, 6 November 2026:** retain this document as planning provenance and, where applicable, the opportunity-signal/Next Move mapping. For the methods actually present after the substantive V3 pass, use [the reconciled principles and patterns](VOLUME_III_PRINCIPLES_AND_PATTERNS.md) and [completion record](volume-3-drafting/whole-volume-reconciliation-2026-11-06.md). Older proposed scopes or unimplemented-status statements below do not override them.

4 October 2026. Correction and technical extension to [the design inventory](VOLUME_III_DESIGN_MAP.md), following the author's challenge to its classification. Sources: canonical Chapters/Interludes 23–33 at revision `e0cd466`, the preceding content review, and the primary references linked below. **Proposed editorial additions; no manuscript rewrite.**

## What the earlier assessment omitted

The preceding report was useful as a map of concerns, requirements, safeguards, and mechanisms. It did not adequately supply the transferable design knowledge the author asked for. Calling a desirable outcome a principle, or a list of features a set of primitives, obscured that gap. The correction is substantive: the reader should learn how to frame a problem, generate alternatives, allocate functions, reason about interactions, build a solution, and evaluate what it actually does.

The author has clarified that both indirect design values and direct technical principles are important. Preserve the first list as a complementary layer. Some ethical commitments are legitimately normative design principles; they do not by themselves supply the whole design spine. Nor does attaching a famous pattern name to them complete the work. Each selected method or pattern needs an intelligible problem, its reasoning or structure, an application, a tradeoff, and evidence by which the result can be judged.

This document supplies the missing technical layer. The original opportunity-signal mapping and proposed Next Moves remain useful; they must now connect through this layer. It also corrects the earlier division of labor: **chapters teach design reasoning, including technical reasoning; interludes teach construction, experimentation, and operation.** Neither is confined to sentiment, and neither has to become a software manual.

## A vocabulary that keeps the layers distinct

| Layer | What it supplies | Justice example |
|---|---|---|
| Purpose or value | The human condition the design should improve. | A mistaken classification should not destroy a person's livelihood. |
| Requirement or constraint | A capability, boundary, or performance condition the solution must meet. | A consequential denial must be challengeable through an accessible route. |
| Design principle | A reusable reason for preferring some structures over others, with a stated scope. | Separate making a decision from independently reviewing it; keep policy changeable without rebuilding the whole service. |
| Analysis/design method | A disciplined way to derive, compare, or refine alternatives. | Model the decision rules, trace their authority, and compare review arrangements against explicit criteria. |
| Architecture or design pattern | A recurring solution structure for a recurring problem, with consequences. | A stateful case workflow coordinating independent review, with versioned rules and durable decision records. Not every useful workflow is a named catalog pattern. |
| Primitive | A smaller object or operation from which a mechanism can be assembled. | Case identifier, evidence reference, rule version, authorized state transition. |
| Development/operating practice | How builders produce, integrate, assess, and maintain the system. | Contract tests, adverse-case tests, controlled releases, incident analysis. |
| Acceptance evidence | What demonstrates that the particular implementation works adequately. | A disputed denial is reconstructed, reviewed, corrected, and propagated without losing the case or requiring the claimant to coordinate agencies. |

“Track provenance” is a requirement until we specify the provenance model, recording points, identities, correction rules, queries, and tests. Explainability is a quality with several design dimensions. Repeatability is a property supported by an experimental and configuration practice. Adapter is a named structural pattern. Abstract Factory is a named creational pattern. These belong together in the builder spine, under their proper types.

## Designer and builder: a useful emphasis, not a rigid border

The author's further clarification makes the working intention more specific. **Chapters principally offer principles and reasoning for designing civilization. Interludes principally offer methodologies, patterns, and practices for building the systems through which that civilization operates—including its Silicon side.** This remains a provisional editorial distinction, chosen for usefulness rather than taxonomy.

A chapter can therefore examine institutional boundaries, allocation, learning, belonging, public authority, and relations between people and machines. Its technical methods earn their place by helping the reader choose a civilizational arrangement. An interlude can construct, test, operate, and revise the enabling systems: software, organizations, care workflows, fabrication processes, or experiments. “Builder” is not limited to programmer, and “designer” is not limited to philosopher.

Use the local teaching question to decide placement. A pattern may illuminate a chapter's architectural choice; an interlude may need to reopen a value question when implementation reveals a conflict. Retain that useful overlap. If a proposed item below becomes a digression at its assigned location, move its full explanation to the paired piece and preserve the conceptual connection. The labels are aids to precision, not a rule that overrides the book's argument.

## The common method: establish it in Theta, exercise it in the pairs

Use a light, recurring design discipline, not eleven copies of a methodology chapter:

1. Establish the need and context, including people affected without becoming direct users.
2. Describe the current arrangement and the desired change; separate ends from an initially preferred technology.
3. Model relevant functions, information, authority, resources, interfaces, and failure paths.
4. Develop credible alternatives, including a simpler arrangement or improvement to an existing institution.
5. Compare alternatives against explicit criteria and constraints; record conflicts and assumptions.
6. Allocate responsibilities and capabilities, implement an appropriate experiment, and evaluate outcomes.
7. Revise the design, its assumptions, or the problem framing when experience contradicts them.

This is an editorial synthesis drawing on [IIBA's business-analysis tasks](https://www.iiba.org/knowledgehub/business-analysis-standard/4-tasks-and-knowledge-areas/introducing-business-analysis-tasks/), [NASA's systems-engineering account](https://www.nasa.gov/reference/2-0-fundamentals-of-systems-engineering/), and [NASA's decision-analysis method](https://www.nasa.gov/reference/6-8-decision-analysis/). It is not presented as a new official methodology or a verbatim BABOK procedure. IIBA's public material supports the task families and technique names; this review does not claim a complete reading of access-restricted BABOK content.

Across that loop, use requirements traceability to connect a need to a design decision and its evaluation. Distinguish **verification** against specified requirements from **validation** against intended use and stakeholder needs. Add quality-attribute scenarios: under a particular stimulus and operating condition, what response is required, and how will it be assessed? [SEI's Quality Attribute Workshop](https://insights.sei.cmu.edu/library/quality-attribute-workshop-collection/) helps elicit such concerns before choosing architecture; [ATAM](https://insights.sei.cmu.edu/library/architecture-tradeoff-analysis-method-collection/) examines tradeoffs in candidate architectures. Do not describe a short book exercise as a completed formal ATAM evaluation.

The purposes and legitimate authorities of a civilization remain contestable. An engineering score cannot decide whose rights count. These methods make assumptions and consequences inspectable; they do not turn politics into an optimization problem with a uniquely correct answer.

## Reading the proposed additions

**P** = design principle; **M** = analysis/design method; **A** = architectural approach or model; **DP** = named design/integration pattern; **E** = development or operating practice. The placement and examples are editorial proposals, not endorsements by the cited authors. Ordinary proposed mechanisms are described as such rather than given invented catalog status.

The following are candidates for the working lists, not a requirement to insert every term. Give each pair one or two sustained technical demonstrations and use the other candidates where they materially improve the argument. The named-method scan in the audit found none of the selected explicit labels in the 22 drafts; related ideas such as provenance, interfaces, validation, and failure modes already occur. Keyword absence is not proof of conceptual absence. Develop the existing ideas rather than pretending to introduce them all from nothing.

<a id="pair-23"></a>

## 23 — Renewal: composing a service across boundaries

### Chapter design spine

- **M — Functional decomposition and allocation.** Start with what a need requires—recognition, qualification, matching, acceptance, delivery, follow-up—then decide what belongs to a person, group, institution, or tool. This makes “institutions to flows” a design operation. [NASA's logical decomposition](https://www.nasa.gov/reference/4-3-logical-decomposition/) supplies the method; the civic allocation is our proposed application.
- **P — Modularity through information hiding.** Group decisions likely to change behind stable interfaces, rather than merely drawing a box around every present department. [Parnas's original argument](https://www.cs.lafayette.edu/~gexia/cs301/resources/parnas.html) gives the reader a reason one composition will be easier to change than another. A clinic's internal system should not determine how every neighbor asks for a ride.
- **M — Process and interface analysis.** Trace the actual request across organizational boundaries, including waits, duplicated entry, unowned work, and exceptions. Compare what the person experiences with the work needed behind it. The artifact is a process/interface map, not another list of stakeholder virtues.
- **P — Decouple coordination from provision.** A proposed architectural principle for this book: routing a request does not create the skill, stock, time, or authority to fulfill it. State the resource assumption at each handoff. This is a synthesis, not a named law from Parnas or BABOK.

### Interlude builder spine

- **A/DP — Ports and Adapters; Adapter.** Define the core service's operations independently of a particular clinic API, phone interface, or municipal database. Adapters translate external representations into those operations. [Cockburn's architecture](https://alistair.cockburn.us/hexagonal-architecture) is the architectural treatment; the smaller object-level Adapter pattern is related but not identical.
- **A — Explicit workflow/state model.** Represent offered, accepted, in progress, completed, declined, expired, and returned work; define valid transitions and who may trigger them. This makes a handoff implementable and inspectable without claiming the state diagram captures the whole human encounter.
- **DP/E — Idempotent Receiver and retry tests.** A repeated delivery message must not create two rides or pay a helper twice. The [integration pattern](https://www.enterpriseintegrationpatterns.com/patterns/messaging/IdempotentReceiver.html) addresses duplicate processing. Define the identity of the operation; it is not enough to compare two similar messages.
- **E — Contract testing and a thin working service.** Verify each adapter against the same externally observable obligations, then exercise one useful request from start to finish. Test timeouts and refusal as well as success.

**Worked demonstration:** a translation request moves from a phone call through a digital coordinator into an existing clinic. Replace the coordinator's vendor without changing the service promise. **Tradeoff:** a stable common interface can simplify integration while concealing important local distinctions; preserve explicit exceptions rather than forcing every need into one card.

<a id="pair-24"></a>

## 24 — Agency: designing a useful delegation boundary

### Chapter design spine

- **P — Least privilege and separation of privilege.** Give an agent the authority required for its task, with separate authorization for distinct consequential actions. [Saltzer and Schroeder](https://www.mit.edu/~Saltzer/publications/protection/index.html) supply established protection principles. Their extension to institutional roles needs separate political justification; a citizen is not a computer account.
- **P/M — Human control, intelligibility, and recoverability.** Use interface design to expose what assistance can do, permit correction, and make limits discoverable. The [Human–AI Interaction guidelines](https://www.microsoft.com/en-us/haxtoolkit/ai-guidelines/) turn “agency” into interaction choices across initial use, errors, and changing behavior.
- **M — Roles/permissions and scenario analysis.** Model who may propose, authorize, execute, inspect, revoke, and contest each action. Test ordinary use and boundary cases: changed capacity, emergency, household conflict, and a delegated agent trying to delegate again.
- **P — Encapsulate changeable policy.** Keep a person's preferences, an institution's mandatory rules, the provider's commercial objectives, and execution mechanics distinguishable. Changing one should not silently rewrite the others. This gives practical content to the right to outgrow a model.

### Interlude builder spine

- **A — Policy decision and enforcement separation.** Specify where a request is evaluated and where the permission is actually enforced. [NIST's ABAC model](https://csrc.nist.gov/pubs/sp/800/162/upd2/final) is one established option: evaluate relevant subject, object, action, and context attributes. A consent screen alone is not enforcement.
- **DP — Strategy.** Place genuinely interchangeable decision procedures behind a common contract—for example, alternative scheduling strategies. Do not let a change of strategy alter the permitted action space. The pattern is a means of varying behavior, not a claim that all human judgments are interchangeable algorithms. See the [GoF pattern collection](https://www.informit.com/store/design-patterns-elements-of-reusable-object-oriented-software-9780201633610).
- **E — Authorization and revocation tests.** Exercise permission boundaries, expiry, stale credentials, nested delegation, and attempted bypasses. Confirm what revocation prevents and what already-completed actions require separate repair.
- **E — Usability tests under realistic burden.** Ask whether a tired person can understand, alter, or withdraw an important delegation. Count assistance required and meaningful mistakes, not merely whether the menu exists.

**Worked demonstration:** an assistant can arrange transport and reserve an appointment, but a change in treatment has a different authority path. **Tradeoff:** frequent confirmation can destroy useful assistance; use consequence-sensitive boundaries rather than prompting for everything.

<a id="pair-25"></a>

## 25 — Economy: designing allocation rather than decorating accounting

### Chapter design spine

- **M — Mechanism design and incentive analysis.** Begin with desired allocation and participation conditions; examine how rules work when participants know different things and respond strategically. This is a substantive design field, not a synonym for building a platform. [The Nobel account of mechanism design](https://www.nobelprize.org/prizes/economic-sciences/2007/9272-the-sveriges-riksbank-prize-in-economic-sciences-in-memory-of-alfred-nobel-for-2007/) anchors the distinction. A humane system must also consider motives beyond stylized economic self-interest.
- **M — Stock/flow and entitlement modelling.** Separate an observed contribution, a monetary claim, a reservation, stock on hand, and an actual service delivered. Define conservation and reconciliation rules for each. The ledger becomes an explicit model of a selected economic arrangement rather than a metaphor for value itself.
- **M — Alternatives and sensitivity analysis.** Compare a contribution-credit proposal with cash, ordinary public provision, shared ownership, and combinations. Vary shortage, participation, administration cost, and the assumed automation gain. Expose whose valuation determines the ranking.
- **P — Separate measurement from entitlement.** Proposed book-specific principle: recognizing useful work should not automatically make access to necessities conditional on being measured. Specify how the protected provision floor is funded and what remains an allocative choice.

### Interlude builder spine

- **A/E — Accounting invariants and atomic local transactions.** Choose an accounting model, identify valid state changes, and reject updates that violate its balance or reservation constraints. Double-entry is appropriate for corresponding financial claims; it need not price every form of contribution.
- **DP — Transactional Outbox.** Record a committed change and the message to be sent in the same local transaction, then deliver the message with retry and duplicate handling. This addresses a specific [database/message dual-write failure](https://docs.aws.amazon.com/en_en/prescriptive-guidance/latest/cloud-design-patterns/transactional-outbox.html), not the solvency of the economy.
- **DP — Saga, conditionally.** Coordinate a sequence of local transactions with explicit compensating actions when a step fails. [Saga](https://learn.microsoft.com/en-us/azure/architecture/patterns/saga) is useful for some multi-party reservations. Compensation is not full rollback; an irreversible delivery or high-stakes settlement may require stronger coordination and different safeguards.
- **E — Reconciliation and adversarial transaction tests.** Try duplicate claims, late messages, concurrent reservations, partial delivery, and a participant leaving. Use the contribution DAG for its declared lineage purpose; do not infer consensus, valid attribution, or spendability merely from its shape.

**Worked demonstration:** allocate a scarce workshop slot across an entitlement service, provider, and payment record; fail the provider midway and show who retains the obligation. **Tradeoff:** a richer record can increase administrative friction and surveillance without improving provision. Compare actual service received.

<a id="pair-26"></a>

## 26 — Minds: engineering evidence and designing learning

### Chapter design spine

- **M — Concept modelling and semantic distinctions.** Separate an observation, attributed claim, inference, prediction, recommendation, and value judgment. Define the relationships that are meaningful rather than storing every item as undifferentiated “knowledge.”
- **P/M — Constructive alignment in learning design.** Align intended learning, learning activity, and assessment. [Biggs's original paper](https://doi.org/10.1007/BF00138871) supplies an educational design method: if the aim is judgment, fluent AI-produced answers cannot alone demonstrate that the learner acquired it.
- **M — Evaluation design and error analysis.** Decide whether the purpose is retrieval, factual accuracy, calibrated uncertainty, understanding, or transfer to a new task. Use suitable comparisons and look at different failure classes. There is no single “wise infosphere” score.
- **P — Explanations fit the audience and the actual system.** [NIST's explainability principles](https://nvlpubs.nist.gov/nistpubs/ir/2021/NIST.IR.8312.pdf) distinguish providing an explanation, making it meaningful, keeping it faithful, and respecting knowledge limits. An eloquent account generated after a decision is not automatically its explanation.

### Interlude builder spine

- **A — Typed provenance graph.** Use [W3C PROV](https://www.w3.org/TR/prov-overview/) concepts to distinguish source entities, transformation activities, and responsible agents. Add versions and correction relationships. Provenance can reveal that five reports derive from one source; it cannot make that source true.
- **A/E — Replaceable processing stages.** Make retrieval, evidence selection, inference, presentation, and correction propagation separately observable and testable. Swap a component under a stable contract to learn which stage caused a failure.
- **E — Explanation evaluation.** Test whether a reader understands what mattered, whether the explanation matches the decision procedure, and whether uncertainty is communicated appropriately. Different audiences may need different views of the same decision record.
- **E — Reproducible evaluation and learning tests.** Preserve the data/sample, software and model versions, configuration, metric, and stated tolerance. Evaluate educational transfer separately from assistant output quality. Track changes without freezing the learner into a profile.

**Worked demonstration:** a plausible but incorrect claim crosses a tutoring service and a community news feed; trace its origin, correct its derivatives, then test the learner on a new case. **Tradeoff:** provenance completeness and replay can conflict with privacy, licensing, and retention limits; record the test's limitations explicitly.

<a id="pair-27"></a>

## 27 — Commons: fitting institutions and infrastructure to the resource

### Chapter design spine

- **P/M — Ostrom's institutional design principles.** Examine resource and membership boundaries, locally fitted rules, participation in changing them, accountable monitoring, graduated responses, accessible dispute resolution, and nested arrangements where needed. [Ostrom's Nobel lecture](https://www.nobelprize.org/uploads/2018/06/ostrom_lecture.pdf) treats these as patterns in enduring institutions, not a universal constitution. A watershed, compute pool, and cultural archive require different applications.
- **M — Resource classification and boundary modelling.** Identify what is depleted, congested, renewable, copyable, excludable, sensitive, or jointly governed. Separate a physical stock from information describing it and from authority over either. This determines which commons analogy is useful.
- **M — Capacity, lifecycle, and allocation analysis.** Model operating cost, replenishment, maintenance, peak demand, and the consequences of competing uses. Compare access rules against the actual resource budget, including future users and burdens outside the immediate service.
- **P — Federate decisions at the scale of their consequences.** Proposed application of institutional and systems reasoning: keep local knowledge operative while accounting for effects that cross local boundaries. Localism is not a substitute for managing a shared river or grid.

### Interlude builder spine

- **A — Attribute-based access policy.** Translate a legitimate access rule into inspectable conditions involving the requester, resource, proposed use, and context. Keep the authority that establishes the rule distinct from the software that enforces it; build on Interlude 24's [ABAC treatment](https://csrc.nist.gov/pubs/sp/800/162/upd2/final).
- **A/E — Quotas, admission control, and resource isolation.** Allocate scarce capacity before uncontrolled demand collapses it. Use separate budgets or pools where one workload must not consume everything. For information services, [Google's overload engineering](https://sre.google/sre-book/handling-overload/) offers concrete practice; decisions about who receives scarce essentials require independent justification.
- **E — Test a policy against a workload.** Combine realistic demand, actual cost, and deliberately difficult access cases. Measure resource condition, service delivered, exclusion, and who bears the work of maintenance.
- **A — Separate public accountability from confidential payloads.** Publish appropriate aggregate use and custodial decisions while retaining restricted data in its governed store. Provenance, transparency, and universal visibility are different things.

**Worked demonstration:** govern a community compute pool serving learning and health workloads while accounting for energy cost and service continuity. **Tradeoff:** technically efficient pooling can centralize authority; isolation improves autonomy but can leave capacity idle. Work through the choice rather than praising either arrangement universally.

<a id="pair-28"></a>

## 28 — Making: modular products, qualified processes

### Chapter design spine

- **P — Modularity and defined interfaces.** Decide what should be replaceable independently and what must remain tightly coupled for safety or performance. Extend the reasoning of information hiding carefully into product architecture; a physical interface has tolerances, loads, wear, and material behavior that a software signature lacks.
- **M — Design for manufacture, assembly, repair, and disassembly.** Evaluate a design through how it will be made, inspected, serviced, taken apart, and recovered. These goals can conflict. A sealed component may resist contamination while becoming harder to repair; the reader should see the choice.
- **M — Life-cycle assessment.** Compare alternatives over a defined function and system boundary rather than by material adjective. [ISO's LCA framework](https://www.iso.org/standard/37456.html) supports examining inputs, outputs, impacts, interpretation, and limitations. “Bio-based” is not a life-cycle result.
- **M — Failure analysis and qualification planning.** Identify consequential failure modes and determine what evidence is needed for a particular design/process/material combination. Use component failure analysis where suitable and system-interaction analysis where failure can arise without a broken component. The design file alone cannot certify every manufactured instance.

### Interlude builder spine

- **DP — Abstract Factory, where the software actually needs it.** A fabrication application may need compatible families of machine-specific planners, simulators, and validators behind common interfaces. [Abstract Factory](https://www.informit.com/articles/article.aspx?p=1398599) can construct the appropriate family without hard-coding its concrete classes into the application. It does not manufacture a safe physical object or establish material compatibility by itself.
- **A/E — Versioned configuration and process envelopes.** Bind a job to the design revision, permitted parameter range, material specification, machine/process configuration, and relevant calibration. A changed member of that set triggers an explicit qualification decision.
- **E — Tolerance and interface tests.** Check actual parts and assemblies against their functional requirements. Software contract tests and physical inspection are complementary; a simulated fit is not a measured fit.
- **A — Lifecycle trace linked to repair and recall.** Connect batches and artifacts to inspections, repairs, updates, and material recovery. Build on provenance from 26 without collecting unrelated personal behavior.

**Worked demonstration:** use two fabrication cells to produce the same replaceable component; show which software varies, which interfaces remain stable, and which physical results still require inspection. **Tradeoff:** an elaborate Abstract Factory hierarchy is wasteful when there is only one stable product family or a simple configuration object suffices. Include it only if the example genuinely needs related interchangeable objects.

<a id="pair-29"></a>

## 29 — Governance: bounded authority and the limits of scale

### Chapter design spine

- **P — Separate policy from execution mechanism.** A rule's authority, justification, change procedure, and execution are distinct design concerns. A faster implementation should not make the rule harder to change or give its supplier the power to interpret every exception.
- **A/M — Bounded contexts and explicit interfaces.** [Domain-driven design's bounded-context approach](https://martinfowler.com/bliki/BoundedContext.html) makes the limits and translations of a model explicit. Apply the lesson to information systems serving different institutions: “resident,” “member,” and “beneficiary” need not be one universal category. Political jurisdiction is not conferred by drawing a software boundary.
- **M — Decision modelling and institutional change analysis.** Make the consequential rules and dependencies explicit, then determine how an existing legitimate body can authorize and revise a proposed arrangement. [OMG's DMN](https://www.omg.org/dmn/) is useful for well-defined business decisions; it cannot encode every contested legal meaning or replace deliberation.
- **M — Scalability analysis, including organizational capacity.** Distinguish more transactions from more jurisdictions, exceptions, stewards, and disputes. The governing question is what becomes a bottleneck, expensive coordination, or a concentration of authority as the arrangement grows.

### Interlude builder spine

- **DP — Anti-Corruption Layer.** Translate between systems without importing one system's whole conceptual model into another. The [pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/anti-corruption-layer) is particularly useful when a new civic service connects to legacy records. Here “corruption” means corruption of the domain model, not political corruption.
- **A/E — Versioned decisions and compatibility contracts.** Associate an action with its applicable rule version and jurisdiction. Test old and new clients across a rule transition; route unresolved semantic conflicts explicitly rather than guessing a translation.
- **DP/M — Strangler Fig migration.** Introduce a working replacement around a bounded part of an existing system and migrate deliberately. [Fowler's account](https://martinfowler.com/bliki/StranglerFigApplication.html) supplies the software pattern. Institutional application additionally requires authority, service continuity, staff transition, and remedy.
- **E — Load, partition, and coordination tests.** Use realistic workloads to distinguish computation from coordination limits. [Gunther's Universal Scalability Law](https://www.perfdynamics.com/Manifesto/USLscalability.pdf) models how contention and coherence costs can limit measured computer-system scaling. Do not turn it into a mathematical law of democratic legitimacy.

**Worked demonstration:** federate a service across three differently governed communities, change one local rule, and then lose network connectivity. Show which operations can continue, which must wait, and who resolves conflicting authority. **Tradeoff:** autonomy and rapid local operation can conflict with global consistency. More nodes do not settle the conflict.

<a id="pair-30"></a>

## 30 — Justice: designing a decision that can be examined and repaired

### Chapter design spine

- **P — Separation of duties and independent review.** Allocate decision, enforcement, review, and remedy powers deliberately so that the same interest does not control every stage. State conflicts and genuine independence requirements. This is an institutional architecture principle; it cannot be satisfied merely by running two software services owned by the same authority.
- **M — Business-rule and decision-table analysis.** Convert an apparently neutral classification into explicit conditions, evidence dependencies, exceptions, and outcomes. Apply [decision modelling](https://www.omg.org/dmn/) where the rules can be formalized; leave genuine discretionary judgment visible and accountable.
- **M — Requirements and evidence traceability.** Connect a rule's authority and purpose to its implementation, a particular decision, and the tests or review that can challenge it. A trace is useful only if it can answer a consequential question.
- **M — Multi-criteria fairness analysis.** Specify which harms, populations, and error types matter. [Chouldechova's research](https://arxiv.org/abs/1610.07524) demonstrates conflicts among particular statistical fairness criteria under stated conditions. The lesson is to expose choices; neither a single metric nor the impossibility of satisfying every metric excuses discrimination.

### Interlude builder spine

- **P/M/E — Design by Contract.** [Meyer’s contract approach](https://www.eiffel.com/values/design-by-contract/) makes component obligations explicit. State preconditions, postconditions, and invariants for a consequential operation: required evidence and authority, permitted outcomes, and conditions that must remain true. These engineering contracts make implementation obligations testable; they are not substitutes for legal rights.
- **A/DP — Stateful cases and selective Event Sourcing.** Model notice, challenge, interim protection, review, and remedy as an explicit workflow. [Event Sourcing](https://learn.microsoft.com/en-us/azure/architecture/patterns/event-sourcing) is one option for reconstructing state from recorded events; a simpler state store plus adequate audit may be sufficient. Avoid retaining unnecessary sensitive payloads merely because append-only logs are attractive.
- **E — Property-based and metamorphic tests.** Test declared invariants across generated cases. Where an exact answer is unavailable, test a specified relationship between related inputs—for example, changing an attribute formally declared irrelevant must not alter the rule's result. Research such as [METTLE](https://arxiv.org/abs/1807.10453) illustrates metamorphic testing where an ordinary answer oracle is unavailable; the justice example here is our application. These tests examine chosen properties; they do not prove the policy itself is just.
- **E — Replay and downstream correction tests.** Reconstruct a decision using the rule and evidence versions actually used, then trace how a correction changes dependent records and actions. Replay must not repeat the original real-world side effects.

**Worked demonstration:** a benefit denial rests on a stale category. Follow the rule, evidence, review independence, case transitions, and downstream correction. **Tradeoff:** complete replay, privacy, deletion obligations, and record retention can conflict. Specify what the system preserves and what it can no longer reconstruct.

<a id="pair-31"></a>

## 31 — Care: changing coupled systems, beyond the diagnostic drawer

**6 November 2026 scope correction:** the biological and surrounding systems are the intervention object; the person supplies its purpose and stakes. Disease labels remain useful summaries, not the compulsory unit of treatment. The chapter is broader than patient-service design, and the interlude is broader than clinical software. These methods now appear in substantive source; final narrative integration remains pending.

### Chapter design spine

- **P/M — Mechanistic and multiscale systems analysis.** Examine pathway, cell, tissue, organ, treatment/exposure and environmental interactions. Separate correlated networks from intervention-relevant causal models. [Network medicine](https://doi.org/10.1038/nrg2918) and [quantitative systems pharmacology](https://bmsr.usc.edu/files/2012/12/NIH-White-Papaer-2011.pdf) are foundations, not claims that a complete personalized model exists. Nosology becomes a revisable summary.
- **M — Goal-oriented requirements analysis.** Establish a desired capability or relief, identify obstacles and compare biological, assistive, environmental and service alternatives. Preserve patient choice and plural outcomes rather than a universal optimization score.
- **P/M — Minimally disruptive medicine and burden evaluation.** Compare clinical benefit with treatment work, caregiver load and access. [May, Montori and Mair (2009)](https://doi.org/10.1136/bmj.b2803) supply an established discipline; lower burden does not mean refusing a demanding but worthwhile therapy.
- **M — Functional allocation and SEIPS human factors.** Allocate tasks by capability, context and consequence among AI/human clinicians, physical services, patient and family. [SEIPS 2.0](https://pmc.ncbi.nlm.nih.gov/articles/PMC3835697/) exposes work-system interactions rather than merely exhorting individuals to be careful.
- **M — Robust design, option preservation and service design.** Compare routes under changing physiology and treatment availability, then trace the practical work through delivery and follow-up. Include resources, household and ecosystem effects.
- **M — Evolutionary reasoning applied to intervention.** Cancer populations can change under treatment; the next response depends on the selection imposed by the previous one. Adaptive treatment is indication-specific, not a general instruction to leave curable cancer untreated.

### Interlude builder spine

- **M — Multimodal biological integration.** Join omics and clinical observations while preserving tissue, time, assay, uncertainty and sampling limits. A variant or correlation is not automatically actionable.
- **M — PK/PD, PBPK and quantitative systems pharmacology.** Connect exposures to changing physiology and effects. A small one-compartment equation gives the reader a concrete model before introducing richer tissue/pathway coupling.
- **A/E — Therapeutic platforms and living circuits.** Separate target validity, delivery, exposure, response and tolerability. Reuse delivery/manufacturing/evidence only where transferable. Gene, RNA, immune-cell and tissue interventions have different persistence, targeting and failure properties.
- **M/A — Partial digital twins and value of information.** Generate competing explanations and intervention routes, then select observations that can change a decision. Preserve the boundary between measured, simulated, hypothesized and demonstrated.
- **A — Blackboard, capability registry, adapter and event-driven composition.** Specialist services work over an explicit shared case state; devices and external records retain semantics. These are genuine architecture patterns supporting post-app care, not new names for an all-purpose chatbot.
- **A/E — Stateful workflow and clinical control.** Track proposed, accepted, performed, failed and revised actions; prevent duplicates and close feedback loops. Account for physical irreversibility, timing and recovery.
- **E — Interface contracts, fault injection and staged evaluation.** Test missing/conflicting observations, unavailable services and changed consent; then distinguish retrospective performance, prospective shadow use, clinical evidence and monitored operation. STPA from Pair 30 remains an available cross-pair method; it is not the whole Care spine.

**Worked demonstrations:** changing clearance alters exposure despite unchanged input; partial models investigate a changed clinical pattern; a tissue-repair route connects modeling, manufacturing, intervention, rehabilitation and observed effects. **Tradeoff:** richer representations and more observations help only when they improve an intervention or a useful choice. Novel treatment ambition and disciplined evidence must develop together.

**Scope boundary:** VitalEdge exposes the possibility space and does not itself diagnose/treat. Future AI doctors and advanced therapies remain fully in the interlude's broader remit. See [the completion brief](volume-3-drafting/31-substantive-completion-2026-11-06.md) for author overrides, projections and evidence limits.

<a id="pair-32"></a>

## 32 — Continuity: sources that endure, commitments that learn

**6 November 2026: methods now implemented in substantive source.** The new design ambition is living cultural/religious renewal and reciprocal learning with agents. Standards support this work without defining the outer limit of the future. See the [brief](volume-3-drafting/32-substantive-completion-2026-11-06.md) and [projection companion](volume-3-drafting/32-vignette-constructions-2051.md).

### Chapter design spine

- **P/M — Representation independence and significant-property analysis.** Decide which meanings, relations and forms must survive a transformation. A song's sound and occasion may matter where a record's typography does not. Cultural transmission can require living practice outside the representation.
- **M — Value sensitive design.** Use iterative conceptual, empirical and technical investigation, including indirect stakeholders. Apply it to inherited hospitality, care and ecological responsibilities; let observed consequences revise the design. [VSD Lab](https://vsdesign.org/vsd/) is the established basis, not a claim that the proposed civilizational application is already validated.
- **M — Concept modelling and plural ontology mapping.** Identify distinct meanings and contexts; map practical compatibility without asserting total equivalence. Shared action may generate a new attributed agreement rather than require a single inherited vocabulary.
- **M — Distributional analysis and participatory design.** Evaluate benefits, burdens, exposure, consent, resources and ecological effects across overlapping meshes. Do not equate identical treatment with fairness or infer a permanent cultural identity from contextual participation.
- **M — Lifecycle, succession and multi-lifespan design.** Transfer practical capacity to future custodians, rehearse handoffs, preserve room for amendment and fund living transmission. Future generations are represented through options and responsibilities rather than fabricated consent.

### Interlude builder spine

- **A — Separate evidence from interpretation and action.** Version sources, readings, commitments, decisions, outcomes and revisions separately. The proposed two-track architecture joins preservation to adaptation without overwriting source history.
- **A/E — Provenance and temporal assertions.** [PROV-O](https://www.w3.org/TR/prov-o/) entities, activities and agents support lineage. Distinguish when a claim applies from when it entered the system; capture dispute and correction. Provenance does not establish truth.
- **A — Adapter pattern with explicit semantic loss.** Use contextual mappings; [SKOS](https://www.w3.org/TR/skos-reference/) distinguishes close and exact matches and does not make close matches transitive. Do not translate custodianship into a permission to sell by accident.
- **A/E — Scoped normative representation.** [ODRL](https://www.w3.org/TR/odrl-model/) offers permissions, prohibitions, constraints and duties for assets/services. It supports a bounded policy layer, not an automated derivation of the morally right rule from scripture.
- **M/E — Principle-guided training, retrieval and runtime authorization.** Keep these distinct. Test behavior under inconvenient help, group changes, new evidence and genuine conflicts. The [Constitutional AI paper](https://arxiv.org/abs/2212.08073) is an antecedent; situated reciprocal cultural learning remains proposed.
- **M — Multi-criteria and distributional comparison.** Preserve consequence dimensions before aggregation; search for better alternatives. Pareto improvement is a useful comparison, not a proof of fairness. Normative legitimacy remains a distinct problem from optimization.
- **A/E — OAIS/PREMIS preservation and tested migration.** Carry representation information, source identity, rights and events; test significant properties and successor understanding as well as bytes. [OAIS](https://ccsds.org/Pubs/650x0m3.pdf), [PREMIS](https://www.loc.gov/standards/premis/).
- **A/E — Living autobiographical and community authority.** Distinguish memory, advice and mandate; account for relational privacy and conflicting memories. Apply [CARE](https://doi.org/10.5334/dsj-2020-043) and community-defined reuse conditions; state enforcement and withdrawal limits honestly.

**Worked demonstrations:** a Samaritan-inspired service translates hospitality into actual access and capacity; a watershed partnership composes plural meanings and distributed consequences; a cultural collection migrates while preserving distinct source/translation/reconstruction objects. **Frontier test:** migrate a commitment and its correction history into more capable machinery, then examine useful conduct in genuinely new cases. The methods make this experiment buildable without claiming that moral continuity has already been solved.

<a id="pair-33"></a>

## 33 — Release: reality, experiments and a useful successor

### Chapter design spine

- **M — Hypothesis-driven design and alternatives.** State what should improve, compared with what, and which observations would change the decision. Exploratory inquiry retains room for unanticipated value.
- **M — Constraint modelling.** Distinguish physical relationships, chosen obligations and negotiable preferences; changes to each require different kinds of evidence or authority. Avoid collapsing everything into an optimization score.
- **M — Robust decision-making and value of information.** Examine strategies across plausible conditions, locate vulnerabilities and spend inquiry where it could alter action. The shared-facility example carries these methods into civic design.
- **P — Design for replacement and retirement.** Make assets, operating knowledge and authority transferable; preserve essential services and unfinished obligations through a change. Release includes continuing responsibility.
- **Author's frontier — Feasible forms of life.** Alice asks whether designs can change the institutional categories being optimized and make new sustainable capabilities possible. This is a research direction, not an established method or a verified novelty claim.

### Interlude builder spine

- **M — Separate substrate, model and consequence.** A simulated conservation rule, its physical implementation and the effect on a user are different things. Meaningful virtual experience does not establish model accuracy.
- **E — Model verification, empirical validation and uncertainty analysis.** Check implementation, compare against suitable observations, estimate parameters without circular validation, examine sensitivity and state the intended use. The worked thermal example exposes assumptions and units.
- **E — Reproducible experiment packages.** Preserve model/data versions, configuration, conditions, execution environment and criteria. Specify achievable tolerances or statistical behavior where exact replay is unavailable. Repetition is not independent confirmation.
- **A — Replaceable environments and explicit action boundaries.** Ports/adapters support simulation, replay, shadow operation and authorized real use. Shared interfaces do not imply shared permissions or equal evidential standing.
- **E — Staged exposure, observation and repair.** Expand through meaningful field evidence. Shadow runs do not establish every causal effect; software rollback does not undo physical or social consequences.
- **A — Mental-exoskeleton components.** Separate evidence storage, retrieval, personal inference, rendering and delegation. Distinguish quotation from generated proposal and remembered preference from authorization. This is a proposed composition, not a formally named universal pattern.
- **E — Succession exercise.** Another group operates, changes and retires an instance without a founder's private intervention. The useful inheritance includes means of inquiry, not only code.
- **Author's frontier — Continuing inquiry beyond impersonation.** Bob asks whether reciprocal coupling develops a practice that can survive component change and become useful to successors. Extended cognition is an antecedent, not proof of consciousness or personal survival.

**Worked demonstrations:** thermal model → measured comparison → authorized experiment; a long-term personal Mirror → corrected assumption → new inquiry; a Breadboard → independent operation and consequential change. **Tradeoffs:** greater detail is not always better information; immersive persuasion can outstrip evidence; excessive standardization can suppress discovery. Art and speculative inquiry need explicit room without being misrepresented as empirical proof.

**Applied status, 6 November 2026:** incorporated into the canonical pair's substantive middle. Final projections and closing prose remain reserved. [Completion brief](volume-3-drafting/33-substantive-completion-2026-11-06.md) records the evidence and limits. Pair 33 leaves room for an optional Coda III before the Epilogue.

## Where the author's examples belong

| Requested example | Primary home | What the reader should learn |
|---|---|---|
| Adapter | Interlude 23 | Translate an external interface while keeping the core service independent of a vendor or channel. Translation must preserve meaning, not just field names. |
| Abstract Factory | Interlude 28, conditional | Construct compatible families of software components without coupling the application to their concrete classes. Use a simpler arrangement when no family-level variability exists. |
| Track provenance | Interlude 26; specialized in 25, 28, 30–32 | Represent sources, transformations, actors, and corrections explicitly; distinguish lineage from truth, entitlement, or permission. |
| Explainability | Chapter/Interlude 26; applied to personal agency in 24 and decisions in 30 | Design explanations for their audience, check fidelity, and expose relevant limits. Access to an explanation and power to obtain a remedy remain different capabilities. |
| Repeatability/reproducibility | Interlude 33; first exercised in 26 | Specify the experiment and preserved artifacts, the allowed differences, and who can repeat it. A repeated model result is not proof of real-world validity. |
| “The myth of scalability” | Interlude 29; resource application in 27 | Test the assumption that adding participants or machines simply multiplies capacity. Examine bottlenecks, coordination costs, failure modes, institutional workload, and concentrated authority. |

“The myth of scalability” is a possible essay framing, not the formal name of a single established principle or a claim that scale never works. The useful argument distinguishes scaling, replication, federation, and the redesign sometimes required between them.

## Building with agents: the reader needs more than better prompts

A recurring interlude practice can translate design knowledge into competent use of increasingly capable development agents. This is a proposed working discipline, not an assertion that every future agent will have today's limitations:

- Give the agent the problem, relevant actors, context, constraints, and intended outcomes before prescribing a technology.
- Request contrasting designs and their assumptions. Preserve the rationale for the selected alternative so later builders can challenge it.
- Specify interfaces, invariants, and observable behavior. Let the implementation vary where variation is harmless.
- Derive acceptance cases from the need and failure analysis, not solely from whatever implementation the agent produced. An agent writing both a mistaken implementation and matching tests has not supplied independent assurance.
- Produce a small working instance, instrument it, and test real consequences within an appropriate scope. Expand on evidence of value and adequate behavior, not on the persuasiveness of the generated explanation.
- Preserve enough versions, evidence, and operating knowledge for another builder to examine, change, and take responsibility for the work.

An agent can help perform analysis, generate diagrams and code, run comparisons, find counterexamples, and improve a design. The method makes those contributions inspectable. Legitimate choices about rights, priorities, institutions, and acceptable tradeoffs still need the appropriate people and processes.

## How this becomes readable prose

Keep both lists active. The first supplies values, purposes, domain requirements, and existing mechanisms; the second supplies reusable design knowledge and construction practice. Trace a connection when it is useful:

**Opportunity signal → value or design concern → design reasoning → mechanism → evidence → the reader's Next Move.**

This is an editorial aid, not a sequence of seven compulsory headings. For the reader, begin with the concrete difficulty, work through the choice, name the useful principle, and show its consequences. A plain explanation can carry a formal name in the sentence or source note. Preserve enough terminology for the curious reader to find the discipline again.

For example, the Justice chapter can first show why giving the original decision-maker sole control over review is structurally weak. It can then introduce separation of duties, work through a decision model, and compare review arrangements. The interlude can follow one contested decision through its versioned rules, evidence, case states, tests, and correction. “Challenge and remedy” stays important throughout, but the reader now knows something about how to build for it.

Similarly, a reader should leave Renewal understanding how to break a service into functions and connect them without welding institutions together. They should leave Making understanding why a design can be easy to fabricate and impossible to repair, and how interface and lifecycle choices create that result. The technical lesson produces the humor and philosophical implications naturally; it need not arrive as a catalog recital.

Give full explanations primary homes and use later cases to extend them. These methods apply from the baseline implementation onward. A chapter's future Gate supplies demanding conditions in which to examine them; it is not the year at which the principle is first invented or becomes relevant.

## Status and research limits

This adds a distinct technical list for all eleven chapters and interludes. It does not replace the first list, the opportunity-signal map, or the proposed Next Moves. No manuscript passage has been changed. Selection and narrative integration remain a later task.

The linked primary sources establish the method, framework, pattern, or qualification associated with them. Our civic examples, chapter placements, and many cross-domain applications are editorial proposals, not results proven by those sources. Vendor implementation guidance illustrates engineering patterns without prescribing that vendor's services. Public standard descriptions and indexed excerpts support the limited claims made here; they are not represented as a complete review of restricted standards or books. Clinical, institutional, and cultural applications still need their domain-specific validation when developed.
