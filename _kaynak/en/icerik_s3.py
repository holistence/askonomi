# -*- coding: utf-8 -*-
# Aşkonomi quiz series — Season 3 "Crisis" (tests 21–30). English edition. Source: book v45, Chapters 22–28 and Introduction.
# Page references: /home/claude/askonomi_in/rapor_s3.md

ICERIK = {}

# 21 — calculator — Chapter 28
ICERIK["beklenti-enflasyonu"] = {
    "kanca": "Lover, best friend, confidant, career coach: how many job titles can one person hold?",
    "sorular": [
        ("Lover, best friend, confidant, flatmate, travel buddy, crisis support, career coach, personal growth cheerleader… How many of these roles do you expect your partner to fill?", [
            (0, "Three or four, I have other people in my life for the rest"), (1, "About half"),
            (2, "Most of them"), (3, "All of them, that's what a partner is")]),
        ("You've been struggling with a hard problem for a long time. Who do you lean on for support?", [
            (0, "My partner, my friends, and a professional if needed"), (1, "My partner first, then others too"),
            (2, "Mostly my partner, I rarely tell anyone else"), (3, "Only my partner, nobody understands me better")]),
        ("Your birthday is coming up. Do you tell your partner what you want?", [
            (0, "I say it clearly, I don't like guessing games"), (1, "I drop hints, the rest is up to them"),
            (2, "No, if they know me, they'll know"), (3, "If I have to say it, the gift loses its meaning")]),
        ("Years from now, what do you expect from your partner?", [
            (0, "Security, and we'll create the excitement together now and then"), (1, "Security, plus a surprise from time to time"),
            (2, "Constant security and constant excitement"), (3, "The first-day spark never fading, if it fades, something's wrong")]),
        ("How many items on your ideal-partner list are “non-negotiable”?", [
            (0, "A few: respect, honesty, trust and the like"), (1, "Five or six"),
            (2, "Most of the list"), (3, "All of them, giving up one means I've settled")]),
        ("Which sentence feels closest to you?", [
            (0, "“Some areas of my life are richer with you.”"), (1, "“You are my closest person.”"),
            (2, "“You are my everything.”"), (3, "“You complete me.”")]),
    ],
    "seviyeler": [
        (0, "Price stability", "You've put your expectations of your partner in order: there's a core, and the rest is shared with other people in your life. The book describes this not as lowering expectations but as spreading them out: a strong romantic bond and a rich social network are not rivals. But a low index does not mean “ask for less”. According to the book, expectations such as non-violence, consent, basic respect and honesty should be neither spread out nor lowered. This is not a measurement, it's a tool for reflection."),
        (26, "Moderate inflation", "Your expectations are high, but most of them are reasonable. The book says having standards is not the problem: standards help us spot bad matches. The real line runs between having standards and demanding perfection, and a few items on your list may be getting close to it. The book's questions may help: “Does my partner know about this expectation, is it mutual, does it fit our resources, and is it truly essential for me?”"),
        (51, "High inflation", "Your partner's job description is long: lover, confidant, crisis support, maybe a bit of career coach too. The book compares this to a job advert: we expect one person to do every task equally well. Each expectation may be reasonable on its own, but the full package gets heavy. The cost: when you expect everything from one person, every area where they fall short can look like the failure of the whole relationship. According to the book, a partner doesn't have to replace professional support either."),
        (76, "Hyperinflation", "In your eyes, your partner is the sole supplier of every need. The book quotes an image from Finkel and colleagues: high up the mountain the view is more stunning, but there is less oxygen. Expectations this high can only be met if the relationship gets that much time and energy. The book doesn't say “lower your expectations”, it looks at the fit between expectations and resources. The book's question: “Is what I want from my partner truly essential to my relationship?”"),
    ],
    "bolum": "28",
    "birim": "Expectation Inflation Index",
}

# 22 — calculator — Chapter 25
ICERIK["iliski-getirisi"] = {
    "kanca": "You didn't invest money, but you invested time, effort and attention. So what's building up in return?",
    "sorular": [
        ("You got good news: a promotion, an acceptance, a success. How does your partner usually react?", [
            (3, "They're happy, ask for details and want to celebrate"), (2, "They congratulate me sincerely, then the topic changes"),
            (1, "They say “nice” but their mind is elsewhere"), (0, "They immediately list possible problems or what's missing")]),
        ("Are the small things you do (keeping them posted, remembering a detail, sharing a load) noticed?", [
            (3, "Usually noticed and mentioned"), (2, "Noticed, but rarely said out loud"),
            (1, "Only noticed when I don't do them"), (0, "They stay invisible, as if they just happen by themselves")]),
        ("When it comes to your own goals (education, health, work, a hobby), where is this relationship taking you?", [
            (3, "Closer to the person I want to be"), (2, "It supports me, but doesn't change much"),
            (1, "My goals are in the shadow of the relationship"), (0, "I dropped my goals “for the sake of us”")]),
        ("When did you last do something new together (a place, a hobby, an experience)?", [
            (3, "In the last few weeks"), (2, "In the last few months"),
            (1, "I can barely remember"), (0, "All our shared memories are in the past")]),
        ("Looking at the long run, who gives what in the relationship?", [
            (3, "It shifts over time, but it balances out"), (2, "A bit uneven, but we both see it"),
            (1, "Usually the same side gives"), (0, "Always the same side gives, and we can't talk about it")]),
        ("Where does most of the energy spent on the relationship go?", [
            (3, "Building new things, making plans together"), (2, "Keeping the daily routine running"),
            (1, "Calming down the same old arguments"), (0, "Damage repair, there's no energy left for anything else")]),
    ],
    "seviyeler": [
        (0, "Warning light", "Your answers suggest that most of the effort spent on the relationship goes into repairs, or that what is given stays invisible. The book sets a threshold here: the balance sheet of a shared life may never be perfectly even, but if it keeps recording losses on one side, the investment metaphor starts flashing a warning. This is not a verdict, it's a tool for reflection. The question at the start of the chapter: which investments truly nourish a relationship?"),
        (26, "Account needs maintenance", "Your relationship works, but its returns seem to be shrinking. According to the book, before a relationship ends there is sometimes no dramatic crisis, just long-term neglect. The bills get paid, things run, but shared life can slowly turn into a logistics company. The cost: while the relationship keeps doing its job, closeness can quietly fade. The book looks for the fix not in grand gestures but in small behaviours repeated hundreds of times."),
        (51, "Steady returns", "Your relationship adds value to your life: small contributions are seen and the balance is mostly kept. The book describes caring for a relationship not as constant spending but as regular investment that protects the partnership's use value. One warning: some returns of a relationship don't renew themselves. When no new shared experiences are created, all the memories gradually belong to the past. Sometimes investing means adding new material to the relationship."),
        (76, "Compound returns", "Your relationship works like insurance on hard days and like a partnership that multiplies returns on good days. In the book's words, a good partner is someone who can carry not only our load but also our growth. Still, a high score is no guarantee. According to the book, some of the highest returns in a romantic relationship can't be turned into numbers. This index doesn't measure them either, it only invites you to think about them."),
    ],
    "bolum": "25",
    "birim": "Return Index",
}

# 23 — scenario — Chapter 25 / 26 (and 22)
ICERIK["batik-maliyet"] = {
    "kanca": "How much does what you gave in the past control the decision you make today?",
    "sorular": [
        ("A friend is talking about their seven-year relationship: “I'm not happy, but I've given it so many years.” What do you say?", [
            ("G", "“Seven years is a lot, don't give up so fast.”"), ("S", "“Those years are gone, don't count them.”"),
            ("A", "“Look at which of those years still carries something today.”"), ("Y", "“How do you want to spend the next seven years?”")]),
        ("Months ago you planned an expensive holiday together and paid for it. Now things are tense between you and the date is getting close.", [
            ("G", "It's paid for, so we go, it shouldn't go to waste"), ("S", "The money is already gone, it shouldn't affect the decision at all"),
            ("A", "First I check whether any part of it is refundable"), ("Y", "I also weigh how else I could spend that week")]),
        ("What would scare you most about a relationship ending?", [
            ("G", "That everything I gave would be wasted"), ("S", "Getting stuck in the past and not turning the page"),
            ("A", "Our shared home, friends and routine falling apart"), ("Y", "Staying in the wrong life and missing other chances")]),
        ("You moved to another city for someone you've been with for a long time. Now things aren't what they used to be. What goes through your mind?", [
            ("G", "“I gave up so much for them, I can't back out now.”"), ("S", "“The move is in the past, it doesn't affect today's decision.”"),
            ("A", "“The job I lost is in the past, but my income and friends here today are real.”"), ("Y", "“I can't help wondering where I'd be today if I hadn't gone.”")]),
        ("What does the sentence “You've given it so many years, how can you walk away now?” mean to you?", [
            ("G", "A fair question, effort shouldn't be thrown away lightly"), ("S", "Meaningless, past years can't be the measure of a decision"),
            ("A", "Half true, some of those years still shape today"), ("Y", "The real question isn't the years given, but the years still to come")]),
        ("If a relationship ended, what would you think about those years?", [
            ("G", "All that effort should have led somewhere"), ("S", "A page has closed, I don't look back"),
            ("A", "Even if it ended, the good parts and what I learned stay with me"), ("Y", "I'd wonder what would have happened if I'd taken another path")]),
    ],
    "sonuclar": {
        "G": ("Guardian of the past", "For you, effort that was given can't easily be erased, and that is part of loyalty. Economics calls part of this a sunk cost: whatever you decide today, it won't come back. The cost: deciding only so that “all those years aren't wasted” can mean choosing an option that's bad for today just to rescue the past. That doesn't mean staying is wrong. The book's question: if I feel I have to continue, is it “only because I gave so much in the past”?", "25"),
        "S": ("Clean slate", "You don't get stuck in the past: what's done is done, and decisions are made for today. That's strong immunity against the sunk cost fallacy. But the book also points to the other extreme: wiping out the whole history of a relationship as “sunk cost, forget it” is just as misleading as surrendering to the past. Shared children, a home, social networks were built in the past but still shape today. The risk is writing real ties off the books too.", "25"),
        "A": ("The one who tells them apart", "You neither worship the past nor throw it away. You try to separate what is sunk cost that won't come back from what is relationship-specific capital that still shapes today. That is exactly the distinction the book suggests. The hard part: the book admits that separating the two perfectly in real life isn't easy. And it reminds us: an investment that has ended and a worthless past are not the same thing.", "22"),
        "Y": ("Eyes on tomorrow", "You weigh decisions against the years ahead, not the years behind. In economic terms, you look at opportunity cost: which lives am I giving up with this choice? That's a good compass against the sunk cost trap. But there's a risk: the lives you didn't choose always look brighter, because you never lived their costs. The book's warning: “Real life competes with all its costs, an imagined life with only its best scenes.”", "26"),
    },
}

# 24 — calculator — Chapter 26
ICERIK["neye-mal-oldu"] = {
    "kanca": "Every “yes” carries a few silent “no”s. What were yours?",
    "sorular": [
        ("Did you give up an opportunity at work or in your studies for this relationship?", [
            (0, "No, it was never needed"), (1, "A small opportunity"),
            (2, "An important offer"), (3, "I largely changed my career direction")]),
        ("How were the city and home you live in chosen?", [
            (0, "It's where I'd have chosen anyway"), (1, "We chose together, we both bent a little"),
            (2, "Mostly based on their needs"), (3, "I moved for them, I wouldn't have gone on my own")]),
        ("What happened to the friends and hobbies you had before the relationship?", [
            (0, "They're still there as they were"), (1, "They've thinned out a bit"),
            (2, "They've mostly turned into shared friends"), (3, "I've left most of them behind")]),
        ("The hours in a week that are just for yourself…", [
            (0, "Same as before the relationship"), (1, "A little fewer"),
            (2, "Clearly fewer"), (3, "Almost none left")]),
        ("In shared decisions (moving, holidays, big purchases), whose preference becomes the default?", [
            (0, "We genuinely decide together"), (1, "It changes from time to time"),
            (2, "Usually theirs"), (3, "Almost always theirs")]),
        ("Are the things you gave up talked about in the relationship?", [
            (0, "I haven't given up anything important"), (1, "Yes, they're seen and appreciated"),
            (2, "Not really talked about"), (3, "Never seen, they're taken for granted")]),
    ],
    "seviyeler": [
        (0, "Light luggage", "So far you haven't given up anything big for this relationship, or what you gave up doesn't weigh on you much. Still, opportunity cost is never zero. In the book's words, every “yes” quietly says “no” to some other possibilities. A low price doesn't mean the relationship is worthless, it may simply mean two lives fit together well. This is not a measurement, it's a tool for reflection."),
        (26, "Visible price", "This relationship has cost you some things: some time, some flexibility, maybe an opportunity. According to the book, a costly choice is not a wrong choice. On the contrary, what we give up for what shows what we value. The thing to watch is that the costs don't always pile up on the same side. The book's question: “Who gave up which opportunity, and how has that loss been made up for over time?”"),
        (51, "High price", "You've given up serious things for this relationship: a city, a job, a circle of friends, or time of your own. The book reminds us: a job you turned down doesn't appear on any payslip, but it can stay in the relationship's memory. A high price doesn't mean a wrong choice. The risk is that unseen sacrifice slowly turns into resentment. The book's answer is not to put a price tag on every sacrifice, but to be able to talk about the invisible losers of big decisions."),
        (76, "Heavy price", "This relationship has largely set the direction of your life, and what you gave up is big. The book says this is not a wrong choice in itself: a good life is not a life without opportunity costs, but one where you find the life you chose worth living despite what you gave up. But if the costs always land on the same person, that's a distribution problem. The book's standard: the missed opportunities should be as visible as the costs of shared life."),
    ],
    "bolum": "26",
    "birim": "Opportunity Cost Index",
}

# 25 — profile — Chapter 27 (and 26)
ICERIK["cok-secenek"] = {
    "kanca": "As your options multiply, do you choose better, or does choosing just get harder?",
    "sorular": [
        ("You see fifty new profiles on a dating app. What do you do?", [
            ("M", "I look at all of them, the best might be the last one"), ("Y", "I start chatting with the first few that feel right"),
            ("F", "First I filter them by my must-haves"), ("A", "I chat with a few and don't close any doors"),
            ("B", "I keep in mind one feature I liked in each of them")]),
        ("At a restaurant, the menu runs for pages.", [
            ("M", "I read all of it, I won't decide until I find the best"), ("Y", "I stop at the first thing that looks good"),
            ("F", "I cross out what I won't eat and pick from what's left"), ("A", "We order a few to share and see how it goes"),
            ("B", "After ordering, I look at what the next table got")]),
        ("Your relationship is going well. What crosses your mind most?", [
            ("M", "“Is there someone better out there?”"), ("Y", "“So glad this was so easy.”"),
            ("F", "“Everything that matters to me is in place.”"), ("A", "“Good for now, let's see what happens.”"),
            ("B", "“If only they had this quality too.”")]),
        ("After you make a big decision (a home, a job, a partner)…", [
            ("M", "I keep thinking about the other options"), ("Y", "The matter is closed, I look ahead"),
            ("F", "If it meets my criteria, I'm at peace"), ("A", "Knowing I can go back makes me feel better"),
            ("B", "I compare it with other people's choices")]),
        ("A friend wants to introduce you to someone.", [
            ("M", "First I'd like to hear who else is out there"), ("Y", "Sure, if they're nice, why not"),
            ("F", "First I ask a few basics: age, city, what they want from life"), ("A", "I'll meet them, but I promise nothing to anyone"),
            ("B", "While listening, I compare them with my exes")]),
        ("Which sentence feels closest to you?", [
            ("M", "When the best exists, I won't settle for second best."), ("Y", "Good enough is often the best."),
            ("F", "If you know what you want, you get less tired."), ("A", "As long as the doors stay open, I'm free."),
            ("B", "Every person is missing something different.")]),
    ],
    "sonuclar": {
        "M": ("Chasing the best", "You don't settle for good enough, you look for the best that's within reach. The book calls this the maximising tendency. In studies by Schwartz and colleagues, this tendency was linked to more regret and less satisfaction with choices, though the book notes these findings are debated. In romantic choice it's even harder, because there is no one-dimensional ranking of “the best partner”. The risk: each new option can push the end of the search a little further away.", "27"),
        "Y": ("Good enough", "When you find what's “right for me”, you can stop searching. Because you don't put every new candidate back into the competition, lots of options don't wear you out much. This may be the style least affected by the decision burden the book describes. Still, the book gives a warning: an easy decision and a good life are not the same thing. According to the book, some things about a person can only be learned over time.", "27"),
        "F": ("The filterer", "You know what you want and you rule out the mismatches early. According to the book, clear preferences lower search costs, so a large set of options may even work in your favour. The risk: the more filters you add, the sooner you may lose the chance of an unexpected match with people you haven't met yet. Easy-to-filter traits like height, age and job can push aside things that only show over time, like humour or sensitivity.", "27"),
        "A": ("Open door", "You like keeping your options open. That flexibility has value; economists call it option value. But the book's warning is this: in romantic life, the price of keeping every option alive may be that your partner doesn't invest in you as much either, because they also feel the relationship could be swapped for another option at any moment. In the book's words: “Freedom is when closing the door is our own decision.”", "26"),
        "B": ("The imaginary rival", "Even after choosing, you keep comparing: one person's humour, another's romance, someone else's success. Comparison can be useful, a good habit you see in another couple can improve your own relationship. But the book points to a trap: if you build a composite partner in your head from everyone's strongest traits, a real person can never win. Abundance creates the toughest rival of all: the perfect alternative who never existed.", "27"),
    },
}

# 26 — calculator — Chapter 24
ICERIK["guven-sermayesi"] = {
    "kanca": "When trust works well, it's invisible. So how much of it have you built up?",
    "sorular": [
        ("How often does your partner keep their small promises (“I'll call”, “I'll come”, “I'll sort it out”)?", [
            (3, "Almost always"), (2, "Most of the time"),
            (1, "About half the time"), (0, "Rarely")]),
        ("What happened to a secret or a vulnerable moment you shared with them?", [
            (3, "They protected it and never brought it up"), (2, "They protected it, but hinted at it once"),
            (1, "They've used it in an argument"), (0, "I found out they shared it with others")]),
        ("When a problem comes up, your partner usually…", [
            (3, "Is there and takes responsibility"), (2, "Shows up, even if a bit late"),
            (1, "Disappears, then comes back"), (0, "Blames someone else")]),
        ("When your partner makes a mistake, they…", [
            (3, "Tell me on their own"), (2, "Explain honestly when asked"),
            (1, "Play it down first, then admit it"), (0, "Deny it until there's proof")]),
        ("When there's a delay or an unclear message, what do you do?", [
            (3, "I don't think much of it, there's an explanation"), (2, "I wonder, I ask, it passes"),
            (1, "It sticks in my head and I feel the urge to check"), (0, "I can't relax until I've verified it")]),
        ("On important matters (money, health, your shared future), do you keep each other informed?", [
            (3, "Openly"), (2, "Mostly, some things get said in time"),
            (1, "I've found out some important things later"), (0, "I feel I'm making decisions with missing information")]),
    ],
    "seviyeler": [
        (0, "In the red", "Your answers suggest your trust account is currently in the red: the need to verify is high, and promises carry little information. The book doesn't see this as a personal flaw: earned suspicion can also be healthy information processing. The cost of low trust is constant checking, verifying and defending. According to the book, if behaviour broke the trust, behaviour must also repair it. Where someone's safety is under threat, the book puts protecting that person first."),
        (26, "Fragile balance", "Your trust account is open but fragile: some promises are kept, some doubts remain. The book sees trust not as a single score but as a set of expectations that differ by area. You can trust someone's faithfulness and still not trust their punctuality. The risk is that small repeats turn into a pattern. Then the question shifts from “What happened this time?” to “How much does this person's word tell me about the future?”"),
        (51, "In credit", "Your trust account is in credit: promises are mostly kept, and nobody disappears when a problem comes up. The book explains its value through transaction costs: a couple who trust each other don't have to verify every piece of information or investigate every delay. Still, this capital doesn't work mechanically like money in the bank. A small delay may not wipe out years of trust, but a single big betrayal can change how the whole past is read."),
        (76, "Strong capital", "Your trust capital is strong: actions back up words, and your vulnerability is protected. The book sees trust's biggest return not so much as peace of mind but as room to move. You can spend time on your work, your friends and yourself without staying on the defensive. One warning: the book's goal is not maximum trust but a level of trust that matches behaviour. In the book's words, good trust grows stronger not despite the evidence but because of it. This index is also a tool for reflection."),
    ],
    "bolum": "24",
    "birim": "Trust Capital Index",
}

# 27 — myth — Chapter 23
ICERIK["aldatma-mitleri"] = {
    "kanca": "Everyone has a firm opinion about cheating, but the data isn't nearly as sure.",
    "sorular": [
        ("Once a cheater, always a cheater: someone who cheated once will definitely cheat in their next relationship.", False,
         "False. In a study by Knopp and colleagues that followed 484 adults across two consecutive relationships, people who reported infidelity in their first relationship were about three times more likely to report it in the next one. But the book stresses that this is a difference in risk, not destiny: three times more likely is not one hundred per cent certain."),
        ("Cheating doesn't happen in a happy relationship; if someone was cheated on, the relationship was already bad.", False,
         "False. Low relationship satisfaction goes together with infidelity in some studies, but the cause can run the other way too: infidelity itself can lower satisfaction. According to the book, many people who are unhappy never cheat, and some who say they're happy may still engage in behaviour outside the relationship."),
        ("People don't always draw the line in the same place on what counts as cheating.", True,
         "True. On the scale by Wilson and colleagues, behaviours were grouped as “explicit”, “deceptive” and “ambiguous”, and opinions split more on the ambiguous ones. The book's summary: people largely agree on the core of what cheating means, but can differ seriously at its edges."),
        ("A debt or spending deliberately hidden from a partner can also count as a kind of infidelity.", True,
         "True. Garbinsky and colleagues call this financial infidelity: doing something with money that you expect your partner wouldn't approve of, and deliberately hiding it from them. According to the book, not reporting every personal purchase doesn't count; the key element is the gap between an expected shared rule and deliberate secrecy."),
        ("Once cheating comes out, the relationship can't be repaired.", False,
         "False. In the therapy research the book cites, the gap between the high initial distress of couples who had experienced infidelity and that of other couples could largely close by the end of treatment and at the six-month follow-up. The book adds that this doesn't mean “after cheating you must stay together”: it only shows that infidelity doesn't automatically make a relationship beyond repair."),
        ("Behind cheating there may be not one single cause but a range of different motives.", True,
         "True. In a study by Selterman and colleagues with 495 people who had experienced infidelity, anger, feeling neglected, falling out of love, low commitment, a wish to boost self-esteem, and situational factors like stress emerged as separate motives. A large part of the sample were young adults, so the breakdown can't be generalised. The book also stresses that this doesn't remove responsibility: an explanation is not an excuse."),
    ],
    "seviyeler": [
        (0, "Trusts the old sayings", "Most of your beliefs sit close to the firm sentences of everyday talk: “Once a cheater, always a cheater”, “Happy people don't cheat.” The book shows that some of these sentences hold a grain of truth, but the data doesn't carry that certainty. Research usually talks about differences in risk, not destiny. Past behaviour can carry information about risk, but it doesn't stick a lifelong label on a person. The book's warning: “Assessing risk and condemning a person are not the same thing.”"),
        (3, "Sees the grey area", "On some beliefs you're in the same place as the data, on others you're closer to the old sayings. That's exactly why cheating is a hard topic: people largely agree at the centre and split seriously at the edges. According to the book, when two people say “we're monogamous”, they may not have signed the same contract. Faithfulness is not just a list of things you can't do, it's a shared expectation about boundaries. Digital communication makes this grey area even bigger."),
        (5, "Economist of betrayal", "You can tell common beliefs about cheating apart from the data. That's also where the book lands: the economic core of cheating is less about the number of partners and more about a secret departure from an agreed rule. So the real cost is not only the lost relationship but the decisions the other person made with missing information. That's why secrecy adds a separate cost on top of the act itself. Now the chapter's closing question: “Can trust be rebuilt once it's broken, and if so, which behaviours, how much time and what kind of mutual effort will pay the price?”"),
    ],
    "bolum": "23",
}

# 28 — profile — Chapter 24 (and 23)
ICERIK["affetmek-guvenmek"] = {
    "kanca": "Three separate decisions are often mistaken for one. Where do you stand?",
    "sorular": [
        ("Someone close lied to you about something important and apologised. In the first few weeks, you…", [
            ("F", "Can't get past my anger, even hearing the apology is hard"), ("G", "Accept the apology, but weigh every word they say"),
            ("U", "I'm not angry, but I don't know how we'll go on"), ("H", "They apologised, so it's closed, I don't drag it out")]),
        ("For you, forgiving…", [
            ("F", "Feels like saying what they did was acceptable"), ("G", "Is possible, but trust is a separate account"),
            ("U", "Forgiving the person doesn't mean continuing the relationship"), ("H", "Means forgetting and moving on")]),
        ("If someone who shook your trust says “You should trust me now”…", [
            ("F", "I think they have no right to ask that"), ("G", "I say words aren't enough, I need to see their behaviour"),
            ("U", "Even if I trust them, we need to talk about how we go on"), ("H", "They may have a point, how long can we drag this out")]),
        ("A friend found out their partner hid a debt from them. What do you tell them?", [
            ("F", "“Your anger is completely natural, take your time.”"), ("G", "“From now on you might want to go through the accounts together.”"),
            ("U", "“Forgiving and staying together are separate decisions.”"), ("H", "“It's only money, it can be fixed, don't blow it up.”")]),
        ("In a process like this, what would be hardest for you?", [
            ("F", "Carrying what happened around inside me"), ("G", "Worst-case thoughts popping up whenever their phone rings"),
            ("U", "Acting as if everything is back to normal"), ("H", "The topic being brought up again and again")]),
        ("Which sentence feels closest to you?", [
            ("F", "Forgiveness has to be earned."), ("G", "I've forgiven, but it's not like before."),
            ("U", "Forgiving is one thing, staying is another."), ("H", "Holding a grudge wears you out first.")]),
    ],
    "sonuclar": {
        "F": ("Stuck at forgiving", "For you, what happened doesn't close easily. The book doesn't see forgiveness as forgetting or as calling the act acceptable; it links it more to being able to step out of a cycle of constant retaliation and anger. Some studies have found a tendency to forgive linked with less negative conflict. But the book stresses this doesn't mean “forgive whatever they do”. And the person who broke the trust can't set the repair timetable on their own.", "23"),
        "G": ("Stuck at trusting again", "You can forgive, but it takes time for trust to come back. The book treats these two as separate decisions anyway. Wanting more information after a breach is understandable, but temporary reassurance and permanent surveillance are not the same thing. In the book's image, training wheels help you learn to ride a bike, but the skill only settles once you can balance without them. Maybe the goal isn't the old trust, but a new trust built on new information.", "24"),
        "U": ("Stuck at reconciling", "You can forgive the person, and even trust them again. Where you get stuck is on what terms the relationship will continue. The book draws a very clear line here: forgiving, trusting and reconciling are three separate decisions. Staying together isn't, on its own, proof of true forgiveness either. In economic language, forgiveness is not a past debt magically wiped from the books, but a new decision about the terms on which the relationship will go on.", "23"),
        "H": ("Quick to close", "You don't like dragging out hurt feelings; once an apology comes, you turn the page. That can give a relationship flexibility. But the book points to a limit: in McNulty's study of newlywed couples, when problem behaviour was repeated often, being very forgiving didn't lead to good outcomes in every case. In the book's words, forgiveness being good doesn't make boundaries unnecessary. An apology is a signal; what comes next decides whether it can be trusted.", "24"),
    },
}

# 29 — scenario (8 questions) — Chapters 22–28
ICERIK["kriz-senaryolari"] = {
    "kanca": "When a crisis hits, everyone's eyes drift somewhere different. Where do yours go?",
    "sorular": [
        ("You've been together for years and lately the same fight keeps coming back. One evening, alone, what's your first thought?", [
            ("H", "How much effort I've put into this relationship"), ("G", "Why they've changed, whether they're hiding something"),
            ("A", "What a different life could look like"), ("B", "Whether we've ever talked about what we expect from each other"),
            ("C", "What kind of life I'm living on my own two feet")]),
        ("You found out your partner has been having long chats with their ex without telling you.", [
            ("H", "I think, “After all our years, this?”"), ("G", "First I want to see all the messages"),
            ("A", "I think, so they're looking at other options too"), ("B", "I want to talk about whether this counts as cheating for us"),
            ("C", "I look at what I have of my own outside the relationship")]),
        ("Your partner confessed to a big purchase from the shared budget without telling you, and apologised.", [
            ("H", "I weigh the money spent against everything I've given so far"), ("G", "From now on I want to see every expense"),
            ("A", "I think someone else wouldn't have done this"), ("B", "We talk again about the rules we live by when it comes to money"),
            ("C", "I check how my own savings and income are doing")]),
        ("For a long time you've felt like you're the only one putting effort into the relationship.", [
            ("H", "A list of who gave what forms in my head"), ("G", "I try to figure out how willing they really are"),
            ("A", "I wonder if I'd go to this much trouble with someone else"), ("B", "I realise I never clearly said what I expect"),
            ("C", "I realise I've been neglecting my own friends and hobbies")]),
        ("Your partner got a good job offer in another city. You're at the best point of your career here.", [
            ("H", "We look at who has sacrificed for whose career so far"), ("G", "I wonder how long they've been thinking about this"),
            ("A", "Going and staying both mean giving something up, I weigh both"), ("B", "We put on the table what we each expect from this relationship"),
            ("C", "Whatever we decide, I look for a way to protect my own career")]),
        ("You're going through a hard time. A friend shows you a dating app and says, “Look how many options there are.”", [
            ("H", "Dropping all that investment and starting from zero feels too expensive"), ("G", "I say, who knows what the people on the screen are really like"),
            ("A", "I look with curiosity, maybe there really is someone better"), ("B", "I say I first need to know what I actually want"),
            ("C", "Knowing there are options is comforting, but I don't rush")]),
        ("Your partner said, “You don't understand me any more.”", [
            ("H", "I list the things I've done for them"), ("G", "I think about why they're saying it now and what's behind it"),
            ("A", "The thought crosses my mind that they might fit better with someone else"), ("B", "I ask what I expect from them and what they expect from me"),
            ("C", "I remind myself my life isn't only this relationship")]),
        ("You got through a crisis and people around you say, “You're back to your old selves.” And you?", [
            ("H", "I'm still calculating what this crisis cost us"), ("G", "I'll keep my eyes open for a while longer"),
            ("A", "Now and then I wonder what would have happened if we'd chosen differently"), ("B", "We're not like before, we have new rules now"),
            ("C", "I saw that keeping a space of my own helped me through it")]),
    ],
    "sonuclar": {
        "H": ("The ledger", "In a crisis, your first reflex is to weigh what was given and what was received. That isn't coldness: the book says the line “true love doesn't keep score” can sometimes hide inequality. But the ledger has a trap. Part of what was given in the past is sunk cost that can't be recovered, and it can carry too much weight in today's decision. Expecting an equal return for every act right away can also turn the relationship into an accounting book.", "25"),
        "G": ("The watcher", "In a crisis, you need information first: what happened, why, what else is there? The book says wanting more transparency after a breach is understandable, but it separates temporary reassurance from permanent surveillance. Demands for information under surveillance have no natural end: when the phone comes up clean, you might start wondering about deleted messages. In the book's words: the alternative to trust is not perfect information.", "24"),
        "A": ("Weighing the alternatives", "In a crisis, your mind wanders to roads not taken: another person, another city, another life. That's a natural way of seeing opportunity cost, and according to the book this awareness is sometimes genuinely useful. But the book reminds us this comparison isn't fair: we know our current partner's flaws, but we don't know the mistakes the person we passed up would make. In the book's words: the alternative life isn't cost-free, we just haven't lived its costs yet.", "26"),
        "B": ("Expectation writer", "In a crisis, you ask whether the problem lies with the person or with the expectation. According to the book, an expectation gap isn't always the partner's fault: the expectation may be contradictory, out of line with resources, or never discussed at all. That's a strong style. The risk: treating every crisis as a matter of expectations can make you miss what is truly non-negotiable. As the book reminds us, rearranging expectations doesn't mean erasing basic boundaries.", "28"),
        "C": ("On your own feet", "In a crisis, you want to be sure your own life is still standing: your job, your income, your friends. The book doesn't see this as preparing to escape: having more ability to leave is not the same as wanting to leave more. According to the book, being able to leave can even make staying more meaningful. The risk: if these supports replace shared investment, the relationship may feel less like “the chosen option” and more like “the option kept for now”.", "22"),
    },
}

# 30 — couple — Chapter 24
ICERIK["kriz-aninda"] = {
    "kanca": "Answer separately, then compare: when a crisis hits, do you run in the same direction?",
    "sorular": [
        ("After a big argument:", ["Talk it through the same day", "Sleep on it, then talk"]),
        ("After something that shook trust, the priority is:", ["Understanding why it happened", "Talking about what comes next"]),
        ("What makes an apology most believable:", ["Saying it right away and clearly", "Seeing it in behaviour over time"]),
        ("After a crisis, phones and passwords:", ["Stay open for a while", "Everyone keeps their own space"]),
        ("If a crisis breaks out over money:", ["The rules get written down clearly", "Trust-based flexibility is kept"]),
        ("When discussing a hard topic:", ["Everything goes on the table at once", "Step by step, piece by piece"]),
        ("Forgiving is:", ["Closing the page completely", "Keeping the record and moving on"]),
        ("Once the crisis is over, the relationship should:", ["Go back to how it was", "Be rebuilt with new rules"]),
        ("When debating whether to stay or go, what weighs more:", ["The years spent together", "The years ahead"]),
        ("Support in hard times:", ["Stays between the two of us", "Is also shared with friends, family or a professional"]),
    ],
    "seviyeler": [
        (0, "Different crisis languages", "In a crisis, you stand in different places on most things. That doesn't mean your relationship is weak, it means you live through crises in different languages. The book sees a relationship as an incomplete contract: you can't write down every situation in advance, and not everything can be turned into a written rule. The gaps get filled by each other's goodwill, sense of fairness and past behaviour. The items where you answered differently may simply be items you haven't talked about yet."),
        (4, "Partial agreement", "On some things you're on the same side, on others not. According to the book, trust isn't a single score but a set of expectations that differ by area. You can be in the same place on money and still differ on how you talk things through. Look at the items where you split, together. In the book's words, a solid relationship uses clear agreements and earned trust together. Trust is not an alternative to a contract; neither one is enough on its own."),
        (7, "On the same side", "In a crisis, you stand in the same place on most things. This is the valuable side of what the book calls trust capital: when you don't have to renegotiate every small decision, the relationship's transaction costs fall. Still, the book gives a warning: a crisis doesn't automatically make a relationship stronger. Agreement on paper is a start; according to the book, trust feeds on behaviour."),
        (9, "Shared crisis map", "You gave the same answer on almost every item. It looks like you share a map of what to do when a crisis hits. In the book's words, trust doesn't remove uncertainty, it lowers the cost of acting together within it. Your answers suggest this cost may be low for you, and that you fill the gaps in your incomplete contract in similar ways. The real test is still behaviour: according to the book, an apology is a signal. What comes next decides whether it can be trusted."),
    ],
    "bolum": "24",
}
