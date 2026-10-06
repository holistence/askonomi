# -*- coding: utf-8 -*-
# Aşkonomi test serisi — içerik kaynağı.
# DURUM: 39 test, Aşkonomi v45 metniyle karşılaştırıldı (6 Ekim 2026).
# tur: profil | senaryo | mit | cift | hesap | nesil | karne

import datetime as _dt

SEZONLAR = [
    {"no": 1, "ad": "Piyasaya Giriş", "alt": "Kim, kimi, neden seçer?"},
    {"no": 2, "ad": "Sözleşme", "alt": "Evlilik, ev ve emek"},
    {"no": 3, "ad": "Kriz", "alt": "İlişki sarsılınca"},
    {"no": 4, "ad": "Dijital Çağ", "alt": "Kaydırılan kalpler"},
]

TUR_AD = {"profil": "Profil", "senaryo": "Ne yapardın?", "mit": "Mit mi, gerçek mi?", "cift": "Çift testi",
          "hesap": "Hesaplayıcı", "nesil": "Nesil testi", "karne": "Final"}

BOLUM = {
    "01": "Aşk Nedir?", "02": "Aşk ve Rasyonalite", "03": "Kıtlık", "04": "İhtiyaç, Arzu ve Tercih",
    "05": "Aşk Piyasası", "06": "Sinyaller", "07": "Güzellik Ekonomisi", "08": "Para ve Servet",
    "09": "Denklik ve Benzerlik", "15": "Evliliğin Ekonomisi", "16": "Görünmeyen Emek",
    "17": "Çocukların Ekonomisi", "18": "Çok Eşlilik", "19": "Kıskançlık Ekonomisi",
    "22": "Boşanmanın Ekonomisi", "23": "Aldatma ve İhanet Ekonomisi", "24": "Güven Sermayesi",
    "25": "İlişkiye Yatırım", "26": "Fırsat Maliyeti", "27": "Seçenek Bolluğu", "28": "Beklenti Enflasyonu",
    "29": "Modern Evlilik", "30": "Tinder’dan Önce ve Sonra", "31": "Aşkın Endüstrisi",
    "32": "Küreselleşen Mahremiyet", "33": "Yalnızlığın Ekonomisi", "34": "Geleceğin Aşk Ekonomisi",
}

# ---- Başlık listesi (onaylı) ----
LISTE = [
    # no, slug, başlık, tür, bölüm
    (1, "fiyatin-ne", "Aşk piyasasında fiyatın ne?", "profil", "05"),
    (2, "kacan-mi-kovalanan-mi", "Kaçan mısın, kovalanan mı?", "profil", "03"),
    (3, "kalp-mi-akil-mi", "Kalbin mi hesap yapıyor, aklın mı?", "senaryo", "02"),
    (4, "ilk-bulusma-sinyali", "İlk buluşmada verdiğin sinyal aslında ne diyor?", "profil", "06"),
    (5, "guzellik-mitleri", "Güzellik hakkında inandığın 6 şeyden kaçı doğru?", "mit", "07"),
    (6, "para-konusulunca", "Para konuşulunca ilişkinde ne oluyor?", "senaryo", "08"),
    (7, "benzer-mi-zit-mi", "Kendine benzeyeni mi seçiyorsun, zıttını mı?", "profil", "09"),
    (8, "ihtiyac-arzu-tercih", "Sevgilin ihtiyaç mı, arzu mu, tercih mi?", "profil", "04"),
    (9, "askin-alti-tanimi", "Aşkın 6 tanımından hangisi senin?", "profil", "01"),
    (10, "birbirinizi-fiyatlamak", "Birbirinizi ne kadar doğru “fiyatlıyorsunuz”?", "cift", "05"),
    (11, "evlilik-ne", "Evlilik senin için yatırım mı, sigorta mı, ortaklık mı?", "profil", "15"),
    (12, "gorunmeyen-emek", "Görünmeyen Emek Hesaplayıcı: Evde kimin mesaisi yazılmıyor?", "hesap", "16"),
    (13, "ev-isini-kim-yapiyor", "Ev işini kim yaptığını sanıyor, kim yapıyor?", "cift", "16"),
    (14, "cocugun-maliyeti", "Bir çocuğun gerçek maliyeti: 6 iddia", "mit", "17"),
    (15, "kiskanclik", "Kıskançlığın koruma mı, sahiplenme mi?", "profil", "19"),
    (16, "cok-eslilik-mitleri", "Çok eşlilik tarihi: Mit mi, gerçek mi?", "mit", "18"),
    (17, "iliski-sozlesmesi", "İlişkin bir sözleşme olsaydı hangi maddesi bozuk olurdu?", "senaryo", "15"),
    (18, "bosanmanin-faturasi", "Boşanmanın gerçek faturası", "mit", "22"),
    (19, "evliligin-yuzyili", "Evliliğin hangi yüzyıldan?", "nesil", "29"),
    (20, "ayni-evlilik", "İkiniz aynı evliliği mi hayal ediyorsunuz?", "cift", "15"),
    (21, "beklenti-enflasyonu", "Beklenti Enflasyonu Endeksin kaç?", "hesap", "28"),
    (22, "iliski-getirisi", "İlişki Yatırım Getirisi hesaplayıcı", "hesap", "25"),
    (23, "batik-maliyet", "Batık maliyet: Bitmesi gereken bir ilişkide misin?", "senaryo", "25"),
    (24, "neye-mal-oldu", "Bu ilişki sana neye mal oldu?", "hesap", "26"),
    (25, "cok-secenek", "Çok seçenek seni mutsuz mu ediyor?", "profil", "27"),
    (26, "guven-sermayesi", "Güven Sermayen artıda mı, ekside mi?", "hesap", "24"),
    (27, "aldatma-mitleri", "Aldatma hakkında 6 yaygın inanç: Kaçı doğru?", "mit", "23"),
    (28, "affetmek-guvenmek", "Affetmek, güvenmek, uzlaşmak: Hangisinde takılıyorsun?", "profil", "24"),
    (29, "kriz-senaryolari", "Ne yapardın? 8 kriz senaryosu", "senaryo", "22"),
    (30, "kriz-aninda", "Kriz anında aynı tarafta mısınız?", "cift", "24"),
    (31, "tinder-oncesi-sonrasi", "Tinder öncesi mi aşıksın, sonrası mı?", "nesil", "30"),
    (32, "hangi-on-yil", "Aşk hayatın hangi on yıla ait?", "nesil", "29"),
    (33, "kaydirma-ekonomisi", "Kaydırma ekonomisi: Uygulamalar hakkında 6 iddia", "mit", "30"),
    (34, "ask-endustrisi", "Aşk endüstrisi seni ne kadar satın aldı?", "hesap", "31"),
    (35, "yalnizligin-fiyati", "Yalnızlığın fiyatı hakkında ne biliyorsun?", "mit", "33"),
    (36, "yalniz-misin", "Yalnız mısın, yalnızlığı mı seçtin?", "profil", "33"),
    (37, "ask-icin-ulke", "Aşk için ülke değiştirir miydin?", "senaryo", "32"),
    (38, "goruldu-ekonomisi", "“Görüldü” ekonomisi: Mesajların ne sinyal veriyor?", "senaryo", "06"),
    (39, "2040-aski", "2040’ın aşkına hazır mısın?", "profil", "34"),
    (40, "karne", "Aşkonomi Karnesi", "karne", ""),
]

# ---- Yayın takvimi: ilk 6 test hemen, sonra her Pazartesi ve Perşembe ----
ILK_ACILIS = _dt.date(2026, 10, 6)
def takvim():
    d = {}
    for no in range(1, 7):
        d[no] = ILK_ACILIS
    gun = _dt.date(2026, 10, 12)  # Pazartesi
    no = 7
    while no <= 39:
        if gun.weekday() in (0, 3):
            d[no] = gun; no += 1
        gun += _dt.timedelta(days=1)
    d[40] = d[39]
    return d

# ---- İçerikler: kitabın v45 metnine dayanır; kaynak sayfaları _kaynak/raporlar/ ----
import importlib.util as _iu, os as _os
ICERIK = {}
for _n in (1, 2, 3, 4):
    _sp = _iu.spec_from_file_location(f"icerik_s{_n}", _os.path.join(_os.path.dirname(__file__), f"icerik_s{_n}.py"))
    _m = _iu.module_from_spec(_sp); _sp.loader.exec_module(_m); ICERIK.update(_m.ICERIK)


def tum_testler():
    t = takvim()
    out = []
    for no, slug, ad, tur, bolum in LISTE:
        sezon = (no - 1) // 10 + 1
        d = {"no": no, "slug": slug, "ad": ad, "tur": tur, "bolum": bolum, "sezon": sezon,
             "acilis": t[no].isoformat()}
        if slug in ICERIK:
            d.update(ICERIK[slug])
        out.append(d)
    return out
