# -*- coding: utf-8 -*-
# Aşkonomi quiz series — Season 2 "The Contract" (quizzes 11–20), English edition.
# Translated from _kaynak/icerik_s2.py (Turkish). Same structure, keys, codes and numbers.
# Source: Aşkonomi v45, chapters 15, 16, 17, 18, 19, 22, 24, 25, 28, 29 (+ pp. 21–22).

ICERIK = {}

# ---------------------------------------------------------------- 11
ICERIK["evlilik-ne"] = {
    "kanca": "At the wedding table everyone signs the same paper, but not everyone signs up for the same thing.",
    "sorular": [
        ("Someone asks you, “Why get married?” What is your first sentence?", [
            ("Y", "To build something lasting together"),
            ("S", "So that someone is by my side on hard days"),
            ("O", "Life works better when two people are a team"),
            ("T", "Sharing life with them is more fun"),
            ("H", "To give our relationship an official guarantee")]),
        ("What do you think is most “shared” in a marriage?", [
            ("Y", "The home, the savings, the long-term plans"),
            ("S", "The bad days and the surprises"),
            ("O", "The daily chores and responsibilities"),
            ("T", "Holidays, hobbies, free time"),
            ("H", "Rights and obligations")]),
        ("Your partner has lost their job. What is your first thought?", [
            ("Y", "How do we protect our shared plans?"),
            ("S", "This is what we are here for. My income is enough for a while."),
            ("O", "We will reorganise who does what at home."),
            ("T", "We have more time together now, let’s use it well."),
            ("H", "I will check our official rights and protections.")]),
        ("What does a legal marriage add to a relationship?", [
            ("Y", "The courage to make shared investments"),
            ("S", "A promise of support for whatever the future brings"),
            ("O", "Clear roles and duties"),
            ("T", "A celebration of the life we are building together"),
            ("H", "A legally recognised package of rights")]),
        ("What would wear you down most in a marriage?", [
            ("Y", "Not being able to invest in a shared future"),
            ("S", "Being left alone at a difficult moment"),
            ("O", "The work always landing on one person"),
            ("T", "Not finding anything we both enjoy"),
            ("H", "Rules and rights staying unclear")]),
        ("Which sentence feels closest to you?", [
            ("Y", "Marriage is an investment two people make in the future."),
            ("S", "Marriage is a safety net, for better or for worse."),
            ("O", "Marriage is a division of labour that works well."),
            ("T", "Marriage is choosing to live life together."),
            ("H", "Marriage is a written promise between two people.")]),
    ],
    "sonuclar": {
        "Y": ("Marriage for you is: An investment",
              "For you, marriage is an investment two people make in the future: a shared home, shared plans, the long run. The book calls these relationship-specific investments, because when the relationship ends, most of them lose much of their value. A legally recognised partnership can make the message “I won’t just walk away tomorrow” more believable. There is a price too: if one partner gives up a career to specialise, that can become an investment whose cost falls on one person alone if the couple splits.",
              "15"),
        "S": ("Marriage for you is: Insurance",
              "For you, a spouse is a small safety network against life’s uncertainties. If one loses a job, the other’s income continues. In illness, time and resources are shared out again. The book reads “for better, for worse” exactly like this: a mutual promise against an uncertain future. But it adds a warning: a family is not a perfect insurance company. An experiment with married couples in Kenya showed that risk-sharing between spouses can be incomplete.",
              "15"),
        "O": ("Marriage for you is: A partnership",
              "You see marriage as a team that works well: each person takes on what they do best, and the household produces together. Gary Becker’s 1973 theory of marriage also studied marriage not as the opposite of romance but as a partnership that creates gains. A household does not only consume; it uses time to create value inside the home. The risky part: even if total output is high, market income may be written in only one person’s name, and the work done at home can stay invisible.",
              "15"),
        "T": ("Marriage for you is: Companionship",
              "For you, marriage is not about splitting the jobs you can’t do alone. It is about sharing the things you love doing together. Economists Stevenson and Wolfers call this consumption complementarity: shared tastes, trips, projects. According to the book, in modern marriage this side may have become more important than the classic division of labour. The price: as economic need gets smaller, the answer to “Why am I staying with this person?” depends more and more on free choice.",
              "15"),
        "H": ("Marriage for you is: A contract",
              "For you, a legal marriage is a written guarantee that stands next to love. The book also sees marriage, in many legal systems, as a ready-made package of rights and obligations: inheritance, shared property, social security, rules for separation. In other words, a legal tool for coordinating an uncertain future. But the book also draws a line: commitment and prison are not the same thing. A good institution makes commitment stronger while also protecting it as a free choice.",
              "15"),
    },
}

# ---------------------------------------------------------------- 12
ICERIK["gorunmeyen-emek"] = {
    "kanca": "Some work never shows up on anyone’s payslip, but it still comes out of someone’s day.",
    "birim": "Invisible Labour Index",
    "bolum": "16",
    "sorular": [
        ("At home, when the detergent, bread or toothpaste is about to run out, who usually notices?", [
            (0, "Almost never me"), (1, "Sometimes me, sometimes someone else"),
            (2, "Mostly me"), (3, "Always me, and I keep the list too")]),
        ("Who keeps track of things like doctor’s appointments, birthdays and payment dates?", [
            (0, "Someone else reminds me, I follow"), (1, "Everyone remembers their own"),
            (2, "I remember most of them"), (3, "The family calendar lives in my head")]),
        ("What happens when you get home from work or school?", [
            (0, "My day is over, I rest"), (1, "I do a few small jobs now and then"),
            (2, "Most evenings I work for another hour or two"), (3, "The real rush starts when I get home")]),
        ("When someone at home is upset, or there is tension with relatives, who calms things down?", [
            (0, "Usually someone else"), (1, "Whoever is free"),
            (2, "Mostly me"), (3, "Always me, and everyone expects it from me")]),
        ("A task has been given to someone. Who checks that it really gets done?", [
            (0, "Someone else checks"), (1, "No need to check, it gets done"),
            (2, "I check most of the time"), (3, "If I don’t ask, it doesn’t happen")]),
        ("When someone at home gets ill or needs care, who changes their work or plans?", [
            (0, "Usually someone else"), (1, "We take turns or do it together"),
            (2, "Mostly me"), (3, "Always me, and my working life has been shaped around it")]),
    ],
    "seviyeler": [
        (0, "Visible hours",
         "Your answers suggest that most of the invisible work at home does not pile up on you. That may be a truly shared system, or it may mean the load sits with someone else. Think about the question in the book’s box: who noticed the detergent was running low, and who added it to the shopping list? When the mental load is done well, nothing goes wrong, so the work itself goes unnoticed. This is not a measurement; it is a tool for reflection."),
        (30, "Shared hours",
         "Part of the invisible work is with you, part is with someone else. According to the book, fairness does not mean splitting everything fifty-fifty: one person can do the cooking and the other the bills, and if working hours differ, even equal tasks may not be fair. Research shows that perceived fairness is linked to relationship satisfaction as much as the actual split is. This is a tool for reflection: look at which items the load gathers on you."),
        (55, "Hidden manager",
         "The jobs at home may get done, but the person who notices, remembers and follows up on what needs doing is mostly you. Allison Daminger studies this cognitive labour in four stages: anticipating a need, identifying the options, deciding, and monitoring the result. This is exactly where the sentence “I would have done it if you’d asked” comes from: the physical work may be shared while the management load is not. This is a tool for reflection, but remember: attention is as scarce a resource as time."),
        (80, "The second shift",
         "Your answers suggest that coming home feels like the start of a second working day. The concept that Arlie Hochschild and Anne Machung made famous has exactly this name: the second shift. Since a day still has only twenty-four hours, every extra hour of unpaid work is taken from rest, education or paid work. In the book’s words: “Being unpaid is not the same as being free of cost.” This is not a diagnosis; it is a tool for reflection."),
    ],
}

# ---------------------------------------------------------------- 13
_EV = ["Always the same person", "We take turns or do it together"]
ICERIK["ev-isini-kim-yapiyor"] = {
    "kanca": "Answer separately, then compare: you live in the same home, but do you see the same home?",
    "sorular": [
        ("Noticing that something is running out and adding it to the list:", list(_EV)),
        ("Keeping track of bills and payment deadlines:", list(_EV)),
        ("Deciding what to eat for dinner:", list(_EV)),
        ("Remembering birthdays and sorting out the gift:", list(_EV)),
        ("Emptying the dishwasher and putting the plates away:", list(_EV)),
        ("Booking doctor’s appointments for family members:", list(_EV)),
        ("Researching options for a holiday:", list(_EV)),
        ("Calling relatives and keeping in touch with them:", list(_EV)),
        ("Calming things down after an argument:", list(_EV)),
        ("Checking whether a job has really been done:", list(_EV)),
    ],
    "seviyeler": [
        (0, "Two different homes",
         "You live under the same roof, but you see the division of labour very differently. As the book reminds us, “doing” a job may be just one link in a chain that runs from noticing the need to checking the result. One of you may see only the last link while the other sees the whole chain. The items where your answers differ show exactly where the invisible labour sits. The difference in perception may come from part of the work never being seen at all."),
        (4, "Half a map",
         "On some jobs you see the same picture, on others you don’t. The items where you differ are probably the easy-to-miss ones: planning, remembering, following up. According to the book, when the mental load is done well, nothing goes wrong, so the work itself goes unnoticed. One question: for the jobs where you both said “always the same person”, do you also agree on who that person is?"),
        (7, "A shared map",
         "You see the division of labour at home mostly the same way. That is a valuable start: when two people see who does what in the same way, talking about it gets easier. Still, the book’s warning applies: seeing it the same way does not mean the split is fair. Research shows that even an unequal split can be accepted as “normal” or “fair” by both partners. The real question is whether the picture you both see actually suits you both."),
        (9, "The same map",
         "You gave the same answer on almost every job: the map of your home is the same in both your heads. Now the book’s bigger question gets interesting: does your division of labour only share out today’s comfort, or does it also change one partner’s future chances in education, income and free time? If you have many “always the same person” answers, this question matters most for those items."),
    ],
    "bolum": "16",
}

# ---------------------------------------------------------------- 14
ICERIK["cocugun-maliyeti"] = {
    "kanca": "Nappies show up on the receipt, but the real cost of a child hides somewhere else.",
    "sorular": [
        ("There is one single figure, valid everywhere, for what a child costs from birth to adulthood.", False,
         "False. According to the book, the cost varies hugely by country, income group, the reach of public services and the living standard a family chooses. A single figure only means something for a specific country, year and set of assumptions."),
        ("Some of the biggest costs of a child never appear in the family budget.", True,
         "True. The book thinks about the cost of a child in three layers: money, time and the alternatives given up. Not being able to work for pay or study in the hours spent on a child, or accepting a lower wage for flexible work, does not appear on any bill, but it is a real cost."),
        ("Children in large families getting less education proves that family size causes it.", False,
         "False. In the study by Black and colleagues (2005) using Norwegian data, children in large families seemed to get less education at first sight. But once birth order was taken into account and twin births were used, the causal effect of family size largely disappeared. Correlation is not causation."),
        ("In high-income countries, the link “higher income, fewer children” has weakened, and in some places it has reversed.", True,
         "True. According to the review by Doepke and colleagues (2023), the economics of fertility has entered “a new era”. Some countries where many women are in paid work can show relatively high fertility. What matters is how possible it is to combine a career and a family."),
        ("Cash incentives such as a baby bonus raise fertility strongly and permanently.", False,
         "False. According to the OECD (2024) review cited in the book, cash transfers to families mostly have no effect on fertility, or only a small or temporary one. A one-off payment covers only a small part of the cost of raising a child, which can last twenty years."),
        ("In Denmark, after the first child, a long-term gap of about 20 per cent was found in women’s earnings compared with men’s.", True,
         "True. The study by Kleven and colleagues (2019) calls this gap the “child penalty”. The figure is specific to Denmark and cannot be applied directly to other countries. According to the book, it is not a biological law either: paid leave, childcare and how care is shared can change who carries the cost."),
    ],
    "seviyeler": [
        (0, "Price tag",
         "Most of your beliefs about the cost of a child differ from the findings in the book. That’s not surprising: most of the cost is not on the bill but hidden in time and in missed opportunities. The book’s principle is clear: the cost of a child can be calculated, but its value cannot be priced. Keeping these two kinds of accounting apart may be the most basic rule of the economics of children. A sleepless night is an opportunity cost; what that night means cannot be measured in the same units."),
        (3, "Budget reader",
         "You read some claims correctly and got others wrong. That is exactly why the economics of children is hard: ideas that feel strongly true may not work the same way everywhere once they are tested with data. For example, the link between large families and education is not as simple as it first looks. The book’s question is still open: why do people, knowing the cost, make one of the biggest investments of their lives with nothing expected in return?"),
        (5, "Family economist",
         "You read the economics of children very well: you know the hidden costs, the correlation trap and the limits of incentives. Now the hard question: according to the book, the benefits of raising children spread across society while the family carries a large part of the cost. How much of this burden should fall on shared shoulders? The book also draws a line: the existence of a social benefit does not change the fact that the right to have children belongs to the individual."),
    ],
    "bolum": "17",
}

# ---------------------------------------------------------------- 15
ICERIK["kiskanclik"] = {
    "kanca": "Everyone gets a little jealous. What matters is what you do with the feeling.",
    "sorular": [
        ("Your partner often texts a colleague you don’t know.", [
            ("R", "Unless they break a rule we agreed on, it’s fine with me"),
            ("D", "I don’t show it, but it stings a bit inside"),
            ("S", "A hundred scenarios start running in my head"),
            ("K", "I ask who it is and what they talk about"),
            ("T", "I mention someone too, to see how they react"),
            ("G", "If I’m curious I ask; the rest is their business")]),
        ("Your partner’s phone is on the table and a notification lights up the screen.", [
            ("R", "I don’t look; if I sense a problem, I talk about it openly"),
            ("D", "I don’t look, but I wonder who it’s from"),
            ("S", "I take a quick secret look, just to feel calm"),
            ("K", "I know the passcode anyway, I check now and then"),
            ("T", "I pretend to be busy with my own phone"),
            ("G", "It wouldn’t even cross my mind to look")]),
        ("In your view, jealousy is most often a sign of…", [
            ("R", "…a boundary being crossed"),
            ("D", "…how much I value them"),
            ("S", "…something going wrong"),
            ("K", "…me looking after what’s mine"),
            ("T", "…me still being wanted"),
            ("G", "…trust being shaken a little")]),
        ("Your partner has stayed friends with their ex.", [
            ("R", "No problem, as long as it’s within the limits we agreed"),
            ("D", "I accept it, but part of me is always on alert"),
            ("S", "I think there’s still something between them"),
            ("K", "I ask them to see each other less"),
            ("T", "I start mentioning my own ex too"),
            ("G", "Their past is their past; I look at today")]),
        ("Your partner is out with friends one evening and is later than they said.", [
            ("R", "If they’re very late without a message, I call"),
            ("D", "I miss them, and feel a bit lonely too"),
            ("S", "With every minute, other thoughts cross my mind"),
            ("K", "I ask them to share their location with me"),
            ("T", "Next time, I’ll be late too"),
            ("G", "I enjoy my evening; they’ll tell me about it later")]),
        ("Which sentence feels closest to you?", [
            ("R", "Rules are agreed on; break them and you answer for it."),
            ("D", "If you love someone, you fear losing them."),
            ("S", "You never know, it’s better to be careful."),
            ("K", "You have a right to know where the person you love is."),
            ("T", "A little jealousy adds spice to a relationship."),
            ("G", "Trust is a stronger bond than control.")]),
    ],
    "sonuclar": {
        "R": ("Boundary guard",
              "You use jealousy like an alarm: it rings if a clear boundary is crossed and stays quiet if not. The book calls this reactive jealousy: a reaction to a real, clear violation is different from jealousy that keeps looking for threats without evidence. Your risk is this: what counts as a violation changes from culture to culture and from relationship to relationship. When you react to a boundary you never talked about, your partner may be learning that rule for the very first time.",
              "19"),
        "D": ("Fear of loss",
              "You feel jealousy inside: a sting, a longing, a little worry. It comes from the fear of losing a relationship you value. In the study by Pfeiffer and Wong, some positive links were found between emotional jealousy and romantic love. But the book draws a line: the presence of jealousy may show that a relationship matters, but its intensity does not measure the amount of love. The book’s question fits you perfectly: what exactly are we afraid of losing?",
              "19"),
        "S": ("Constant alarm",
              "Your jealousy lives mostly in your mind: scenarios, possibilities, clues. The book calls this cognitive jealousy and reports an important finding: constant suspicion and doubt do not move in the same direction as love. The digital age produces plenty of fuel for it: a heart emoji can mean friendship, or it can mean flirting. In the book’s image, jealousy is the relationship’s alarm, but an alarm going off does not prove there is a fire.",
              "19"),
        "K": ("Possessiveness",
              "Your answers show the point where jealousy moves from feeling to action: asking, checking, limiting. These actions may come from a fear of loss. But according to the book, explaining where they come from does not make them right. The book says it plainly: “A feeling being understandable does not make every action taken because of it acceptable.” Control starts to shrink the other person’s space to act. One of the book’s clearest ideas is this: love can create commitment, but it does not create property rights.",
              "19"),
        "T": ("The provoker",
              "To measure how much attention you get, you sometimes put a rival on the other side of the scales. The book describes this as one of the strategies people use to keep a partner in the relationship. A study in Spain found that people who reported lower commitment to their relationship used deliberately making their partner jealous more often. In the short term, attention may go up. But the book’s signalling rule applies here too: a signal carries the meaning the receiver reads into it, not the sender’s intention.",
              "19"),
        "G": ("Safe harbour",
              "You rarely feel jealous, and when you do, you prefer to ask. According to the book, as trust grows, the same threat can feel smaller. Part of trust comes from information you can check, and part from respecting your partner’s boundaries despite uncertainty. There is just one risk: romantic culture treats jealousy as a sign of love, so someone who is never jealous can sometimes be seen as not caring. Being relaxed and not caring are not the same thing.",
              "24"),
    },
}

# ---------------------------------------------------------------- 16
ICERIK["cok-eslilik-mitleri"] = {
    "kanca": "The history of polygamy tells a far more surprising story than most of us think.",
    "sorular": [
        ("Most of the human societies that have been studied at least allowed men to take more than one wife.", True,
         "True. According to the study by Henrich and colleagues (2012), which reviewed the ethnographic records, the share is about 85 per cent."),
        ("So, throughout history, most men were married to more than one woman.", False,
         "False. A society allowing polygyny is not the same as most of its people living that way. According to the book, in most societies polygamous marriage was an arrangement open only to certain men who had land, livestock, income, status or political power."),
        ("Today, about 2 per cent of the world’s population lives in polygamous households.", True,
         "True. This is the estimate from a Pew Research Center study covering 130 countries and territories. The share is much higher in some parts of West and Central Africa. Today’s world is far more monogamous than the ethnographic records suggest."),
        ("Polyandry, where a woman is married to more than one man, has never been seen in human societies.", False,
         "False. Polyandry is much rarer, but it is real. Starkweather and Hames (2012) identified 53 societies that allowed polyandry and showed that this form of marriage was spread over a wider area than people thought."),
        ("Fraternal polyandry in the Himalayas can stop scarce farmland from being divided from one generation to the next.", True,
         "True. According to the book, when several brothers marry the same woman, it can stop family property from being split into smaller and smaller pieces each generation in places where land is scarce. But the book also reminds us not to squeeze every case of polyandry into this one formula."),
        ("Women in polygynous households have less control over everything than women in monogamous households.", False,
         "False, at least not everywhere. Studying polygynous households in Burkina Faso, Eissler and colleagues (2025) found that decision-making usually stayed hierarchical, but in some households women kept more control over their own earnings than women in monogamous households."),
    ],
    "seviyeler": [
        (0, "Myth reader",
         "Most of your beliefs about polygamy differ from the findings in the book. The most surprising distinction is this: a type of relationship being seen as legitimate in many societies does not mean most people live that way. Today’s world is far more monogamous than the ethnographic records suggest. According to the book, polygamy can also be studied as an institution that turns the distribution of wealth and status into a family structure."),
        (3, "History buff",
         "You read some claims correctly and got others wrong. Polygamy is one of the topics surrounded by the most stereotypes. The key lesson of this chapter may help you: family forms are not independent of wealth, inheritance and the scarcity of land. Even rare institutions do not have a single economic cause. In the book’s words, one of the defining features of human nature is being flexible enough to build very different relationship institutions."),
        (5, "Field anthropologist",
         "You read the history of polygamy very well. Now the harder question the book asks: to judge whether an arrangement is fair, shouldn’t we look not at how many people are in it, but at who gets to decide, how resources are shared, and whether someone who wants to leave can actually leave? According to the book, legal permission and equal bargaining power are different things. The measure does not end with the question “how many?”"),
    ],
    "bolum": "18",
}

# ---------------------------------------------------------------- 17
ICERIK["iliski-sozlesmesi"] = {
    "kanca": "No relationship starts with a written contract, but every one has invisible clauses.",
    "sorular": [
        ("An argument starts one evening. What is it most likely about?", [
            ("K", "Money spent without asking"),
            ("E", "The housework always landing on the same person"),
            ("G", "What was said not matching what was done"),
            ("B", "Forgetting to spend time together"),
            ("C", "Someone saying “If this goes on, it’s over”")]),
        ("If your relationship had a contract, which clause would you add first?", [
            ("K", "How the money is shared"),
            ("E", "Who handles the housework and keeps track of it"),
            ("G", "That nothing important will be hidden"),
            ("B", "That one evening a week belongs to just the two of us"),
            ("C", "That either of us can leave with dignity")]),
        ("Your partner goes on a week-long work trip. What do you notice?", [
            ("K", "I see more clearly who actually pays for things"),
            ("E", "That I was the one keeping track of everything at home anyway"),
            ("G", "That I keep wondering where they are and who they’re with"),
            ("B", "That we don’t really talk much even when we’re together"),
            ("C", "That I can manage perfectly well on my own")]),
        ("A friend asks you to describe your relationship. Which sentence are you most likely to say?", [
            ("K", "“Money is always a bit tense for us.”"),
            ("E", "“If I don’t remind them, nothing gets done.”"),
            ("G", "“Sometimes I feel they’re hiding something.”"),
            ("B", "“We’re fine, but we’re like flatmates.”"),
            ("C", "“Even if I wanted to leave, it wouldn’t be easy.”")]),
        ("Your anniversary is coming up. What is your first thought?", [
            ("K", "What’s our budget, and who’s paying?"),
            ("E", "Am I doing the planning again?"),
            ("G", "Will they keep their promise this time?"),
            ("B", "When were we last alone together?"),
            ("C", "Are we together because we really want to be?")]),
        ("Which sentence does your relationship need most?", [
            ("K", "Let “our money” really be ours."),
            ("E", "Let the invisible work be seen too."),
            ("G", "Let what’s said be done, and nothing be hidden."),
            ("B", "Let us find each other inside the routine too."),
            ("C", "Let staying be a choice, not a must.")]),
    ],
    "sonuclar": {
        "K": ("Broken clause: The money box",
              "The clause that creaks most in your relationship is money. The problem is often not how much money there is, but how it is shared. The book says it is misleading to think of a household as one single decision-maker: partners’ preferences are partly shared but not identical. Saying “our money” is easy; how it is divided is a separate question. According to the book, the gains from marriage cannot be judged only by the size of the pie; you also need to know how the pie is sliced.",
              "15"),
        "E": ("Broken clause: Labour",
              "The clause under strain in your relationship is the work nobody writes down: noticing, remembering, following up. The book calls this the mental load. The person who says “I would have done it if you’d asked” may really do every job they are asked to do. But if noticing what needs doing, defining the task and following it up always fall to the other person, the physical work may be shared while the management load is not. Until this clause is written, the cost of the labour keeps piling up in the same column.",
              "16"),
        "G": ("Broken clause: Trust",
              "The clause under strain in your relationship is the one no contract can fully write: trust. The book describes a relationship as an incomplete contract. We cannot write down in advance the illness, the job loss or the crisis that will come in five years. In every situation that can’t be written down, two people rely on each other’s good will and past behaviour. According to the book, trust is not an alternative to the contract; it is what makes living together possible where the contract can’t reach, and its raw material is repeated consistency.",
              "24"),
        "B": ("Broken clause: Maintenance",
              "The clause under strain in your relationship is not a crisis but neglect. The bills get paid, things keep running, but the relationship itself rarely gets its turn. The book names this danger clearly: shared life can slowly turn into a purely logistical company. In Ogolsky and Bowers’ meta-analysis of 35 studies, the length of a relationship did not show a consistently positive link with maintenance behaviours. In other words, being together for a long time is not proof that the relationship is being well looked after.",
              "25"),
        "C": ("Broken clause: The exit",
              "The clause under strain in your relationship is the one talked about least: the exit. Whether staying is a choice or a necessity may have become blurred. The book sees a basic difference between commitment and prison: when leaving becomes impossible, the investment is protected, but the way out of a bad relationship is blocked too. On the other hand, a constant threat to leave can also be manipulation. The book’s observation: “Having more freedom to leave is not the same as wanting more to leave.”",
              "15"),
    },
}

# ---------------------------------------------------------------- 18
ICERIK["bosanmanin-faturasi"] = {
    "kanca": "The cost of divorce does not start at the courthouse door, and it does not end there either.",
    "sorular": [
        ("Even if a separating couple’s total income doesn’t change at all, the cost of living per person can go up.", True,
         "True. When one kitchen, one internet connection and one living room are split into two households, economies of scale are lost. As the book puts it, when you separate from your spouse, you also separate from the economies of scale of a shared household."),
        ("Laws allowing one partner alone to start a divorce caused a large, permanent rise in divorces.", False,
         "False. According to Justin Wolfers’ (2006) re-examination of US states, there was a temporary rise after the reforms, but most of it reversed within about ten years."),
        ("“Half of all marriages end in divorce” is true for every country and every generation.", False,
         "False. According to the book, single figures like this are not universal truths. Dividing the number of divorces in a year by the population does not tell you how many existing marriages will end in divorce. To understand divorce, the denominator matters at least as much as the numerator."),
        ("In the US, in divorces after age 50, the wealth of both women and men fell by about half.", True,
         "True. In the study by Lin and Brown (2021), wealth fell by about half in both groups, while a measure of living standards fell by about 45 per cent for women and about 21 per cent for men. These are results for a specific country, period and age group, not universal rates."),
        ("A rising divorce rate shows that the quality of marriages is falling.", False,
         "False, at least not always. According to the book, in times of high economic dependence some bad marriages may never have appeared in the statistics, because one partner could not afford to leave. When the cost of leaving falls, these marriages become visible (Stevenson and Wolfers, 2006)."),
        ("A long-term study in Germany found that the income loss and poverty risk after divorce were bigger and longer-lasting for women.", True,
         "True. In Thomas Leopold’s (2018) study, men had sharper but shorter drops in some subjective measures, such as life satisfaction. Women’s loss of household income and higher poverty risk, however, were bigger and longer-lasting. The answer to “Who is it worse for?” depends on which outcome you are talking about."),
    ],
    "seviyeler": [
        (0, "Quick sum",
         "Most of your beliefs about the economics of divorce differ from the findings in the book. Perhaps the most important point is this: the first economic shock of divorce is not romantic, but it is real. Fixed costs that one household used to carry are now spread over two. Rent, heating, furniture and moving put the same income under pressure twice. Even if total income doesn’t change, the cost of living per person can go up."),
        (3, "Half the bill",
         "You read some items correctly and missed others. That’s very natural, because some of the most repeated sentences about divorce do not match the data. That is exactly why divorce statistics can be misleading: a single rate does not show who pays which cost, and for how long. According to the book, the outcome of a divorce depends on which marriage you are leaving and which life you go into afterwards. The book’s question still stands: when is staying more expensive than leaving?"),
        (5, "Full statement",
         "You read the bill for divorce very well: you know about the loss of scale, the limits of the law’s effect, and who loses what. Now the book’s hardest question is yours: if this marriage continues, or if it ends, who carries which costs? According to the book, a good divorce does not mean a painless one. A more meaningful test is whether the unavoidable costs are made bigger by unnecessary conflict."),
    ],
    "bolum": "22",
}

# ---------------------------------------------------------------- 19
ICERIK["evliligin-yuzyili"] = {
    "kanca": "Marrying for love is a newer idea than you think. So which era does your dream of marriage belong to?",
    "sorular": [
        ("When choosing a spouse, who or what should have the biggest say?", [
            ("K", "My family, because marriage joins two families"),
            ("R", "My heart: no love, no marriage"),
            ("U", "Being clear about who takes on what"),
            ("A", "Whether they can be my best friend"),
            ("B", "The moment I feel ready")]),
        ("Where does marriage sit in a life?", [
            ("K", "At the start of adulthood and family life"),
            ("R", "As the natural ending of a great love"),
            ("U", "When a home is set up and roles are shared"),
            ("A", "Where a friendship lasts a lifetime"),
            ("B", "At the very top, once everything else is in place")]),
        ("How should money and work be split at home?", [
            ("K", "As tradition and the family expect"),
            ("R", "If there’s love, the rest sorts itself out"),
            ("U", "One earns outside, the other runs the home"),
            ("A", "We decide together and do it together"),
            ("B", "We talk everything through and build our own system")]),
        ("What is the most important quality of a good spouse?", [
            ("K", "Being devoted to their family and responsibilities"),
            ("R", "Still giving me butterflies like on the first day"),
            ("U", "Doing their share of the work reliably"),
            ("A", "Being someone I can talk to for hours"),
            ("B", "Supporting my personal growth")]),
        ("What does a wedding mean to you?", [
            ("K", "The approval of two families and the community"),
            ("R", "Announcing our love to the world"),
            ("U", "The founding day of a new household"),
            ("A", "A lovely celebration with the people closest to us"),
            ("B", "The day that crowns what we have achieved together")]),
        ("What would be the biggest disappointment in a marriage?", [
            ("K", "Letting down the family and the community"),
            ("R", "Love fading away over time"),
            ("U", "One person not doing their share"),
            ("A", "Having nothing left to tell each other"),
            ("B", "The relationship not helping me grow")]),
    ],
    "sonuclar": {
        "K": ("For centuries: The institutional marriage",
              "Your idea of marriage has very old roots. According to the book, marriage in history brought together, in one institution, the passing on of property, placing children in a family line, organising care, sharing productive work and forming alliances between families. Romantic love could be there, but it did not have to be the main reason for choosing a spouse. The book’s warning: the fact that such marriages lasted a long time is not proof of deep emotional satisfaction; if there is no way out, a couple stays together anyway.",
              "29"),
        "R": ("18th and 19th centuries: The romantic ideal",
              "Love is at the centre of your idea of marriage: marrying the person you love and needing no other reason. The book talks about the romantic ideals that took shape in the eighteenth and nineteenth centuries. The change Stephanie Coontz calls the “love revolution” weakened the legitimacy of marrying someone you didn’t love for the family’s sake, and made it normal to expect emotional fulfilment from marriage. The price: marriage got a new test of success, “Am I happy with this person?”",
              "28"),
        "U": ("Mid-20th century: The division-of-labour marriage",
              "Your idea of marriage rests on a clear division of labour: one partner earns outside, the other runs the home and the care. According to the book, Gary Becker’s specialisation model had features that described many mid-twentieth-century households quite well. But a description is not an unchangeable law. Education, paid work and services you can buy on the market changed what this model pays off. The long-term cost of specialisation can also pile up on one person.",
              "15"),
        "A": ("20th century: The companionate marriage",
              "For you, a spouse is above all a best friend. The book cites sociologist Andrew Cherlin’s scheme: during the twentieth century, marriage based on companionship came to the fore, and love and friendship between partners moved to the centre of marriage. Marriage was no longer just a union where duties were carried out. This model promises deep closeness. Its risk comes from the same place: when there is less to talk about, the main pillar holding up the marriage weakens too.",
              "29"),
        "B": ("Today: The capstone marriage",
              "Your idea of marriage is completely of today: first a job, savings, a home and getting to know yourself, then the wedding. Sociology calls this the difference between a cornerstone and a capstone. In the old model, marriage was the cornerstone of a life; in the new one, it is the capstone placed on top of a life already built. Across the OECD, the average age at first marriage rose by 2021 to about 31 for women and about 33.4 for men. The price: as the bar for entry rises, people who are economically fragile may reach marriage later.",
              "29"),
    },
}

# ---------------------------------------------------------------- 20
ICERIK["ayni-evlilik"] = {
    "kanca": "Answer separately, then compare: when you say “yes”, are you saying yes to the same marriage?",
    "sorular": [
        ("Marriage is:", ["The start of building a life together", "The crown on a life already built"]),
        ("A legal marriage is mostly:", ["A legal safeguard", "A public declaration of commitment"]),
        ("The real gain from marriage:", ["Sharing the jobs and the burdens", "Doing the things we love together"]),
        ("Money:", ["One shared pot", "A joint budget, separate accounts"]),
        ("Careers:", ["If needed, one leads and the other supports", "Both carry equal weight"]),
        ("Before getting married:", ["We should be financially ready", "We’ll get ready together after the wedding"]),
        ("Living together without marrying:", ["A step towards marriage", "An option in its own right"]),
        ("Free time:", ["We spend most of it together", "Each of us also has our own space"]),
        ("What I expect most from my spouse:", ["Sharing life’s load", "Supporting me as I grow"]),
        ("The wedding:", ["Big and grand", "Small and simple"]),
    ],
    "seviyeler": [
        (0, "Two different marriages",
         "You expect very different things from the same institution. The book does not see this as a problem in itself: one person may see marriage as a partnership of two independent people, the other as a union where almost all free time is spent together. According to the book, the problem may not be the models themselves but the partners expecting different things from the same institution. The items where your answers differ are a map of unspoken expectations."),
        (4, "Same building, different plans",
         "On some basic points you imagine the same marriage; on others your paths split. According to the book, as tradition gives fewer answers in modern marriage, more negotiation is needed: the couple has to design its own institution. The items where you differ are the parts of that design not yet drawn. As the book puts it, freedom grows, and so may the need for coordination. Different answers are not proof of a mismatch; they are a list of things to talk about."),
        (7, "A shared plan",
         "You expect mostly the same things from marriage. As the book observes, the state gives everyone the same marriage certificate, and couples load different stories onto it. Your stories overlap in most places. If there are a few items where you differ, they are probably the ones you will talk about again as life changes. A shared plan is not a plan that never changes. When jobs, children or cities change, the same questions come back to the table."),
        (9, "The same story",
         "You imagine the same marriage on almost every item. According to the book, a defining feature of modern marriage is that couples increasingly write its meaning themselves. You are writing the same lines. One note from the book: couples may start with an equal-partners ideal, but children, pay gaps and the demands of working life can slowly pull them towards a more traditional arrangement. The dream is the same; life may change."),
    ],
    "bolum": "15",
}
