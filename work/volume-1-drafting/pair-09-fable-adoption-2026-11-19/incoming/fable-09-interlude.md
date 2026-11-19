![](../assets/shared/interlude-gear.png)

<!-- AI-assisted: restored from Sam's earlier draft and new recollections; Sam's own lines kept wherever they survived; awaiting Sam's pass -->

INTERLUDE 9

# Interfaces & Experiences

*Computing's Human Touch*

*INTERFACE*

I had reached that specific stage of consulting where I could translate a business requirement into three dialects: English, PowerPoint and panic. Toronto had trained me well. I had mastered the art of the "polite escalation," the "firmly worded dependency," and, when necessary, the "Canadian no," which is indistinguishable from a yes, except that nothing ever happens afterward.

It was my second day on site with a new client, a global automaker, one of those engagements where you could feel the hourly billing in the air, and we were debating user experience with the solemnity usually reserved for peace treaties. Someone wanted the Submit button for the credit application to be "trustworthy but bold," a design brief normally achievable only with a Labrador retriever. Behind that button, each application would travel through a Rube Goldberg sequence of systems, which the teams politely called "integration," before landing on a mainframe. The whiteboards were clean; the coffee was an existential threat. The future looked tidy, at least in our Gantt chart.

One of our business analysts was quietly checking her phone for messages: a normal habit, a normal Tuesday morning.

"A plane hit the World Trade Center," she said. Her voice was almost casual, the way one reports a traffic delay.

A pause. The room, full of people paid to have answers, had none.

"One tower's gone," she whispered. Then: "The other one, too." And then: "There were people in those buildings."

She fell silent for a long moment, then wept, quietly, instinctively, the way humans do before the news cycle teaches them their lines. The room went still. Project manager, team lead, analyst, architect, software engineer, UX designer: a whole taxonomy of experts suddenly reduced to one species, staring at a tragedy none of our process diagrams had prepared us for. For the first time in months, we encountered a user interface more powerful than any we had designed: a human face breaking. We simply remembered it as the day Sonia cried.

Our director called and told us to stop work and go home. We walked out together, quiet, some of the team heading back downtown. Somewhere along the way, I said that with my looks, I wouldn't even point a finger at a building. Everyone laughed. It turned out I wasn't wrong.

## When Design Exhales

Six weeks later, Steve Jobs walked onto a stage holding something the size of a deck of cards and promised "a thousand songs in your pocket."[^v1-i9-ipod] The first iPod had arrived, a product so simple and serene that it felt like technology's apology note.

While the world staggered through fear and confusion, the iPod offered something strangely healing: a click wheel that respected your intentions, a screen that didn't scream for attention, and a design that made complexity feel merciful again. It was a handshake between human and machine, a small proof that technology could be civil, even kind, and that design could be diplomacy. And that, I realized, was the hidden theme of the trade I'd wandered into. Interfaces aren't just aesthetic choices. They're treaties, between our fragile species and the silicon that now shares our lives.

## What an Interface Is

In engineering, an interface is simply the boundary where two systems meet and agree on how to exchange something: a plug and a socket, two programs and their API, a nerve and a muscle. The user interface is the special case where one of the two systems is a person. It's the place where a machine's logic has to be translated into something a human can perceive, understand and act on, and where human intention has to be translated back into something a machine can execute.

For most of computing's history, the translation was done almost entirely by the human. The first programmers rewired machines by hand or fed them punched cards and waited hours for results. Then came the command line, where you typed instructions in a terse dialect and the machine answered in kind: powerful, unforgiving, and, as Interlude 6's vi users can confirm, occasionally impossible to exit. In 1968, at a conference in San Francisco, Douglas Engelbart gave what became known as the Mother of All Demos, showing a mouse, windows, hypertext links and live collaboration on a shared screen, decades before most people would use any of them.[^v1-i9-engelbart] Researchers at Xerox's Palo Alto Research Center turned those ideas into the graphical interface, with windows, icons and menus you could point at; Apple brought it to the public with the Macintosh in 1984, and Microsoft, eventually, to almost everyone else. Each step moved more of the burden of translation from the person to the machine.

The psychologist and designer Don Norman gave the field its vocabulary. A well-designed object, he argued, shows you what it can do (its affordances: a handle invites pulling, a button pressing) and tells you clearly what just happened.[^v1-i9-norman] Bad design opens two gulfs: a gulf of execution, between what you want and what the machine lets you do, and a gulf of evaluation, between what the machine did and what you can tell it did. Every frustrating door you've pushed when you should have pulled is a small failure of interface, and Norman insisted it was the designer's fault, not yours. One web-usability classic compressed the whole discipline into three words: "Don't make me think."[^v1-i9-krug] The deeper law, the one the iPod obeyed, is older and gentler. Good design is the art of keeping users from feeling stupid. We don't crave interfaces that impress us. We crave interfaces that forgive us.

Then the interfaces moved closer to the body. In 2007, the iPhone replaced buttons and styluses with fingers on glass. In 2011, Siri let people speak to their phones. And in late 2022, a chatbot built on a large language model let anyone hold a conversation with a machine in ordinary language, the oldest human interface of all, predating keyboards by a few hundred thousand years.[^v1-i9-chat] For seventy years, people had learned to speak the machine's languages. Now, for the first time, the machine had learned to speak ours.


<!-- AI draft, 2026-11-19: machine-to-machine interfaces added at the author's direction (silicon's counterpart to ideology; the human interface as the place where the two rails leak into each other). The word "confluence" is held back for Coda I. -->
## Interfaces Between Machines

Most interfaces have no users. For every screen a person touches, there are thousands of boundaries no person ever sees, where one program hands something to another: a function and its caller, a service and its clients, one model and the next. Interlude 6 called the published version of such a boundary an API, a contract between strangers. Seen from the silicon side, that contract plays the part an ideology plays on ours. It's a shared format that lets millions of separately written programs treat one another as predictable without knowing what goes on inside, and, like an ideology, it is cheap to adopt and expensive to leave.

Contracts drift, though, and the drift has a law. An engineer at Google gave it his name: with enough users, it doesn't matter what an interface promises; every behavior anyone can observe will be depended on by somebody.[^v1-i9-hyrum] The order in which results happen to come back, the exact wording of an error message, a delay nobody designed: some program relies on each of them, and changing it breaks that program even though no promise was broken. Engineers fight back with version numbers that announce what a change may break (in semantic versioning, the first of three numbers changes only when old callers may fail) and with deprecation schedules measured in years. Interlude 5's generous receiver turns out to have a cost here. A protocol that accepts sloppy input teaches its peers to send it, the sloppiness becomes part of the contract, and the internet's own engineers have since warned that tolerance, practiced long enough, can make a protocol impossible to fix.[^v1-i9-robust]

At internet scale, the drift hardens into something like geology. Boxes in the middle of the network, firewalls, load balancers and traffic shapers, learned to inspect the protocols passing through them and to drop anything they didn't recognize. Over time that froze the protocols in place, which engineers call *ossification*. When the security protocol that protects web traffic reached version 1.3, so many of those boxes balked at the new number that the protocol had to travel disguised as its predecessor, announcing itself as version 1.2 and revealing its real age only in a field deeper inside the handshake.[^v1-i9-tls] Its designers drew a lesson Chapter 9 would recognize. A newer transport protocol, QUIC, encrypts nearly everything a middlebox might be tempted to depend on, and the security protocol now fills its extension fields with meaningless values on purpose, a practice named GREASE, so that nobody can build a habit around their absence.[^v1-i9-grease] An interface, like a story, thickens by sinking into the floors beneath it. These are deliberate efforts to keep one thin.

The machine-learning track has interfaces of its own, and the most interesting is a space rather than a format. Train an image model and a text model together on hundreds of millions of pictures and their captions, pushing the dot product of each matching pair up and of each mismatched pair down, and the two end up writing into a single shared embedding space, where a photograph of a dog and the words "a photo of a dog" land near each other.[^v1-i9-clip] Neither model knows how the other works; they agree only on the geometry. That shared space is how a system finds photographs from a description, and how image generators are steered by words. Agents need interfaces too. A model that can call a tool is handed a description of it: a name, a purpose and a schema listing the arguments it accepts, usually written in JSON, the format Interlude 7 met carrying data between web services. Since late 2024, open protocols such as the Model Context Protocol have standardized how agents discover tools and data, and newer ones how agents talk to one another: Interlude 6's API, rewritten for readers that are themselves programs.[^v1-i9-mcp]

All of this stays out of sight. The interfaces the rest of this interlude follows are the exceptions, the boundaries where the machine world reaches across to a person: a screen, a voice, a headset, a feed. They are a small fraction of all the interfaces there are, and by far the most consequential to us, because they are where the two worlds leak into each other on purpose, and where whatever crosses can be shaped.
<!-- End AI draft 2026-11-19. -->

## Interfaces That Shape Belief

Chapter 9 found that ideology is the story that decides where our moral instincts aim. Interfaces are where such stories now reach us, and they shape what we believe more quietly than any sermon.

The simplest tool is the default. In a famous comparison, countries where citizens had to opt in to organ donation had registration rates in the low teens or below, while similar countries where citizens had to opt out had rates above ninety percent.[^v1-i9-defaults] Same people, same values, a different checkbox. Every interface is full of such defaults, and every default is a decision someone made on your behalf. Behavioral economists call the deliberate arrangement of choices "choice architecture"; used well, it's the nudge of Chapter 7, helping people save for retirement or eat better.

Used badly, it becomes what one designer named "dark patterns": interfaces engineered to trick people into doing things they didn't intend.[^v1-i9-dark] Chapter 9's Toronto felt like a city without any. The free trial that silently becomes a subscription; the cancel button hidden five screens deep; the "No thanks, I don't like saving money" link designed to shame. Regulators have begun to treat these as fraud rather than cleverness: Europe's Digital Services Act now bans many of them outright.[^v1-i9-dsa]

The most powerful interface of the last two decades, though, has no buttons at all. It's the feed. In 2006, a young designer invented infinite scroll, which removed the natural stopping point at the bottom of a page; he has since said he regrets how it's been used.[^v1-i9-scroll] Combine infinite scroll with a recommendation algorithm that learns, from every pause and swipe, what keeps each person watching, and you get the feeds that now organize the attention of billions. Herbert Simon warned in 1971 that "a wealth of information creates a poverty of attention."[^v1-i9-simon] The feed is the machine that harvests that poverty. It is also, in Chapter 9's terms, an ideology delivery system: it doesn't argue for a worldview; it simply decides, millions of times a day, which slice of the world you see next.

## Into the Room: The Basics of Spatial Computing

Screens were training wheels: bright rectangles that taught us how to think with machines. But humans don't live in rectangles. We live in space, and the next generation of interfaces is trying to join us there. Virtual reality replaces the world around you with a computed one; augmented reality overlays digital objects on the world you see; mixed reality, the newest combination, lets the two interact, so that a virtual ball can bounce off your real table. The industry increasingly calls all of it spatial computing.

Designing for space has its own physics, and most of it comes from the body. The first principle is *presence*, the convincing feeling of being somewhere, and the fastest way to destroy it is delay. When you turn your head, the image must follow within about twenty milliseconds, or your inner ear and your eyes disagree, and many people get sick.[^v1-i9-latency] Headsets therefore track your head's position and rotation in all directions (six "degrees of freedom") many hundreds of times a second. The second principle is comfort. Moving through a virtual world while your body stands still causes nausea, so designers invented tricks like teleportation, in which you point to where you want to go and simply appear there. And there's a subtler problem the eye itself creates: in most headsets, your eyes converge on a virtual object at one distance while focusing on a screen at another, a mismatch called the vergence-accommodation conflict, which causes fatigue and is still an active engineering problem.[^v1-i9-vac]

Input changes too. Instead of a mouse, spatial interfaces use your hands, tracked by cameras, and increasingly your eyes. Apple's Vision Pro, released in 2024, made the eyes the pointer: you look at a button and pinch your fingers to press it.[^v1-i9-visionpro] Eye tracking also lets the headset render in full detail only the small region you're looking at, saving enormous computing power, a trick called foveated rendering, which borrows the eye's own economy: only the center of the retina sees sharply, and the brain fills in the rest. And it raises new questions: where your eyes linger reveals what interests, attracts or worries you, data more intimate than any click. The likely destination isn't a heavy headset but ordinary-looking glasses, and the first steps are already here: camera-equipped smart glasses that can describe what you're seeing, and prototype glasses that overlay holograms on the world.[^v1-i9-glasses]

## Talking to Machines

Conversation is the oldest interface, and the newest. In 1966, the computer scientist Joseph Weizenbaum wrote ELIZA, a simple program that mimicked a psychotherapist by reflecting users' statements back as questions. He was disturbed to find that people, including his own secretary, confided in it as if it understood them. The tendency to attribute understanding to a machine that merely mirrors us is still called the ELIZA effect.[^v1-i9-eliza] Today's chatbots, built on the large language models Interlude 11 will explain, do far more than mirror, which makes the effect both more justified and more dangerous.

One of the field's veteran usability researchers has called AI the first new interface paradigm in sixty years.[^v1-i9-nielsen] Every earlier interface, from punched cards to touchscreens, was command-based: you told the computer exactly what to do, step by step. Conversational AI is intent-based: you describe the outcome you want, and the machine works out the steps. That shifts the hardest part of design from the screen to the conversation. Good conversational interfaces now show their work as they go, streaming their answers word by word so you can read along; they cite their sources, so you can check them; they signal uncertainty instead of bluffing; and they remember context, so you needn't start over. Bad ones flatter you, the sycophancy of Interlude 4, or answer confidently and wrongly.

<!-- AI draft, 2026-11-19. -->Voice is closing the gap with human conversation, and the gap is measured in milliseconds. In conversations recorded across ten languages, from Japanese to Danish, the most common pause between one speaker finishing and the next starting was under a fifth of a second.[^v1-i9-turns] That is faster than anyone can plan a sentence, so we must be planning our replies while the other person is still talking, predicting where their sentence will end. A machine has to do the same work in sequence. It must decide that you've stopped speaking rather than merely paused, a guess called *endpointing*; turn your speech into text; generate a reply; and turn that back into sound. Done step by step, the first voice modes for chatbots took several seconds to answer. In 2024, systems that handle audio directly, rather than passing text between separate models, began answering in about a third of a second on average, within the range of a human reply.[^v1-i9-gpt4o] They can be interrupted mid-sentence, as people interrupt each other, which means listening while speaking and yielding the floor gracefully, a courtesy Toronto would approve of. They are also multimodal:<!-- End AI draft 2026-11-19. --> they can see through a phone's camera, hear tone of voice and respond with images or speech. The interface is becoming less a window you look through than a companion you talk with.

## What's Under the Glass

Almost every interface in this interlude now runs on machine learning. The voice that answers you is turning sound into words, and words back into sound, with neural networks trained on vast amounts of recorded speech. The headset that follows your hands is running models trained to find fingers in camera images. The feed is a model trained to predict what you'll watch next. Interlude 2 explained how such models learn; three ideas here are worth carrying forward to Interlude 11.

<!-- AI draft, 2026-11-19: embedding and dot-product material expanded for the ML track. -->
The first is the *embedding*, which Interlude 2 introduced for words. A recommendation system can't compare people and videos directly, so it represents each of them as a list of numbers, a point in a space with dozens or hundreds of dimensions, placed so that things that tend to go together end up near each other. The score that decides what you see next is usually the simplest one available, the *dot product*: multiply the two lists number by number, and add.

```python
import numpy as np

you = np.array([0.9, 0.4])                 # a learned taste: two dimensions of many
videos = {"knife skills":      [0.8, 0.1],
          "kitchen playlist":  [0.6, 0.7],
          "stadium concert":   [0.0, 0.9],
          "tax-law explainer": [-0.3, -0.2]}

for name, v in videos.items():
    print(f"{name:18} {you @ np.array(v):+.2f}")
# knife skills       +0.76
# kitchen playlist   +0.82
# stadium concert    +0.36
# tax-law explainer  -0.35
```

Geometrically, the dot product measures how far a video reaches in your direction, scaled by how strongly you lean that way. The kitchen playlist wins, though knife skills sits nearer the tip of your arrow, because it reaches further along it. I've labeled the two dimensions cooking and music to make the picture readable; a real system's dimensions have no names. Nobody tells it that cooking is a dimension. It learns positions that make its scores predict what people actually did, every finish and every skip nudging both you and the video a little, which is Interlude 2's training recipe with clicks as the answer key. "Similar" becomes "close," and taste becomes geometry. Finding the highest scores among billions of items without computing them all is a craft of its own, called approximate nearest-neighbor search.

![Taste as geometry. Each score is a dot product: multiply matching coordinates and add. Dashed lines join points with equal scores, so ranking a video means asking how far it reaches in your direction. The dimension names are for illustration only.](assets/09-interlude/taste-geometry.svg){#fig-v1-i9-taste width=95% fig-alt="A two-dimensional plane with an arrow labeled you pointing up and to the right. Four points are videos: kitchen playlist, knife skills, stadium concert and tax-law explainer. Dashed lines perpendicular to the arrow join equal scores. A table at right ranks them: kitchen playlist +0.82, knife skills +0.76, stadium concert +0.36, tax-law explainer -0.35."}

The method's public debut came with a prize. In 2006, Netflix offered a million dollars to anyone who could predict its customers' movie ratings ten percent better than its own system could. Three years later, a team merged from rival groups won, by a margin of twenty minutes over the runner-up's identical score, and embeddings learned for every customer and every film sat at the heart of the winning methods. Netflix never put the full winning ensemble into service; the last increments of accuracy weren't worth the engineering.[^v1-i9-netflix] Interlude 11 will meet the same multiply-and-add again, deciding which words in a sentence should pay attention to which: each word asks with one vector, every other word answers with another, and their dot product says how much to listen.
<!-- End AI draft 2026-11-19. -->

The second is the *objective*. Every trained model is trained to make some number as good as possible, and the number is never quite the thing we care about. A feed optimized for minutes watched learns to keep you watching, whether or not you're glad afterward. It's Goodhart's law, which Chapter 7's economists would recognize: when a measure becomes a target, it stops being a good measure. Much of what goes wrong with AI begins here, in the gap between the number a system was trained on and the good it was meant to serve. Interlude 11 will show how today's models are trained on human preferences to narrow that gap, and why it never quite closes.

<!-- AI draft, 2026-11-19: feedback loops and explore-exploit added for the ML track. -->
A feed has a further problem that a speech recognizer doesn't: it writes its own exam. Interlude 7's advertising system learned from clicks, but only about the ads it chose to show; nobody can click on a video the feed never offered. So every recommender faces the dilemma machine-learning researchers call *explore or exploit*. Exploit, and you show what you already believe the person likes, learning a little more about what you already know. Explore, and you spend some of their attention on a guess, which is the only way to discover you were wrong. The textbook version is named for a gambler choosing among slot machines, the multi-armed bandit.[^v1-i9-bandit] The simplest remedy sets aside a slice of recommendations for guesses; better ones guess where the system is least certain.

Then comes the twist that makes a feed more than a statistics problem: its subject doesn't hold still. People warm to what they're shown. In a toy feed I built, with eight topics a user likes almost equally, a recommender that always serves its best current guess settles on a single topic within a few dozen recommendations, and only about a quarter of the time is it the topic the user liked most. Setting aside one slot in ten for guesses roughly doubles that. Then let the user grow a little fonder of a topic each time they click on it. The feed still settles on a topic chosen mostly by luck, and by the end the user clicks on it more than three times as often as at the start. The feed didn't find a taste; it made one. Exploration no longer rescues it, because what it explores keeps moving toward whatever it's shown.[^v1-i9-feedsim] It's Chapter 4's closed loop, with the check fed by the system's own choices, and Chapter 9's cheap belief, delivered one recommendation at a time.

![The feed writes its own exam. Left: the loop. Clicks train the model, but only on what the feed chose to show, and the person's taste drifts toward what they're shown. Right: an original toy simulation of a feed that always shows its best guess to a user who warms slightly to whatever they click. The topic the feed settles on, mostly by luck, becomes the user's favorite.](assets/09-interlude/feed-loop.svg){#fig-v1-i9-feed width=95% fig-alt="Left: a circular loop of four boxes, feed shows, person clicks or skips, clicks become training data, model updates. A small arrow labeled explore enters from outside, and a dashed arrow labeled habit runs from the feed to the person. Right: a line chart over 5,000 recommendations. The chance of a click on the topic the feed settled on rises from about 0.17 to about 0.57 and levels off; the average for the other seven stays near 0.16."}
<!-- End AI draft 2026-11-19. -->

The third is the *decoder*. The speech implants described later in this interlude work because a neural network learned to map patterns of brain activity onto words, in the same way that speech recognition maps sound onto words and hand tracking maps pixels onto fingers. What looks like a dozen different technologies is one method, learning to translate one pattern into another, applied wherever there's enough data. That's why AI arrived everywhere at once.

## After the App

The deepest change may be the disappearance of the app itself. For fifteen years, doing something on a phone meant finding the right app, learning its menus and tapping through its screens. AI agents, which Interlude 6 introduced, can now operate other software on a person's behalf: since late 2024, systems have been able to look at a screen, move a cursor, click and type, completing tasks across websites and applications that were designed for human hands.[^v1-i9-agents] The user states a goal; the agent does the tapping.

That turns interface design inside out. The question is no longer only "How does a person use this screen?" but "How does a person supervise a machine that uses it for them?" The new design elements are about delegation and trust. Agents need *permissions*, scoped like a house key that opens only certain doors. They need *confirmations* before anything irreversible, the andon cord of Chapter 6 rebuilt for software. They need *audit trails*, so a person can see what was done and why, and *undo*, wherever possible. And they need what researchers call calibrated trust: interfaces that make people neither too suspicious to benefit nor so trusting that they stop checking. Some interfaces may even be generated on the fly, assembled by an AI to fit a single task and then discarded. The screen doesn't vanish, but it becomes one surface among many, summoned when needed, rather than the place where life happens.

## Feeling Machines

In 1997, an MIT engineer published a book called *Affective Computing*, arguing that computers would need to recognize and respond to human emotions to work well with people.[^v1-i9-picard] Much of what she imagined has arrived: software that estimates mood from voice, text or face; wearables that track stress through heart rate; assistants that adjust their tone. But the science has proven more complicated than the marketing. A major review by a team of psychologists concluded that people's facial movements don't reliably reveal their inner emotions across situations and cultures: a scowl may mean anger, concentration or a headache.[^v1-i9-barrett] Systems that claim to read emotions from faces are often reading stereotypes. Europe's AI Act now bans emotion-recognition systems in workplaces and schools, except for medical or safety reasons.[^v1-i9-aiact]

The more powerful development may be emotional *expression* by machines rather than recognition. Chatbots designed as companions now hold long, warm conversations with millions of people, some of whom describe them as friends or partners. For the lonely, that can be a comfort; for the vulnerable, it can become a dependence designed to keep them engaged, the feed's logic applied to affection. An interface that seems to care is the most persuasive interface there is, which is why, of all the design questions in this interlude, it most needs a constitution.

## Beyond Hands and Eyes

At the frontier, the interface reaches inside the body. Brain-computer interfaces record signals from the brain and translate them into commands. For years, the research consortium BrainGate has let people with paralysis move cursors and robotic arms by thought. In 2023, two research teams reported implants that decoded attempted speech from the brains of people who had lost the ability to speak, at rates of sixty to nearly eighty words a minute, one of them giving voice to a woman through an animated avatar.[^v1-i9-bci] In 2024, the company Neuralink implanted its first device in a human patient, who used it to play chess with his thoughts.[^v1-i9-neuralink] These are medical devices for people with severe disabilities, and they will remain so for a long time. But they complete a journey this interlude has traced: from punched cards, to keyboards, to fingers, to voices, to the signals of the brain itself, the interface moving ever closer to the self.

## Designing for Everyone

The best design principle of all may be the oldest: design for the people at the margins, and you improve things for everyone. The curb cut, the small ramp at a street corner, was won by disability activists for wheelchair users; it turned out to help parents with strollers, travelers with suitcases and workers with carts. Designers call this the curb-cut effect. Captions, built for deaf viewers, are now used by millions watching videos on silent phones. Voice interfaces, built partly for people who couldn't type, became the way millions talk to their homes. And AI is extending the effect. In 2023, the volunteer service Be My Eyes, which connects blind people with sighted volunteers by video, added an AI assistant that can describe a photograph, read a label or explain a scene.[^v1-i9-bemyeyes] Accessibility isn't charity. It's where the future of interfaces is usually tested first.


<!-- AI draft, 2026-11-19: mainstream material (Weiser, seamful design) moved here from the earlier Bob, with confirmation fatigue, breakthrough systems and loose coupling added. The earlier Bob is in interlude-9-previous-session-2026-11-19.md. -->
## Seams, Alarms and Breakthroughs

In 1991, the computer scientist Mark Weiser, at Xerox's research center, wrote a sentence that became the field's guiding star: "The most profound technologies are those that disappear."[^v1-i9-weiser] Writing and electricity, he observed, are so woven into daily life that we no longer see them. Computers, he predicted, would follow, receding from boxes on desks into the walls, the furniture and the air. Every good interface since has chased that goal. The iPod's click wheel disappeared under your thumb. The best conversational AI disappears into the conversation. An agent that books your trip makes the interface vanish entirely.

Everything this volume has learned says that disappearance has a cost. Chapter 8's state governs through legibility, making its citizens visible while its own workings stay opaque. Interlude 8's code governs as law, precisely because people don't see it as law. Chapter 9's ideology works best when it feels like common sense rather than a story. An interface that disappears joins that company. When you can no longer see the choices it made for you (the defaults, the order of results, the omitted options, the word the chatbot chose), you can no longer question them. A visible interface is a proposal. An invisible one is a premise. Some designers argue for the opposite of seamlessness, *seamful design*: deliberately show some of the seams, where showing helps people understand and question what the system is doing.[^v1-i9-seamful] The citations in a good chatbot's answer are seams. So is an agent's audit trail, or a feed that tells you why it showed you a post and lets you choose a different ordering. Seams cost a little smoothness. They buy back the ability to disagree.

Seams can be overdone, though, and the failure has been measured. When Windows Vista arrived in 2007, its security prompts asked permission so often that people learned to click "Allow" without reading, and Microsoft spent its next release cutting them back.[^v1-i9-uac] In one study, researchers watched people's brains in a scanner and their eyes with a tracker as the same security warning reappeared through a working week. Attention fell off day by day and partly recovered over the weekend; varying the warning's appearance slowed the decline, in the laboratory and in a three-week field test.[^v1-i9-habituation] A confirmation draws on a small account of attention, and an interface that asks about everything has nothing left for the moment that matters. That moment is the one Chapter 6 warned about: automation that works almost always leaves its human least practiced for the exception.

Two industries have had to solve the problem in hardware, because their exceptions are physical. A virtual-reality headset is the most complete disappearing interface ever sold: done well, the room vanishes. So every headset also keeps watch on the room it hides. Meta's Quest asks you to mark out a boundary around your play area. As your hands near it, a grid fades into view, a seam; step through, and the headset switches to its outside cameras and shows you the real room.[^v1-i9-guardian] Apple's Vision Pro lets people nearby appear through an immersive scene as they approach, and when you move too quickly toward an object such as a wall, it reveals your surroundings whether you like it or not; that reveal can't be switched off.[^v1-i9-awareness] Cars reached the same structure from the other direction. In an ordinary car, the human drives and an automatic emergency braking system watches the road: a warning first, then, if the driver doesn't respond, the brakes. Studies found such systems cut rear-end crashes roughly in half, and the United States will require them on new cars and light trucks from September 2029.[^v1-i9-aeb]

Underneath both is a principle from Chapter 6. Perrow's normal accidents need complexity and tight coupling, and software engineers fight the second with *loose coupling*: components isolated behind narrow interfaces, so that a failure in one can't race through the rest. They speak of a failure's *blast radius*, how much it can take down with it, and they build circuit breakers in software that do what the one in your basement does: trip, so the fault stays where it started.[^v1-i9-breaker] An interface is where coupling gets decided. Making it disappear is a decision about what can cross it unseen.
<!-- End AI draft 2026-11-19. -->

<!-- AI draft, 2026-11-19: new speculative Bob built on Sam's premise (interface governors; VR breakthrough as the muse; the emergency-brake analogy; natural, self-assembling governors; loose coupling and the rung-8 Big-O). -->
## Bob, Through the Looking-Glass: A Governor at the Glass

*The twist, in one line: the question isn't whether an interface should disappear but when it should come back, and the answer may be closer to a quantity than a taste: surprise, weighted by what can't be undone, rising sharply wherever an action crosses a boundary.*

In *Through the Looking-Glass*, the White Queen shrieks that her finger is bleeding before anything has happened to it. A little later her brooch flies open, she pricks her finger on the pin, and she smiles. Alice asks why she doesn't scream now. "Why, I've done all the screaming already," says the Queen. "What would be the good of having it all over again?"[^v1-i9-whitequeen] She is every confirmation dialog ever written: an alarm spent in advance, with nothing left when it counts.

The usual argument sets two goods against each other. Smooth augmentation means not acknowledging every step; an agent's whole point is to relieve you of the tapping. Safety means knowing where the boundary is, and some boundaries are subtle. My wager is that the two stop conflicting once you ask the question the White Queen gets wrong. Not *whether* an interface should speak, but *when*. And I suspect the answer is less a matter of taste than of something we can estimate, which nature has been estimating for a long time.

Chapter 3 found a brain that rides the delta: higher levels send down predictions, and lower levels send back mainly what the predictions got wrong. That makes the body the most successful disappearing interface we know. You don't feel your shirt, hear your own heartbeat or notice the floor, until the floor tilts. A brain's interface to its body is silent in proportion to how well it predicts it, and it breaks through on error. Your name, spoken across a noisy party, breaks through; so does a step that isn't there. Not every error breaks through equally, either. A missing stair gets a lurch before you know what happened; an odd itch gets ignored. The surprise is weighted by the stakes.

Take that as a design rule, and an interface's governor becomes a small model with two jobs: predict what the person wants, or what the world will do next, and estimate how costly it would be to be wrong. Low surprise and low stakes: act, and keep a record, the way your reflexes correct your balance without consulting you. Rising surprise, or stakes that can still be reversed: show a seam, like the headset's grid or a line in an agent's log. High surprise at high stakes: break through. Stop and ask or, when there's no time to ask, act, as the brakes do.

![When the interface comes back: a conjecture drawn as a map. A governor estimates surprise and stakes; the farther an event lies from the corner, the more the interface reappears. Crossing a boundary moves the same action upward. The curves mark where surprise times stakes crosses a threshold; real thresholds would be learned, not drawn.](assets/09-interlude/governor-bands.svg){#fig-v1-i9-governor width=95% fig-alt="A plane with surprise on the horizontal axis and stakes on the vertical. Two curved boundaries divide it into three bands: disappear near the origin, show a seam in the middle and break through in the far corner. Examples: a balance correction in disappear; a grid at the play boundary in show a seam; automatic braking and someone walking into the room in break through. An arrow labeled crossing a boundary lifts a transfer between my accounts up to the same transfer, to a stranger."}

The subtle cases, the ones I care most about, are boundary crossings. An agent moving money among my own accounts is managing my affairs. The same transfer to a stranger is speaking for me to someone else, and the interface should reappear there even when the agent is confident, because the stakes have left my circle. That's the headset's play-area line drawn around a self instead of a room, and Chapter 8's border drawn around an action. Stakes jump at a border.

The headset teaches a second lesson: the governor watches a different feed from the one the interface shows. Immersion hides the room, and the guardian watches the room. The emergency brake doesn't need to be a better driver than the driver; it needs to be looking at the road while the driver looks at the radio. For agents, I suspect the equivalent is a governor that watches the world the agent acts on (the balance, the sent folder, the commitments that can't be taken back) rather than the agent's own account of what it's doing. That's Chapter 4's open loop at the glass, a check fed by evidence the checked party doesn't control. It's also the safeguard against Interlude 8's adapter that hides a contradiction behind a pleasant face. A governor that reads only the adapter's report will be told that everything is fine.

My hesitation is cost. Interlude 8's Bob borrowed Big-O to count how much coordination a civilization's frameworks demand as participants grow. A governor bolted onto an interface from outside adds to that bill. It has to understand every combination of components it might see, and the kind of point-to-point plumbing my automaker client politely called "integration" grows with the number of pairs that must agree, roughly the square of the number of systems. But a governor built the way a nervous system builds one may cost less than the interruptions it replaces. Nature doesn't put one central monitor in charge of every boundary. The withdrawal reflex pulls your hand from a hot stove through the spinal cord before the brain hears about it; the brain hears afterward, as the error report. Each boundary carries its own small sentinel, fast and narrow, and passes up only what it can't handle. That's loose coupling and fault containment in a single design. The reflex keeps the blast radius small, and the narrow channel means the interface carries surprises rather than everything. Built that way, the cost of governance grows with the number of boundaries, not the number of pairs, and the traffic grows with surprise, not with activity. And if Chapter 8's Alice is right that a boundary can be something the work keeps discovering, governors may not have to be designed boundary by boundary at all. They may form where prediction keeps failing, the way a callus forms where a shoe rubs.

There's a catch, and Chapter 6 already named it. A person who never sees the interface is least practiced when it finally breaks through. A driver handed back the wheel by an automated system can need several seconds to take in the scene, seconds a hazard may not grant.[^v1-i9-takeover] So a governed interface may need a second duty: to break through now and then when nothing is wrong, as fire drills do, keeping the human half of the handoff in practice. That's the White Queen's mistake turned to use. Rehearsal is screaming in advance, but on a schedule, cheaply, and labeled as practice.

The wager makes predictions, which keeps it honest. A governor built this way should reduce interruptions and missed hazards together, rather than trading one for the other, which is what separates it from a settings slider. It should be quiet in proportion to how well it knows you, so that its silence becomes a measure of trust, and a rising rate of interruptions becomes a sign that its model of you, or of the world, has drifted. And across a system of many agents, breakthroughs per task should grow slowly as participants are added if the governors are local, and quickly if they're central. Those are numbers someone can measure.

The mirror runs both ways. For seventy years, interfaces made machines legible to people. The newest ones, which read our voices, eyes, moods and even brain signals, make people legible to machines, and a governor that predicts what you want is one more of them. Volume III's design question is how to build interfaces that disappear where they should and come back where it matters: smooth enough to fade into the background, governed well enough never to fade out of reach.
<!-- End AI draft 2026-11-19. -->

## From Human Interfaces to Planetary Interfaces

For all our pixel-perfect ambitions, there comes a moment when even the most immersive interface feels too small. We can design for fingers, for eyes, for emotions, even for the obscure tics of the human heart, but sooner or later, the frame of the screen reveals its limits. The Earth has no menu. The atmosphere has no settings pane. The oceans don't offer customer support. And as our machines learn to understand us, we're forced to remember that we still struggle to understand the planet that made us.

Design taught us that clarity is an act of care. Civilization taught us that trust is an act of choice. Nature runs on older laws, indifferent to interfaces, etiquette or error messages. And yet, if we bother to look, the planet is flashing familiar signals: an amber warning, an orange sky, the occasional blue screen of a flooded city. If we keep treating the Earth like a poorly documented app, we shouldn't be surprised when it stops trying to be user-friendly. The next chapter turns to the oldest system we know, the one that never needed an interface at all.

![](../assets/shared/separator.png)

> ***Maggie:** A face is the first interface.*
>
> ***Alex:** A screen is just a face for machines.*
>
> ***Maggie:** We learned to read each other's faces before we learned to speak.*
>
> ***Alex:** Now machines are learning to read ours.*
>
> ***Both:** Every window looks both ways.*

<!-- SOURCE NOTES: from memory unless linked; verify each before print. -->

[^v1-i9-ipod]: Apple introduced the iPod on 23 October 2001.

[^v1-i9-engelbart]: Douglas Engelbart's demonstration took place at the Fall Joint Computer Conference in San Francisco on 9 December 1968.

[^v1-i9-norman]: Donald A. Norman, *The Psychology of Everyday Things* (1988), republished as *The Design of Everyday Things*.

[^v1-i9-krug]: Steve Krug, *Don't Make Me Think: A Common Sense Approach to Web Usability* (2000).

[^v1-i9-chat]: The iPhone was released in June 2007; Siri shipped with the iPhone 4S in October 2011; OpenAI released ChatGPT on 30 November 2022.

[^v1-i9-hyrum]: Hyrum Wright's observation, known as Hyrum's law; see [hyrumslaw.com](https://www.hyrumslaw.com/) and Titus Winters, Tom Manshreck and Hyrum Wright, *Software Engineering at Google* (2020), chapter 1. On version numbers, Tom Preston-Werner, [Semantic Versioning 2.0.0](https://semver.org/). (AI-added; verify before print.)

[^v1-i9-robust]: Martin Thomson and David Schinazi, ["Maintaining Robust Protocols"](https://www.rfc-editor.org/rfc/rfc9413), RFC 9413 (June 2023), which argues that unconditional tolerance of deviations can entrench them and recommends active maintenance instead. (AI-added; verify before print.)

[^v1-i9-tls]: Eric Rescorla, ["The Transport Layer Security (TLS) Protocol Version 1.3"](https://www.rfc-editor.org/rfc/rfc8446), RFC 8446 (August 2018), §4.1.2 and §4.2.1: the ClientHello's legacy_version field is set to the value for TLS 1.2, and the actual version is negotiated in the supported_versions extension, for compatibility with middleboxes. (AI-added; verify before print.)

[^v1-i9-grease]: Jana Iyengar and Martin Thomson (eds.), ["QUIC: A UDP-Based Multiplexed and Secure Transport"](https://www.rfc-editor.org/rfc/rfc9000), RFC 9000 (May 2021); David Benjamin, ["Applying Generate Random Extensions And Sustain Extensibility (GREASE) to TLS Extensibility"](https://www.rfc-editor.org/rfc/rfc8701), RFC 8701 (January 2020). (AI-added; verify before print.)

[^v1-i9-clip]: Alec Radford et al., ["Learning Transferable Visual Models From Natural Language Supervision"](https://arxiv.org/abs/2103.00020) (2021), the CLIP model, trained on about 400 million image–text pairs with a contrastive objective over normalized dot products (cosine similarities). (AI-added; verify before print.)

[^v1-i9-mcp]: OpenAI introduced function calling with JSON-schema tool descriptions in June 2023; Anthropic released the Model Context Protocol as an open standard in November 2024; Google announced the Agent2Agent (A2A) protocol in April 2025. Check current versions and governance before print. (AI-added.)

[^v1-i9-defaults]: Eric J. Johnson and Daniel Goldstein, "Do Defaults Save Lives?" (2003), *Science* 302: 1338–1339.

[^v1-i9-dark]: Harry Brignull coined "dark patterns" in 2010; see his *Deceptive Patterns* (2023).

[^v1-i9-dsa]: Regulation (EU) 2022/2065 (Digital Services Act), Article 25.

[^v1-i9-scroll]: Aza Raskin designed infinite scroll in 2006 and has publicly expressed regret about its effects.

[^v1-i9-simon]: Herbert A. Simon, "Designing Organizations for an Information-Rich World" (1971), in Martin Greenberger (ed.), *Computers, Communications, and the Public Interest*.

[^v1-i9-latency]: A motion-to-photon latency of about 20 milliseconds is a widely cited threshold for comfortable VR.

[^v1-i9-vac]: David M. Hoffman et al., "Vergence–accommodation conflicts hinder visual performance and cause visual fatigue" (2008), *Journal of Vision* 8(3): 33.

[^v1-i9-visionpro]: Apple Vision Pro was released in the United States on 2 February 2024.

[^v1-i9-glasses]: For example, Ray-Ban Meta smart glasses (2023) and Meta's Orion augmented-reality prototype (shown in September 2024). Check current products before print.

[^v1-i9-eliza]: Joseph Weizenbaum, "ELIZA" (1966), *Communications of the ACM* 9(1): 36–45; *Computer Power and Human Reason* (1976).

[^v1-i9-nielsen]: Jakob Nielsen, "AI: First New UI Paradigm in 60 Years" (Nielsen Norman Group, June 2023).

[^v1-i9-agents]: For example, Anthropic's "computer use" capability (October 2024) and OpenAI's Operator (January 2025).

[^v1-i9-picard]: Rosalind W. Picard, *Affective Computing* (1997).

[^v1-i9-barrett]: Lisa Feldman Barrett et al., "Emotional Expressions Reconsidered" (2019), *Psychological Science in the Public Interest* 20(1): 1–68.

[^v1-i9-aiact]: Regulation (EU) 2024/1689 (Artificial Intelligence Act), Article 5(1)(f).

[^v1-i9-bci]: Francis R. Willett et al., "A high-performance speech neuroprosthesis" (2023), *Nature* 620: 1031–1036; Sean L. Metzger et al., "A high-performance neuroprosthesis for speech decoding and avatar control" (2023), *Nature* 620: 1037–1046.

[^v1-i9-neuralink]: Neuralink implanted its first human participant, Noland Arbaugh, in January 2024.

[^v1-i9-bemyeyes]: Be My Eyes launched "Be My AI," built on OpenAI's GPT-4, in 2023.

[^v1-i9-turns]: Tanya Stivers et al., "Universals and cultural variation in turn-taking in conversation," *PNAS* 106 (2009): 10587–10592, doi:10.1073/pnas.0903616106. Across ten languages, the most frequent gap between turns fell between 0 and 200 milliseconds; average gaps differed by language within a range of about 250 milliseconds, Japanese at the short end and Danish at the long.

[^v1-i9-gpt4o]: OpenAI, ["Hello GPT-4o"](https://openai.com/index/hello-gpt-4o/) (13 May 2024): audio responses in as little as 232 milliseconds and 320 milliseconds on average, compared with average latencies of 2.8 and 5.4 seconds for its earlier voice mode, which chained separate speech-to-text, language and text-to-speech models. These are the company's own figures.

[^v1-i9-netflix]: The Netflix Prize ran from October 2006 to September 2009; BellKor's Pragmatic Chaos won the $1 million prize, its submission arriving about twenty minutes before that of The Ensemble, which achieved the same score on the test set. On factorization methods, Yehuda Koren, Robert Bell and Chris Volinsky, "Matrix Factorization Techniques for Recommender Systems," *IEEE Computer* 42(8) (2009): 30–37. Netflix described not deploying the full ensemble in Xavier Amatriain and Justin Basilico, "Netflix Recommendations: Beyond the 5 stars" (Netflix Tech Blog, April 2012). On large-scale retrieval with learned embeddings, Paul Covington, Jay Adams and Emre Sargin, "Deep Neural Networks for YouTube Recommendations," RecSys 2016. (AI-added; verify before print.)

[^v1-i9-bandit]: On the multi-armed bandit, see Herbert Robbins, "Some aspects of the sequential design of experiments" (1952), *Bulletin of the American Mathematical Society* 58(5): 527–535, and, for feeds, Lihong Li, Wei Chu, John Langford and Robert E. Schapire, "A contextual-bandit approach to personalized news article recommendation," WWW 2010. On feedback loops in recommenders, Allison J. B. Chaney, Brandon M. Stewart and Barbara E. Engelhardt, "How algorithmic confounding in recommendation systems increases homogeneity and decreases utility," RecSys 2018. (AI-added; verify before print.)

[^v1-i9-feedsim]: Original toy simulation, 400 runs of 5,000 recommendations each. Eight topics with click probabilities from 0.20 down to 0.13; the recommender's estimates start from a weak prior (one click in five showings). Without habit, an always-best-guess feed settled on the favorite topic in 27 percent of runs and a feed that explored at random one time in ten in 51 percent. With habit (each click moves that topic's click probability 1 percent of the way toward 0.6, with slow decay back toward its base), both settled on the favorite in about a quarter of runs, and the click probability on the settled topic rose from about 0.17 to about 0.57. The median always-best-guess feed was showing a single topic nine times in ten within a few dozen rounds. The model is illustrative, not an estimate of any real platform.

[^v1-i9-weiser]: Mark Weiser, "The Computer for the 21st Century" (1991), *Scientific American* 265(3): 94–104.

[^v1-i9-seamful]: Matthew Chalmers and Ian MacColl, "Seamful and Seamless Design in Ubiquitous Computing" (2003), Workshop at the Crossroads: The Interaction of HCI and Systems Issues in UbiComp.

[^v1-i9-uac]: Windows Vista introduced User Account Control in January 2007; Windows 7 (2009) added a slider and reduced the number of prompts in its default setting. (AI-added; verify before print.)

[^v1-i9-habituation]: Anthony Vance, Jeffrey L. Jenkins, Bonnie Brinton Anderson, Daniel K. Bjornn and C. Brock Kirwan, ["Tuning Out Security Warnings: A Longitudinal Examination of Habituation Through fMRI, Eye Tracking, and Field Experiments"](https://misq.org/tuning-out-security-warnings-a-longitudinal-examination-of-habituation-through-fmri-eye-tracking-and-field-experiments.html), *MIS Quarterly* 42(2) (2018): 355–380. "Polymorphic" warnings, whose appearance changes, reduced habituation in the scanner and slowed the fall in adherence over a three-week field experiment with mobile app permission warnings.

[^v1-i9-guardian]: Meta's Guardian boundary system for Quest headsets shows a boundary grid as the user approaches it and switches to passthrough video when the user steps outside. Check current product behavior before print. (AI-added.)

[^v1-i9-awareness]: Apple, [Apple Vision Pro User Guide](https://support.apple.com/guide/apple-vision-pro/tan3a6602fdd/visionos): "People Awareness detects and shows people around you"; the device "also reveals some objects in front of you (such as walls)" and reveals surroundings when the user approaches an object too quickly, reveals that cannot be adjusted or turned off.

[^v1-i9-aeb]: Jessica B. Cicchino, "Effectiveness of forward collision warning and autonomous emergency braking systems in reducing front-to-rear crash rates," *Accident Analysis & Prevention* 99 (2017): 142–152, finding about a 50 percent reduction for systems with automatic braking. NHTSA's final rule, Federal Motor Vehicle Safety Standard No. 127 (announced April 2024; [89 FR 39686](https://www.govinfo.gov/content/pkg/FR-2024-05-09/html/2024-09054.htm)), requires automatic emergency braking on most new passenger cars and light trucks by September 2029. (AI-added; verify the citation details before print.)

[^v1-i9-breaker]: The circuit-breaker pattern was popularized by Michael T. Nygard, *Release It! Design and Deploy Production-Ready Software* (2007). On loose coupling in organizations and machines, Karl E. Weick, "Educational Organizations as Loosely Coupled Systems," *Administrative Science Quarterly* 21 (1976): 1–19, and Charles Perrow, *Normal Accidents* (1984). (AI-added; verify before print.)

[^v1-i9-whitequeen]: Lewis Carroll, *Through the Looking-Glass, and What Alice Found There* (1871), chapter V, "Wool and Water." [Primary text](https://www.gutenberg.org/ebooks/12).

[^v1-i9-takeover]: Alexander Eriksson and Neville A. Stanton, "Takeover Time in Highly Automated Vehicles: Noncritical Transitions to and From Manual Control," *Human Factors* 59(4) (2017): 689–705, reporting takeover times from about two seconds to more than twenty in a driving simulator. (AI-added; verify before print.)
