![](../assets/shared/interlude-gear.png)

INTERLUDE ∅

# The Edges of Reason

*From Gödel's Paradox to the Silicon Mind*

*INQUIRY*

**ONTOLOGIST'S JOURNAL** --- _Coordinates: Indeterminate_ --- _Subject: The Emergent Thought_

**Inquiry I.** --- _On the baseline testing of physical boundaries and containment (reconstructed; the subject was not available for comment)._

> "What will happen if I throw this vase on the floor? Can I chew my way out of this crib?"

**Inquiry II.** --- _An inquiry into the necessity of predatory reptiles._

> "Mom, why did God create snakes?"

**Inquiry III.** --- _On the early confrontation with eschatology._

> "Mom, the night watchman was saying that according to scripture the world will end in ten years. Is this true? ... Oh, so he is saying this because he's old and he thinks he will die. Does this mean that the world will end for him? ... I wish people didn't die."

**Inquiry IV.** --- _On the mechanics of invisible atmospheric phenomena._

> "Dad, where inside the radio is that thing that takes the wave thing and make it into sound? Why can't we see these waves, what would they look like if we could see them? Where do they come from? How does the antenna find them?"

**Inquiry V.** --- _A proposal for an enclosed ecological experiment._

> "Dear uncle, what will happen if you put a gecko and a mouse in a box? What will they do? What if we add a frog?"

**Inquiry VI.** --- _On technological forecasting and youthful ambition._

> "Dad, will we have flying cars in the future? I will invent them when I grow up."

**Inquiry VII.** --- _On the futility of enforced routine and domestic order._

> "Why do they make me go to the school every day? Why should I make my bed if I have to take the bedcover off in the night anyway?"

**Inquiry VIII.** --- _On the apparent paradox of planetary gravitation._

> "I know the earth is round and we live on all sides of it, like this globe. But if I put things on this globe they fall off, especially from the bottom. But we are not stuck to earth, why don't we fall down? Why is it so special? Why is it not like this globe in space? Why doesn't this globe have gravity then?"

**Inquiry IX.** --- _On animal consciousness and the ethics of consumption._

> "Do dogs think? It seems like sometimes they are thinking? ... Why do we eat animals? Why does it feel okay to eat plants though?"

**Inquiry X.** --- _On the arbitrary distribution of wealth and divine equity (asked aloud more than once, and later only of myself)._

> "Why are some people more poor? What makes them poor? Would a just God make half of the people poor?"

**Inquiry XI.** --- _On the incomprehensibility of infinite space and linear time._

> "If time has no beginning then that makes no sense, but if time started at some point, then what was before then, and that puts us back to where we started (literally, and figuratively). If space ends somewhere, then what's on the other side, and so on; but if all this never ends, then that is also difficult to imagine."

(Roughly in order of how grown-up the questions became, not the boy.)

## One Thousand and One Lamps

They sound silly because they are real: a child's actual questions, retrieved from the unorganized Trash folder of my mental storage, where they somehow survived the "permanently delete" button. Some were only thought, some were asked out loud, and all could easily have been dismissed. A few got cleaned up in the rituals of learning and growing up. Others stuck around unresolved, like a broken shoelace: not long enough to tie, but just long enough to make you stop and tug at the two frayed ends in fits and starts. What embarrasses this subject (me) more than the questions is that I could be embarrassed by them while leaving established thinking unchallenged.

Civilization has never been any more immune to questions of its own. Something deep always turns out to be permanently AWOL, while the window dressing stays exquisitely full. Growing up doesn't cure these questions; their language just slogs up a few rungs of the sophistication ladder. The same goes for the collective. The stories get better, but never fully real, and admitting that can even be a virtue. Ignoring the questions as bliss would take a very large rug to sweep them under, so we should answer them where we can and keep the rug as small as possible. And remember that flying rugs are just that: floating over dust bowls of illusion, turtles of dust all the way down.

Looking back at even that over-curious child, what strikes me as odd is not the questions but the lack of them: how much I didn't question, and accepted as baseline reality on experience or on someone's word. Curiosity and innovation may be our superpowers, but humans are even better at the opposite trait: object permanence, quick center-surround conclusions made in survival-seconds. And when that kind of settlement cracks into questions, it is even more unsettling, like a basket you can no longer see from your seat.

## Down Under the Magic Rug

One of those questions stayed with me longer than the rest, though not because it was the deepest. The night watchman sometimes told us stories. Now, it seemed, he was becoming one himself, a story with an ending already scheduled, and the world he said would end was somehow both his and ours. My mother's answer didn't add up for me at first: his dying and the world ending were two different things. I remember the oddness of it more than the sadness, though the sadness was real and close. Two realities inside one reality, his on a plane that was splitting away from mine. I had no words for any of that. I had a follow-up question, and a wish that people didn't die.

That's the trouble with children's questions: they arrive long before the tools to handle them. The tools do exist, though, and some were invented for exactly this kind of trouble. How do you tell an empty answer from a missing one? How do you keep track of which reality a statement belongs to? How do you follow a conclusion without smuggling in a wish? How do you measure what you can't see, like the waves an antenna somehow finds?

So this interlude goes down under the rug, to the machinery beneath the aiming arm. The chapter was about how we aim. Down here the floor is covered in chalk: symbols, sets and graphs, a 1920s mathematician muttering about completeness in one corner, and on the workbench a computer that hums quietly and pretends not to know it was built on all of this. We'll take it in roughly the order the questions demand: first how to represent a thing, then how its parts relate, then what could be, what follows, what can be computed, and what can be measured.

The last question on the list, about time with no beginning and space with no edge, stays on the table. It belongs to the next chapter, which has the nerve to try.

## What the Mirror Leaves Out

Start with the basket again, this time as a worked example rather than a memory.

Suppose a list represents its contents. An empty list says there are no items. A blank where the list should be may only mean that nobody has looked. And a basket nobody can find is a third condition altogether. A good representation keeps those three apart. A careless one files all of them under zero and waits for some more complicated system to inherit the error.

Mathematics has a clean way to hold the first distinction. The empty set, written ∅, has no members. The set {∅} has exactly one member, and that member happens to be the empty set: a basket containing an empty basket, which is not at all the same as an empty basket. The number of members of the first is zero; the number of members of the second is one.[^v1-phi-i-sets]

That small difference turns out to be astonishingly productive, and John von Neumann (whom we last saw reading Gödel's mail) found a way to build every natural number out of it. Call ∅ zero. Call {∅} one. Call {∅, {∅}} two, the set containing everything built so far, and keep going. With nothing but the empty set and the act of collecting, you can climb to any number you like.[^v1-phi-i-ordinals](https://file+.vscode-resource.vscode-cdn.net/Users/samseatt/projects/book-poma/work/sam/!--%20TODO:%20source%20the%20von%20Neumann%20construction%20of%20the%20natural%20numbers%20\(John%20von%20Neumann,%20%22Zur%20Einf%C3%BChrung%20der%20transfiniten%20Zahlen,%22%201923,%20or%20a%20standard%20set%20theory%20text\).%20The%20creation-story%20framing%20is%20the%20author's,%20with%20the%20stated%20caution.%20--) It is the closest thing mathematics offers to a creation story, and I want to be careful with it, since a definition is not a cosmological event. But it does teach one thing the next chapter will need. Structure doesn't always need prior stuff to be built from. Sometimes it needs only a distinction and the patience to repeat it.

Databases need a different kind of care. In SQL, the language behind most of the world's business records, a missing value is written NULL, and NULL is not a number waiting to be compared in the usual way. Ask whether a NULL equals zero, and the answer is neither yes nor no but _unknown_. Ask whether a NULL equals another NULL, and the answer is still _unknown_. It may be the most honest thing a database ever says. To find missing values, you have to ask a different question (IS NULL) instead of pretending that absence is a quantity.[^v1-phi-i-null] The little inconvenience preserves a useful confession: the system lacks a value where the question expects one.

Every representation is already making commitments, then. It decides what counts as an item, which properties get recorded, and which differences can be ignored. If the purpose is to count toys, their individual weights don't matter. If the purpose is to load an aircraft, that omission becomes much less philosophical.

This is the sense in which a model is a mirror, and why it matters what the mirror leaves out. Mathematics lets us study the relationships in a representation without constantly consulting the original object, and that freedom is enormously productive. It also means we have to remember to come back. A flawless calculation inside an inadequate description is still inadequate, now with excellent arithmetic.

## Structure Before Furniture

Two toys and two toys make four toys, provided the toys stay distinct and we count them the same way. Two drops of water, on the other hand, can merge into one larger drop. Arithmetic hasn't failed. We changed the operation while keeping the label _add_.

Much of mathematics' power comes from removing the furniture and keeping the arrangement. A relation can be studied apart from the particular things it relates, and an ordering, a symmetry or a network of connections can turn up again in completely different materials. Structure is what remains when you forget the nouns and remember the relevant grammar. The adjective _relevant_ is doing real work there. The same collection can be ordered by size, by price or by date of arrival, producing three different structures, and nothing in the objects announces which order serves our purpose. Abstraction makes a choice explicit enough to reason with; it doesn't release us from choosing.

A graph is the simplest piece of furniture-free architecture: nodes, and edges connecting some of them. It can represent roads between towns or obligations between people while deliberately ignoring almost everything else about either. The results proved about a graph apply to the graph. To carry one back into the world, we have to check that the real connections have the properties the result requires. A friendship doesn't become an undirected, unweighted edge just because that's the diagram I know how to draw.[^v1-phi-i-structure]

The chapter introduced a trick worth doing properly here, because the rest of the book leans on it. Take any graph and build a new one, its _line graph_, in which every edge of the old graph becomes a node, and two of these new nodes are connected whenever their old edges shared an endpoint.[^v1-phi-i-linegraph](https://file+.vscode-resource.vscode-cdn.net/Users/samseatt/projects/book-poma/work/sam/!--%20TODO:%20source%20the%20line%20graph%20definition%20\(e.g.,%20Frank%20Harary,%20*Graph%20Theory*,%201969,%20chapter%20on%20line%20graphs\).%20The%20roundabout%20example%20\(the%20line%20graph%20of%20a%20four-pointed%20star%20is%20a%20complete%20graph%20on%20four%20nodes\)%20and%20the%20emergence%20reading%20are%20the%20author's.%20--) Try it on the simplest interchange: four roads meeting at one roundabout. In the original graph, the roundabout is a hub with four spokes. In the line graph, the hub disappears entirely, and the four roads become four nodes, every one connected to every other, a tight little clique. The roundabout hasn't vanished, exactly; it has turned into the fact that every road is now a neighbor of every road. What used to be a place has become a relationship, and what used to be relationships have become the places.

Do it again, and the line graph of the line graph is a structure of relations among relations. There's no limit in principle, and each round answers different questions from the last. That's the formal skeleton of the emergence picture from the chapter. On its own, it's just bookkeeping; a new level only becomes interesting when there are enough nodes for crowd behavior and something that drives a transition. But it shows that "turning edges into nodes" isn't a metaphor I invented to make a point. It's an operation with rules, and it can be carried out by anyone with a pencil.

Logic performs a related separation of form from furniture. In the simplest setting, we can write:

P⇒Q,P∴ Q.P⇒Q,P∴ Q.

If the premises hold, the conclusion follows, whatever statements we put in place of the letters. The chapter's basket ran this form backward, and so does almost everyone, almost daily: starting from QQ and concluding PP. If a particular fault would trigger an alarm, the alarm sounding doesn't establish that this fault is present. Another fault could produce the same signal, and so could a fault in the alarm itself. We have to check the actual direction and conditions of the inference, not the family resemblance between the sentences.[^v1-phi-i-logic]

Formalization also separates _syntax_, the allowed expressions and the rules for transforming them, from _semantics_, what they're taken to mean. A proof follows authorized steps from stated assumptions. Whether those assumptions describe an engine, a person or a society is additional work, and the formal system won't do it for you. It will not notice that _healthy_ has been defined as _not yet billed_ unless the defect shows up in the rules it's allowed to examine. (Volume II will meet a few institutions that run on definitions like that.)

## The Futures That Didn't Arrive

Once a relationship is specified, we can ask how it changes, and for that humanity has calculus, invented independently by Isaac Newton and Gottfried Leibniz in the late seventeenth century. (The two men who gave us the mathematics of change then spent years refusing to change their minds about who had got there first.)[^v1-phi-i-priority](https://file+.vscode-resource.vscode-cdn.net/Users/samseatt/projects/book-poma/work/sam/!--%20TODO:%20source%20the%20Newton%E2%80%93Leibniz%20priority%20dispute%20\(e.g.,%20A.%20Rupert%20Hall,%20*Philosophers%20at%20War*,%201980\).%20--) A derivative describes change at an instant: how fast something is moving right now, not on average over the trip. An integral accumulates: add up all those instants of motion, and you get how far you've gone. For a position that changes smoothly along a line, the derivative is velocity, and integrating the velocity gives back the distance traveled.[^v1-phi-i-calculus]

There's a catch, and it's a lovely one. A complete record of a plane's velocity, every turn and every change of speed, still won't tell you where the plane took off. You need a starting point. Calculus can reconstruct a journey from its changes only if somebody, somewhere, supplies the origin. (Hold that thought until Chapter 1, which has the same problem with a much larger aircraft.)

The philosophical temptation here is to hear _rate of change_ and believe we've explained change itself. We've acquired a powerful description of certain relationships. Whether a particular equation captures a real process, and what its variables actually stand for, are questions for the model and its evidence. That isn't a defect in mathematics. It's where mathematics meets its assignment.

It's also where prediction lives, and prediction is where the Inquiries get their revenge. Inquiry VI asked my father whether we'd have flying cars, and announced that I would invent them. My father, gently, agreed that someday cars would fly, and left it to time to decide whether his son would be the one to build them. Time has so far declined to comment. A few prototypes have hovered over trade shows, but the sky over my commute (these days, from one room of the house to the next) remains disappointingly free of traffic.

The general lesson is less personal. Every past was full of futures once. Some arrived on schedule, some arrived in disguise (we were promised flying cars and received a telephone that knows where we parked), and some are still waiting in the departures lounge. A trend line is a derivative stretched past the data that earned it. It can be exactly right, until the thing driving it changes, and the line, having no way of knowing, keeps going. The alarm clock from the chapter rang every morning for the same reason.

## Chance Is Not Permission to Guess

Uncertainty needs arithmetic too. Probability works out how likely events are within a specified model. Statistical inference uses observations to learn about the world, and depends on assumptions about how the observations came to be. The direction of the reasoning matters enormously. The chance of seeing a signal, given a fault, is not the chance of a fault, given the signal, and confusing the two is how intelligent people end up terrified by accurate tests.

Here's an invented example. Take ten thousand machines, one hundred of which have a particular fault. A detector catches ninety of those hundred, which sounds excellent. It also falsely flags five percent of the 9,900 healthy machines, which sounds tolerable. Do the sums: 90 true alarms and 495 false ones. Among the 585 machines flagged, only about fifteen percent actually have the fault.

So the detector catches ninety percent of faults, and yet a flagged machine is still far more likely to be healthy than faulty. Both statements are true because they answer different questions. The ingredient the careless reader forgot was how rare the fault was to begin with.[^v1-phi-i-bayes] (If a doctor ever tells you a positive result from a ninety-percent-accurate test means you're ninety percent likely to be sick, it's worth asking, politely, how common the illness is. Then it's worth asking for a second test.)

Thomas Bayes gave his name to the reasoning that handles such reversals explicitly: evidence shifts the relative plausibility of competing explanations according to how well each one would have predicted it, starting from how plausible each was beforehand. The mathematics doesn't supply an honest starting point, a complete list of alternatives or a trustworthy sensor. It tells you what follows once you've supplied them. A bad premise can survive a very elegant update.

Other statistical traditions ask other questions. A p-value, for instance, is not the probability that the hypothesis being tested is true, and clearing a conventional threshold doesn't show that an effect matters. The American Statistical Association felt obliged to say this in a formal statement in 2016,[^v1-phi-i-pvalues] which suggests that even mathematical notation can become a ceremonial object, recited more than understood.

An estimate should also carry the uncertainty appropriate to the question, including weaknesses no narrow interval can capture. Repeating a biased sampling process makes its answer more stable without making it more representative. If the relevant people or events were left out of the observations, additional decimal places won't invite them back.

What all of this teaches is a habit: keep the operation attached to its result. A probability belongs to a model and the information fed into it. An estimate belongs to a sampling procedure. A conclusion belongs to assumptions whose survival matters. That may look like administrative fussiness. It's how the apparatus stays available for correction, instead of becoming an oracle with a maintenance contract.

## A Space of Possibilities

Probability needs something to range over, and mathematicians call that something a space. Flip a coin and the sample space has two members, heads and tails; roll a die and it has six. It's the set of everything that could happen, written down before anything does, which makes it the most patient object in mathematics.

Physics generalized the idea. The _state_ of a swinging pendulum, everything you'd need to predict its future, comes down to two numbers: where it is and how fast it's moving. Plot those two numbers as a point on a plane, and every possible state of the pendulum is a point somewhere on that plane, called its state space (or phase space). The pendulum's whole life becomes a curve traced through it, a loop if nothing slows it down, and a spiral that winds inward as friction takes its toll. The space contains every swing the pendulum could ever make. The physics decides which path it actually takes.

Quantum mechanics changed the rules of that space in a way that still unsettles people who understand it best. The state of a quantum system is described by a vector in what mathematicians call a Hilbert space, named for the same David Hilbert whose completeness program Gödel overturned. (Hilbert lost the war for the foundations and got a space named after him anyway, which is more than most generals manage.) It was von Neumann, making his third appearance in these pages, who set quantum mechanics on that footing in 1932.[^v1-phi-i-hilbert](https://file+.vscode-resource.vscode-cdn.net/Users/samseatt/projects/book-poma/work/sam/!--%20TODO:%20source%20Hilbert%20space%20and%20its%20naming;%20John%20von%20Neumann,%20*Mathematische%20Grundlagen%20der%20Quantenmechanik*%20\(1932\);%20the%20Born%20rule%20\(Max%20Born,%201926\);%20and%20the%20pendulum%20phase-space%20example%20\(any%20standard%20mechanics%20text\).%20The%20%22possibilities%20bearing%20on%20possibilities%22%20reading%20is%20the%20author's%20framing%20for%20Chapter%201.%20--)

Three features of a Hilbert space matter for this book. First, possibilities can be added together. A quantum system can be in a combination, a superposition, of states that would be mutually exclusive in a coin-and-die world, each weighted by a number called an amplitude. Second, because amplitudes can be negative (or, more exactly, complex), possibilities can cancel each other out as well as reinforce each other. That's interference, and it's why the arithmetic of quantum chance is not the arithmetic of ordinary chance. The probabilities we eventually observe come from the squared sizes of the amplitudes, a rule named after Max Born. Third, and strangest, two systems can share a joint state that can't be split into a state for each one separately. This is entanglement. The possibilities of the pair are more than the possibilities of its members; a basket, so to speak, whose contents can't be described toy by toy.

It's tempting to say all of this in a hushed voice, and physicists talk about Hilbert space as though they had moved there. But it's worth keeping two things apart. Hilbert space is mathematics, an exquisitely successful description of how quantum systems behave and what we'll observe when we measure them. What it says about what reality _is_, underneath the description, is the subject of interpretations that have been arguing, courteously and otherwise, for nearly a century.

Chapter 1 will start from exactly this space: possibilities, bearing on other possibilities, entangled before anything is decided. For now it's enough to notice that the most precise physical theory we have is written, at bottom, in the language of what could be.

## The Sentence with Its Own Address

The chapter told the story of Gödel's upheaval. Here is the machinery at its center, and it's more ingenious than it is difficult.

Start with bookkeeping. A formal proof is a finite string of symbols whose legitimacy can be checked against fixed rules. Gödel's first move was to give every symbol a number, and then to turn any string of symbols into a single number as well. One way to do it: take the symbols' numbers in order and use them as powers of successive primes, so that a string whose symbols are numbered 3, 1 and 4 becomes 2³ × 3¹ × 5⁴. Because every whole number breaks into primes in exactly one way, the original string can always be recovered from its number. Every formula now has a unique street address, and so does every proof (a proof is just a very long street). The payoff is that statements _about_ formulas, such as "this string is a proof of that formula," become statements about numbers, which arithmetic is perfectly equipped to discuss. Arithmetic could now gossip about itself.[^v1-phi-i-godel-coding]

The second move was self-reference. Using that bookkeeping, Gödel built a sentence, call it G, which says, in effect: _the formula at address g has no proof_, where g turns out to be G's own address. This is not the old liar's sentence ("This sentence is false"), which is a paradox about truth and goes nowhere. G is about provability, and that makes all the difference. The liar's sentence is a party trick; Gödel's is a party trick that passed peer review.

Now reason about G. If the system could prove G, it would be proving that G has no proof while holding one in its hand, which would make the system inconsistent. So if the system is consistent, G has no proof, and that is exactly what G says. G is therefore true and unprovable. (Showing that the system can't _refute_ G either needed a slightly stronger assumption in Gödel's original paper; J. Barkley Rosser removed that requirement in 1936.)[^v1-phi-i-rosser] This is why the Open's sentence says it cannot be proven _here_. In a stronger system, G may be provable. That system will have a G of its own.

The second theorem follows from asking the system to run that very argument on itself. The reasoning "if I'm consistent, then G is true" can be carried out inside the system. So if the system could also prove "I'm consistent," it could put the two together and prove G, which we've just seen it can't. A consistent system of this kind can't prove its own consistency.[^v1-phi-i-godel-consistency] That doesn't mean contradiction is secretly lurking, or that proofs can't be checked. It limits one particular kind of guarantee: the kind a system would issue about itself.

It also leaves one achievement standing, and it's worth naming. Checking a proposed proof is mechanical; any patient clerk could do it. What Gödel ruled out is a method that _settles_ every question. We can inspect a completed route without having a procedure that finds, or rules out, a route to every destination. The failure of the larger promise doesn't invalidate the smaller one. And we can always enlarge the system, as long as we account for the new assumptions; we just haven't escaped the question by moving it to a larger office. The discipline worth keeping is knowing which guarantee was established and which one was merely desired. It will matter again when the guarantees arrive in a sales presentation.

## A Machine That Can Read a Machine

Five years after Gödel, another man in his twenties gave the idea of a mechanical procedure a body. Alan Turing imagined the simplest possible computer: an endless paper tape divided into squares, a head that reads and writes one symbol at a time, a small set of internal states, and a table of rules saying what to do next. It looks less like the most powerful idea in computing than like a very patient clerk with a very long receipt.[^v1-phi-i-turing] (Alonzo Church, in Princeton, had reached closely related conclusions a few months earlier by an entirely different route, which suggests the idea was ready to be had.)

Turing's decisive step was the universal machine: a single machine that, given an encoded description of any other machine on its tape, could imitate it. Instructions became data. A decade later, von Neumann (on his fourth appearance, and I promise this one is structural) described a design for electronic computers that keeps the program in the same memory as the numbers it works on, so a machine can load, store, and even modify its own instructions. Nearly every computer since, including the one I'm writing on, is a descendant of that arrangement, still widely called the von Neumann architecture. (The name is his; the credit is shared, and still argued about.)[^v1-phi-i-vonneumann](https://file+.vscode-resource.vscode-cdn.net/Users/samseatt/projects/book-poma/work/sam/!--%20TODO:%20source%20John%20von%20Neumann,%20*First%20Draft%20of%20a%20Report%20on%20the%20EDVAC*%20\(1945\),%20on%20the%20stored-program%20design,%20and%20a%20history%20covering%20the%20credit%20dispute%20with%20J.%20Presper%20Eckert%20and%20John%20Mauchly.%20--)

How little does a language need, to be universal? Astonishingly little. There are computers with exactly one instruction (a single operation that subtracts one number from another and jumps elsewhere if the result is negative) that can, given enough memory and time, compute anything any computer can. A row of cells, each updating by a single fixed rule about its two neighbors, can do the same: the cellular automaton called Rule 110 was proved universal in 2004.[^v1-phi-i-universality](https://file+.vscode-resource.vscode-cdn.net/Users/samseatt/projects/book-poma/work/sam/!--%20TODO:%20source%20one-instruction-set%20universality%20\(e.g.,%20the%20SUBLEQ%20literature\)%20and%20Matthew%20Cook,%20%22Universality%20in%20Elementary%20Cellular%20Automata,%22%20*Complex%20Systems*%2015%20\(2004\),%20for%20Rule%20110.%20The%20threshold%20and%20emergence%20readings%20are%20the%20author's.%20--) That is the chapter's question about when a code becomes rich enough to tell stories, answered for machines: the threshold is shockingly low, and what matters is less the size of the vocabulary than the ability to combine, remember and repeat. It's also a small case of emergence. Nothing in a single cell's rule mentions arithmetic.

Then Turing showed where the machines run out of road. Suppose someone hands you a perfect program called the Decider, which can look at any program and any input and tell you, correctly, whether that program will eventually stop or run forever. Now build a deliberately contrary program (the teenager of computing). Given the code of some program, it asks the Decider whether that program would stop when fed its own code, and then does the opposite: if the answer is "stops," it loops forever, and if the answer is "loops forever," it stops. Finally, feed the contrary program its own code. Whatever the Decider predicts, the contrary program does the reverse. So the perfect Decider can't exist.[^v1-phi-i-halting] It's Gödel's trick again, a description turned back on itself, wearing overalls instead of a gown.

This is a general impossibility, not a claim that we can never tell whether an ordinary program finishes. Plenty of programs, and whole useful families of them, can be analyzed perfectly well. What's missing is the one instrument that promises the right answer for every possible case. Nor is undecidable a fancy word for expensive. Some problems are decidable in principle and would still take longer than the age of the universe at the sizes we care about; others are easy on most inputs and have no universal procedure at all. "The computer can't do it" can hide several quite different explanations, and buying a faster computer fixes only some of them.

There's an oddly domestic consequence. Our machines can read descriptions of machines, including descriptions of themselves, without ever getting a final view from outside all procedures. They are passengers too. Whether a machine understands, experiences anything, or deserves our trust in a particular role takes further arguments, and the tape doesn't settle them on our behalf.

## Giving the World a Way to Answer

A proof establishes what follows inside a framework. The world, unfortunately, has no obligation to live inside the framework we find most convenient. To find out whether it does, we need contact.

Scientific measurement is organized contact. We specify a quantity (the metrologists, who have a word for everything, call it the _measurand_) and a procedure for obtaining a value that can be attributed to it. Calibration then ties an instrument's readings to reference values, with the uncertainty accounted for. A result belongs to an operation, a set of conditions and a chain of comparisons. A number on its own is an orphan.[^v1-phi-i-metrology]

Imagine a thermometer whose readings wobble. Taking many readings can characterize the wobble, but it can't, by itself, reveal a steady offset that affects every reading equally. An instrument can be impressively consistent about being wrong (a talent it shares with some people). Catching that kind of error takes a comparison with something else, another instrument or a known reference. Precision and accuracy are different achievements, and an instrument can win the first while losing the second.

What we choose to measure matters as much. A temperature taken at one spot isn't automatically a measurement of a whole room, still less of whether the people in it are comfortable, as anyone who has shared an office thermostat already knows. Each extension brings in assumptions. A sensor can be perfectly accurate about what it measures while the system using it is wrong about what the reading means.

At the quantum scale, the encounter between a system and the apparatus measuring it belongs inside the physics, not outside it. A measurement interaction correlates the two, and interaction with the wider environment suppresses the observable interference between alternatives that we met in Hilbert space. That process, decoherence, helps explain how stable, effectively classical records emerge from quantum possibilities. On its own, without further interpretive commitments, it doesn't settle every part of what physicists call the measurement problem.[^v1-phi-i-decoherence] Nor is there an agreed little border booth where the quantum world turns classical whenever a person looks; the physical interactions and our interpretation of their results have to be kept apart.[^v1-phi-i-quantum-records]

This is where I'd plant the more adventurous question from the chapter. If one physical system can retain a trace of another, might human experience belong to a much longer history of registration, memory and modeling? The question is mine, and calling its early stages _experience_ would be a deliberate stretch of the word, not a finding that apparatus has sensations. We can follow the possibility through physics and biology without asking the metaphor to impersonate a result.

Even ordinary measurement has already complicated our position, though. Measuring is arranging an encounter through which something about the world becomes legible to us. The arrangement needn't invent the property it measures, but it does decide the form, the resolution and the reliability of the answer we get.

## Facts with a Return Address

A scientific account has to do more than accommodate what we already know. We want to know what follows from it, what would count against it, and whether a rival account would lead us to expect something different. Karl Popper made exposure to possible refutation the center of his account of scientific testing.[^v1-phi-i-popper] An explanation compatible with every conceivable observation is like a horoscope: it never fails, because it never risks anything, and it has bought its invulnerability by giving up the most useful kind of contact.

There's no single ritual that every science performs. We can't rerun the formation of a galaxy at a more convenient hour. We can compare consequences, look for independent traces, exploit differences that nature has arranged for us, and experiment wherever intervention is possible. What matters is the disciplined relation between the proposed account and the evidence it has to face.

Suppose a model predicts how a steel beam will bend under a load. We work out the expected bend, load the beam, measure what happens, and find a mismatch. The mismatch alone doesn't tell us which part failed. The model may be inadequate, the beam may differ from its description, or the load or the bend may have been measured badly. This is where the tidy diagram of the scientific method from school runs out of boxes. Hypotheses, instruments, classifications and background knowledge all meet in the test, and Pierre Duhem pointed out that a physical experiment tests that whole arrangement, never a single isolated sentence.[^v1-phi-i-duhem]

A fact doesn't become somebody's whim because establishing it took instruments and interpretation. The dependence tells us where to inspect the account. We can improve a procedure, compare independent approaches, find a source of error, or discover that something we thought general holds only within a narrower range. What I want science to replace in our myths is the privilege of being exempt from that work. The new account may be stranger than the old story, but it should come with better ways of finding out where it fails. Otherwise we've changed the costumes and kept the priesthood.

The social side of inquiry matters for the same reason: an individual investigator is capable of attachment, exhaustion and self-deception, sometimes all before lunch. Someone else needs enough information to inspect the route: what was measured, how the data were handled, which assumptions went in, and what happened when the analysis was repeated. Reproducing a result from the same data and replicating it with new data test different parts of that route.[^v1-phi-i-reproduction]

The habit travels well outside the laboratory. A chart without its denominators, a result without its conditions, or a benchmark without the test that produced it can travel much faster than the knowledge it claims to carry. A fact should have a return address. Someone ought to be able to ask how it got here.

## When Logic Learned to Click

In 1854 George Boole published a book with the modest title _An Investigation of the Laws of Thought_, which turned logical relationships into an algebra you could calculate with. Eighty-four years later, a young Claude Shannon showed in his master's thesis (it has been called the most consequential master's thesis of the century) that the same algebra could describe, and design, circuits of electrical switches.[^v1-phi-i-switching]

The idea fits in a sentence. Two switches in a row let current through only if both are closed, which is AND; two switches side by side let it through if either is closed, which is OR. Arrange enough switches, and the physical behavior of the circuit carries out logical operations. The mapping is a design achievement, not a sign that copper has understood conjunction. But from such arrangements you can build arithmetic, memory and control, and eventually Turing's universal machine with a power cord. The abstract operation may be exact; the apparatus still has timing, tolerances, heat and failure modes, and Interlude 1 will take up that material side of the bargain.

Learning adds another route to useful behavior: adjusting a model with data and feedback instead of specifying every desired response in advance. The results can be striking, but performing well on examples and offering a formal guarantee about some property remain different achievements. They can also cooperate. In 2024, DeepMind's AlphaProof combined learning with formal proof construction and checking to reach silver-medal standard at the International Mathematical Olympiad, and within a year AI systems were reported at gold-medal level.[^v1-phi-i-learning-proof] That already disposes of the comfortable claim that learned systems can only imitate and never contribute to proof.

So the important boundary runs between kinds of warrant, not neatly between humans who understand and machines that merely calculate. A human may guess; a machine may deliver a checkable proof. Either may produce something that works within a tested range and fails outside it. We should inspect the accomplishment before deciding which flattering story to tell about its author.

The detailed architectures can wait for later interludes. At this entrance to the Silicon mirror, the important inheritance is already visible: we choose what gets represented, how a claim is evaluated, and what counts as success. Later systems will act within those choices, sometimes at a scale that makes it hard to remember how small the choices once were.

## The Instrument Goes Outside

The boy's radio question deserves an answer by now. _Where inside the radio is the thing that takes the wave thing and makes it into sound? How does the antenna find them?_

The antenna, it turns out, doesn't find anything. The air around it (and around you, as you read this) is crowded with radio waves from every station within range, all at once, and every one of them nudges the electrons in the antenna's metal. What a radio does is choose. A tuned circuit inside it resonates at one frequency, the way a child on a swing only goes higher if you push in time with the swing, so one station's nudges add up while the others mostly cancel out. A further stage pulls the slow ripples of voice and music out of that fast-oscillating signal, and a speaker turns them into pressure in the air, which your ear turns back into something you'd call sound. There isn't a thing inside the radio that does it. There's an arrangement: a chain of relationships, each passing the message along to the next. The answer to the boy's question was structure, not furniture.

The explanation doesn't make the event less remarkable. If anything, it makes it more so, by showing how many relationships a voice from nowhere depends on. That's the kind of disenchantment I can live with.

The tools we've inspected each do different work. Proof follows consequences under stated assumptions. Measurement makes particular aspects of the world available for comparison. A model concentrates the relationships we want to understand, empirical inquiry tests the fit, and probability helps us handle what the available information doesn't settle. None of them inherits the duties of all the others just by being useful. Together, they let us ask sharper questions without claiming a view from nowhere. What did we represent, and what did we leave out? What follows inside the representation, and what makes it apply outside? At what point did a useful device start pretending to be the world?

Later in this book, our instruments will look more and more like ourselves. They'll speak, organize and advise, and perhaps expose habits we had mistaken for uniquely human depth. For now it's enough to have made the mirror inspectable, so we can consider what it preserves before we grow attached to the face in it.

One question from the boy's list is still on the table: time with no beginning, space with no edge. Every symbol in this interlude has needed some matter to be written on, and every machine has needed a body. The next chapter turns to the physical world they all depend on.

We have been discussing what follows.

Now we meet what was there first.

---

> _**Maggie:** The child learned that out of sight is not out of the world._
> 
> _**Alex:** The system learned that true is not the same as proven._
> 
> _**Maggie:** A question outgrew the boy who asked it;_
> 
> _**Alex:** A sentence outgrew the system that wrote it._
> 
> _**Both:** And still, someone has to go and look._


[^v1-phi-i-sets]: Eric Lehman, F. Thomson Leighton and Albert R. Meyer, [Mathematics for Computer Science](https://courses.csail.mit.edu/6.042/spring18/mcs.pdf) (2018). §§4.1 and 4.5. The cardinalities of ∅ and {∅} are respectively zero and one.

[^v1-phi-i-null]: PostgreSQL Global Development Group, [PostgreSQL 18 Documentation: Comparison Functions and Operators](https://www.postgresql.org/docs/18/functions-comparison.html). §9.2. Ordinary comparisons involving NULL yield unknown, including comparison of NULL with NULL; the dedicated IS NULL predicate performs a different operation.

[^v1-phi-i-structure]: Eric Lehman, F. Thomson Leighton and Albert R. Meyer, [Mathematics for Computer Science](https://courses.csail.mit.edu/6.042/spring18/mcs.pdf) (2018). Chapter 12 opening and §12.1. The friendship example is the author's illustration of the modeling choice, not an empirical finding about friendship.

[^v1-phi-i-logic]: Eric Lehman, F. Thomson Leighton and Albert R. Meyer, [Mathematics for Computer Science](https://courses.csail.mit.edu/6.042/spring18/mcs.pdf) (2018). §1.4.1, modus ponens and sound inference rules. The alarm example contrasts modus ponens with the invalid converse inference known as affirming the consequent.

[^v1-phi-i-calculus]: Silvanus P. Thompson, [Calculus Made Easy](https://www.gutenberg.org/cache/epub/33283/pg33283-images.html) (1914), Macmillan and Co. Chapters VIII and XVII–XIX. The prose specifies smooth one-dimensional motion; integrating velocity requires an initial position to recover a particular position history.

[^v1-phi-i-bayes]: Thomas Bayes, [An Essay towards solving a Problem in the Doctrine of Chances](https://www2.isye.gatech.edu/isyebayes/bank/Bayesessay.pdf) (1763), _Philosophical Transactions_ 53: 370–418. Section I, conditional probability propositions. The detector example is invented: 100 × 0.90 = 90 true alarms; 9,900 × 0.05 = 495 false alarms; 90/585 ≈ 15.38%. The modern update description is not a quotation from Bayes.

[^v1-phi-i-pvalues]: American Statistical Association, [American Statistical Association Releases Statement on Statistical Significance and P-Values](https://www.amstat.org/asa/files/pdfs/p-valuestatement.pdf) (2016). Principles 2, 3 and 5.

[^v1-phi-i-godel-coding]: Kurt Gödel, [Über formal unentscheidbare Sätze der Principia Mathematica und verwandter Systeme I](https://homepages.uc.edu/~martinj/History_of_Logic/Godel/Godel%20%E2%80%93%20On%20Formally%20Undecidable%20Propositions%20of%20Principia%20Mathematica%201931.pdf) (1931), _Monatshefte für Mathematik und Physik_ 38: 173–198. §§1–2 and Proposition VI, in B. Meltzer's English translation. The self-reference concerns formal provability, not the liar paradox. The prime-power example is a standard simplified illustration.

[^v1-phi-i-rosser]: J. Barkley Rosser, [Extensions of some theorems of Gödel and Church](https://www.cambridge.org/core/journals/journal-of-symbolic-logic/article/abs/extensions-of-some-theorems-of-godel-and-church/0461E34DC1F219C459EE84CC2FA89068) (1936), _The Journal of Symbolic Logic_ 1(3): 87–91. The strengthening from omega-consistency to ordinary consistency. The result still requires an effective theory of sufficient arithmetical strength.

[^v1-phi-i-godel-consistency]: Kurt Gödel, [Über formal unentscheidbare Sätze der Principia Mathematica und verwandter Systeme I](https://homepages.uc.edu/~martinj/History_of_Logic/Godel/Godel%20%E2%80%93%20On%20Formally%20Undecidable%20Propositions%20of%20Principia%20Mathematica%201931.pdf) (1931), _Monatshefte für Mathematik und Physik_ 38: 173–198. §4, Proposition XI. The prose gives the standard informal sketch; the claim concerns the theory's standard formal representation of its own consistency under the theorem's conditions.

[^v1-phi-i-turing]: Alan M. Turing, [On Computable Numbers, with an Application to the Entscheidungsproblem](https://www.cs.virginia.edu/~robins/Turing_Paper_1936.pdf) (1936), _Proceedings of the London Mathematical Society_ s2-42: 230–265. §§1–2 and 6.

[^v1-phi-i-halting]: Alan M. Turing, [On Computable Numbers, with an Application to the Entscheidungsproblem](https://www.cs.virginia.edu/~robins/Turing_Paper_1936.pdf) (1936), _Proceedings of the London Mathematical Society_ s2-42: 230–265. §8. The draft uses the modern halting presentation of diagonalization, rather than reproducing Turing's circle-free-machine argument verbatim.

[^v1-phi-i-metrology]: Joint Committee for Guides in Metrology, [International Vocabulary of Metrology: Basic and General Concepts and Associated Terms (VIM)](https://www.bipm.org/documents/20126/2071204/JCGM_200_2012.pdf) (2012). §§2.1, 2.3, 2.15, 2.17, 2.26 and 2.39. The thermometer and room examples are hypothetical. Repeated readings alone need not reveal a shared systematic offset.

[^v1-phi-i-decoherence]: Maximilian Schlosshauer, [Decoherence, the measurement problem, and interpretations of quantum mechanics](https://arxiv.org/abs/quant-ph/0312059) (2005), _Reviews of Modern Physics_ 76: 1267–1305. Introduction and §§II, III.D and IV.A. Decoherence and the interpretation of definite outcomes are distinguished; no consciousness-induced collapse is asserted.

[^v1-phi-i-quantum-records]: Wojciech H. Zurek, [Decoherence, einselection, and the quantum origins of the classical](https://arxiv.org/abs/quant-ph/0105127) (2003), _Reviews of Modern Physics_ 75: 715–775. Discussion of measurement, environmental monitoring and stable correlations. The text does not assert a unique settled quantum/classical boundary or equate a physical record with subjective experience.

[^v1-phi-i-popper]: Karl R. Popper, [Conjectures and Refutations: The Growth of Scientific Knowledge](https://www.inf.fu-berlin.de/lehre/SS06/materials/eng/PopperScience.pdf) (1963), Routledge and Kegan Paul. Chapter 1, section I, especially numbered conclusions 1–7. Falsifiability is presented as one influential account of scientific testing; the horoscope comparison is the author's.

[^v1-phi-i-duhem]: Pierre Duhem, [The Aim and Structure of Physical Theory](https://thehangedman.com/teaching-files/hps/duhem.pdf) (1954), Princeton University Press. Part II, chapter VI, §2. The beam-under-load illustration is the author's application of the argument, not Duhem's example.

[^v1-phi-i-reproduction]: National Academies of Sciences, Engineering, and Medicine, [Reproducibility and Replicability in Science](https://www.nationalacademies.org/read/25303/chapter/6) (2019), The National Academies Press. Chapter 3. Following this report's usage: reproducibility concerns results from the same data and computational procedures; replication uses newly collected data. Usage varies by field.

[^v1-phi-i-switching]: George Boole, [An Investigation of the Laws of Thought](https://www.gutenberg.org/files/15114/15114-pdf.pdf) (1854), Walton and Maberly; Claude E. Shannon, [A Symbolic Analysis of Relay and Switching Circuits](https://tubes.mit.edu/6S917/_static/2025/resources/shannon38.pdf) (1938), _Transactions of the American Institute of Electrical Engineers_ 57: 713–723. Boole, chapters II–III; Shannon, §§I–II. The switch illustration takes conduction as true; Shannon's original hindrance notation uses zero for a closed circuit and one for an open one.

[^v1-phi-i-learning-proof]: Google DeepMind, [AI achieves silver-medal standard solving International Mathematical Olympiad problems](https://deepmind.google/blog/ai-solves-imo-problems-at-silver-medal-level/) (2024). AlphaProof: a formal approach to reasoning. This is the research team's report about a particular system, not a claim that all learned systems supply proofs or that a proof establishes general understanding.

