# -*- coding: utf-8 -*-
"""Aşkonomi test serisini üretir: veri.js, merkez sayfa, test sayfaları, sonuç paylaşım sayfaları, OG görselleri.
Çalıştır:  python3 _kaynak/insa.py   (depo kökünden)"""
import json, os, html, datetime, textwrap
from PIL import Image, ImageDraw, ImageFont
import veri as V

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONT = os.path.join(KOK, "_kaynak", "font")
SITE = "https://askonomi.com"
SURUM = datetime.datetime.now().strftime("%Y%m%d%H%M")

def yaz(yol, icerik, ikili=False):
    p = os.path.join(KOK, yol); os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "wb" if ikili else "w", **({} if ikili else {"encoding": "utf-8"})) as f: f.write(icerik)

E = html.escape
TESTLER = V.tum_testler()

# ---------- veri.js ----------
def js_veri():
    tl = []
    for t in TESTLER:
        d = {k: t[k] for k in ("no", "slug", "ad", "tur", "bolum", "sezon", "acilis")}
        for k in ("kanca", "sorular", "sonuclar", "seviyeler"):
            if k in t: d[k] = t[k]
        if t["tur"] == "mit": d["bolum"] = t.get("bolum", t["bolum"])
        tl.append(d)
    o = {"sezonlar": V.SEZONLAR, "turAd": V.TUR_AD, "bolum": V.BOLUM, "testler": tl}
    yaz("testler/veri.js", "/* otomatik üretildi: _kaynak/insa.py */\nwindow.ASKV=" + json.dumps(o, ensure_ascii=False, separators=(",", ":")) + ";\n")

# ---------- sayfa iskeleti ----------
def sayfa(baslik, aciklama, url, gorsel, govde, sayfa_tur, slug="", aktif=""):
    return f"""<!doctype html>
<html lang="tr">
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
<meta property="og:locale" content="tr_TR">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:site" content="@askonomikitap">
<link rel="canonical" href="{SITE}{url}">
<link rel="icon" href="/favicon-32.png" sizes="32x32" type="image/png"><link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,500;0,9..144,600;1,9..144,400&family=Crimson+Pro:ital,wght@0,400;0,500;1,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/testler/stil.css?v={SURUM}">
<script defer src="https://cloud.umami.is/script.js" data-website-id="e2b973cb-62c0-4a6a-b9de-1fd1de7402e8"></script>
</head>
<body data-sayfa="{sayfa_tur}" data-slug="{slug}">
<header><div class="wrap"><a class="logo" href="/"><img src="/img/simge.png" alt="">AŞKONOMİ</a><nav><a href="/testler/"{' class="aktif"' if aktif=='testler' else ''}>Testler</a><a href="/#takip">Takip et</a></nav></div></header>
<main>{govde}</main>
<footer><div class="wrap"><span>© 2026 Mehmet Şahin · askonomi.com</span><span>Testler eğlence ve düşünme amaçlıdır; psikolojik tanı aracı değildir. <a href="/kvkk.html">KVKK</a></span></div></footer>
<script src="/testler/veri.js?v={SURUM}"></script>
<script src="/testler/motor.js?v={SURUM}"></script>
</body></html>
"""

def merkez_sayfa():
    acik = sum(1 for t in TESTLER if t["tur"] != "karne" and t["acilis"] <= datetime.date.today().isoformat() and t.get("sorular"))
    govde = """<div class="wrap"><div class="ust-alan"><span class="etiket">Aşkonomi Test Serisi</span>
<h1>40 test.<br><em>4 sezon.</em></h1>
<p class="giris">Kalbin kararlarını iktisadın diliyle sınayan bir seri. Her Pazartesi ve Perşembe yeni bir test açılıyor. Beş test çöz, Aşkonomi Karnen açılsın.</p></div>
<div id="uygulama"><noscript>Testleri çözmek için JavaScript gerekiyor.</noscript></div></div>"""
    yaz("testler/index.html", sayfa("Aşkonomi Testleri · 40 test, 4 sezon", "Aşk hayatını hangi iktisadi kavram anlatıyor? 40 test, 4 sezon. Her Pazartesi ve Perşembe yeni test.",
                                   "/testler/", "/og/testler.jpg", govde, "merkez", aktif="testler"))

def test_sayfalari():
    for t in TESTLER:
        no = f"{t['no']:02d}"
        tur = V.TUR_AD.get(t["tur"], "")
        kanca = t.get("kanca", "")
        govde = f"""<div class="wrap test-sayfa"><div class="test-ust"><span class="etiket">Test {no} · {E(tur)} · Sezon {t['sezon']}</span>
<h1>{E(t['ad'])}</h1>{f'<p class="kanca">{E(kanca)}</p>' if kanca else ''}</div>
<div id="uygulama"><noscript>Bu testi çözmek için JavaScript gerekiyor.</noscript></div></div>"""
        acik = kanca or ("Aşkonomi test serisi, test " + no + ".")
        yaz(f"test/{t['slug']}/index.html", sayfa(t["ad"] + " · Aşkonomi", acik, f"/test/{t['slug']}/", f"/og/{t['slug']}.jpg", govde, "test", t["slug"], "testler"))
        # sonuç paylaşım sayfaları
        for k, ad, metin, bolum in sonuclar(t):
            g = f"""<div class="wrap test-sayfa"><div class="test-ust"><span class="etiket">Aşkonomi · Test {no}</span><h1>{E(t['ad'])}</h1></div>
<div class="kart sonuc"><span class="bolumno">Arkadaşının sonucu</span><h2>{E(ad)}</h2><p>{E(metin)}</p>
{f'<p class="not">Kitapta: Bölüm {int(bolum)} · {E(V.BOLUM[bolum])}</p>' if bolum else ''}
<p class="not" id="kendi"></p>
<p style="margin-top:18px"><a class="btn" href="/test/{t['slug']}/">Sen de çöz →</a> <a class="btn ikincil" href="/testler/">Tüm testler</a></p></div></div>"""
            yaz(f"test/{t['slug']}/s/{k}/index.html", sayfa(f"“{ad}” · {t['ad']}", f"Benim sonucum: {ad}. Seninki ne? Aşkonomi test serisi.",
                                                         f"/test/{t['slug']}/s/{k}/", f"/og/{t['slug']}-{k}.jpg", g, "sonuc", t["slug"], "testler"))

def sonuclar(t):
    if "sonuclar" in t:
        return [(k, v[0], v[1], v[2]) for k, v in t["sonuclar"].items()]
    if "seviyeler" in t:
        return [(f"s{i}", s[1], s[2], t.get("bolum", "")) for i, s in enumerate(t["seviyeler"])]
    return []

# ---------- OG görselleri ----------
W, H = 1200, 630
ZEMIN, MUREKKEP, SOLUK, BORDO, CIZGI = (242, 235, 224), (38, 32, 40), (107, 96, 112), (179, 38, 58), (216, 204, 187)
def F(ad, b): return ImageFont.truetype(os.path.join(FONT, ad + ".ttf"), b)
SIMGE = Image.open(os.path.join(KOK, "img", "simge.png")).convert("RGBA").resize((72, 72), Image.LANCZOS)
mask = Image.new("L", (72, 72), 0); ImageDraw.Draw(mask).ellipse([0, 0, 71, 71], fill=255)

def sar(d, metin, font, genislik):
    sozler, satirlar, s = metin.split(), [], ""
    for w in sozler:
        dene = (s + " " + w).strip()
        if d.textlength(dene, font=font) <= genislik: s = dene
        else: satirlar.append(s); s = w
    satirlar.append(s); return satirlar

def sigdir(d, metin, ad, buyuk, kucuk, genislik, max_satir):
    for b in range(buyuk, kucuk - 1, -2):
        f = F(ad, b); s = sar(d, metin, f, genislik)
        if len(s) <= max_satir: return f, s
    return f, s[:max_satir]

def tr_upper(x): return x.replace("i","İ").replace("ı","I").upper()

AYLAR=["Ocak","Şubat","Mart","Nisan","Mayıs","Haziran","Temmuz","Ağustos","Eylül","Ekim","Kasım","Aralık"]
GUNLER=["Pazartesi","Salı","Çarşamba","Perşembe","Cuma","Cumartesi","Pazar"]

def taban(ust_metin):
    im = Image.new("RGB", (W, H), ZEMIN); d = ImageDraw.Draw(im)
    d.rectangle([28, 28, W - 29, H - 29], outline=CIZGI, width=2)
    d.rectangle([0, H - 14, W, H], fill=BORDO)
    im.paste(SIMGE, (64, 60), mask)
    d.text((152, 76), "AŞKONOMİ", font=F("Fraunces-SemiBold", 30), fill=MUREKKEP)
    d.text((152, 112), ust_metin, font=F("Fraunces-Medium", 18), fill=SOLUK)
    return im, d

def og_test(t):
    no = f"{t['no']:02d}"
    im, d = taban(tr_upper(f"TEST {no} · {V.TUR_AD.get(t['tur'],'')} · SEZON {t['sezon']}"))
    f, sat = sigdir(d, t["ad"], "Fraunces-SemiBold", 76, 46, W - 140, 3)
    y = 200 + (3 - len(sat)) * 24
    for s in sat:
        d.text((64, y), s, font=f, fill=MUREKKEP); y += int(f.size * 1.12)
    dt = datetime.date.fromisoformat(t["acilis"])
    alt = t.get("kanca") or (f"{dt.day} {AYLAR[dt.month-1]} {GUNLER[dt.weekday()]} açılıyor." if t["tur"] != "karne" else "Beş test çöz, karnen açılsın.")
    fa, sa = sigdir(d, alt, "CrimsonPro-Italic", 32, 24, W - 140, 2)
    y += 16
    for s in sa: d.text((64, y), s, font=fa, fill=SOLUK); y += int(fa.size * 1.2)
    d.text((64, H - 78), "askonomi.com/testler", font=F("Fraunces-Medium", 24), fill=BORDO)
    tag = "ÇÖZ, SONUCUNU PAYLAŞ"
    ft = F("Fraunces-Medium", 20); d.text((W - 64 - d.textlength(tag, font=ft), H - 74), tag, font=ft, fill=MUREKKEP)
    return im

def og_sonuc(t, ad):
    im, d = taban(tr_upper(f"TEST {t['no']:02d} · {t['ad']}")[:80])
    d.text((64, 186), "Sonucum:", font=F("CrimsonPro-Italic", 38), fill=SOLUK)
    f, sat = sigdir(d, ad, "Fraunces-SemiBold", 92, 52, W - 140, 2)
    y = 246
    for s in sat: d.text((64, y), s, font=f, fill=BORDO); y += int(f.size * 1.1)
    fa, sa = sigdir(d, t["ad"], "Fraunces-Medium", 30, 22, W - 140, 2)
    y += 18
    for s in sa: d.text((64, y), s, font=fa, fill=MUREKKEP); y += int(fa.size * 1.25)
    d.text((64, H - 78), "Seninki ne?  askonomi.com", font=F("Fraunces-Medium", 26), fill=BORDO)
    return im

def og_merkez():
    im, d = taban("TEST SERİSİ")
    d.text((64, 190), "40 test.", font=F("Fraunces-SemiBold", 110), fill=MUREKKEP)
    d.text((64, 310), "4 sezon.", font=F("Fraunces-Italic", 110), fill=BORDO)
    d.text((64, 450), "Aşk hayatını hangi iktisadi kavram anlatıyor?", font=F("CrimsonPro-Italic", 36), fill=SOLUK)
    d.text((64, H - 78), "askonomi.com/testler", font=F("Fraunces-Medium", 24), fill=BORDO)
    return im

def kaydet_jpg(im, yol):
    p = os.path.join(KOK, yol); os.makedirs(os.path.dirname(p), exist_ok=True); im.save(p, "JPEG", quality=86, optimize=True, progressive=True)

def gorseller():
    kaydet_jpg(og_merkez(), "og/testler.jpg")
    for t in TESTLER:
        kaydet_jpg(og_test(t), f"og/{t['slug']}.jpg")
        for k, ad, _, _ in sonuclar(t):
            kaydet_jpg(og_sonuc(t, ad), f"og/{t['slug']}-{k}.jpg")

def site_haritasi():
    bugun = datetime.date.today().isoformat()
    u = ["/", "/kvkk.html", "/testler/"] + [f"/test/{t['slug']}/" for t in TESTLER if t.get("sorular") or t["tur"] == "karne"]
    yaz("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' +
        "".join(f"<url><loc>{SITE}{x}</loc><lastmod>{bugun}</lastmod></url>" for x in u) + "</urlset>\n")

if __name__ == "__main__":
    js_veri(); merkez_sayfa(); test_sayfalari(); gorseller(); site_haritasi()
    print("tamam:", len(TESTLER), "test;", sum(len(sonuclar(t)) for t in TESTLER), "sonuç sayfası")
