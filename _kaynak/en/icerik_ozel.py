# -*- coding: utf-8 -*-
# Love's Chemistry special section — two unnumbered tests outside the 40-test series (English edition).
# No link to a book chapter (by the rule on chapters 10–14, not linked to Chapter 10 either).
# Sources are listed in APA style at the end of the /en/kimya/ page.

ICERIK = {}

ICERIK["ask-evresi"] = {
    "kanca": "Desire, attraction and attachment work like separate systems in the brain. Which one are you in?",
    "sorular": [
        ("When you think of them, what comes to mind first?", [
            ("A", "Closeness, wanting to touch"), ("C", "The next message, the next date"),
            ("B", "The everyday routine we’ve built together")]),
        ("How would you feel if you heard nothing from them for a whole day?", [
            ("A", "I’d miss them, but my life would carry on"), ("C", "I’d check my phone every minute"),
            ("B", "I’d wonder, but I wouldn’t worry. I trust them")]),
        ("How are your sleep and appetite lately?", [
            ("A", "Normal. My energy just jumps when I see them"), ("C", "I can’t sleep, and I forget to eat"),
            ("B", "Regular. I even sleep better next to them")]),
        ("What do you think about their flaws?", [
            ("A", "Haven’t really thought about it, the attraction is stronger"), ("C", "Flaws? I can’t see any yet"),
            ("B", "I know them all, and I’ve made peace with most")]),
        ("What do you love most when you’re together?", [
            ("A", "Physical closeness"), ("C", "My heart racing, that thrill"),
            ("B", "Being side by side without needing to talk")]),
        ("When a problem comes up between you, what’s your first reaction?", [
            ("A", "I take some distance, and come back if the pull is still there"), ("C", "My world falls apart, I want to fix it right now"),
            ("B", "We talk and find a way together")]),
        ("What do you talk about when you talk about the future?", [
            ("A", "We don’t really, we live in the moment"), ("C", "I dream about everything, but nothing is concrete"),
            ("B", "We make concrete plans: a home, work, holidays")]),
        ("If a friend described your relationship in one word, which would they pick?", [
            ("A", "Passionate"), ("C", "Head over heels"), ("B", "Peaceful")]),
    ],
    "sonuclar": {
        "A": ("The desire phase", "Right now you are pulled most by closeness and the body. Researchers treat sexual desire as a system linked to romantic attraction, but separate from it. Hormones such as testosterone play a big part in desire, in women as well as men. Desire alone tells you nothing about a relationship’s future. But it is the first spark of most stories. The real question is this: does this closeness grow into curiosity and attachment over time?", ""),
        "C": ("The attraction phase", "You are right in the middle of it. Sleepless nights, a phone you keep checking, someone who looks flawless. Brain imaging studies show that in this phase the dopamine-driven reward and wanting system lights up clearly. Meanwhile, activity can drop in some areas linked to critical judgement of the loved one. Enjoy it. But it may be wise to put big decisions on hold for a while, because your brain is not giving you a neutral report right now.", ""),
        "B": ("The attachment phase", "Calm seems to have replaced the thrill. That is not a decline, it is a different system taking over. Oxytocin and vasopressin are thought to play a role in attachment, although the strongest evidence comes from animal studies. The good news: some studies show the reward system can stay active even in long marriages. The capital of attachment is trust. Its maintenance is new experiences you share.", ""),
    },
}

ICERIK["askin-kimyasi-mitleri"] = {
    "kanca": "Six sentences about love’s chemistry you hear everywhere. How many are backed by science?",
    "sorular": [
        ("Oxytocin is the “love hormone”: a nasal spray of oxytocin bonds people to each other.", False,
         "False. Oxytocin plays a role in childbirth, breastfeeding, touch and social bonding. But many studies on the behavioural effects of oxytocin nasal spray used small samples, and their results could not be reliably replicated (Walum, Waldman & Young, 2016). There is no single “love hormone”."),
        ("The brain of someone who has been dumped but is still in love shows activity in areas linked to addiction.", True,
         "True. Brain scans of people who had recently been rejected but were still in love showed activity in areas linked to reward, motivation and addiction (Fisher et al., 2010). This does not mean love is an illness. But it helps explain why letting go is so hard."),
        ("Love lasts three years at most. That is a biological rule.", False,
         "False. This sentence owes its fame more to pop culture than to science. People married for an average of twenty-one years who still reported intense romantic love showed reward-system activity in brain scans similar to that of new lovers (Acevedo et al., 2012). The shape of love can change. But it has no biological expiry date."),
        ("Heartbreak can cause a real heart problem.", True,
         "True. Sudden, intense emotional stress can cause a temporary weakening of the heart muscle known as “broken heart syndrome”. These patients were found to have markedly high levels of stress hormones (Wittstein et al., 2005). In most cases it is temporary. But chest pain always needs urgent medical attention."),
        ("When you are in love, your critical judgement of the loved one can weaken.", True,
         "True. In lovers looking at a photo of their partner, activity dropped in some brain areas linked to negative emotions and social judgement (Bartels & Zeki, 2004). People call this “love is blind”. The scientific finding is more limited, but it points the same way."),
        ("Sexual desire and romantic attachment are the same thing and run on the same chemistry.", False,
         "False. Anthropologist Helen Fisher described lust, romantic attraction and attachment as linked but separate brain systems (Fisher, 1998). That is why a person can desire someone they feel no bond with, and feel a deep bond with someone they do not desire. The two can meet in the same relationship, but they are not the same thing."),
    ],
    "seviyeler": [
        (0, "Slogan collector",
         "Most of the popular sentences about love’s chemistry sounded convincing to you. You are not alone: these slogans are everywhere. The real picture is more complicated. There is no single “love hormone”; several brain systems work at the same time. And no chemical decides for you who you will build a life with."),
        (3, "Curious observer",
         "You got some right and fell for the popular story on others. The most common mistake about love’s chemistry is reducing a complex process to a single molecule. The brain, the heart and hormones work together. But desire, attraction and attachment can also run separately."),
        (5, "Neuroscience reader",
         "You can tell love’s chemistry apart from the slogans. The next step is this question: if chemistry tells us what we feel, how do we decide who to build a life with? That is exactly where Aşkonomi begins."),
    ],
}
