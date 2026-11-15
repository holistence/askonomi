# -*- coding: utf-8 -*-
# Aşkonomi test series — English text constants (translated from _kaynak/veri.py).
# Only human-readable text is translated; numbers, slugs, type codes and chapter codes are unchanged.
# tur: profil | senaryo | mit | cift | hesap | nesil | karne

SEZONLAR = [
    {"no": 1, "ad": "Entering the Market", "alt": "Who chooses whom, and why?"},
    {"no": 2, "ad": "The Contract", "alt": "Marriage, home and labour"},
    {"no": 3, "ad": "Crisis", "alt": "When the relationship is shaken"},
    {"no": 4, "ad": "The Digital Age", "alt": "Hearts on swipe"},
]

TUR_AD = {"profil": "Profile", "senaryo": "What would you do?", "mit": "Myth or fact?", "cift": "Couples test",
          "hesap": "Calculator", "nesil": "Generation test", "karne": "Final"}

BOLUM = {
    "01": "What Is Love?", "02": "Love and Rationality", "03": "Scarcity", "04": "Needs, Desires and Preferences",
    "05": "The Love Market", "06": "Signals", "07": "The Economics of Beauty", "08": "Money and Wealth",
    "09": "Equal Matches and Similarity", "15": "The Economics of Marriage", "16": "Invisible Labour",
    "17": "The Economics of Children", "18": "Polygamy", "19": "The Economics of Jealousy",
    "22": "The Economics of Divorce", "23": "The Economics of Cheating and Betrayal", "24": "Trust Capital",
    "25": "Investing in the Relationship", "26": "Opportunity Cost", "27": "Too Many Options", "28": "Expectation Inflation",
    "29": "Modern Marriage", "30": "Before and After Tinder", "31": "The Love Industry",
    "32": "Globalised Intimacy", "33": "The Economics of Loneliness", "34": "The Future Economics of Love",
}

# ---- Title list (approved) ----
LISTE = [
    # no, slug, title, type, chapter
    (1, "fiyatin-ne", "What’s your price on the love market?", "profil", "05"),
    (2, "kacan-mi-kovalanan-mi", "Do you run, or do you get chased?", "profil", "03"),
    (3, "kalp-mi-akil-mi", "Is your heart doing the maths, or your head?", "senaryo", "02"),
    (4, "ilk-bulusma-sinyali", "What does your first-date signal really say?", "profil", "06"),
    (5, "guzellik-mitleri", "6 things you believe about beauty: how many are true?", "mit", "07"),
    (6, "para-konusulunca", "What happens to your relationship when money comes up?", "senaryo", "08"),
    (7, "benzer-mi-zit-mi", "Do you choose someone like you, or your opposite?", "profil", "09"),
    (8, "ihtiyac-arzu-tercih", "Is your partner a need, a desire or a preference?", "profil", "04"),
    (9, "askin-alti-tanimi", "Which of love’s 6 definitions is yours?", "profil", "01"),
    (10, "birbirinizi-fiyatlamak", "How accurately do you “price” each other?", "cift", "05"),
    (11, "evlilik-ne", "Is marriage an investment, an insurance policy or a partnership for you?", "profil", "15"),
    (12, "gorunmeyen-emek", "Invisible Labour Calculator: whose hours at home go unrecorded?", "hesap", "16"),
    (13, "ev-isini-kim-yapiyor", "Who thinks they do the housework, and who really does it?", "cift", "16"),
    (14, "cocugun-maliyeti", "The real cost of a child: 6 claims", "mit", "17"),
    (15, "kiskanclik", "Is your jealousy protection or possession?", "profil", "19"),
    (16, "cok-eslilik-mitleri", "The history of polygamy: myth or fact?", "mit", "18"),
    (17, "iliski-sozlesmesi", "If your relationship were a contract, which clause would be broken?", "senaryo", "15"),
    (18, "bosanmanin-faturasi", "The real bill for divorce", "mit", "22"),
    (19, "evliligin-yuzyili", "Which century is your marriage from?", "nesil", "29"),
    (20, "ayni-evlilik", "Are you two dreaming of the same marriage?", "cift", "15"),
    (21, "beklenti-enflasyonu", "What’s your Expectation Inflation Index?", "hesap", "28"),
    (22, "iliski-getirisi", "Relationship Return on Investment calculator", "hesap", "25"),
    (23, "batik-maliyet", "Sunk cost: are you in a relationship that should end?", "senaryo", "25"),
    (24, "neye-mal-oldu", "What has this relationship cost you?", "hesap", "26"),
    (25, "cok-secenek", "Are too many options making you unhappy?", "profil", "27"),
    (26, "guven-sermayesi", "Is your Trust Capital in the black or in the red?", "hesap", "24"),
    (27, "aldatma-mitleri", "6 common beliefs about cheating: how many are true?", "mit", "23"),
    (28, "affetmek-guvenmek", "Forgiving, trusting, compromising: where do you get stuck?", "profil", "24"),
    (29, "kriz-senaryolari", "What would you do? 8 crisis scenarios", "senaryo", "22"),
    (30, "kriz-aninda", "In a crisis, are you on the same side?", "cift", "24"),
    (31, "tinder-oncesi-sonrasi", "Do you love like it’s before Tinder, or after?", "nesil", "30"),
    (32, "hangi-on-yil", "Which decade does your love life belong to?", "nesil", "29"),
    (33, "kaydirma-ekonomisi", "The swipe economy: 6 claims about dating apps", "mit", "30"),
    (34, "ask-endustrisi", "How much has the love industry sold you?", "hesap", "31"),
    (35, "yalnizligin-fiyati", "What do you know about the price of loneliness?", "mit", "33"),
    (36, "yalniz-misin", "Are you lonely, or have you chosen to be alone?", "profil", "33"),
    (37, "ask-icin-ulke", "Would you move to another country for love?", "senaryo", "32"),
    (38, "goruldu-ekonomisi", "The “Seen” economy: what signal do your messages send?", "senaryo", "06"),
    (39, "2040-aski", "Are you ready for love in 2040?", "profil", "34"),
    (40, "karne", "Your Aşkonomi Report Card", "karne", ""),
]

# ---- Love's Chemistry special section: outside the series, unnumbered ----
OZEL = [
    ("ask-evresi", "Which phase is your in-love brain in?", "profil"),
    ("askin-kimyasi-mitleri", "Love’s chemistry: 6 claims, how many are true?", "mit"),
]
