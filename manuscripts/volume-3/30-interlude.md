![](../assets/shared/interlude-gear.png)

INTERLUDE 30

# Protocols of Integrity

*Designing Fairness into Systems*

*INTEGRITY*

<!-- Legacy opening retained verbatim as a prose bank, not the approved 2046 projection. Reconstruct as a prospective builder reflection at 9 AM, 11 September 2046; see work/volume-3-drafting/30-vignette-constructions-2046.md. Its existing fictional review remains available to Sam/Claude. -->

Nothing had broken.

That was the problem.

The wall display showed the decision chain from Mara's case as a clean green sequence, each link wearing the little badge of compliance that systems use when they want to sleep well.

**Identity credential accepted.**\
**Jurisdiction routed.**\
**Eligibility inferred.**\
**Duplicate-benefit risk detected.**\
**Automated denial issued.**\
**Appeal path assigned.**\
**Review pending.**

Green. Green. Green. Green. Green. Green. Yellow only at the end, where the harm had finally acquired enough dignity to interrupt the machine.

The integrity review chamber was attached to the federated civic mesh office, though "chamber" made it sound more solemn than it looked. It had screens, tables, transcripts, flow maps, a coffee machine of dubious moral standing, and a corner where legal mediators, systems engineers, auditors, model evaluators, and community advocates were learning how to speak to one another without needing a translator or a sedative.

The harmed person was not in the room.

That was deliberate.

Mara had already explained herself enough. The system had taken days from her life; it was not entitled to take more simply so engineers could experience closure. A community advocate represented her account, and the case record included her statement, her correction requests, the emergency bridge, the care timeline, and the phrase that had cut through the previous room like a clean blade:

**I don't need the system to explain why it trapped me. I need it to let me out.**

That sentence sat at the top of the review file.

Good.

Every integrity review should begin with the human sentence the system failed to understand.

In the room were a civic auditor, a legal mediator, a model evaluator, a systems reliability engineer, a community advocate, a machine-actor registry steward, a care mesh representative, and an AI evidence assistant useful enough to invite and not trusted enough to chair anything. I sat near the side, where aging authors, former engineers, and repeat offenders of systems metaphor are usually placed until needed.

The first display showed local compliance.

Everything looked fine.

The identity system had accepted Mara's credential.

The municipal system had flagged a stale residency record.

The provincial eligibility engine had deferred to the updated residency inference.

The care mesh had prevented a duplicate benefit.

The appeal router had assigned the matter to the correct stream according to the rule set.

The rule set had performed as written.

The mediator switched views.

The same chain turned red at the interfaces.

Between identity and residency: **temporary-care context dropped.**

Between residency and eligibility: **confidence threshold treated as final.**

Between eligibility and care mesh: **continuity-of-care rule not invoked.**

Between denial and appeal: **emergency need not surfaced.**

Between appeal and review: **time-to-harm exceeded safe window.**

Between systems: **no owner for global outcome.**

There it was.

The failure was not in a single node.

It was in the spaces between nodes.

The systems reliability engineer leaned back.

"Each component passed its local tests."

The community advocate said, "Then the tests were too local."

The room went quiet in the healthy way.

A young evaluator asked whether the denial should be classified as model error, workflow error, policy conflict, or jurisdictional ambiguity.

The AI assistant suggested: **compound integrity failure.**

The auditor added, "With human harm."

The assistant updated:

**Compound integrity failure with human harm.**

"Better," said the advocate. "Still sounds like the harm filed the paperwork late."

The machine, mercifully, did not defend itself.

The review began.

Not to find one villain. There might not be one. Not to absolve everyone because the system was complex. Complexity has become one of the more fashionable hiding places for irresponsibility. The task was harder: reconstruct the decision, locate the moral breakpoints, assign responsibility, repair the case, modify the system, and prevent recurrence without pretending the future could be made safe by one more checkbox.

Aviation learned this painfully. Medicine learned this painfully. Software learned this noisily. Justice, having had several millennia to prepare, was now being asked to learn it properly:

A system can function exactly as specified and still be wrong.

That is why integrity cannot be a virtue painted onto the wall.

It must be built into the architecture.

<!-- End of reserved opening. AI-assisted substantive completion, 6 November 2026. Earlier undated technical mirror retained separately. -->

## 1951: Quality Acquires a Handbook

In **1951**, the same year as Iran's oil nationalization and the Rosenbergs' trial, McGraw-Hill published the first *Quality-Control Handbook*, edited by Joseph M. Juran. The date belongs exactly to our institutional marker. The book did not invent quality control; it assembled a substantial engineering discipline into a working reference.[^v3-30i-juran]

Juran's formulation of quality as *fitness for use* offers a useful entrance.[^v3-30i-fitness] A component can conform to its specification while the assembled service fails the person using it. Our further question is what that use ought to be. A wonderfully reliable machine for manufacturing dependency still requires a design review (possibly with fewer congratulations).

The **1001** chapter marker found Ferdowsi composing a poem in which a ruler's certificate could be torn apart by the person it purported to vindicate. By **1951**, our parallel history supplies a handbook for examining whether production fulfils its promises. At the **2046** gate, the proposed task is to carry that scrutiny through institutions, agents and their material consequences, while keeping the promises themselves open to challenge. The passage from quality control to civilizational integrity is our design argument; it is not something we are attributing to Juran.

## Build an Argument That Can Lose

A test suite begins with expectations. If those expectations encode an injustice, passing the tests will reproduce it efficiently. The builder needs an explicit account of why the expected behavior deserves confidence.

An *assurance case* connects a claim to supporting evidence through a reasoned argument. It states the context and assumptions under which the claim holds. It can include test results, analysis, operational observations and independent review. It is not an unequivocal proof; a well-structured case should make its weaknesses easier to find.[^v3-30i-assurance]

For our temporary-address example, a useful top-level claim is narrow: *this service can handle a disputed address without an unjustified interruption of essential provision*. Supporting claims concern authority, contextual accuracy, continuity capacity, usable review and downstream correction. Evidence might include generated edge cases, simulated outages, actual continuity performance and testimony from people who encountered the process. An impressive model benchmark addresses only a small part of that claim.

Keep a counterargument alongside the evidence. The fallback provider may have no spare capacity. A temporary flag may be discarded by a downstream service. People who cannot obtain the required credential may never appear in the success statistics. These are reasons to revise the design, not defects in the report's tone.

An assurance case also expires in parts. A policy change can invalidate a test's assumptions without changing a line of code. A model update can alter behavior while preserving the interface. A depleted reserve can make a once-valid continuity claim false. Link each material change to the claims that must be reconsidered. The certificate should know what would make it stop certifying.

## TACK at the Point of Action

Neuverse's proposed **TACK** discipline asks whether a capability is **Tactical, Aligned, Constrained and Knowable**. It applies to an action or capability in context, including the introduction of a sensor, a service or a decision rule. A sensor changes who can know and act; installing one is already an intervention.

| TACK question | Obligation in the temporary-address service | Evidence that could defeat the claim |
| --- | --- | --- |
| **Tactical:** what legitimate purpose does this action serve here? | Resolve the relevant eligibility uncertainty while preserving essential continuity. | The requested domestic history does not affect the decision. |
| **Aligned:** which values and affected interests must survive? | Respect care, privacy, accountable provision and the resources supporting it. | Cost savings depend on leaving affected people without an alternative. |
| **Constrained:** what bounds the action and its consequences? | Limit data access, delegated powers and the duration of provisional restrictions; provide review. | A temporary classification becomes a permanent cross-service exclusion. |
| **Knowable:** what can someone inspect and contest? | Record material evidence, rule versions, authority, uncertainty and actual effects. | The operator can explain the intended workflow but cannot establish what happened. |

These are design obligations for this example, not a universal certification recipe. C8 supplies values; MOxAIC exposes the orders and burdens crossing here; TACK asks whether the proposed operation respects them in practice. If the conflict is unresolved, a green badge cannot resolve it.

In Tiers, several layers participate: relations describe relevant dependencies, orchestration carries obligations across work, and organs supply purpose and legitimate service. An organ includes people and accountability as well as software. TACK is not merely an external connector check, and the intrinsic *x* of MOxAIC is not an API we can install to make values agree.

## The Failure Is Between the Green Checks

Use *Systems-Theoretic Process Analysis* to examine the control arrangement. Identify the losses to prevent, the hazardous conditions, the controllers and their feedback. Then examine control actions that are missing, unsafe in context, mistimed or sustained for the wrong duration.[^v3-30i-stpa]

Here, an eligibility service issues a withdrawal, a provision service executes it, and a review service receives the complaint. The hazardous condition is an interruption of essential provision without a timely legitimate alternative. It may occur even if every local component follows its instructions.

The control model is wrong if an address change is assumed permanent. Feedback is inadequate if the withdrawal is acknowledged by the software but nobody checks whether replacement provision exists. Timing is unsafe if review finishes after the need becomes acute. Authority is incomplete if the person observing the danger cannot authorize continuity. These are different defects; replacing the classifier addresses only one of them.

The resulting constraint should reach the whole path: no interruption solely on that unresolved inference, unless an authorized alternative preserves the relevant protection or a separately justified action requires it. The rule needs explicit exceptions and a means of resolving them. It also needs resources. An invariant that requires an unavailable provider is an unfunded wish in mathematical clothing.

![A justice feedback loop connects purpose and constraints, release evidence, authorized operation and observed effects. A detected hazard or challenge starts protection and investigation in parallel; repair reaches all affected cases, verification checks actual outcomes, and the findings return to the original purpose and rules.](../assets/v3-30-interlude/justice-through-the-lifecycle.svg){#fig-v3-30-integrity width=95% fig-alt="A two-way justice lifecycle: purpose and constraints lead through evidence and authorized operation to observed effects. Hazards or challenges open parallel protection and investigation, followed by class-wide repair and independent verification. Verified findings revise purposes, rules and operating constraints. Contested matters remain open."}

The return path matters as much as the release path. An observation that disproves the design's purpose must be able to change that purpose. Otherwise we have built an excellent maintenance department for the wrong machine.

## Contracts Across the Handoff

*Design by Contract* specifies preconditions, postconditions and invariants: what must hold before an operation, what it promises afterward, and what must remain true.[^v3-30i-contract] For a consequential action, these need to cover authority and meaning as well as data types.

Before withdrawing a service, the executor must have the applicable mandate, the current rule version and evidence meeting the declared standard. Afterward, it must record what actually changed and which parties received notice. Across the workflow, unresolved temporary context must not silently become a final adverse fact.

A decision table can make the combinations explicit. In a simplified design, confirmed eligibility continues provision; material uncertainty opens review with authorized continuity; a justified restriction follows its own proportionate, reviewable route. A missing field takes the uncertainty route. It must not acquire the meaning of false merely because the programming language finds that convenient.

These contracts belong to the services and institutions exercising power. They do not become extra forms that an injured person must complete. Nor do assertions in code prove the complete arrangement safe. A precondition can be wrong, a necessary condition omitted, and a downstream system outside the tested boundary.

Test the handoff itself. Drop the temporary-context marker. Deliver an old decision after its correction. Duplicate a notice. Lose the receiving service's acknowledgement. Check that the system preserves continuity, rejects stale authority where appropriate and exposes unresolved work. The test passes when the intended protection survives, not when all processes exit successfully.

## Tests That Ask Better Questions

*Property-based testing* generates many cases against a declared property.[^v3-30i-quickcheck] Here, a correction to an adverse inference should not leave a dependent service executing the superseded decision. Generate changes of address, conflicting evidence, reordered messages and service interruptions. Record the cases that falsify the claim and make them reproducible regression tests.

*Metamorphic testing* checks relations between related inputs and outputs when a complete answer oracle is unavailable.[^v3-30i-metamorphic] If a presentation detail is declared irrelevant, changing only that detail should not change the applicable decision. If two records contain the same material evidence in different orders, ordering alone should not alter the result. These relations must be justified for the task. Treating every contextual difference as irrelevant would manufacture a new unfairness.

Keep outcome tests separate from label imitation. Historical decisions can contain the very inequity the redesign aims to remove. Include affected people's counterexamples, cases outside the training distribution, resource shortages and interactions with other services. For AI-generated tests, inspect whether the generator merely shares the builder's assumptions. More tests with the same blind spot give it better company.

Statistical fairness measures need a declared purpose and denominator. Report serious errors, their distribution and the availability of remedy, alongside aggregate performance. Some fairness criteria are incompatible under specified conditions; a test suite cannot make that political and ethical choice disappear.[^v3-30i-fairness] Examine whether changing the service can reduce the conflict before optimizing the score.

## Release the Change, Keep the Obligation

Continuous integration and delivery can carry this discipline into ordinary work. A consequential change has a bundle of versions: code, model, data transformation, decision policy, delegated authority and dependencies. The release must identify which bundle the evidence supports. Changing the policy through a configuration screen is still a release of power.

<!-- AI-assisted whole-volume reconciliation: Codex, 2026-11-06. -->

Carry forward the repeatable deployment discipline from the first bench. Promote the tested artifact and its declared configuration through the release process; do not rebuild an unrecorded variant for production. Rehearse state migration and recovery as well as code replacement. If an update changes the meaning of a stored decision, restoring yesterday's executable may leave today's records misread. Reversal may require a compatible transition or a forward repair, with outstanding obligations still assigned.

Run the candidate against recorded or carefully constructed cases without repeating real actions. Where lawful and appropriate, *shadow operation* compares proposed decisions with the live arrangement while withholding the candidate's actuations. Simulation can expose failures; it cannot establish that unmodelled harms do not exist. A limited rollout likewise needs an adequate basis for use, monitoring, exit and remedy. Calling it a canary does not exempt the people in it from having lungs.

At runtime, an independently maintained control can enforce a bounded action envelope: permissions, resource ceilings, required evidence, prohibited transitions and conditions requiring escalation. Independence here needs attention to ownership, failure modes and common assumptions; running the same model twice is not automatically a second opinion.

The fallback depends on the consequence. A potentially dangerous machine may need to stop. An essential support service may need to continue provision under a bounded, funded authorization while the dispute is resolved. “Fail closed” and “fail open” are incomplete instructions until we name what closes, who loses access and what remains available.

This can permit more useful autonomy. Within a justified envelope, agents can identify errors, supply authorized continuity and carry corrections without waiting for a committee to bless every obvious repair. Actions outside that mandate need another route. Speed is valuable where it shortens harm; legitimacy determines which work may be accelerated.

## Keep the Evidence Typed

A usable trace distinguishes an observation from an inference, a proposal from an authorization, and a command from a completed effect. Record when the underlying event occurred as well as when the system received it. A fresh timestamp on an old fact is a remarkably portable mistake.

For a material decision, preserve the relevant rule and model versions, evidence references, mandate, uncertainty, effective period, downstream dependencies and available correction route. This is selective evidence, with purpose, access and retention limits. A universal biography is neither necessary nor innocent.

Event sourcing can reconstruct state from recorded events, although a well-designed state store with an adequate audit trail may be simpler. Sensitive payloads need not live forever in an append-only log; protected references and explicit retention decisions can limit exposure.[^v3-30i-events] Where deletion prevents exact reconstruction, acknowledge that limit. Do not promise both perfect historical replay and complete erasure of the same information.

Neo4j, the current Neuverse implementation direction, can help traverse dependencies: this classification influenced these decisions, which triggered these actions. That makes a correction search possible. The graph records asserted or observed relationships; it does not establish causation by drawing an edge. Feedback loops are allowed in the broader model. A particular event history may impose ordering constraints without making civilization a directed acyclic graph.

Evidence of behavior also differs from a model's account of its reasoning. A fluent explanation cannot establish which tool ran, what information was supplied or whether a service arrived. Keep externally checkable action records and outcome evidence. Confidence should have something outside its own voice to lean on.

## Two Tracks After a Warning

A report of credible harm should start two connected tracks: **protection and continuity**, and **investigation and accountability**. The first cannot always wait for the second to finish. Neither should silently close the other.

Before operation, assign the receiving duty, interim powers, funding and escalation paths. A person can challenge the outcome without identifying the defective component. The case acquires an accountable route; the institutions resolve their internal routing problem. A correction should not expire because the complaint was initially addressed to the wrong department.

For a specified hazard, a useful engineering requirement is:

$$
T_{\mathrm{detect}}+T_{\mathrm{protect}}<T_{\mathrm{harm}}.
$$

Here, detection time is measured from the start of the hazardous condition; protection time is the additional time after detection until protection becomes effective. The harm interval runs from that same hazardous condition to the earliest credible occurrence of the specified serious harm. This is a design constraint for a bounded case, not a universal law of justice. If the bound is too uncertain or the inequality cannot be supported, redesign the exposure or establish protection before entering it. Averaging fast and slow responses will not protect the person in the slow tail.

Review then needs evidence, independence, competence and power to act. A reviewer who can only repeat the original model's result is a latency device. State what the institution must demonstrate, what the claimant is not required to prove and how unresolved facts affect provisional measures. Serious restrictions require their own justification and review; predicted wrongdoing alone is not a finding of guilt.

## A Patch Has to Reach a Life

After an error is established, correction has a scope. Find decisions dependent on the faulty rule or evidence, identify affected cases through authorized queries, and distinguish clear corrections from cases needing individual review. The search includes people who never complained. It must also acknowledge the people missing from the available records.

Send versioned correction instructions to dependent services. Each reports whether it applied the correction and which effects remain unresolved. Retries need idempotent handling so a repeated instruction does not create duplicate compensation or contradictory state. An unreachable service enters a tracked escalation path. Silence cannot count as acceptance.

A *compensating transaction* helps undo or offset completed steps across distributed services, and may itself require retries or intervention.[^v3-30i-compensation] Its name does not settle what a person is owed. Reversing a ledger entry cannot undo an injury, and restoring yesterday's database may destroy legitimate changes made since then. Identify reversible state, compensable effects and irreparable losses separately.

Verify outcomes at the appropriate boundary. A corrected eligibility record is one result; resumed provision is another. Receiving the ordered service is another again. Verification should use proportionate evidence and accessible confirmation without burdening people with repeated proof of their own lives. Outstanding consequences remain open even after the software defect is fixed.

This gives a civic postmortem something concrete to produce: an account of contributing conditions, duties and choices; funded remedies; changes to the recurring cause; and a date to verify the effect. A no-blame learning process can coexist with a separate accountable investigation. Neither “everyone followed procedure” nor “one person failed” is an adequate endpoint by itself.

## Observe the Observer

The integrity machinery can cause harm too. It can overcollect, harass people with verification requests, normalize a majority's values or suppress reports to improve its own metrics. Give it the same obligations it imposes elsewhere: scoped purpose, contestable authority, retention limits and independent review.

Measure unresolved serious harms and time to effective protection, not merely ticket closure. Examine repeated burdens, missing populations and whether repairs survive beyond the first successful case. Low complaint rates can mean little harm, little access or little faith in the process. The number needs an explanation.

Reliability targets can allocate engineering effort, but an error budget is not a licence to injure a proportion of the population. Some constraints prohibit an action; some risks need reduction and informed, legitimate acceptance; some losses call for immediate protection regardless of whether the quarterly average looks excellent. Keep those categories distinct.

By **2046**, capable agents could maintain much of the evidence, search dependencies, generate adversarial cases and carry authorized repairs across services. The design achievement would be a network able to improve its own operation while remaining answerable to those living with it. No dashboard gets to declare that achievement on its own behalf.

## Bob at the Crossing: Can Repair Travel as Well as Failure?

Failures propagate through dependencies with little ceremony. A bad category can become a denied service, a missed obligation, a new risk flag and another denied service. Correction usually travels with less enthusiasm.

I would like to explore a **repair protocol** that carries more than a revised value. It would carry the reason for correction, the affected scope, the authority to act, required continuity, outstanding consequences and the evidence needed to close each obligation. Receiving systems would translate that obligation into their own context while preserving what matters. Where translation fails, they would expose the conflict instead of quietly acknowledging receipt.

Distributed transactions, assurance cases and existing remediation practices provide pieces. The open wager is whether we can compose those pieces across institutions whose meanings, duties and capabilities differ, without installing a central interpreter entitled to settle every conflict. An AI might generate a proposed repair plan and its testable obligations. Affected people and authorized bodies would retain ways to challenge both the plan and the assumptions beneath it.

Test it on one recurring failure with several downstream effects. Compare it with ordinary case-by-case correction. Does it reduce repeat harm, reach silent cases and preserve legitimate differences? Does it disclose uncertainty and resist capture? Does a later review find that the remedy itself created a new dependency? These outcomes would determine whether the idea deserves expansion.

The ambitious part is not automatic absolution. It is making a civilization's capacity to correct itself propagate with something approaching the speed of its mistakes.

<!-- Legacy closing retained verbatim for Sam/Claude; reconcile the Mara callback with the new projection and broaden beyond a one-case fix. Noēsis remains reserved for the literary pass. -->

## All Green Checks, One Wrong Life

By the end of the review, Mara's case had changed the system.

Not enough.

Never enough.

Enough to matter.

The temporary-care context became a protected signal. Eligibility conflicts triggered continuity review before denial. Emergency need could suspend duplicate-benefit enforcement. Residency inferences gained a confidence display and human review threshold. Appeal routing now measured time-to-harm, not merely time-to-ticket. Similar cases were searched. A public incident summary was drafted, stripped of private detail but not of responsibility.

The green chain no longer looked innocent.

Good.

Systems should lose innocence when they harm someone. Not confidence, necessarily. Not usefulness. Innocence.

Integrity is not a moral feeling.

It is a system property.

Consequential decisions must be traceable. Evidence must carry provenance. Fairness must be tested across edge cases. Automation must be contestable. Due process must be navigable. Proportionality must be encoded. Prevention must not become punishment. Human review must actually review. Cross-jurisdiction systems must carry recourse with authority. Every system must have repair and learning loops before it deserves power.

In implementation language, justice needs cases, persons, evidence edges, review edges, and integrity meshes.

In human language, it needs a way for the harmed person to say, **This is wrong**, and for the system to answer with more than a ticket number.

Integrity can keep a system from crushing a person by mistake.

But not every wound begins as injustice.

Some begin as weakness, age, pain, fear, chemistry, loneliness, inflammation, memory, and the body's quiet failure to keep negotiating with time.

After justice comes care --- not because care is softer, but because bodies are where every system eventually presents its bill.

[^v3-30i-juran]: Joseph M. Juran, ed., *Quality-Control Handbook*, first edition (New York: McGraw-Hill, **1951**), 800 pp.; [National Diet Library catalogue](https://ndlsearch.ndl.go.jp/books/R100000002-I000006236427), bibliographic ID 000006236427, and [American Society for Quality, “Joseph M. Juran”](https://asq.org/about-asq/honorary-members/juran). The date is the first edition's publication year, not the invention of quality control.

[^v3-30i-fitness]: Juran Institute, [“Features of Quality & Definition of Quality Excellence”](https://www.juran.com/blog/features-of-quality-definition-of-quality-excellence/) (2019), on Juran's “fitness for use” formulation and its relationship to other quality definitions. The further question about legitimate civilizational purposes is this book's extension, not a quotation from the 1951 edition.

[^v3-30i-assurance]: John Rushby, Xidong Xu, Murali Rangarajan and Thomas L. Weaver, [*Understanding and Evaluating Assurance Cases*](https://ntrs.nasa.gov/citations/20160000772), NASA/CR-2015-218802 (2015). Claims, argument and evidence support a context-dependent case rather than unequivocal proof. The civic-service case and its counterarguments here are proposed applications.

[^v3-30i-stpa]: Nancy G. Leveson and John P. Thomas, *STPA Handbook* (2018), chapter 2, [MIT PSASS books and handbooks](https://psas.scripts.mit.edu/home/books-and-handbooks/). See the identification of unsafe control actions and causal scenarios. The address, continuity and review example is hypothetical and is not an actual agency's policy.

[^v3-30i-contract]: Bertrand Meyer's *Design by Contract*, described by [Eiffel Software](https://www.eiffel.com/values/design-by-contract/), especially preconditions, postconditions and invariants. Software contracts do not replace legal rights, civic mandates or the evaluation of the specification itself.

[^v3-30i-quickcheck]: Koen Claessen and John Hughes, [“QuickCheck: A Lightweight Tool for Random Testing of Haskell Programs”](https://research.chalmers.se/en/publication/237427), *Proceedings of ICFP 2000*, pp. 268–279, DOI [10.1145/351240.351266](https://doi.org/10.1145/351240.351266). Generated tests exercise specified properties; they do not prove the completeness or justice of the specification.

[^v3-30i-metamorphic]: Xiaoyuan Xie et al., [“METTLE: a METamorphic testing approach to assessing and validating unsupervised machine LEarning systems”](https://arxiv.org/abs/1807.10453), preprint 2018, revised 2019; published in *IEEE Transactions on Reliability*, DOI [10.1109/TR.2020.2972266](https://doi.org/10.1109/TR.2020.2972266). Its clustering experiments illustrate testing through justified relations when a direct oracle is unavailable. The civic decision examples are our extensions.

[^v3-30i-fairness]: Alexandra Chouldechova, [“Fair prediction with disparate impact: A study of bias in recidivism prediction instruments”](https://arxiv.org/abs/1703.00056), *Big Data* 5(2), 2017, pp. 153–163. Statistical criteria, assumptions and the relevant populations must be specified; no single score establishes that a service is just.

[^v3-30i-events]: Microsoft Azure Architecture Center, [“Event Sourcing pattern”](https://learn.microsoft.com/en-us/azure/architecture/patterns/event-sourcing). Event histories support reconstruction but introduce complexity and retention/privacy concerns. This book does not prescribe Event Sourcing for every civic service.

[^v3-30i-compensation]: Microsoft Azure Architecture Center, [“Compensating Transaction pattern”](https://learn.microsoft.com/en-us/azure/architecture/patterns/compensating-transaction). Compensation may require context-dependent operations, idempotent retries and manual intervention; it need not restore the original state. The distinction between technical compensation and adequate civic remedy is developed here.
