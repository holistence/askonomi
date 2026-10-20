# -*- coding: utf-8 -*-
"""Türkiye'nin aşk haritası için veri üretir: oyunlar/harita/veri.js
Kaynaklar: _kaynak/harita/tuik/ (TÜİK il tabloları), il nüfusu (TÜİK ADNKS, araştırma arşivi), dogum_verisi.csv, hane_verisi.csv, iller.json.
Kaba hızlar = olay sayısı / yıl ortası nüfus × 1000 (yıl ortası = iki yıl sonu nüfusunun ortalaması).
Bu yöntem TÜİK'in resmi kaba boşanma hızı tablosunu (2014–2022, 729 il-yıl) ortalama 0,002 farkla tekrar ediyor.
Çalıştır: python3 _kaynak/harita/tuik_isle.py (depo kökünden)"""
import os, sys, csv, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tuik_oku as T

KOK = T.KOK
DEPO = os.path.dirname(os.path.dirname(KOK))
YIL = list(range(2014, 2026))
t = lambda ad: os.path.join(KOK, 'tuik', ad)

# ---- nüfus (yıl sonu, ADNKS) ----
NUF = {}
for r in csv.DictReader(open(os.path.join(KOK, 'nufus.csv'), encoding='utf-8')):
    NUF[(int(r['plaka']), int(r['yil']))] = float(r['nufus'])
def orta(p, y): return (NUF[(p, y)] + NUF[(p, y - 1)]) / 2

ev = T.ng(t('_l_ve__l_e_Evlenme_Say_s__TRDF_EVLENME_IL_ILCE1.0.xlsx'), ['Zaman'])
bo = T.ng(t('_l_ve__l_e_Bo_anma_Say_s__TRDF_BOSANMA_IL_ILCE1.0.xlsx'), ['Zaman'])
ilk = T.satirlar(t('_l_ve_cinsiyete_g_re_ortalama_ilk_evlenme_ya__.xls'))
iy = ilk[3]
ILK = {}
for r in ilk:
    p = 0 if str(r[0]).strip() == 'Türkiye' else T.plaka(r[0])
    if p is None: continue
    for j, c in enumerate(iy):
        y = str(c)[:4]
        if y.isdigit() and int(y) in YIL:
            ILK[(p, int(y), 'E')] = T.sayi(r[j]); ILK[(p, int(y), 'K')] = T.sayi(r[j + 1])
# Not: 'İl ve Yaş Grubuna Göre İlk Evlilikler' (2025) tablosu kullanılmadı: erkek ve kadın yaş dağılımları neredeyse aynı
# (16-19: 5.460 erkek, 5.287 kadın), ilk evlenme yaşındaki 2,5 yıllık cinsiyet farkıyla bağdaşmıyor.
yf = T.ng(t('_l_ve_E_lerin_Ya__Fark_na_G_re_Evlilikler_TRDF_EVLENME_ERKKAD_YASFARK1.0.xlsx'), ['Yaş Farkı Türü', 'Yaş Farkı'])
ds = T.ng(t('_l_ve_Dava_S_resine_G_re_Bo_anmalar_TRDF_BOSANMA_DAVA_SURE1.0.xlsx'), ['Dava Süresi (Ay)'])
TDH = {int(r['plaka']): float(r['tdh']) for r in csv.DictReader(open(os.path.join(KOK, 'dogum_verisi.csv'), encoding='utf-8'))}
HANE = {int(r['plaka']): float(r['hane_buyuklugu']) for r in csv.DictReader(open(os.path.join(KOK, 'hane_verisi.csv'), encoding='utf-8'))}
GEO = json.load(open(os.path.join(KOK, 'iller.json'), encoding='utf-8'))

r1, r2 = lambda x: round(x, 2), lambda x: round(x, 1)
def seri(p):
    E = [ev[p][(str(y),)] for y in YIL]; B = [bo[p][(str(y),)] for y in YIL]
    N = [orta(p, y) for y in YIL]
    return {
        'ev': [r1(e / n * 1000) for e, n in zip(E, N)],
        'bos': [r1(b / n * 1000) for b, n in zip(B, N)],
        'oran': [r2(b / e * 100) for e, b in zip(E, B)],
        'ilkE': [r2(ILK[(p, y, 'E')]) for y in YIL],
        'ilkK': [r2(ILK[(p, y, 'K')]) for y in YIL],
        'nE': [int(e) for e in E], 'nB': [int(b) for b in B],
    }
def kesit(p):
    return {
        'kadinB': r2(yf[p][('Erkeğin Yaşı Küçük', 'Toplam')] / yf[p][('Toplam', 'Toplam')] * 100),
        'hizli': r2(ds[p][('2 aydan az',)] / ds[p][('Toplam',)] * 100),
    }

iller = []
for g in GEO['iller']:
    p = int(g['plaka'])
    d = {'p': p, 'il': g['il'], 'd': g['d'], 'cx': round(g['cx'], 1), 'cy': round(g['cy'], 1)}
    d.update(seri(p)); d.update(kesit(p)); d['tdh'] = TDH[p]; d['hane'] = HANE[p]
    iller.append(d)

# Türkiye: sayılar il toplamı, nüfus il toplamı
TE = [sum(ev[p][(str(y),)] for p in T.IL.values()) for y in YIL]
TB = [sum(bo[p][(str(y),)] for p in T.IL.values()) for y in YIL]
TN = [sum(orta(p, y) for p in T.IL.values()) for y in YIL]
tr = {'ev': [r1(e / n * 1000) for e, n in zip(TE, TN)], 'bos': [r1(b / n * 1000) for b, n in zip(TB, TN)], 'oran': [r2(b / e * 100) for e, b in zip(TE, TB)],
      'ilkE': [r2(ILK[(0, y, 'E')]) for y in YIL], 'ilkK': [r2(ILK[(0, y, 'K')]) for y in YIL], 'nE': [int(x) for x in TE], 'nB': [int(x) for x in TB],
      'kadinB': r2(yf[0][('Erkeğin Yaşı Küçük', 'Toplam')] / yf[0][('Toplam', 'Toplam')] * 100),
      'hizli': r2(ds[0][('2 aydan az',)] / ds[0][('Toplam',)] * 100), 'tdh': 1.42, 'hane': 3.08}
H = {'viewBox': GEO['viewBox'], 'yillar': YIL, 'tr': tr, 'iller': iller}
bas = ('/* otomatik: _kaynak/harita/tuik_isle.py\n'
       '   TÜİK Evlenme ve Boşanma İstatistikleri il tabloları (2014–2025), ortalama ilk evlenme yaşı (2010–2025), ilk evliliklerde yaş grubu, eşlerin yaş farkı ve boşanma dava süresi (2025);\n'
       '   il nüfusu TÜİK ADNKS (araştırma arşivi v1); doğurganlık TÜİK Doğum İstatistikleri 2025 (ikincil kaynak); hane büyüklüğü TÜİK ADNKS 2025;\n'
       '   il sınırları alpers/Turkey-Maps-GeoJSON, Apache-2.0 */\n')
yol = os.path.join(DEPO, 'oyunlar', 'harita', 'veri.js')
open(yol, 'w', encoding='utf-8').write(bas + 'window.HARITA=' + json.dumps(H, ensure_ascii=False, separators=(',', ':')) + ';\n')
print('yazıldı', yol, os.path.getsize(yol), 'bayt')
