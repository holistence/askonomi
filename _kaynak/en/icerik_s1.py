# -*- coding: utf-8 -*-
# Aşkonomi quiz series, Season 1 (tests 1-10). English edition, translated from _kaynak/icerik_s1.py.
# Source page numbers (Turkish book): /home/claude/askonomi_in/rapor_s1.md

ICERIK = {}

# 1 ------------------------------------------------------------------
ICERIK["fiyatin-ne"] = {
    "kanca": "Your partner has no price tag, but in your eyes love still has a price.",
    "sorular": [
        ("What puts you off most on a first date?", [
            ("Z", "Cancelling at the last minute"), ("D", "Checking their phone all the time"),
            ("G", "Stories that don’t add up"), ("O", "Rushing to plan the second date right away"),
            ("H", "Everything feeling too ordinary")]),
        ("Which gesture wins you over?", [
            ("Z", "Making time for you in their busiest week"), ("D", "Remembering a small detail you mentioned a month ago"),
            ("G", "Being exactly where they said, exactly when they said"), ("O", "Saying “Take some time for yourself this weekend”"),
            ("H", "Suggesting something neither of you has ever tried")]),
        ("What goes in the “loss” column of a relationship for you?", [
            ("Z", "Plans that always get pushed to next week"), ("D", "Being listened to with half an ear"),
            ("G", "Lies, even small ones"), ("O", "Having every move questioned"),
            ("H", "Every day being a copy of the one before")]),
        ("A friend is telling you about their new partner. Which line convinces you?", [
            ("Z", "“However busy they are, they make time for me.”"), ("D", "“They really listen to me.”"),
            ("G", "“They did everything they said they would.”"), ("O", "“They’re not jealous, they give me space.”"),
            ("H", "“I’m never bored with them.”")]),
        ("Which line feels closer to you?", [
            ("Z", "Love is measured in the hours you give someone."), ("D", "Being seen comes before being loved."),
            ("G", "A promise is stronger than a contract."), ("O", "To love is not to hold on, but to be able to let go."),
            ("H", "Routine is the silent killer of love.")]),
        ("The fastest way to make up after a fight?", [
            ("Z", "Coming over right away and talking face to face"), ("D", "Really trying to understand how I feel"),
            ("G", "Making a promise that can actually be kept"), ("O", "Giving it a little time, then talking"),
            ("H", "A crazy idea that makes me laugh out of nowhere")]),
    ],
    "sonuclar": {
        "Z": ("Your price: Time",
              "For you, the most convincing proof of love is a free slot in someone’s calendar. The book treats time as one of love’s most basic scarce resources: nobody can add a twenty-fifth hour to the day. And what an hour means depends on the circumstances and on what was given up for it. The cost: it becomes easy to accuse a partner going through a busy period of not loving you. The book warns that the conclusion “They don’t make time for me, so they don’t love me” is not always true.",
              "03"),
        "D": ("Your price: Attention",
              "You want to be seen before you are loved. Sitting at the same table is not enough; their mind has to be there too. According to the book, scarce resources other than money also send signals in a romantic relationship, and attention is at the top of the list. An expensive but impersonal gift won’t impress you. A cheap gift that remembers a tiny detail you mentioned months ago, though, says a lot about attention. The cost: because attention can be measured at any moment, disappointment can be produced at any moment too.",
              "06"),
        "G": ("Your price: Trust",
              "Your currency is consistency: being there at the time they said, keeping the small promise. The book compares trust to capital. It builds up from past behaviour and lowers the everyday transaction costs of a relationship. But it doesn’t work like a bank account: a small delay may not wipe out years of trust, while a single big betrayal can change how the whole past is read. The cost: according to the book, a relationship that keeps asking for new proof can turn into one where no signal ever counts as reliable enough.",
              "24"),
        "O": ("Your price: Space",
              "The way to win you is to not try to hold on to you. The book says people want different things from a relationship: for one person, seeing each other often is the main sign of a good relationship; for another, protecting personal space is just as valuable. In you, the second one wins. According to the book, privacy is not the same as living a secret second life behind your partner’s back. The cost: someone who wants frequent contact may read your need for space as a lack of interest.",
              "24"),
        "H": ("Your price: Novelty",
              "For you, the biggest cost is boredom. The same weekend routine feels like stagnation to you, not security. The book cites research on this: sharing new and exciting experiences can support relationship quality for some couples. But according to the book, novelty is not about how much you spend; it is about the quality of shared experiences outside the routine. The cost: people get used to new experiences too, and turning life into a constant hunt for excitement is not sustainable.",
              "25"),
    },
}

# 2 ------------------------------------------------------------------
ICERIK["kacan-mi-kovalanan-mi"] = {
    "kanca": "They say “play hard to get and you’ll be chased.” So which one are you?",
    "sorular": [
        ("Someone you like replied to your message 6 hours later. You?", [
            ("K", "I wait at least 7 hours too"), ("V", "I reply right away, maybe something happened"),
            ("D", "I reply whenever I’m free"), ("S", "I don’t reply at all, it wasn’t going anywhere anyway")]),
        ("At the end of a first date…", [
            ("K", "I say “I’ll call you” and don’t call for a few days"), ("V", "I text “that was lovely” before I even get home"),
            ("D", "If I liked them, I say so clearly"), ("S", "I leave the next step to them")]),
        ("Who attracts you most?", [
            ("V", "Someone mysterious and hard to reach"), ("K", "Someone who makes an effort and works for me"),
            ("D", "Someone who says clearly what they want"), ("S", "Someone who never pushes me and takes it slow")]),
        ("How does always being available in a relationship make you feel?", [
            ("K", "Like my value is dropping"), ("V", "Peaceful, I’m always there anyway"),
            ("D", "Nice, if it goes both ways"), ("S", "A bit suffocating")]),
        ("How would your friends describe you?", [
            ("K", "“Hard to catch.”"), ("V", "“Gives everything when in love.”"),
            ("D", "“Knows what they want.”"), ("S", "“Always watching, rarely makes a move.”")]),
        ("Which statement do you agree with?", [
            ("K", "Value comes from being out of reach."), ("V", "Love shouldn’t be hidden, it should be shown."),
            ("D", "Whoever plays games loses."), ("S", "A relationship that never starts can never end.")]),
    ],
    "sonuclar": {
        "K": ("The Runner: Scarcity strategy",
              "You cut your supply on purpose: late replies, vague plans, a little distance. You believe staying out of reach will raise your value. The book doesn’t reject this instinct completely, but it draws a line: scarcity alone does not create value; the scarce thing also has to be wanted. The cost: according to the book, not replying, always keeping your distance or leaving the other person in uncertainty can sometimes end the relationship instead of increasing interest.",
              "03"),
        "V": ("The Chaser: Strong demand",
              "When you love, you stop keeping score, and you are often the one who makes the first move. That generosity is lovely. But the book’s chapter on the love market reminds us of one rule: in a romantic relationship, two preference systems run at the same time, and the other person has to choose you too. In the book’s words: “Wanting a lot does not, on its own, produce a match.” The cost: your sacrifice is not a price that guarantees something in return, because your beloved has no price tag.",
              "05"),
        "D": ("In Balance: Clear signal",
              "You don’t play games. You say what you want and expect the same in return. The book makes a distinction here: talk is cheap, because someone who isn’t sincere can easily say the same words. What makes your openness believable is that your words and actions match over time. According to the book, one of the strongest signals in a long relationship is not showing off but consistency. The cost: the same behaviour can look like strong interest to one person and like crossing a boundary to another.",
              "06"),
        "S": ("The Spectator: Waiting on the sidelines",
              "You choose waiting over taking risks. The chance of rejection weighs more than the chance of winning. The book says the price of romantic decisions is not only money: the risk of rejection and emotional vulnerability are also costs. For you, that cost is high. The cost: as the book reminds us, “Not deciding is also, in practice, a decision, because time passes.” The chances you miss while waiting never show up on any bill, but that is exactly where opportunity cost sits.",
              "26"),
    },
}

# 3 ------------------------------------------------------------------
ICERIK["kalp-mi-akil-mi"] = {
    "kanca": "Are heart and head really enemies? Test yourself with six tough choices.",
    "sorular": [
        ("Two options: someone who excites you but lives a chaotic life, or someone reliable but without a “spark”.", [
            ("R", "The reliable one. The spark can come later; stability won’t."), ("T", "Excitement. You only live once."),
            ("S", "Whatever I feel in the first moment."), ("D", "I’ll meet each of them once more, then decide.")]),
        ("Your partner got a job offer in another city.", [
            ("R", "Rent, transport, career… I make a pros and cons list."), ("T", "Wherever they go, I follow."),
            ("S", "I do whatever my gut tells me."), ("D", "First we talk about what we want, then we do the maths.")]),
        ("You had a huge fight at 2 a.m. You’re about to say “It’s over.”", [
            ("R", "Once I calm down, I make a pros and cons list and decide."), ("T", "I say whatever I feel in that moment; the rest can wait."),
            ("S", "I know from past relationships where fights like this end up."), ("D", "I sleep on it; if it still looks the same in the morning, I take it seriously.")]),
        ("Your friends set you up with someone. On paper they tick every box, but you felt nothing.", [
            ("R", "I give it another chance; I didn’t set my criteria for nothing."), ("T", "No spark, no deal. I don’t continue."),
            ("S", "My first impression is what it is, and it’s rarely wrong."), ("D", "I meet them a few more times. A feeling is information, but not the only information.")]),
        ("What do you think of the saying “Love is blind”?", [
            ("R", "It isn’t blind, it just does the maths later."), ("T", "It is blind, and thank goodness for that."),
            ("S", "It isn’t blind, it’s just very fast."), ("D", "It’s blind at first, then it puts its glasses on.")]),
        ("When should you decide to get married?", [
            ("R", "When the financial and practical conditions are ready"), ("T", "The moment you find the right person"),
            ("S", "The day you feel “this is it”"), ("D", "When your heart says yes and the circumstances allow it")]),
    ],
    "sonuclar": {
        "R": ("Your heart is an accountant",
              "It’s not that you don’t love; you just keep the books on love too. According to the book, that isn’t coldness: economic rationality is not about finding the option that pays the most, but about being able to choose between different goals you care about. The cost: weighing everything all the time can delay commitment. The book’s standard is clear: “Rationality is not keeping constant accounts of the relationship, but keeping the capacity to change an old judgement when important new information arrives.”",
              "02"),
        "T": ("Your heart is a gambler",
              "You play big. You see the risks, but you follow your heart. The book doesn’t automatically call this irrational: if a shared life is worth more to you than what you give up, your choice makes sense within your own preferences. But it also reminds us that the feeling “I can’t live without them” in a moment of intense longing doesn’t predict the future perfectly. The cost: according to the book, rationality here is not a lack of emotion, but the ability to judge hard-to-reverse decisions in more than one emotional state.",
              "02"),
        "S": ("Your heart takes shortcuts",
              "You don’t do long calculations, but you don’t decide at random either. Your intuitions are quick rules filtered from your experience. Building on the classic work of Tversky and Kahneman, the book explains that these shortcuts make decisions under uncertainty easier, but can sometimes lead to systematic errors. The cost: a recent bad break-up can inflate how risky new people seem to you. The book’s standard is noticing in which situations your intuition is a good guide, and how good.",
              "02"),
        "D": ("Heart and head in partnership",
              "You don’t jump in blindly, and you don’t put everything in a spreadsheet either. You feel first, then you check. The book defends exactly this distinction: “Do I love them?” and “Can I live with them?” are different questions. Emotion tells you what you care about; reason helps you think through the consequences. The cost: this path is slow. If you drag out the decision too long, as the book says, not deciding also turns into a decision in practice, because time passes.",
              "02"),
    },
}

# 4 ------------------------------------------------------------------
ICERIK["ilk-bulusma-sinyali"] = {
    "kanca": "You say one thing, the other person hears something else.",
    "sorular": [
        ("How do you choose the place for a first date?", [
            ("E", "I research what they like and pick it myself"), ("V", "A stylish, well-known place"),
            ("D", "I ask, “I like this place, what do you think?”"), ("G", "I don’t say until the last minute, let it be a surprise")]),
        ("What do you wear?", [
            ("E", "I get ready carefully, so the effort shows"), ("V", "My best, most eye-catching piece"),
            ("D", "Just what I always wear"), ("G", "Something a bit unusual, let them try to figure me out")]),
        ("How much do you talk about yourself?", [
            ("E", "Not much, I mostly listen to them"), ("V", "My achievements, the places I’ve travelled"),
            ("D", "The good and the bad, whatever there is"), ("G", "Very little, let them be curious")]),
        ("The bill arrives.", [
            ("E", "I pay, it’s my gesture"), ("V", "I pull out my card straight away"),
            ("D", "I offer to split it"), ("G", "I smile and wait to see what they do")]),
        ("After the date…", [
            ("E", "A long message referring back to what we talked about"), ("V", "A photo or a story"),
            ("D", "“I really enjoyed it, let’s meet again.”"), ("G", "Nothing until the next day")]),
        ("Which line from them would impress you?", [
            ("E", "“I can tell you put effort into this.”"), ("V", "“You’re so impressive.”"),
            ("D", "“I feel comfortable with you.”"), ("G", "“I can’t figure you out.”")]),
    ],
    "sonuclar": {
        "E": ("The Effort signal",
              "Instead of saying “I love you”, you do things that cost something: time, care, research. The book says that in romance some strong signals come not from the wallet but from the calendar. Behaviour that is hard to fake can carry more information. The cost: according to the book, “Cost on its own is not a certificate of sincerity.” The other person sees your effort, but they decide what it means.",
              "06"),
        "V": ("The Shop-window signal",
              "You make your power and means visible: a stylish venue, a bold outfit, success stories. The book explains this with Veblen’s idea of conspicuous consumption. A bank account is invisible, but a venue and a lifestyle can hint at economic capacity. The cost: according to the book, a wealth signal can be read in more than one way. An expensive restaurant may look like generosity to you and like showing off to them. Money being visible doesn’t mean everyone will like what they see.",
              "08"),
        "D": ("The Transparency signal",
              "You play with your cards on the table. According to the book, words alone are a weak signal: a trustworthy person and an untrustworthy one can both present themselves as trustworthy. What makes your openness valuable is that you keep acting the way you talk. In the book’s example, politeness on a first date is a small piece of data; consistency observed over six months is much more. The cost: openness may not dazzle at first. Its return builds up over time.",
              "06"),
        "G": ("The Mystery signal",
              "You create curiosity by holding back information. The book accepts that this can work: uncertainty, unavailability or inconsistency can sometimes increase emotional intensity. But it adds right away: “Intensity and relationship quality are not the same variable.” The cost: according to the book, people draw conclusions about hidden qualities from behaviour they can observe. Give little data, and the other person draws the conclusions. Mystery may win you the first date, but trust is what carries a relationship.",
              "02"),
    },
}

# 5 ------------------------------------------------------------------
ICERIK["guzellik-mitleri"] = {
    "kanca": "They say “beauty is in the eye of the beholder”, but research isn’t so sure.",
    "sorular": [
        ("People rated as below average in looks may earn less at work than average-looking people.", True,
         "True. In Hamermesh and Biddle’s classic 1994 study, people rated as below average in attractiveness earned roughly 5–10 per cent less than average-looking people. Still, the book warns: this finding should not be turned into a formula like “Be beautiful and you’ll earn X per cent more.”"),
        ("The beauty premium is the same size in every job.", False,
         "False. In an experiment cited in the book (Deryugina and Shurchkov, 2015), attractive workers received higher wage offers in the task where looks were expected to matter for performance. No similar premium appeared in analytical and data-entry tasks. And as real performance information came out, the effect of looks could shrink."),
        ("People disagree a lot about who is beautiful.", False,
         "False, at least not as much as people think. A study by Langlois and colleagues (2000), built on eleven meta-analyses, showed that people can agree to a certain degree about who is attractive, both within the same culture and across cultures. The book adds that this does not mean there is one universal standard of beauty."),
        ("People who are seen as attractive may also be judged more positively in other ways.", True,
         "True. In psychology this is called the attractiveness stereotype, or more broadly the halo effect. The meta-analytic review by Langlois and colleagues found that children and adults seen as attractive could be judged more positively. According to the book, this doesn’t mean they really are better at everything."),
        ("Couples tend to be similar in physical attractiveness.", True,
         "True. In a 2024 study by Webster and colleagues that re-analysed older meta-analytic data, mixed-sex couples showed a positive correlation of about r = 0.39 between the two partners’ attractiveness as rated by outside observers. The book stresses that this is an average pattern, not an individual’s destiny."),
        ("In real romantic evaluations, physical attractiveness matters much more for men than for women.", False,
         "False. In a meta-analytic review by Eastwick and colleagues (2014), answers to hypothetical partner questions could differ, but in real romantic evaluations the sex difference in the effect of attractiveness was quite small and not significant. According to the book, physical attractiveness can play a meaningful role for both sides."),
    ],
    "seviyeler": [
        (0, "Fooled by the shop window",
         "Most of your intuitions about beauty didn’t match the research cited in the book. In the book’s words, “Human behaviour is more complex than slogans.” The book sums it up in two sentences: Beauty matters. But beauty is not a single, objective value."),
        (3, "Rough estimate",
         "You got some right and some wrong. That is exactly why the economics of beauty is interesting: looks seem to give a lot of information at first glance, but as the book puts it, “A pretty face is not a lab report.”"),
        (5, "Market analyst",
         "You read well how beauty gets rewarded. Now the book’s hard question is yours: in which areas does society reward beauty, and how far is that reward actually relevant to the job?"),
    ],
    "bolum": "07",
}

# 6 ------------------------------------------------------------------
ICERIK["para-konusulunca"] = {
    "kanca": "Money can’t buy love, but who pays the bill?",
    "sorular": [
        ("The bill on a first date?", [
            ("O", "Whoever invited pays, then we take turns"), ("A", "Everyone pays their own share"),
            ("K", "I pick a place that isn’t expensive anyway"), ("C", "I pay, no need to discuss it")]),
        ("You’ve started living together. Rent and bills?", [
            ("O", "All from one joint account"), ("A", "Separate accounts, expenses split"),
            ("K", "Budget spreadsheet first, then we decide"), ("C", "Whoever is better off pays, we don’t count")]),
        ("Your partner made a big purchase without asking you.", [
            ("O", "I’m upset, that’s our shared money"), ("A", "If it’s their own money, I have no say"),
            ("K", "I check whether it wrecked our savings plan"), ("C", "If it made them happy, no problem")]),
        ("One earns 100 units a month, the other 40. Shared expenses?", [
            ("O", "Everything earned goes into a shared pot, expenses come out of it"), ("A", "In proportion to income, each from their own account"),
            ("K", "First set aside savings, then share the rest"), ("C", "The higher earner can easily cover it, let’s not count")]),
        ("Which money fight sounds familiar?", [
            ("O", "“Why didn’t you ask me about this?”"), ("A", "“Don’t talk to me about my money.”"),
            ("K", "“You spent money again?”"), ("C", "“Why are you so tight with money?”")]),
        ("Which line describes you?", [
            ("O", "If marriage is a partnership, the money is shared too."), ("A", "Separate wallets, solid relationship."),
            ("K", "Today’s love grows on tomorrow’s security."), ("C", "Money is for spending, especially on someone you love.")]),
    ],
    "sonuclar": {
        "O": ("The Shared Pot",
              "For you, a relationship is a partnership, and a partnership has one pot. The book cites a striking study: in Gladstone and colleagues’ work (2022), couples who fully pooled their money reported higher relationship satisfaction on average. But the book stresses that this is not a universal recipe: a joint account does not create trust by itself. The cost: with a shared pot, spending decisions have to be shared too, and that is where “Why didn’t you ask me about this?” comes from.",
              "08"),
        "A": ("Separate Wallets",
              "You share love but keep your wallets separate. That isn’t selfishness; it’s a way of protecting your independence. According to the book, a couple with separate accounts is not doomed to a bad relationship. The book also stresses the link between money and freedom: someone with their own income can stay in a relationship by choice, not out of necessity. The cost: contributions other than money, like time and care, easily become invisible in this kind of bookkeeping. As the book reminds us, “Not every line in love’s budget is written in money.”",
              "08"),
        "K": ("The Saving Heart",
              "For you, money is something to protect, not to spend: tomorrow’s security. This can bring stability to a relationship. But the book says money fights often come not from the numbers but from what they mean: for one partner saving means security, for the other it means putting life on hold. According to the book, a budget is made of numbers, but a money fight is often made of values. The cost: in a study cited in the book, money arguments were not the most frequent ones, but they tended to be more recurring and harder to resolve than others.",
              "08"),
        "C": ("The Generous Heart",
              "You show love partly by spending: gifts, invitations, surprises. According to the book, money can be one of the ways “I love you” turns into action. But the book also writes the reverse: money can be used as a substitute for love. One partner may contribute by earning money while the other is waiting for time and emotional closeness. The cost: according to the book, money is not always a full substitute for time, attention and care.",
              "08"),
    },
}

# 7 ------------------------------------------------------------------
ICERIK["benzer-mi-zit-mi"] = {
    "kanca": "Do opposites attract, or are your choices saying something else?",
    "sorular": [
        ("In what ways should your ideal partner be like you?", [
            ("B", "In almost every way"), ("Z", "In none, or I’ll get bored"),
            ("Y", "They should be a bit ahead of me"), ("T", "Same values, different skills")]),
        ("Level of education?", [
            ("B", "Should be close to mine"), ("Z", "Doesn’t matter at all"),
            ("Y", "Higher than mine is better"), ("T", "Doesn’t matter as long as we can talk to each other")]),
        ("Weekend plans…", [
            ("B", "We do the same thing we both love"), ("Z", "I explore their world, they explore mine"),
            ("Y", "I join their circle and meet new people"), ("T", "One plans, the other makes it happen")]),
        ("When you argue…", [
            ("B", "We rarely argue, we think alike"), ("Z", "Often, but it’s exciting"),
            ("Y", "I learn from their point of view"), ("T", "One calms things down, the other solves it")]),
        ("When you meet their family, what do you look at?", [
            ("B", "Whether they’re like my family"), ("Z", "How different they are"),
            ("Y", "What kind of background they come from"), ("T", "How well they get along with each other")]),
        ("A Turkish saying goes: “The pot rolled along and found its lid.”", [
            ("B", "Exactly like that"), ("Z", "I’d go looking for a different pot"),
            ("Y", "The lid should lift the pot up a little"), ("T", "Pot and lid aren’t the same, they just fit each other")]),
    ],
    "sonuclar": {
        "B": ("The Mirror: Choosing someone similar",
              "You choose people like yourself, and the picture of real couples is close to yours. According to the book, people match with others like them in education, religion, lifestyle and many other traits more often than you would expect. This is called assortative mating, or homogamy. But preference isn’t the only reason: the same schools, workplaces and neighbourhoods already bring similar people together. The cost: according to the book, matching with similar people can sometimes concentrate existing inequalities within the same household.",
              "09"),
        "Z": ("The Opposite Pole",
              "You feed on difference; worlds you don’t know attract you. The book shows that the saying “opposites attract” doesn’t really match the overall picture of real couples: people match with similar others in many traits more often than expected. But according to the book, “birds of a feather flock together” isn’t a complete theory of relationships either. The cost: not all differences are equal. A different taste in music is easy to manage; opposite views on having children can create a much more fundamental conflict.",
              "09"),
        "Y": ("One Step Up",
              "You look for a partner who is a little ahead: more knowledgeable, more experienced, with a wider circle. You want the relationship to help you grow. Here the book objects to a common way of talking: expressions like “marrying up” reduce many-sided human qualities to a single ranking. One partner may be more educated, the other wealthier. In such a couple, who is “up”? The cost: while looking up, it’s easy to forget that the other person has their own ranking of preferences too.",
              "09"),
        "T": ("The Complement",
              "You look for fit, not sameness: shared values, different skills. The book sees similarity and complementarity not as rivals but as principles that work together on different dimensions. One partner may be strong at planning, the other at social relationships. Careers in different sectors can spread the risk. The cost: classic family economics sometimes tied complementarity to a rigid division of labour. According to the book, the long-term cost of specialising can pile up on one partner if the couple separates.",
              "09"),
    },
}

# 8 ------------------------------------------------------------------
ICERIK["ihtiyac-arzu-tercih"] = {
    "kanca": "Do you love them, or do you need them?",
    "sorular": [
        ("What if you couldn’t see each other for a whole week?", [
            ("I", "I’d feel incomplete and restless"), ("A", "I’d burn with longing"),
            ("T", "I’d get on with my own things; when they’re back, it’s still them"), ("L", "Nothing much would change, just my routine would be off")]),
        ("Why did you choose them in the first place?", [
            ("I", "I felt safe when they were around"), ("A", "I couldn’t take my eyes off them"),
            ("T", "Of everyone I knew, they suited me best"), ("L", "They were somehow in my life, and it just continued")]),
        ("What if someone more “suitable” on paper came along?", [
            ("I", "I’d be scared, but I couldn’t leave them"), ("A", "It’s not about suitability, it’s about attraction"),
            ("T", "I’d compare, and I think I’d still choose them"), ("L", "Switching would feel like too much hassle")]),
        ("What do you love most about them?", [
            ("I", "That they’re always there"), ("A", "How they make me feel"),
            ("T", "Who they are"), ("L", "That they know everything, so I don’t have to explain")]),
        ("How does the thought of breaking up make you feel?", [
            ("I", "I panic; without them I’d be incomplete"), ("A", "Painful, but a passion worth living"),
            ("T", "Sad, but life goes on"), ("L", "My whole routine would change, exhausting")]),
        ("Which line feels closer?", [
            ("I", "“Without them, I’m incomplete.”"), ("A", "“I can’t stop wanting them.”"),
            ("T", "“Every morning I choose them again.”"), ("L", "“Everything is easy with them.”")]),
    ],
    "sonuclar": {
        "I": ("Need: A safe harbour",
              "At the centre of your bond are security and belonging. According to the book, a need is a general condition important for well-being: closeness, belonging, security. These don’t have to be met within a romantic relationship, but in your case they are largely gathered in this one person. The cost: the book separates two meanings of “we need each other”. In one, people enrich each other’s lives; in the other, a person has no other real option left. In the book’s words, “Commitment is not the complete absence of a way out.”",
              "04"),
        "A": ("Desire: The burning engine",
              "Your bond is built on attraction: wanting, longing, not being able to look away. According to the book, desire is a general need aimed at one particular person. That is exactly where the difference between “I want closeness” and “I want to be with Ayşe” shows up. In the book’s words, “A person can need closeness, but doesn’t fall in love with just anyone.” The cost: the book also reminds us that your lifestyle may not fit with the person you feel a very strong pull towards.",
              "04"),
        "T": ("Preference: Again, every day",
              "You keep them by your side because you see the alternatives and still choose them. According to the book, preference shows which wish you give more weight to when your wishes clash. Economics calls this revealed preference: the choices we make under real constraints say as much about what we value as our words do. The cost: the book is careful here. What we choose is not always what we want most; sometimes it is simply the option we can reach.",
              "04"),
        "L": ("Habit: A shared history",
              "Habit plays a big part in your bond, and that is not a bad thing. According to the book, trust, care, habit and a shared identity can take up more space in a long relationship. A history built together cannot be instantly recreated with another partner. The cost: the book also draws a line: “Having stayed in a relationship for a long time is not, on its own, a good enough reason to keep staying.” The book’s question: when does staying cost more than leaving?",
              "22"),
    },
}

# 9 ------------------------------------------------------------------
ICERIK["askin-alti-tanimi"] = {
    "kanca": "Canadian sociologist John Alan Lee sorted love, like colours, into six basic styles. Which one is closest to you?",
    "sorular": [
        ("What does love remind you of most?", [
            ("E", "Being struck at first sight"), ("L", "A fun game"), ("S", "A friendship that slowly deepens"),
            ("P", "A life built with the right person"), ("M", "Sleepless nights"), ("A", "Giving without expecting anything back")]),
        ("The ideal beginning?", [
            ("E", "A single look"), ("L", "Flirting, jokes, lightness"), ("S", "Someone you’ve known for years"),
            ("P", "Talking about shared goals"), ("M", "Someone you can’t get out of your head"), ("A", "Meeting while helping them")]),
        ("What can’t you stand in a relationship?", [
            ("E", "The spark fading"), ("L", "Too much seriousness"), ("S", "Trust being shaken"),
            ("P", "Lack of planning"), ("M", "Uncertainty, unanswered messages"), ("A", "The person I love being unhappy")]),
        ("How should your partner make you feel?", [
            ("E", "Enchanted"), ("L", "Free"), ("S", "At home"),
            ("P", "Safe and on track"), ("M", "Irreplaceable"), ("A", "Like someone who is good for them")]),
        ("A break-up…", [
            ("E", "If the passion is gone, it’s over"), ("L", "Life goes on, there are other people"), ("S", "The friendship stays"),
            ("P", "If it doesn’t make sense, it has to end"), ("M", "Very hard to accept"), ("A", "If they’re happy, I can accept it")]),
        ("Which line describes you?", [
            ("E", "Love is the heart beating faster."), ("L", "Love is a game too beautiful to take seriously."),
            ("S", "Love is growing old with your best friend."), ("P", "Love is choosing the right partner."),
            ("M", "Love is all or nothing."), ("A", "Love is giving.")]),
    ],
    "sonuclar": {
        "E": ("Eros: Passion",
              "For you, love begins with strong romantic and physical attraction. Lee calls this style eros. The book explains that in early romantic love the brain’s reward and motivation systems can light up, but it adds that we shouldn’t jump too quickly to the conclusion that “love is like a drug.” The cost: according to the book, in a thirty-year marriage the ingredients of love change, and longing may give way to trust, care and a shared identity. The real question is how to carry the spark into everyday life.",
              "01"),
        "S": ("Storge: Friendship",
              "Your love burns slowly but lasts long. Lee calls this style storge: friendship and closeness that grow over time. You believe more in a shared past built up over time than in flashy beginnings. The book describes trust the same way: a capital that comes not from a single gesture but from behaviour observed again and again in different situations. The cost: a slowly built bond can look like a lack of interest to someone who wants to move fast.",
              "24"),
        "L": ("Ludus: Play",
              "You experience love like a light, fun, non-binding game. Lee calls this style ludus: a playful, low-commitment way of relating. You like keeping your options open. The cost: according to the book, keeping every door open has its own opportunity cost, because your partner may also think the relationship can be swapped at any moment and invest just as little. In the book’s words, “Freedom is when closing the door is our own decision.”",
              "26"),
        "P": ("Pragma: The smart choice",
              "You see love as choosing the right partner: values, goals, life plans. Lee calls this style pragma: practical, compatibility-focused love. That isn’t coldness. According to the book, the real point is knowing where similarity is needed: a difference in music taste is easy to manage, while opposite views on having children can create a much more fundamental conflict. The cost: as the book warns, romantic compatibility is not a score we get by adding up similarities.",
              "09"),
        "M": ("Mania: Intensity",
              "Your love is intense: all or nothing. You get restless when a message doesn’t come and struggle with uncertainty. Lee calls this style mania, and the book describes it as a form of love linked to intense dependence and jealousy. Being able to feel deeply is a gift. The cost: according to the book, jealousy can show that a relationship is valuable, but its intensity doesn’t measure the amount of love. The book’s question: what are we afraid of losing?",
              "19"),
        "A": ("Agape: Giving",
              "For you, love means giving without expecting anything back. The well-being of the person you love comes before your own. Lee calls this style agape: selfless, giving love. The book also reminds us that these styles are not fixed personality types. The cost: according to the book, care done well can become invisible. The book’s standard: the fact that someone enjoys giving care doesn’t mean that responsibility should belong to them alone forever.",
              "16"),
    },
}

# 10 -----------------------------------------------------------------
ICERIK["birbirinizi-fiyatlamak"] = {
    "kanca": "Answer separately, then compare how much you both value the same things.",
    "sorular": [
        ("An evening:", ["Just the two of us at home", "Out with friends"]),
        ("Some unexpected money comes in:", ["A holiday", "Savings"]),
        ("When we argue:", ["Let’s talk right away", "Let’s talk once we’ve cooled down"]),
        ("Love is best shown:", ["In words", "In actions"]),
        ("Where to live:", ["A big city", "A quiet small town"]),
        ("Shared expenses:", ["Half and half", "According to income"]),
        ("Phones:", ["We share passwords", "Everyone has their own space"]),
        ("Bayram (religious festivals) and holidays:", ["With our families", "Just the two of us"]),
        ("The future:", ["Planned", "Go with the flow"]),
        ("Housework:", ["With a task list", "Whoever is free"]),
    ],
    "seviyeler": [
        (0, "Different price lists",
         "You value different things in almost every area. That isn’t a verdict. According to the book, a match in the love market is where two separate preference rankings meet, and on these ten items your overlap looks narrow. The items where you answered differently are a map you might both find worth a look."),
        (3, "Different currencies",
         "On some things you value the same, on others different things. The example from the book’s chapter on money may sound familiar: for one partner saving means security, for the other it means putting life on hold. Maybe the items where you differ come less from preferences and more from giving the same thing different meanings."),
        (6, "Close exchange rate",
         "You value the same things in most areas. According to the book, romantic compatibility is not a score we get by adding up similarities. The real question is which of the items you differ on are easy to manage, like music taste, and which are fundamental, like wanting children."),
        (9, "The same price list",
         "You value almost everything the same way. Still, the book reminds us of one thing: there is a love market, but your beloved has no price tag. Today’s overlap doesn’t guarantee tomorrow. According to the book, people don’t have to give the same partner qualities the same weight at different ages."),
    ],
    "bolum": "05",
}
