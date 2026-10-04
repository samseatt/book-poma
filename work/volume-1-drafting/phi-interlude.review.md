![](../../manuscripts/assets/shared/interlude-gear.png)

INTERLUDE Φ

# The Edges of Reason

*From Symbols to the Silicon Mirror*

*INQUIRY*

If time began, what was happening before it? If it never began, how could that make sense either?

Where inside the radio did the wave become a voice? Why could the antenna find what I could not see?

Would we have flying cars in the 1980s? What about 1990? I could invent them when I grew up, if the adults remained occupied with whatever was taking them so long.

These were questions from different years, recovered here as questions rather than a transcript. There was the globe: if we lived on every side of a round Earth, why did people underneath not fall off? Objects placed on my little globe were quite willing to demonstrate the difficulty. There was school every day, and the bed that had to be made although its next scheduled use would undo the work. Civilization was already presenting a suspicious approach to efficiency.

Why were some people poor? What made them poor? Why would God arrange it that way? Did dogs think? They sometimes looked as though they were thinking. Why did eating animals feel different from eating plants?

There was also the night watchman’s prediction that the world would end. My mother’s answer, as I remember it, brought the impending catastrophe down to the scale of the man who feared his own death. I do not have the rest of that conversation clearly enough to rebuild it. The fragment stayed. Someone else’s final day might be travelling under the name of everybody’s future.

And, for an uncle, a proposal: what would happen if a gecko and a mouse were put in a box? What if we added a frog?

I remember the question. It should not be mistaken for an experimental record.

## One Thousand and One Lamps

The questions survived in my unorganized mental storage, somehow avoiding the permanently-delete button. Some were answered; some changed their wording and acquired more expensive books. Others remained like a broken shoelace, not long enough to tie but quite long enough to keep interrupting the walk.

Looking back, what surprises me is less the curiosity than its unevenness. I could be dissatisfied with the beginning of time and accept a considerable amount of the social world on somebody’s say-so. Growing up improved the vocabulary of the questions. It did not automatically improve their distribution.

Civilization has a similar talent. We can become technically accomplished at answering one kind of question while arranging another beneath an increasingly elaborate rug. Eventually the rug becomes part of the architecture. Someone who lifts its corner is accused of undermining the house.

The useful response is to acquire better ways of asking and checking. Curiosity supplies appetite; it does not, by itself, distinguish a discovery from a pleasing mistake. A child can imagine an explanation for the radio. To build one, somebody must understand which relationships actually make the voice arrive.

This is the other half of the compass. We descend into the machinery of representation: how to make a distinction precise, follow its consequences, compare an account with what happens, and let someone else inspect the result. There will be symbols. They are less dangerous than the unexamined sentences they replace.

## What the Mirror Leaves Out

Begin with a basket again, but this time as a worked example rather than another memory.

Let a list represent its contents. An empty list reports no listed items. A blank space where the list should be may report that nobody has looked. If the basket cannot be located, that is another condition. A useful representation preserves those distinctions. A careless one files all three under zero and waits for a more complicated system to inherit the error.

In set notation, ∅ has no members; {∅} has one member, the empty set. The distinction is between an empty collection and a collection containing something that is itself empty. Zero can describe the first collection’s cardinality. It does not follow that every symbol for missing information should behave like the number zero.[^v1-phi-i-sets]

In SQL, for example, NULL is not an ordinary value waiting to be compared in the usual way. Ordinary comparisons involving it can yield unknown. That is why testing for NULL requires different treatment from asking whether a recorded quantity equals zero.[^v1-phi-i-null] This little inconvenience preserves a useful confession: the system lacks a value where the question expects one.

A representation is already making commitments. It decides what counts as an item, which properties are recorded, and which differences can be ignored. If the purpose is to count toys, their individual weights may be irrelevant. If the purpose is to load an aircraft, that omission becomes less philosophical.

Mathematics lets us examine the relationships in such a representation without continually consulting the original object. That freedom is immensely productive. It also means we must remember to come back. A flawless calculation inside an inadequate description remains inadequate with excellent arithmetic.

## Structure Before Furniture

Two toys and two toys make four toys, provided the objects remain distinct and we are counting them in the same way. Two drops of water can merge into one larger drop. Arithmetic has not failed. We changed the operation while retaining the label *add*.

Much of mathematical power comes from removing the furniture and retaining the arrangement. A relation can be studied apart from the particular things related. An ordering, a symmetry or a network of connections can recur in different materials. Structure is what remains when you forget the nouns and remember the relevant grammar.

The adjective matters. The same collection can be ordered by size, price or date of arrival, producing different structures. Nothing in the objects announces which order serves our purpose. Abstraction makes a choice explicit enough to reason with; it does not release us from choosing.

A graph, for instance, consists of nodes and connections. It can represent roads between places or obligations among people, while deliberately omitting almost everything else about either. The mathematical results apply to the specified structure. To carry a result back into the world, we must check whether the connections really have the properties the result requires. A friendship does not become an undirected, unweighted edge merely because that is the diagram I know how to draw.[^v1-phi-i-structure]

Logic performs a related separation. In a simple propositional setting, we can write:

$$
P\Rightarrow Q,\qquad P\qquad\therefore Q.
$$

If the premises hold, the conclusion follows. Replace the letters with appropriate statements and the form remains valid. But starting from $Q$ and concluding $P$ reverses the inference without permission. If a specified fault would trigger an alarm, the sounding alarm does not establish that this fault is present. Another fault—or a fault in the alarm—might produce the same signal. We have to inspect the actual direction and conditions, not the emotional resemblance of the sentences.[^v1-phi-i-logic]

Formalization separates syntax—the allowed expressions and transformations—from semantics, their interpretation. A proof follows authorized steps from stated assumptions. Asking whether those assumptions describe an apparatus, a person or a society is additional work. A formal system will not notice that *healthy* was defined as *not yet billed* unless the defect appears in the rules it is permitted to examine.

Once a relationship is specified, we can ask how it changes. Calculus makes rates and accumulation tractable. A derivative concerns local change; an integral can accumulate a quantity across an interval. For a differentiable position function in one dimension, its derivative gives velocity; speed is its magnitude. Reconstructing position from velocity requires the relevant conditions and an initial value: a velocity history alone does not tell us where the journey began.[^v1-phi-i-calculus]

The philosophical temptation is to hear *rate of change* and believe we have explained change itself. We have acquired a powerful description of certain relationships. Whether a particular differential equation captures the process, and what its variables stand for, remain questions for the model and its evidence. This is not a defect in mathematics. It is where mathematics meets its assignment.

## The Sentence with Its Own Address

The chapter introduced Gödel’s upheaval. Here is the machinery at its centre.

A formal proof is a finite arrangement of symbols whose legitimacy can be checked against specified rules. Gödel showed how expressions and proofs could be encoded by natural numbers, so that arithmetical relationships could represent claims about the formal system’s own syntax. Numbers could now do bookkeeping on the reasoning conducted with numbers.

Through a carefully constructed form of self-reference, a sentence could express its own unprovability in the theory. This is not the liar’s sentence announcing that it is false. It is a statement about whether a particular formal proof exists. The coding and the treatment of provability are what turn the apparent parlour trick into mathematics.[^v1-phi-i-godel-coding]

The modern first incompleteness result applies to consistent, effectively axiomatized theories with enough arithmetic: some statements can be neither proved nor disproved there. Gödel’s original two-sided result used a stronger consistency assumption; Rosser later obtained the result from ordinary consistency. Those qualifications keep the theorem from being recruited to explain every unanswered question in a household.[^v1-phi-i-rosser]

The second theorem concerns the theory’s own formal expression of its consistency. With the usual conditions on the theory and its representation of proof, consistency cannot be proved within that same consistent theory. This does not say that contradiction is secretly present, or that proofs cannot be checked. It limits a particular kind of guarantee.[^v1-phi-i-godel-consistency]

The distinction between checking a proposed proof and having a method that settles every proposition is especially valuable. We may be able to inspect a completed route without having a universal procedure for finding—or ruling out—a route to every destination. The failure of the larger promise does not invalidate the smaller achievement.

We could enlarge the theory. We would then owe an account of the new assumptions. There is useful mathematical work in doing so; we have not escaped the question by placing it in a larger office. What interests me here is the discipline of knowing which guarantee was established and which one was only desired. It will become important again when the guarantees arrive in a sales presentation.

## A Machine That Can Read a Machine

Turing gave the notion of a procedure an austere physical imagination: a tape, symbols, a head that reads and writes, a finite repertoire of states, and rules determining the next step. His universal machine could work from an encoded description of another machine. The instructions themselves could be treated as data.[^v1-phi-i-turing]

The familiar halting argument reveals a limit. Suppose a perfect program could decide whether any program, given its input, would eventually stop. Construct a contrary program: given some program’s code, it asks whether that program stops when fed its own code, then loops if the answer is yes and stops if the answer is no. Now feed the contrary program its own code. Either answer defeats the supposed decider. No such total, always-correct decider exists.[^v1-phi-i-halting]

This is a general impossibility, not an announcement that we cannot determine whether an ordinary calculation finishes. Many programs and useful restricted classes can be analysed. The missing instrument is the one that promises a correct answer for every possible case.

Nor is undecidability a synonym for expense. A problem may be decidable in principle and still require absurd resources at the scale we care about. Another may be practical on many inputs without admitting a universal decision procedure. “The computer cannot do it” can conceal several different explanations; purchasing a faster computer addresses only some of them.

There is an oddly domestic consequence. Our machines can manipulate descriptions of procedures, including descriptions of machines like themselves, without thereby acquiring a final view from outside all procedure. That is a fact about computation’s reach. Whether a machine understands, experiences or should be trusted in a particular role requires further arguments. The tape does not settle those questions on our behalf.

## Giving the World a Way to Answer

A proof can establish what follows inside a formal framework. The world has no obligation to instantiate the framework we find most convenient. To discover whether it does, we need contact.

Scientific measurement is organized contact. We specify a quantity—the *measurand*—and a procedure for obtaining a value attributable to it. Calibration connects an instrument’s indications to reference values, with uncertainty accounted for. A result belongs to an operation, conditions and a chain of comparison; the number alone is an orphan.[^v1-phi-i-metrology]

Imagine a thermometer whose readings fluctuate. Repetition may help characterize the variation. It cannot, by itself, reveal a stable offset affecting every reading. The instrument can be impressively consistent about being wrong. To detect that error, we need an appropriate comparison or another way of testing the measurement arrangement. In this hypothetical example, precision and closeness to the reference are different achievements.

The choice of quantity also matters. Measuring temperature at one location is not automatically a measurement of an entire room’s thermal conditions, still less its occupants’ comfort. Each extension introduces assumptions. A sensor can be accurate about what it measures while the system using it is wrong about what the reading means.

At the quantum scale, the encounter between system and apparatus belongs within the physical account. Measurement interactions can correlate their states; interaction with the environment can suppress observable interference between alternatives in the subsystem description. Decoherence helps explain the emergence of stable, effectively classical records. It does not, by itself and without interpretive commitments, settle every part of the measurement problem.[^v1-phi-i-decoherence]

There is no need to install a human mind at the centre of every such process. Nor is there an agreed little border booth at which the quantum world becomes classical whenever a person looks. The relevant physical interactions and the interpretation of their results must be distinguished.[^v1-phi-i-quantum-records]

This is where I would plant the more adventurous question from the chapter. If one physical system can retain a trace of another, might our human experience belong to a much longer development of registration, memory and modelling? The question is mine. Calling the early stages *experience* would be a deliberate extension of the word, not a finding that the apparatus has sensations. We can follow the possibility through physics and biology without asking the metaphor to impersonate a result.

Meanwhile, even ordinary measurement has already complicated our position. We are arranging an encounter through which something about the world becomes legible. The arrangement need not invent the property it measures. But it determines the form, resolution and reliability of the answer available to us.

## Facts with a Return Address

A scientific account must do more than accommodate what we already know. We want to know what follows from it, what would count against it, and whether another account would lead us to expect something different. Popper made the exposure to possible refutation central to his account of scientific testing.[^v1-phi-i-popper] A story compatible with every conceivable observation has purchased its invulnerability by giving up a particularly useful kind of contact.

There is no single ritual that every science performs. We cannot rerun the formation of a galaxy at a more convenient hour. We can compare consequences, seek independent traces, exploit naturally occurring differences, and conduct experiments where intervention is possible. What matters is the disciplined relation between the proposed account and the evidence it has to face.

Suppose a model predicts how a material will respond under load. We can derive an expected response, measure what happens, and examine the mismatch. But a discrepancy alone does not tell us which part failed. The model may be inadequate; the specimen may differ from our description; the load or deformation may have been measured badly. The reasoning must examine the whole arrangement that connected hypothesis to observation.

This is where the tidy school diagram of scientific method usually runs out of boxes. Hypotheses, apparatus, classifications and background knowledge meet in the test. We need criticism directed at their connections, and ways to make one explanation of a discrepancy compete with another. Duhem drew attention to this dependence of physical tests on a body of assumptions, rather than an isolated sentence.[^v1-phi-i-duhem]

A fact does not become somebody’s whim because establishing it required instruments and interpretation. The dependence tells us where to inspect the account. We can improve a procedure, compare independent approaches, identify a source of error, or discover that something thought general holds only within a narrower range.

What I want science to replace in our myths is the privilege of being protected from that work. The new account may be stranger than the old story. It should also offer better means of finding out where it fails. Otherwise we have exchanged the costumes while retaining the priesthood.

The social arrangements of inquiry matter because the individual investigator is capable of attachment, exhaustion and self-deception. Another person needs enough information to inspect the route: what was measured, how the data were handled, which assumptions entered, and what happened when the analysis was repeated. Computational reproducibility and replication with new data test different parts of that route.[^v1-phi-i-reproduction]

The distinction is useful well outside a laboratory. A chart without its denominators, a result without its conditions, or a benchmark without the test that produced it can travel faster than the knowledge it claims to carry. A fact should have a return address. Someone ought to be able to ask how it got here.

## Chance Is Not Permission to Guess

Uncertainty needs arithmetic too. Probability relates events within a specified model. Statistical inference uses observations to learn about quantities, relationships or competing accounts, while depending on assumptions about how the observations arose. The direction of reasoning matters: the chance of a signal given a fault is different from the chance of a fault given a signal.

Consider an invented population of ten thousand machines. One hundred have a particular fault. Suppose a detector catches ninety of those, but also falsely flags five per cent of the other 9,900. It produces 90 justified alarms and 495 false ones. Among the 585 flagged machines, only about fifteen per cent have the fault.

The detector caught ninety per cent of the faults. A flagged machine was still much more likely to be healthy than faulty. Both statements can be true because they answer different questions. The missing ingredient in the careless inference was how rare the fault was to begin with.[^v1-phi-i-bayes]

Bayesian reasoning makes such reversals explicit: evidence changes the relative plausibility of alternatives through how well each would have predicted it, together with their prior plausibilities. The mathematics does not supply an honest prior, a complete set of alternatives or a trustworthy sensor. It tells us what follows when those ingredients have been specified. A bad premise can survive a very elegant update.

There are other statistical traditions and other questions. A p-value, for example, is not the probability that the hypothesis being tested is true, and crossing a conventional threshold does not establish an effect’s importance. The American Statistical Association has had to say this explicitly, which suggests that mathematical notation is not immune to becoming a ceremonial object.[^v1-phi-i-pvalues]

An estimate should carry the uncertainty appropriate to the question, including weaknesses that a narrow interval cannot capture. Repeating a biased sampling process can make its answer more stable without making it representative. If the relevant people or events were excluded from the observations, additional decimal places will not invite them back.

What we are learning is a habit of keeping the operation attached to its result. The probability belongs to a model and information. The estimate belongs to a sampling and inferential procedure. The conclusion belongs to assumptions whose survival matters. This may look like administrative fussiness. It is how the apparatus remains available for correction instead of becoming an oracle with a maintenance contract.

## When Logic Learned to Click

Formal operations can be embodied. Boole’s nineteenth-century algebra of logic made systematic calculation possible with logical relationships. In his 1938 paper on relay and switching circuits, Shannon connected an algebraic treatment to the analysis and construction of switching arrangements.[^v1-phi-i-switching]

For a simple idealization, two switches in series allow a conducting path only when both are closed; parallel paths permit conduction when either is closed. That physical arrangement can realize the chosen AND or OR relation. The mapping is a design achievement, not a claim that copper has understood conjunction.

From such realizations we can assemble arithmetic and control. We can also store descriptions, manipulate them, and build systems that operate on representations of other systems. The mathematical relationship becomes something with timing, tolerances, heat and failure modes. The abstract operation may be exact; the apparatus still has to function. Interlude 1 will take us further into that material obligation.

Learning adds another route to useful behaviour: adjusting a model using data and feedback rather than specifying every desired response individually. The results can be striking, but performance on examples and formal assurance about a property remain different achievements. They can also cooperate. AlphaProof, for instance, used learning alongside formal proof construction and checking; it is already a counterexample to the claim that learned systems can only imitate and never contribute to proof.[^v1-phi-i-learning-proof]

The important boundary therefore runs between kinds of warrant, not neatly between humans who understand and machines which supposedly just calculate. A human may guess; a machine may deliver a checkable proof. Either may produce something that works within a tested range and fails outside it. We should inspect the accomplishment before deciding which flattering story to tell about its author.

The detailed architectures can wait. At this entrance to the Silicon mirror, the important inheritance is already visible. We choose what can be represented, how a claim is evaluated, and what counts as success. Later systems will act within those choices, sometimes at a scale that makes their original smallness difficult to remember.

## The Instrument Goes Outside

The child’s radio question survives the journey in better shape. A voice arriving from somewhere unseen becomes a chain of physical processes that can be described, built, tested and repaired. The explanation can make the event more remarkable by revealing how many relationships it depends upon.

That is the sort of disenchantment I can live with.

The tools we have inspected do different work. Proof follows consequences under formal assumptions. Measurement makes specified aspects of the world available for comparison. A model concentrates relationships we want to understand. Empirical inquiry tests the fit; probability helps us handle what the available information does not settle. None acquires the duties of all the others merely by being useful.

We can now ask sharper questions without claiming a view from nowhere. What did we represent? What did we omit? Which conclusion follows inside the representation, and what makes it applicable outside? At what point did a useful device begin pretending to be the world?

Later, our instruments will look increasingly like ourselves. They will speak, organize, advise, perhaps expose habits we had mistaken for uniquely human depth. For now, it is enough to have made the mirror inspectable. We can consider what it preserves before becoming attached to the face in it.

The next chapter turns toward the physical world on which every symbol here has depended. Whatever we decide about knowledge, the marks must exist somewhere. The machine must have a body. Even this question has required a little matter to carry it.

We have been discussing what follows.

Now we meet what was there first.

![](../../manuscripts/assets/shared/separator.png)

> ***Maggie:** Did we prove the basket was there?*
>
> ***Alex:** We proved what followed if it was.*
>
> ***Maggie:** So someone still has to look?*
>
> ***Alex:** I was hoping you would.*

<!-- SOURCE NOTES: stable IDs; retain when moving this draft into the manuscript. -->

[^v1-phi-i-sets]: Eric Lehman and F. Thomson Leighton and Albert R. Meyer, [Mathematics for Computer Science](https://courses.csail.mit.edu/6.042/spring18/mcs.pdf) (2018). §§4.1 and 4.5. The cardinalities of ∅ and {∅} are respectively zero and one.

[^v1-phi-i-null]: PostgreSQL Global Development Group, [PostgreSQL 18 Documentation: Comparison Functions and Operators](https://www.postgresql.org/docs/18/functions-comparison.html). §9.2. Ordinary comparisons involving NULL and the dedicated IS NULL predicate perform different operations.

[^v1-phi-i-structure]: Eric Lehman and F. Thomson Leighton and Albert R. Meyer, [Mathematics for Computer Science](https://courses.csail.mit.edu/6.042/spring18/mcs.pdf) (2018). Chapter 12 opening and §12.1. The friendship example is the author’s illustration of the modelling choice, not an empirical finding about friendship.

[^v1-phi-i-logic]: Eric Lehman and F. Thomson Leighton and Albert R. Meyer, [Mathematics for Computer Science](https://courses.csail.mit.edu/6.042/spring18/mcs.pdf) (2018). §1.4.1, modus ponens and sound inference rules. The alarm example contrasts modus ponens with the invalid converse inference known as affirming the consequent.

[^v1-phi-i-calculus]: Silvanus P. Thompson, [Calculus Made Easy](https://www.gutenberg.org/cache/epub/33283/pg33283-images.html) (1914), Macmillan and Co.. Chapters VIII and XVII–XIX. The prose specifies differentiability and one-dimensional motion; integrating velocity requires an initial position to recover a particular position history.

[^v1-phi-i-godel-coding]: Kurt Gödel, [Über formal unentscheidbare Sätze der Principia Mathematica und verwandter Systeme I](https://homepages.uc.edu/~martinj/History_of_Logic/Godel/Godel%20%E2%80%93%20On%20Formally%20Undecidable%20Propositions%20of%20Principia%20Mathematica%201931.pdf) (1931), *Monatshefte für Mathematik und Physik* 38: 173–198. §§1–2 and Proposition VI, in B. Meltzer’s English translation. The self-reference concerns formal provability, not the liar paradox.

[^v1-phi-i-rosser]: J. Barkley Rosser, [Extensions of some theorems of Gödel and Church](https://www.cambridge.org/core/journals/journal-of-symbolic-logic/article/abs/extensions-of-some-theorems-of-godel-and-church/0461E34DC1F219C459EE84CC2FA89068) (1936), *The Journal of Symbolic Logic* 1(3): 87–91. Opening statement of the strengthening from omega-consistency to ordinary consistency. The terminology in the prose is modernized; the result still requires an effective theory of sufficient arithmetical strength.

[^v1-phi-i-godel-consistency]: Kurt Gödel, [Über formal unentscheidbare Sätze der Principia Mathematica und verwandter Systeme I](https://homepages.uc.edu/~martinj/History_of_Logic/Godel/Godel%20%E2%80%93%20On%20Formally%20Undecidable%20Propositions%20of%20Principia%20Mathematica%201931.pdf) (1931), *Monatshefte für Mathematik und Physik* 38: 173–198. §4, Proposition XI. The claim concerns the theory’s standard formal representation of its own consistency under the theorem’s conditions.

[^v1-phi-i-turing]: Alan M. Turing, [On Computable Numbers, with an Application to the Entscheidungsproblem](https://www.cs.virginia.edu/~robins/Turing_Paper_1936.pdf) (1936), *Proceedings of the London Mathematical Society* s2-42: 230–265. §§1–2 and 6.

[^v1-phi-i-halting]: Alan M. Turing, [On Computable Numbers, with an Application to the Entscheidungsproblem](https://www.cs.virginia.edu/~robins/Turing_Paper_1936.pdf) (1936), *Proceedings of the London Mathematical Society* s2-42: 230–265. §8. The draft uses the modern halting presentation of diagonalization, rather than reproducing Turing’s circle-free-machine argument verbatim.

[^v1-phi-i-metrology]: Joint Committee for Guides in Metrology, [International Vocabulary of Metrology: Basic and General Concepts and Associated Terms (VIM)](https://www.bipm.org/documents/20126/2071204/JCGM_200_2012.pdf) (2012). §§2.1, 2.3, 2.15, 2.17, 2.26 and 2.39. The thermometer and room examples are hypothetical. Repeated readings alone need not reveal a shared systematic offset.

[^v1-phi-i-decoherence]: Maximilian Schlosshauer, [Decoherence, the measurement problem, and interpretations of quantum mechanics](https://arxiv.org/abs/quant-ph/0312059) (2005), *Reviews of Modern Physics* 76: 1267–1305. Introduction and §§II, III.D and IV.A. Decoherence and the interpretation of definite outcomes are distinguished; no consciousness-induced collapse is asserted.

[^v1-phi-i-quantum-records]: Wojciech H. Zurek, [Decoherence, einselection, and the quantum origins of the classical](https://arxiv.org/abs/quant-ph/0105127) (2003), *Reviews of Modern Physics* 75: 715–775. Discussion of measurement, environmental monitoring and stable correlations. The text does not assert a unique settled quantum/classical boundary or equate a physical record with subjective experience.

[^v1-phi-i-popper]: Karl R. Popper, [Conjectures and Refutations: The Growth of Scientific Knowledge](https://www.inf.fu-berlin.de/lehre/SS06/materials/eng/PopperScience.pdf) (1963), Routledge and Kegan Paul. Chapter 1, section I, especially numbered conclusions 1–7. The linked essay excerpt predates its inclusion in the 1963 collection. Falsifiability is presented as one influential account of scientific testing.

[^v1-phi-i-duhem]: Pierre Duhem, [The Aim and Structure of Physical Theory](https://thehangedman.com/teaching-files/hps/duhem.pdf) (1954), Princeton University Press. Part II, chapter VI, §2. The material-under-load illustration is the author’s application of the argument, not Duhem’s example.

[^v1-phi-i-reproduction]: National Academies of Sciences, Engineering, and Medicine, [Reproducibility and Replicability in Science](https://www.nationalacademies.org/read/25303/chapter/6) (2019), The National Academies Press. Chapter 3, Defining reproducibility and replicability. Following this report’s usage: reproducibility concerns results from the same data and computational procedures; replication uses newly collected data. Usage varies by field.

[^v1-phi-i-bayes]: Thomas Bayes, [An Essay towards solving a Problem in the Doctrine of Chances](https://www2.isye.gatech.edu/isyebayes/bank/Bayesessay.pdf) (1763), *Philosophical Transactions* 53: 370–418. Section I, conditional probability propositions. The detector example is invented: 100 × 0.90 = 90 true alarms; 9,900 × 0.05 = 495 false alarms; 90/585 ≈ 15.38%. The modern update description is not a quotation from Bayes.

[^v1-phi-i-pvalues]: American Statistical Association, [American Statistical Association Releases Statement on Statistical Significance and P-Values](https://www.amstat.org/asa/files/pdfs/p-valuestatement.pdf) (2016). Principles 2, 3 and 5.

[^v1-phi-i-switching]: George Boole, [An Investigation of the Laws of Thought](https://www.gutenberg.org/files/15114/15114-pdf.pdf) (1854), Walton and Maberly; Claude E. Shannon, [A Symbolic Analysis of Relay and Switching Circuits](https://tubes.mit.edu/6S917/_static/2025/resources/shannon38.pdf) (1938), *Transactions of the American Institute of Electrical Engineers* 57: 713–723. Boole, chapters II–III; Shannon, §§I–II. The switch illustration takes conduction as true. Shannon’s original hindrance notation uses zero for a closed circuit and one for an open one.

[^v1-phi-i-learning-proof]: Google DeepMind, [AI achieves silver-medal standard solving International Mathematical Olympiad problems](https://deepmind.google/blog/ai-solves-imo-problems-at-silver-medal-level/) (2024). AlphaProof: a formal approach to reasoning. This is the research team’s report about a particular system, not a claim that all learned systems supply proofs or that a proof establishes general understanding.
