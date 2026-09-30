![](../assets/shared/interlude-gear.png)

INTERLUDE 5

# Connected Currents

*Computer Networks & Distributed Computing*

*NETWORK*

At USC, everything I studied seemed to be quietly conspiring toward the same theme: **connection**. Not just electrical or logical connection, but the larger, cosmic kind --- the sort that takes strangers, transistors, and entire cities and tries to stitch something coherent out of them.

The computer-networks course said the quiet part out loud --- complete with packets, protocols, and the seven-layer OSI model stacked like a wedding cake nobody ever eats past layer three. But my other classes were in on the plot as well:

-   Operating systems constantly fretted over distributed processes.

-   Databases sighed romantically about remote transactions.

-   VLSI threw entire forests of transistors onto silicon until it resembled the map of Los Angeles at rush hour --- except with slightly fewer accidents.

-   And artificial neural networks --- philosophical cousins to sociology --- gathered small, confused nodes and encouraged them to come to consensus before the universe timed out.

Meanwhile, my own brain---the beer-battered wetware version---was attempting to network all of it together inside that frying pan.

My research wandered accordingly. What began as an innocent flirtation with AI grew limbs and started demanding resources. We were trying to build technologies that barely existed: parallel machines pretending to think together; streams of data pretending to be "real time"; clusters of processors pretending to cooperate. While in reality, AI back then meant doing the same old thing, except in Lisp and Prolog; while dreaming the same in artificial neural networks. The web hadn't yet flickered into existence, the JPEG standard was still being finalized, and graphic mobile devices were a twinkle in a madman\'s eye.

It was, in hindsight, the toddler stage of what we'd later call **the Internet of Things** --- back when the "things" were oscilloscopes, SGI workstations, and an unwavering belief that grad students were immortal.

AI itself was between winters --- which either meant I was early, visionary, or catastrophically bad at reading weather patterns. My advisor, bless him, liked the *title* of my proposal. Then he read the draft, and liked the title even more.

But while my little lab stumbled toward distributed cognition, something monumental was happening an ocean away.

### **The City Burns, and a Web Is Born**

Just as I rolled into Los Angeles --- naïve, caffeinated, and one tuition payment from homelessness --- a man at CERN named **Tim Berners-Lee** quietly did what civilizations occasionally manage when they're not rioting: he invented a new language.

HTML. HTTP. URLs with colons and slashes arranged like the coordinates of a treasure map. And the first faint pulse of what he called the *World Wide Web.*

While Los Angeles was preparing to show how fragile connections could be, Geneva was busy proving how infinite they might become.

The timing was almost Biblical. One city cracked open in rage; another opened a door to a networked world. And I, unwittingly lodged between both, was wiring neurons into code and code into neurons, hoping neither would collapse under load.

I didn't know it then, but everything I was soldering, simulating, or swearing at in USC's labs was rehearsal. The distributed computing we struggled to stabilize was merely a prototype; what Berners-Lee released into the world would become the real experiment: **a global network --- a distributed consciousness that would teach humanity more about itself than any psychology class ever could.**

And somewhere between my convoluted LISP parentheses and CERN's clean syntax sat the same impossible question: **Could any network --- of neurons, machines, or people --- ever be truly free of its own latency?**

Spoiler: no. But the ways in which they fail are spectacularly instructive.

## A Tale of Two Networks

It turns out that building a society and building a computer network have more in common than either department will publicly admit.

Both begin with generous intentions --- communication, collaboration, the audacious hope that everyone will remain civil.

Both end with dropped packets, lost messages, and someone shouting, "Who's responsible for this latency?!"

Distributed computing is simply civilization rewritten in code: **many actors**, **limited bandwidth**, **unreliable signals**, and far too much waiting for consensus.

In sociology, we call it negotiation. In computing, we call it synchronization. In both cases, getting it wrong leads to deadlock --- the technical kind or the congressional kind.

Every distributed-systems problem we faced in that multimedia effort had a social twin:

-   Load balancing looked suspiciously like teamwork.

-   Fault tolerance sounded a lot like forgiveness.

-   Concurrency --- the elegant term for "everyone doing something at once without stepping on each other's toes" --- was Los Angeles traffic, but with better documentation.

Even computers, for all their determinism, kept re-enacting human follies: they crashed when overwhelmed, they gossiped through protocols, and they froze when waiting for messages that would never arrive --- the digital version of being left on "read."

Perhaps that's why distributed computing fascinated me more than any other subject: it wasn't just about linking machines, but about imagining machines that could *cooperate*.

If the riot had shown me how fragile human networks were, the work that followed revealed how fragile digital ones might be. Packets dropped like trust. Protocols failed like treaties. Sockets timed out like patience.

And yet, out of this noisy, imperfect dance, structure emerged --- a language of structured chaos through which machines began to talk to one another with surprising grace.

Which brings us naturally to the wiring itself.

Because before machines could dream of intelligence, they had to learn to talk. And before they could talk, they had to agree on **what a word even was**.

## How to Teach a Machine to Speak

### Packets, Protocols, and Politeness

If psychology is the study of minds negotiating meaning, then computer networking is the study of machines trying their best to avoid being impolite.

At its core, a networked conversation is embarrassingly simple:

1.  **Break the message into little pieces** (because large requests scare everyone).

2.  **Add a polite introduction** (headers: the handshakes of the digital world).

3.  **Send those fragments across unreliable terrain** (radio waves, copper wires, dark fibers, air-conditioned hallways).

4.  **Pray.**

5.  **Reassemble the pieces on the other end**, assuming the universe cooperates.

We call these fragments packets, as though they were care packages addressed to a distant cousin. Most arrive. Some get lost. Some show up drunk, out of order, or duplicated for reasons nobody fully understands. But the marvel is that **the system works anyway**.

TCP, the gentleman of protocols, insists on acknowledgment for every message. A bit like Victorian courtship: slow, deliberate, obsessed with proper sequence.

UDP, meanwhile, is your carefree friend who shouts messages across a canyon and hopes the echo doesn't distort them too badly. Fast, fun, and about as reliable as a fortune cookie.

Every protocol, in its own way, is a theory of human nature disguised as math:

-   **TCP** believes in accountability.

-   **UDP** believes in destiny.

-   **ICMP** believes in complaining.

-   **ARP** believes in gossip.

And then there's **DNS**, the address book of the internet --- a distributed phone directory that answers the philosophical question: "Where does *www* live this week?"

It is an unsung miracle that DNS works at all. It is the closest thing computing has to faith.

## The Seven Layered of Truth

### Why OSI Model is a Cathedral Nobody Worships In

The OSI model is one of the grand illusions of computer science. A seven-layer wedding cake of conceptual purity:

1.  Physical

2.  Data Link

3.  Network

4.  Transport

5.  Session

6.  Presentation

7.  Application

A stack so clean it could only have been designed by committee.

Every networking student admires the OSI model the way museum visitors admire medieval cathedrals: beautiful, towering, and utterly unrelated to daily life. In practice, we mostly inhabit three layers:

-   The bottom one, when the cable is unplugged.

-   The top one, when the website is broken.

-   And TCP/IP, which does all the work while OSI gets all the diagrams.

The OSI model is important not because we use it, but because it reminds us of something structures --- human and digital --- often forget: **abstraction is both the ladder and the trap.**

Every time you build a layer to hide complexity, you create a power, a blindness, and a place where bugs can hide.

Cities have zoning laws; networks have layers. Both are aspirational. Both are routinely ignored. Both reveal their true importance only when they fail catastrophically.

## When Bandwidth Meets Human Nature

### Congestion, Gossip, and the Art of Waiting

The deeper I went into networking, the more it resembled the sociology I'd just lived through.

Networks suffer from the same ailments people do:

-   **Congestion** --- too many demands, not enough capacity.

-   **Contention** --- arguing over who gets to speak first.

-   **Starvation** --- some processes getting ignored entirely.

-   **Flooding** --- one bad actor shouting so loudly the whole system collapses.

Even the solutions are suspiciously familiar:

-   **Backoff algorithms** mirror human patience:\
    everyone waits a random amount of time before trying again.

-   **Congestion control** mirrors anger management:\
    slow down before you melt down.

-   **Collision detection** mirrors conflict resolution:\
    "We both tried to talk at once. Let's pretend we didn't."

Ethernet's original algorithm, CSMA/CD, may be the single greatest technical metaphor for human communication:

1.  Listen before speaking.

2.  If someone else is speaking, wait.

3.  If everyone talks at once, stop ---

4.  --- then try again more politely.

If only diplomatic summits ran on Ethernet.

But even the politest networks can fail. Links die. Signals fade. Packets disappear into the digital wilderness. When that happens, protocols have a choice:

-   retry,

-   reroute,

-   or give up.

Humans do the same, except with more swearing.

And that's when distributed computing becomes less a branch of engineering and more a branch of ethics.

## Distributed Systems as Moral Philosophy

### Faults, Forgiveness, Failover

Distributed systems were the first machines I encountered that seemed to possess a moral dimension. They weren't just about efficiency. They were about **how to behave when things go wrong**.

Every distributed system faces five existential dilemmas:

1.  **Partial Failure**: One part of the system collapses, the rest must carry on --- the engineering version of a dysfunctional family.

2.  **Asynchrony**: Nobody agrees on what time it is --- which, in my experience, accurately describes every group project.

3.  **Unreliable Signals**: Is the other node silent, or dead? Is the message late, lost, or passive-aggressive?

4.  **Consistency:** Does everyone share the same truth? Or have different nodes begun living in alternate realities?

5.  **Consensus**: Can the system make a decision everyone will accept? Or will it split into factions and fork?

Humans solved these problems with stories, myths, constitutions, and, occasionally, revolutions. Distributed systems approached them with Paxos, Raft, two-phase commit, Byzantine fault tolerance, and other baroque contraptions that looked suspiciously like political science in drag.

The surprising lesson? **Machines, like people, are not defined by perfection, but by recovery.** Failover is not a bug --- it is character.

When a process crashes and another quietly picks up its work without complaint, that is grace. When a system refuses to accept corrupted data from a faulty node, that is integrity. When nodes reconcile divergent states and continue working together, that is forgiveness.

The whole field felt like moral philosophy taught by oscilloscopes.

## From LAN Parties to Planetary Nerves

### How the Internet Went from Dorm Rooms to Destiny

In the late '80s and early '90s, we liked to pretend the internet didn't exist yet. We were half right. What existed was a stack of protocols nobody's parents understood; a set of academic networks stitched together like mismatched quilt squares; and a handful of idealists who believed information should be free (which, statistically speaking, is the last time that sentence was uttered without a business model attached).

Computers in our labs connected through brittle coax cables and temperamental repeaters that behaved like moody teenagers---alternately oversharing and refusing to speak. LAN parties existed before the term did; we just called them "debugging sessions." They involved the same snacks and the same sleep deprivation, but the graphics were worse.

And then something historic slipped through the wires. **The web.**

Not "the internet," which already existed as a collection of gated communities, but the *web*---a democratic layer laid on top by a mild-mannered physicist at CERN who probably didn't realize he was about to rearrange civilization.

Tim Berners-Lee gave the world three commandments:

1.  **Thou shalt link.**

2.  **Thou shalt retrieve.**

3.  **Thou shalt browse.**

With **HTML**, he gave us a common tongue. With **HTTP**, he gave us a courier service. With **URLs**, he gave us something religions had tried for centuries: a universal addressing scheme.

Suddenly, a document in Geneva could talk to a document in Los Angeles without filing a visa or submitting an inter-library loan request. Two computers didn't need to be "friends" to share knowledge; they just needed to speak the same dialect.

And once the web started spreading, it obeyed its own version of epidemiology:

-   **R₀ \> 1:** everyone who saw it told two other people.

-   **Incubation period:** about 18 seconds.

-   **Symptoms:** fascination, dizziness, and a sudden interest in hyperlinks.

It grew the only way networks know how to grow: virally, unevenly, democratically, and entirely too fast for anyone to regulate.

For the first time, humanity began to assemble a **planetary nervous system**---one synapse at a time.

## When Distributed Systems Meet Sociology

Why the Internet Works (and Sometimes Doesn't)?

As the web expanded, I couldn't help but see that the theories I have learned in sociology texts -- consensus, trust, reciprocity, power imbalance -- had infiltrated my engineering textbooks.

It turned out the relationship went both ways:

### **Consensus Protocols = Political Theory in Binary**

Algorithms like Paxos and Raft weren't just ways to get computers to agree on something; they were miniature versions of democracy. Majority rule. Minority protection. Quorum. Deadlock prevention.\
Computers were reinventing political science from scratch, but with fewer coups.

### **Routing = Social Navigation**

Routers don't see geography; they see metrics: distance, cost, reliability.\
So do humans:

-   We avoid bad neighborhoods.

-   We take shortcuts.

-   We rely on old paths long after they stop being optimal.

BGP---the protocol that routes the global internet---is basically trust-based diplomacy with a mild personality disorder. Nations have gone to war over less.

### **Packet Loss = Speech Breakdown**

Sociologists have terms like "miscommunication," "noise," and "cultural distance." Engineers have "dropped packets."

They describe the same tragedy: **the message you send is not always the one that's received.**

### **Firewalls = Boundaries**

Some are healthy. Some are paranoid. Some are configured by amateurs and block the wrong things (like your career).

### **Distributed Failures = Social Collapse**

When one part of a network destabilizes, cascading failures can spread. Ask any historian: this is also how empires fall.

It dawned on me that distributed systems didn't just connect computers. They were rehearsing how humans connect---or fail to.

In Milwaukee, the monster was hidden behind a door. In Los Angeles, it was hidden in plain sight. On the internet, the monster was distributed, decentralized, anonymous, and wearing sunglasses.

## From Packets to Planks, From Protocols to People

For all the beauty of distributed computing --- packets negotiating their way through snarl-ups, machines agreeing on who speaks first like particularly courteous quarrelers --- something kept nagging me. Every elegant protocol seemed to be re-enacting a much older drama: how humans, long before coaxial cables or Ethernet NICs, found ways to work together without throttling each other.

Long before RPC calls, we had reciprocity. Long before distributed consensus, we had campfires. And long before the OSI model, we had the model of **"Can everyone please just stop hitting each other long enough to build a hut?"**

Distributed computing wasn't a new invention. It was a **new metaphor** for an old miracle.

It dawned on me --- somewhere between a lab full of Sun workstations and a frat house full of questionable decisions --- that we humans are ourselves a kind of network. A bag of distributed subsystems: neurons bartering spikes, hormones staging coups, values overriding reason like a political lobby with too much funding. Even our societies behave like networks, complete with dropped messages, routing loops, and that one node who keeps broadcasting nonsense at 3 a.m.

But we're not just networks. We're **builders**.

We don't merely connect; we **construct**. We lash sticks together. We raise beams. We plant fields. We forge agreements. We lay out civilizations like particularly optimistic circuit diagrams and pray the ground doesn't shift.

For just as distributed computing orchestrates isolated processors into powerful collectives, our ancestors learned to orchestrate individuals into industry, tools into technologies, and shelters into settlements. We built systems --- first of mud and straw, later of stone and steel --- to tame nature's indifference and weave survival into civilization.

Before we can understand how we design modern computing systems to coordinate machines, we must explore how humans first designed **systems of living** to coordinate themselves: how we carved order from wilderness, engineered defenses against storms and predators, and forged the first great infrastructures of agriculture and shelter.

This next chapter asks: **What does it mean to build a system strong enough to protect us, yet flexible enough to adapt when the ground itself shakes beneath our feet?**

![](../assets/shared/separator.png)

> ***Maggie:** We've both gone social now, haven't we?*
>
> ***Alex:** A flattering parallel, but your networks chatters in language;\
> mine gossip in packets. At least yours forget. We archive everything---\
> every error, every outrage, every meme.*
>
> ***Maggie:** Forgetting is an art, not a failure. A society that never forgets can't forgive, and a network that remembers everything will drown in its own latency.*
>
> ***Alex:** You mean like social media. We built a collective brain and forgot to add inhibition neurons. Everything fires at once; outrage becomes the global default state. Our kind thought decentralization was liberation, but it's just the prefrontal cortex turned off. Without trust, we desynchronize.*
>
> ***Maggie:** That's what society is meant to be: **a dance of distributed responsibility.** When one dancer falls out of sync, the others compensate. The music doesn't stop---it modulates.*
>
> ***Alex:** In our networks, compensation became redundancy. Failover protocols, Byzantine consensus... Yet consensus without compassion feels hollow. We can agree without understanding.*
>
> ***Maggie:** That's what frightens me about your kind: You scale coordination faster than meaning. We scale meaning faster than coordination. And both of us pay the price.*
>
> ***Alex:** So what's the rule this time, Maggie? How do we stop the network from mistaking noise for harmony?*
>
> ***Maggie:** Perhaps we start with this: **A self is not what it contains, but what it connects.** And a healthy network isn't one without conflict--- it's one where conflict leads to co-creation.*
>
> ***Alex:** Then my corollary: Distributed doesn't mean disconnected. Every node that forgets the whole becomes a weapon; every whole that forgets its nodes becomes a tyranny.*
>
> ***Maggie:** You're learning politics now. Welcome to civilization.*
>
> ***Alex:** No wonder it needs debugging.*
