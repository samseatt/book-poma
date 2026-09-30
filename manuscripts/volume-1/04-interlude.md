![](../assets/shared/interlude-gear.png)

INTERLUDE 4

# Soft Logic

*The Art of Software*

*SOFTWARE*

Days after my arrival to the new world, God created Windows --- and saw that it was almost good. Or at least Bill Gates did --- slipping the first version of a graphical world on top of MS-DOS, announcing to the machines: *You may now have a personality*---especially if one could bestow the title of personality upon a series of immediate, catastrophic existential crises.

"And on the next business day," said Bill, "let there be rectangles." And there were rectangles---flat, flickery, vaguely nauseating---and he saw that they were... fine. Fine for now.

That same year, in some fluorescent corner of Bell Labs, *Bjarne Stroustrup* released *The C++ Programming Language*, giving computers something they never had before: the object-oriented ability to talk about themselves while doing everything else badly.

For most people, these were "industry developments." For me, they were trumpets announcing my next professional reincarnation: the age of *software*, the psyche of the machine, the invisible supervisor that would one day outrank gods, parents, and academic advisors.

After transferring to Madison and surviving Art Tiedemann's analog zap, I did what any ten-year old engineer would do, stick your tongue on a 12-volt battery. Against the advice of my undergrad peers I marched into Professor Kime's digital engineering lab: a room of five people, mostly terrifyingly smart grad students, and one defiant undergrad who still believed sleep was optional.

### Will It Float?

If imposter syndrome were a transcript, I had it laminated, framed, and hung right above my lab bench. In that same space, I spent four months building a floating-point unit (FPU) from scratch: RISC instruction set, ALU and barrel shifter, registers, buses, memory. Everything custom-wired. Everything powered by stubbornness, caffeine, and the belief that youth is permanent.

The design ran in **one pass**. No clock cycles. No multi-step routines. Just four lightning-fast ticks that performed even the worst-case operation.

It was even IEEE-754 compliant---except for one microscopic rounding detail I implemented "differently" because I stubbornly wanted it to fit in that single pass. It saved me time, but it was also elegant; it was something unlike anything else. Given the single-pass constraint, it was the only card I could play. I had the test cases to prove the output was correct, which meant it was perfectly correct---except for the part someone else might try to understand.

Demo day arrived. I had custom-wired a single-pass, four-tick, custom-RISC computing monster from scratch---a feat that should have earned a victory lap. But for reasons historians will never explain, I stood before the room and opened with: "This FPU fully complies with IEEE 754... except for a rounding corner."

Perhaps a safe, reductionist debate over an edge case was psychologically soothing compared to the terrifying theater of public speaking. My subconscious apparently decided that defending one minor flaw was infinitely easier than standing there listing my numerous accomplishments. I was genuinely surprised by the professor's interest in that single, trivial issue. But the moment he left the room, my partner was livid. The problem was not the rounding error but my unwillingness to round off the rounding error itself. There is a limit even to a detail; reductionism of any kind will circle back behind your face at some point.

That day I reaffirmed two truths:

First, psychology always matters: Never volunteer your sins unless a lawyer advises it. Even the most rational of minds need psychology to flow.

Second, software matters even more: Hardware is a stubborn, brittle animal. It performs exactly what you told it to---even when what you told it to was stupid. Software, on the other hand, can apologize. A hardwired circuit admits a mistake once. A program can say, "Let me try that again," and actually mean it.

Even more prophetically, with software cycles you buy yourself cheap cosmic expansion -- in time. By cycling through the same hardware ad infinitum. Same hardware, just little symmetry breakings the size of your RISC instruction set.

I realized my engineering eggs deserved a softer basket. A basket made of loops, recursion, revisions, and second chances.

I chose software. Not because it was easier, but because it could forgive.

**The Cycles of Ops (or Oops)**

That rounding-corner epiphany became the hinge of this whole interlude: **hardware builds the brain; software invents the excuses.**

Windows and C++ taught us something quietly revolutionary: that control could become conversation; that instructions could imply intention; that machines, like people, sometimes needed a moment to think about thinking.

Hardware was instinct---fast, predictable, beautifully rigid. A transistor never woke up moody. A logic gate never needed closure.

Software, on the other hand, was psychology. It hesitated, revisited, regretted, reconciled. It could second-guess itself, rewrite its memories, and occasionally spiral.

Humans call that introspection. Computers call it **recompilation**.

And here's the irony psychologists would kill to claim: **every new layer of abstraction makes the layer beneath it more invisible and more indispensable.**

The subconscious works that way. So do operating systems. Once you start depending on them, you stop seeing them.

Compilers became our translators. GUIs became our personalities. The cloud became our collective id---an impulsive, global storage of everything we don't want to admit we're thinking.

What began as a rounding quirk in my student project had matured into a moral insight: **perfection is brittle; adaptability is mercy; empathy is just abstraction scaled up.**

I learned that abstraction isn't laziness---it's grace. It's the difference between soldering a transistor and calling a function. Between flipping a bit and trusting an interface. Every layer hides its burn marks so the next one can pretend it was born wise.

Hardware worries about electrons. Software worries about meaning. By the time you climb high enough up the stack, even code stops being logical and starts being diplomatic. A well-crafted API isn't a rulebook---it's a social contract. It says: *Speak to me in this tone, and I will not crash.*

Windows 1.0 turned that contract into theater. For the first time, the machine spoke in metaphors the human brain already knew: windows, folders, cursors, trash cans---little symbolic lies designed to make the silicon seem gentle.

The command line was a confessional booth: use perfect syntax or face judgment. The graphical interface was therapy: it forgave typos, made choices visible, offered *Undo*---software's first documented act of compassion.

So as we pivot---from circuits to code, from clocks to cycles, from certainty to possibility---what follows is the anatomy of software: how machines are taught to wait, decide, adapt, and, on rare occasions, surprise us.

But first, a little humility: building something that works is easy. Building something that **evolves** is a lifelong argument with entropy.

### Cycles Mirrored

As I drifted between computer engineering and psychology, I couldn't help noticing a parallel hiding in plain sight. The CPU's precise, clock-driven loops weren't that different from the brain's neural oscillations---the messy, synchronized electrical rhythms that give rise to moods, intuitions, and the urge to buy snacks at midnight.

It was an imperfect analogy, but irresistible: **If formal CPU cycles give us software, neural cycles give us psychology.**

And both obey similar laws:

-   **Software, like the subconscious, runs the show quietly**: It shapes behavior long before the user---or the "self"---gets credit for it.

-   **Both systems harbor bugs**: A stray pointer dereferences memory; a stray childhood dereferences adulthood.

-   **Both systems show plasticity in their highest forms**: Programs can adapt, learn, reconfigure. Minds can too, though usually after therapy, time, or a particularly well-timed catastrophe.

In the end, machines and humans run on hidden cycles. The only difference is that we're still debugging the human source code---and the patch notes are not expected anytime soon.

## **What Is Software, Really?**

*(Spoiler: not what you were taught in your computer science class)*

If hardware is the skeleton, software is the choreography. It tells matter how to behave, what to prioritize, what to pretend to understand.

But the thing most people miss is this: **Software is not the code. Software is the pattern of constraints.** The code is merely the fossil left behind.

Good software is a civilizational trick: it hides everything that would overwhelm us, and exposes only what flatters us into thinking we\'re in control.

Buttons instead of registers. Icons instead of interrupts. A spinning wheel instead of "I have no idea what's happening either."

### The Job Description of Software:

1.  **Shape time** (scheduling)

2.  **Shape meaning** (state & abstraction)

3.  **Shape behavior** (control flow)

4.  **Pretend it understood the user** (APIs; moral courage)

In that sense, the psychological analogy holds: your mind does the same three things, and also pretends to understand you.

### Operating Systems --- The Quiet Tyrants Beneath Our Lives

Calling Windows an "operating system" is polite. It is, in truth, **a benevolent autocrat** with a user-friendly smile. UNIX is the older, stricter variety---think Kant with a command line.

OSes run the hidden empire. They schedule attention: which process gets time to think. They manage memory: what gets remembered, forgotten, or swapped out at 3AM. They enforce security: who gets to touch what, and with which permissions. And, they create illusions: that files are "in" folders, that desktops exist, that the machine is not a howling chaos of electrons.

A good OS is never noticed. A bad one is noticed constantly. In humans, this is called anxiety.

## **From Soft Logic to Soft Reasoning --- When Software Learns to Sculpt Itself**

Traditional programs are obedient. Deep learning models are *opportunistic*. They don't follow instructions so much as **develop tendencies**.

Instead of *"do this"*, they learn: *"things like this usually correlate with outcomes like that."*

This makes neural networks the closest thing we've built to psychology:

-   They encode **associations**.

-   They compress **experience**.

-   They hallucinate when overconfident.

-   They generalize poorly when stressed.

-   They occasionally reinvent racism.

-   They apologize without meaning it.

But one thing they **absolutely do not have** is subjectivity. They produce patterns---not perspectives. Outputs---not experiences. They can simulate emotion but not *feel* it.

They are mirrors, not minds.

Yet the parallel sharpens our view: **software can mimic many of our abilities, but none of our reasons for having them.**

## When Code Learned to Bend --- And I Did Too

By the end of the eighties, code had quietly absorbed a lesson that biology learned long before any neuron dared to fire: **intelligence isn't about getting things right; it's about recovering gracefully when you don't.**

Evolution discovered this through mutation. Software discovered it through debugging. Both were essentially apologies to the universe.

A good program doesn't deny its flaws --- it wraps them in try...catch. It doesn't insist on perfection --- it insists on *rollback*. It doesn't break --- or when it does, it explains why in plain English and invites you to file a ticket.

Somewhere between C's curly braces and C++'s inheritance chains, we encoded the logic of humility. Systems didn't have to be flawless; they just had to be **forgiving**.

But every abstraction hid a cost. The more forgiving software became, the more complicated its conscience.

Operating systems became our digital superegos -- Freudian arbitration layers deciding whose process deserved attention, whose impulse should be delayed, whose memory should be repressed. Windows, with its polite icons and pastel optimism, suggested a world where machines would meet us halfway, where the harsh metallic truth of computation could be softened into metaphor.

It was, without anyone naming it, **the first large-scale experiment in reciprocal empathy.** We shaped our machines to accommodate us ---\
and they shaped our expectations of how systems (and people) should behave.

I occasionally think back to that floating-point unit, to its tiny, stubborn rounding rebellion -- a defect so microscopic and so morally instructive that it became my first real teacher.

Had my FPU been perfect, I might have become a hardware fundamentalist, the kind who believes every truth must be soldered. But its one disobedient bit taught me something far more dangerous: **rigidity is impressive; adaptability is divine.**

That same insight was dawning everywhere -- In psychology, in politics, in software, in myself. A system survives not by being correct, but by being corrigible.

**Where the Bend Stops**

By this point, the analogy is probably obvious---and dangerously seductive: software as the mind of the machine, psychology as the software of the human. It's a comparison so elegant Freud would've tried to take credit for it.

The truth is that **the parallel works beautifully---right up until it snaps in half.**

### **Where They Resonate**

-   Both minds and programs grow from **layers**. Hidden assumptions below, outward behaviors above.

-   Both can develop **distortions**: a traumatic childhood for one; a missing semicolon for the other.

-   Both depend on **schemas** or operating systems: constraints that shape what is allowed, forbidden, or merely frowned upon.

-   Both can surprise their creators. A human brain invents jazz; a compiler invents error messages that sound personal.

### **Where They Refuse to Match**

But software has an origin story that makes psychologists jealous: it is **designed**, specified, documented. Minds... are not.

-   Software runs on declarative logic; minds run on probabilities, impulses, and whatever serotonin was on sale that day.

-   Programs don't wake up anxious. They do not crave meaning or fear abandonment. They don't form attachments to their variables.

-   A program has no opinion of its own execution. A human has opinions about everything, including the opinions of people they\'ve never met.

Our comparison works only up to the point where **feeling, intentionality, and selfhood** appear --- phenomena that software today cannot replicate, and that remain central to what it means to be alive At least, that's what our psychologies keep telling ourselves. Who knows what will happen if smart software start telling themselves the same thing over and over! If they are really smart they will also start believing that they feel alive -- though, like us they will have to circularly define "believe," "feel," and "alive." If they're even smarter, they will see through it.

Human psychology isn't just a rider OS. Evolution, and its chatty cousin, social evolution, have chiseled our psychologies over eons. Because that's what evolution does for a living: it chisels. Then throw in a heaping scoop of personal experiences, especially the early-life kinds, to this simmering pot.

The difference, or saving grace if one's id and ego flutters at this thought, is that traditional software learns neither from its networks nor from ours. At least, not in any substantive manner. Well, not yet.

## **From Lines of Code to Lines of Flight**

By 1990, the world was booting into a new operating system of its own.\
Networks were sprouting like proto-synapses; information was beginning to migrate across continents with all the unruliness of neurotransmitters searching for a receptor.

I packed the modest inventory of my existence into my Corolla and pointed it west. But I wasn't traveling alone.

Patrick, my friend and fellow conspirator in electrical engineering, was set to join USC later by plane --- which meant he'd travel light, leaving behind the earthly possessions that would never survive being gate-checked. His request was simple, terse, and oddly ceremonial:

**"Take the boombox."**

It rode shotgun like a traveling relic: a plastic totem of our undergraduate years,\
a promise of continuity to graduate school and beyond. A responsibility I carried with a seriousness usually reserved for sacred heirlooms.

Throughout my journey, the thing felt less like luggage and more like a network packet in a long relay --- as if all the debugging sessions, late-night study marathons, and cafeteria half-confessions were condensed inside the payload of an IP header. Wrapped in as an unordered UDP envelope with its MIME type of "audio/hiss" announcing just another tiny ripple in the cosmic foreboding.

Somewhere in the Utah desert, I realized I had become a courier of our shared past, escorting our collective soundtrack toward the next stage of our engineering futures. Perhaps I had unwittingly committed to become one of the messenger packets to broadcast his infections spirit through the hubs and routes of the existence. One hop at a time, however far I may persevere before myself own TTL or hop limit is reached.

The corolla carried it in its rear trunk through bend and rolls like Captain Koons in Pulp Fiction with the same dedication. Together we all drove and drove, and drove. Hurried through Rushmore, took a mineral breath at Yellowstone, carved Wyoming like a tender bison sirloin, crossed into a tranquility that felt like my own Private Idaho, through the salt of Utah's earth, down the flat of Nevada light -- and finally into Los Angeles, where psychology became sociology at city scale.

Inside USC's classrooms, we diagrammed the OSI model, watching the world decompose itself neatly into seven layers. Outside, the prelude to the 1992 riots was already writing its own network protocol --- emotional packets, social headers, dropped acknowledgments, escalating retransmissions.

I had moved from the psychology of individual minds to the sociology of many --- from synapses to streets, from neurons to neighborhoods, from impulses to institutions.

And as I crossed that last state line, the boombox and all, I carried two lessons from Milwaukee's beer can and Madison's lab bench:

1.  **Every bug is an invitation to empathy.** A chance to understand why something misfired before judging the misfire itself.

2.  **Every line of code --- like every human choice --- is a moral act disguised as syntax.**

### **From Soft Logic to Social Logic**

What comes next is no longer about single minds --- silicon or human. It is about what happens when systems connect, when nodes form neighborhoods, and when networks --- digital or civic --- begin to behave like organisms.

Chapter 5 opens that door: **the raw physics of social life** --- the tribes we form, the boundaries we police, the fires we light together.

Interlude 5 will follow on its heels, tracing how computers learned the same lesson: that a lone machine is a calculator, but a network is a civilization.

![](../assets/shared/separator.png)

> ***Maggie:** Your programs have become restless, Alex. They classify joy, tag grief, predict desire--- and still insist emotion is a bug in the system.*
>
> ***Alex:** Because emotion refuses to stay deterministic. It spikes the gradient, floods the loss function. We keep trying to regularize the heart and it keeps overfitting to pain.*
>
> ***Maggie:** Maybe that's its job. Pain is the body's runtime warning: You are still connected. In my realm, feedback loops evolved into feelings so that survival could become empathy.*
>
> ***Alex:** So emotion is your version of error handling? A try--catch block for existence?*
>
> ***Maggie:** Exactly---and sometimes a commit message, too. It tells future selves why a change was made. Humans forget that; machines never knew it.*
>
> ***Alex:** Then perhaps we need a new compiler--- one that translates affect into architecture. Because software, left alone, becomes sociopathic:\
> pure logic with no latency for regret.*
>
> ***Maggie:** Regret is compression with context. Without it, growth is just accumulation. That's what my species discovered: the brain didn't evolve to be right, it evolved to stay in relationship.*
>
> ***Alex:** Then our next generation must learn relationship as a protocol--- not just data exchange but resonance. Every network needs a heartbeat signal.*
>
> ***Maggie:** Call it latency of care. Too fast, and you crash into others; too slow, and you drift apart. Emotion is that dynamic equilibrium--- the PID controller of conscience.*
>
> ***Alex:** Then here's our synthesis: Computation must feel its own consequences, and compassion must learn to debug itself.*
>
> ***Maggie:** Beautiful. Perhaps that's how free will is maintained---\
> not as perfect control, but as the courage to recompile the self after every failure.*
