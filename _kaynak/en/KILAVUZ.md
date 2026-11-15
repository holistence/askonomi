# askonomi.com English edition — translation brief (shared by all translators)

Goal: an English version of the whole interactive site (quizzes, games, tools) for people who do not read Turkish
(first audience: Romanian university students with modest English, ages 18–35). Turkish site stays untouched.
English pages live under https://askonomi.com/en/… and are built from English source files.

## Hard rules
1. NEVER edit existing Turkish files. Write only the English files you are assigned.
2. Keep structure identical: same Python/JS syntax, same keys, ids, option letters, slugs, numbers, booleans,
   list lengths, ordering, function names, CSS classes, element ids, data-* attributes, localStorage keys (see 6),
   umami event names (data-umami-event values). Translate ONLY human-readable text.
3. Validate before you finish:
   - Python content: `python3 /home/claude/askonomi/_kaynak/en/kontrol.py <tr_file.py> <en_file.py>` must print OK.
   - JS: `node --check <file.js>` must pass. For data files (veri.js) also confirm the same structure:
     `node /home/claude/askonomi/_kaynak/en/kontrol_js.js <tr_veri.js> <en_veri.js>` must print OK.
   - Grep your EN output for leftover Turkish letters: `grep -nP "[çğıöşüÇĞİÖŞÜ]" file` — remaining hits must be
     only proper names (Aşkonomi, Çanakkale, province names, people's names, TÜİK) or glossed Turkish terms.
4. Internal page links in EN files must point to the EN site:
   /test/…  -> /en/test/…      /testler/… -> /en/testler/…   /kimya/… -> /en/kimya/…
   /oyunlar/… -> /en/oyunlar/…  /grafik/… -> /en/grafik/…
   Share URLs "askonomi.com/test/…" etc. -> "askonomi.com/en/test/…". Home page "/" stays "/" (it is bilingual).
   Script/data paths you translate -> their /en/ copy (e.g. /en/oyunlar/ortak.js, /en/oyunlar/harita/veri.js,
   /en/testler/veri.js, /en/testler/motor.js, /en/kimya/kimya.js, /en/grafik/grafik.js).
   Shared assets stay as they are: /img/…, /og/…, /testler/stil.css, /oyunlar/oyun.css, fonts, favicons.
   "/kvkk.html" stays (Turkish privacy notice) — label it "Privacy notice (Turkish)".
5. Dates/numbers: English formats (6 October 2026; 1,250.5). Money: keep Turkish lira amounts, write "₺" or "TL"
   as the source does; do not convert currency. TÜİK -> "TurkStat (TÜİK)".
6. localStorage: keep the same keys, unless the stored value is human-readable text that gets shown again;
   then append "_en" to that key in the EN file.

## Style
- Natural, warm, witty English, short sentences, everyday words (CEFR B1–B2). Not literal, not childish.
- Keep the economics precise: opportunity cost, sunk cost, scarcity, signalling, market, supply and demand,
  return on investment, trust capital, expectation inflation, invisible labour, etc.
- Brand: "Aşkonomi" stays as is. Book subtitle: "The Economics of the Heart's Decisions".
  English edition title (not yet published): "The Invisible Hand That Holds Yours".
- Turkish cultural items: keep the Turkish word with a short gloss the first time, e.g. "takı (wedding gold)",
  "görücü usulü (arranged introduction)", "çeyiz (trousseau)". Province and city names unchanged.
- Quiz result names should still be catchy in English. Questions must remain answerable by non-Turks;
  where an item only makes sense in Turkey, adapt it lightly (keep the meaning), do not delete it.
- Book chapter references ("Bölüm 12") become "Chapter 12". The book itself is in Turkish; if text tells the
  reader "read it in the book", you may add "(in Turkish)" once.
- Disclaimers: "for fun and reflection, not a psychological diagnosis".

## Do not
- Do not run git, do not commit, do not touch files outside your assignment.
