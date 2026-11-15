# -*- coding: utf-8 -*-
"""English edition of the Aşkonomi interactive site -> /en/...
Run from repo root AFTER the Turkish build:  python3 _kaynak/insa.py && python3 _kaynak/en/insa_en.py
Content: _kaynak/en/metin.py (titles), _kaynak/en/icerik_*.py (quizzes), _kaynak/en/*.html (page bodies).
Engines: en/testler/motor.js, en/oyunlar/**, en/kimya/kimya.js, en/grafik/grafik.js (hand-translated copies)."""
import json, os, sys, html, datetime, importlib.util as iu

BURA = os.path.dirname(os.path.abspath(__file__))
KAYNAK = os.path.dirname(BURA)
sys.path.insert(0, KAYNAK)
import veri as VTR          # Turkish data: release calendar
import insa as I            # drawing helpers (fonts, taban, sigdir, kaydet_jpg)

def yukle(ad):
    sp = iu.spec_from_file_location("en_" + ad, os.path.join(BURA, ad + ".py"))
    m = iu.module_from_spec(sp); sp.loader.exec_module(m); return m

M = yukle("metin")
ICERIK = {}
for n in ("s1", "s2", "s3", "s4", "ozel"):
    ICERIK.update(yukle("icerik_" + n).ICERIK)

def tum_testler():
    t = VTR.takvim(); out = []
    for no, slug, ad, tur, bolum in M.LISTE:
        d = {"no": no, "slug": slug, "ad": ad, "tur": tur, "bolum": bolum, "sezon": (no - 1) // 10 + 1, "acilis": t[no].isoformat()}
        d.update(ICERIK.get(slug, {})); out.append(d)
    for slug, ad, tur in M.OZEL:
        d = {"no": 0, "slug": slug, "ad": ad, "tur": tur, "bolum": "", "sezon": 0, "acilis": VTR.OZEL_ACILIS.isoformat(), "ozel": True}
        d.update(ICERIK[slug]); out.append(d)
    return out

TESTLER = tum_testler()
SITE, SURUM, E = I.SITE, I.SURUM, html.escape
yaz = I.yaz

def js_veri():
    tl = []
    for t in TESTLER:
        d = {k: t[k] for k in ("no", "slug", "ad", "tur", "bolum", "sezon", "acilis")}
        for k in ("kanca", "sorular", "sonuclar", "seviyeler", "birim", "ozel"):
            if k in t: d[k] = t[k]
        tl.append(d)
    o = {"sezonlar": M.SEZONLAR, "turAd": M.TUR_AD, "bolum": M.BOLUM, "testler": tl, "dil": "en"}
    yaz("en/testler/veri.js", "/* generated: _kaynak/en/insa_en.py */\nwindow.ASKV=" + json.dumps(o, ensure_ascii=False, separators=(",", ":")) + ";\n")

def sayfa(baslik, aciklama, url, gorsel, govde, sayfa_tur, slug="", aktif="", tr_url=None):
    tr_url = tr_url if tr_url is not None else url[3:]
    akt = lambda k: ' class="aktif"' if aktif in k else ''
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(baslik)}</title>
<meta name="description" content="{E(aciklama)}">
<meta property="og:title" content="{E(baslik)}">
<meta property="og:description" content="{E(aciklama)}">
<meta property="og:image" content="{SITE}{gorsel}">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta property="og:url" content="{SITE}{url}">
<meta property="og:type" content="website">
<meta property="og:locale" content="en_GB">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:site" content="@askonomikitap">
<link rel="canonical" href="{SITE}{url}">
<link rel="alternate" hreflang="en" href="{SITE}{url}"><link rel="alternate" hreflang="tr" href="{SITE}{tr_url}">
<link rel="icon" href="/favicon-32.png" sizes="32x32" type="image/png"><link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,500;0,9..144,600;1,9..144,400&family=Crimson+Pro:ital,wght@0,400;0,500;1,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/testler/stil.css?v={SURUM}">
<style>.dil-sec{{margin-left:10px;padding:3px 10px;border:1.5px solid currentColor;border-radius:999px;font-size:.85em;font-weight:600;white-space:nowrap}}</style>
<script defer src="https://cloud.umami.is/script.js" data-website-id="e2b973cb-62c0-4a6a-b9de-1fd1de7402e8"></script>
</head>
<body data-sayfa="{sayfa_tur}" data-slug="{slug}" data-dil="en">
<header><div class="wrap"><a class="logo" href="/?lang=en"><img src="/img/simge.png" alt="">AŞKONOMİ</a><button class="menu-btn" aria-label="Menu" aria-expanded="false"><i></i><i></i><i></i></button><nav><a href="/?lang=en" class="sadece-mobil">Home</a><a href="/en/testler/"{akt(('testler',))}>Quizzes</a><a href="/en/kimya/"{akt(('kimya',))}>Chemistry</a><a href="/en/oyunlar/"{akt(('oyunlar','grafik'))}>Games</a><a href="/?lang=en#takip">Follow</a><a class="dil-sec" href="{tr_url}" hreflang="tr" lang="tr" title="Türkçe">TR</a></nav></div></header>
<main>{govde}</main>
<footer><div class="wrap"><span>© 2026 Prof. Dr. Mehmet Şahin · askonomi.com</span><span>The quizzes are for fun and reflection; they are not a psychological diagnosis. The book is currently available in Turkish. <a href="/kvkk.html" lang="tr">Privacy notice (Turkish)</a></span></div></footer>
<script>(function(){{var h=document.querySelector('header'),b=h&&h.querySelector('.menu-btn');if(!b)return;b.onclick=function(){{var a=h.classList.toggle('menu-acik');b.setAttribute('aria-expanded',a)}};document.addEventListener('keydown',function(e){{if(e.key==='Escape'){{h.classList.remove('menu-acik');b.setAttribute('aria-expanded','false')}}}})}})();</script>
<script src="/en/testler/veri.js?v={SURUM}"></script>
<script src="/en/testler/motor.js?v={SURUM}"></script>
</body></html>
"""

def merkez_sayfa():
    govde = """<div class="wrap"><div class="ust-alan"><span class="etiket">The Aşkonomi Quiz Series</span>
<h1>40 quizzes.<br><em>4 seasons.</em></h1>
<p class="giris">A series that tests the heart's decisions in the language of economics. A new quiz opens every Monday and Thursday. Finish five quizzes to unlock your Aşkonomi Report Card.</p></div>
<div class="ozel-serit"><a href="/en/kimya/"><span class="etiket">New · Special section</span><b>The Chemistry of Love</b><span>Interactive body map, a phase quiz and 6 myths</span></a><a href="/en/oyunlar/"><span class="etiket">New · Games</span><b>Aşkonomi Games</b><span>Trust game, matching village, expectation budget and more</span></a></div>
<div id="uygulama"><noscript>You need JavaScript to take the quizzes.</noscript></div></div>"""
    yaz("en/testler/index.html", sayfa("Aşkonomi Quizzes · 40 quizzes, 4 seasons", "Which economic idea explains your love life? 40 quizzes, 4 seasons. A new quiz every Monday and Thursday.",
                                      "/en/testler/", "/og/en/testler.jpg", govde, "merkez", aktif="testler"))

def sonuclar(t):
    if "sonuclar" in t: return [(k, v[0], v[1], v[2]) for k, v in t["sonuclar"].items()]
    if "seviyeler" in t: return [(f"s{i}", s[1], s[2], t.get("bolum", "")) for i, s in enumerate(t["seviyeler"])]
    return []

def test_sayfalari():
    for t in TESTLER:
        no = f"{t['no']:02d}"; tur = M.TUR_AD.get(t["tur"], ""); kanca = t.get("kanca", "")
        ust = f"The Chemistry of Love · {E(tur)}" if t.get("ozel") else f"Quiz {no} · {E(tur)} · Season {t['sezon']}"
        govde = f"""<div class="wrap test-sayfa"><div class="test-ust"><span class="etiket">{ust}</span>
<h1>{E(t['ad'])}</h1>{f'<p class="kanca">{E(kanca)}</p>' if kanca else ''}</div>
<div id="uygulama"><noscript>You need JavaScript to take this quiz.</noscript></div></div>"""
        akt = "kimya" if t.get("ozel") else "testler"
        yaz(f"en/test/{t['slug']}/index.html", sayfa(t["ad"] + " · Aşkonomi", kanca or f"Aşkonomi quiz series, quiz {no}.", f"/en/test/{t['slug']}/", f"/og/en/{t['slug']}.jpg", govde, "test", t["slug"], akt))
        for k, ad, metin, bolum in sonuclar(t):
            g = f"""<div class="wrap test-sayfa"><div class="test-ust"><span class="etiket">Aşkonomi · {'The Chemistry of Love' if t.get('ozel') else 'Quiz ' + no}</span><h1>{E(t['ad'])}</h1></div>
<div class="kart sonuc"><span class="bolumno">Your friend's result</span><h2>{E(ad)}</h2><p>{E(metin)}</p>
{f'<p class="not">In the book: Chapter {int(bolum)} · {E(M.BOLUM[bolum])}</p>' if bolum else ''}
<p class="not" id="kendi"></p>
<p style="margin-top:18px"><a class="btn" href="/en/test/{t['slug']}/">Take it yourself →</a> <a class="btn ikincil" href="/en/testler/">All quizzes</a></p></div></div>"""
            yaz(f"en/test/{t['slug']}/s/{k}/index.html", sayfa(f"“{ad}” · {t['ad']}", f"My result: {ad}. What's yours? Aşkonomi quiz series.",
                                                            f"/en/test/{t['slug']}/s/{k}/", f"/og/en/{t['slug']}-{k}.jpg", g, "sonuc", t["slug"], akt))

def oku(ad):
    with open(os.path.join(BURA, ad), encoding="utf-8") as f: return f.read().replace("{SURUM}", SURUM)

def ozel_sayfalar():
    yaz("en/kimya/index.html", sayfa("The Chemistry of Love · Aşkonomi", "What happens in your brain, heart and body when you fall in love? An interactive body map, a phase quiz and 6 myths, with sources.",
                                     "/en/kimya/", "/og/en/kimya.jpg", oku("govde_kimya.html"), "kimya", aktif="kimya"))
    yaz("en/grafik/index.html", sayfa("Your Love Chart · Aşkonomi", "Draw the value–time curve of your relationship and get a market commentary: rally, bubble, recovery or sideways.",
                                      "/en/grafik/", "/og/en/grafik.jpg", oku("govde_grafik.html"), "grafik", aktif="oyunlar"))

OYUN_SAYFA = [
    ("merkez", "Games · Aşkonomi", "Play with the book's economic ideas: a trust game, a matching village, an expectation budget, a swipe simulator and Türkiye's love map."),
    ("guven", "The Trust Game · Aşkonomi", "Ten rounds with one partner. Every token you entrust is tripled. How is trust capital built, and how does it melt away?"),
    ("eslesme", "The Matching Village · Aşkonomi", "Match an eight-person village with a Nobel-winning algorithm. How does who proposes change the outcome?"),
    ("beklenti", "The Expectation Budget · Aşkonomi", "What do you expect from your dream partner? Compare it with what one real person can offer and see your expectation inflation."),
    ("kaydirma", "The Swipe Simulator · Aşkonomi", "Swipe thirty profiles and watch your attention melt, with your own data."),
    ("hikaye", "Türkiye's Family Story · Aşkonomi", "A six-scene scrolling map: from 2008 to 2025 households shrank, marriage was delayed, divorce rose and births fell. With TurkStat data."),
    ("harita", "Türkiye's Love Map · Aşkonomi", "Marriage, divorce, age at first marriage and children in 81 provinces, 2014–2025, province by province. With TurkStat data."),
]

def oyun_sayfalari():
    for slug, baslik, acik in OYUN_SAYFA:
        yol = os.path.join(BURA, "oyunlar", slug + ".html")
        if not os.path.exists(yol): print("  skipped (no EN template):", slug); continue
        url = "/en/oyunlar/" if slug == "merkez" else f"/en/oyunlar/{slug}/"
        hedef = "en/oyunlar/index.html" if slug == "merkez" else f"en/oyunlar/{slug}/index.html"
        og = "/og/en/oyunlar.jpg" if slug == "merkez" else f"/og/en/oyun-{slug}.jpg"
        yaz(hedef, sayfa(baslik, acik, url, og, oku(os.path.join("oyunlar", slug + ".html")), "oyun", slug, aktif="oyunlar"))

# ---------- OG images (English) ----------
F, W, H = I.F, I.W, I.H
MUREKKEP, SOLUK, BORDO = I.MUREKKEP, I.SOLUK, I.BORDO

def og_test(t):
    no = f"{t['no']:02d}"; tur = M.TUR_AD.get(t['tur'], '')
    im, d = I.taban((f"THE CHEMISTRY OF LOVE · {tur}" if t.get("ozel") else f"QUIZ {no} · {tur} · SEASON {t['sezon']}").upper())
    f, sat = I.sigdir(d, t["ad"], "Fraunces-SemiBold", 76, 46, W - 140, 3)
    y = 200 + (3 - len(sat)) * 24
    for s in sat: d.text((64, y), s, font=f, fill=MUREKKEP); y += int(f.size * 1.12)
    dt = datetime.date.fromisoformat(t["acilis"])
    alt = t.get("kanca") or (f"Opens {dt.strftime('%A')}, {dt.day} {dt.strftime('%B')}." if t["tur"] != "karne" else "Finish five quizzes to unlock your report card.")
    fa, sa = I.sigdir(d, alt, "CrimsonPro-Italic", 32, 24, W - 140, 2); y += 16
    for s in sa: d.text((64, y), s, font=fa, fill=SOLUK); y += int(fa.size * 1.2)
    d.text((64, H - 78), "askonomi.com/en", font=F("Fraunces-Medium", 24), fill=BORDO)
    tag = "TAKE IT, SHARE YOUR RESULT"; ft = F("Fraunces-Medium", 20)
    d.text((W - 64 - d.textlength(tag, font=ft), H - 74), tag, font=ft, fill=MUREKKEP)
    return im

def og_sonuc(t, ad):
    im, d = I.taban((f"THE CHEMISTRY OF LOVE · {t['ad']}" if t.get("ozel") else f"QUIZ {t['no']:02d} · {t['ad']}").upper()[:80])
    d.text((64, 186), "My result:", font=F("CrimsonPro-Italic", 38), fill=SOLUK)
    f, sat = I.sigdir(d, ad, "Fraunces-SemiBold", 92, 52, W - 140, 2); y = 246
    for s in sat: d.text((64, y), s, font=f, fill=BORDO); y += int(f.size * 1.1)
    fa, sa = I.sigdir(d, t["ad"], "Fraunces-Medium", 30, 22, W - 140, 2); y += 18
    for s in sa: d.text((64, y), s, font=fa, fill=MUREKKEP); y += int(fa.size * 1.25)
    d.text((64, H - 78), "What's yours?  askonomi.com/en", font=F("Fraunces-Medium", 26), fill=BORDO)
    return im

def og_baslik(ust, s1, s2, alt, adres):
    im, d = I.taban(ust)
    d.text((64, 190), s1, font=F("Fraunces-SemiBold", 104), fill=MUREKKEP)
    d.text((64, 306), s2, font=F("Fraunces-Italic", 104), fill=BORDO)
    fa, sa = I.sigdir(d, alt, "CrimsonPro-Italic", 34, 24, W - 140, 2); y = 446
    for s in sa: d.text((64, y), s, font=fa, fill=SOLUK); y += int(fa.size * 1.2)
    d.text((64, H - 78), adres, font=F("Fraunces-Medium", 24), fill=BORDO)
    return im

def gorseller():
    k = I.kaydet_jpg
    k(og_baslik("QUIZ SERIES", "40 quizzes.", "4 seasons.", "Which economic idea explains your love life?", "askonomi.com/en"), "og/en/testler.jpg")
    k(og_baslik("SPECIAL SECTION", "The chemistry", "of love.", "What happens in your brain, heart and body when you fall in love?", "askonomi.com/en"), "og/en/kimya.jpg")
    k(og_baslik("INTERACTIVE TOOL", "Your love", "chart.", "Draw your curve, get a market commentary.", "askonomi.com/en"), "og/en/grafik.jpg")
    for slug, baslik, acik in OYUN_SAYFA:
        ad = baslik.split(" · ")[0]
        if slug == "merkez": k(og_baslik("GAMES", "Aşkonomi", "games.", acik, "askonomi.com/en"), "og/en/oyunlar.jpg"); continue
        w = ad.split(" "); yarim = (len(w) + 1) // 2
        k(og_baslik("GAME", " ".join(w[:yarim]), " ".join(w[yarim:]) + ".", acik, "askonomi.com/en"), f"og/en/oyun-{slug}.jpg")
    for t in TESTLER:
        k(og_test(t), f"og/en/{t['slug']}.jpg")
        for kk, ad, _, _ in sonuclar(t): k(og_sonuc(t, ad), f"og/en/{t['slug']}-{kk}.jpg")

def site_haritasi():
    bugun = datetime.date.today().isoformat()
    u = ["/en/testler/", "/en/kimya/", "/en/grafik/", "/en/oyunlar/"] + [f"/en/oyunlar/{s}/" for s, _, _ in OYUN_SAYFA if s != "merkez"] + \
        [f"/en/test/{t['slug']}/" for t in TESTLER if t.get("sorular") or t["tur"] == "karne"]
    yaz("en/sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' +
        "".join(f"<url><loc>{SITE}{x}</loc><lastmod>{bugun}</lastmod></url>" for x in u) + "</urlset>\n")

if __name__ == "__main__":
    js_veri(); merkez_sayfa(); test_sayfalari(); ozel_sayfalar(); oyun_sayfalari(); gorseller(); site_haritasi()
    print("done (en):", len(TESTLER), "quizzes;", sum(len(sonuclar(t)) for t in TESTLER), "result pages")
