# -*- coding: utf-8 -*-
"""'Türkiye'nin aile hikâyesi' için zaman serilerini üretir: oyunlar/hikaye/veri.js
Seriler (il, yıl):
  hane  2008–2025  ortalama hanehalkı büyüklüğü (TÜİK ADNKS; araştırma arşivi v1)
  ilkK  2010–2025  kadınlarda ortalama ilk evlenme yaşı (TÜİK)
  ev    2014–2025  kaba evlenme hızı (TÜİK il evlenme sayısı / yıl ortası nüfus)
  bos   2012–2025  kaba boşanma hızı (2012–2013 TÜİK resmi tablo; 2014–2025 il boşanma sayısı / yıl ortası nüfus)
  tdh   2011–2022 ve 2025  toplam doğurganlık hızı (2011–2022 arşiv; 2025 TÜİK 2025, ikincil kaynak) — 2023–2024 yok
  yasli 2009–2024  65 ve üstü nüfusun payı (TÜİK ADNKS; arşiv)
Türkiye değerleri: ilk evlenme yaşı TÜİK tablosundan; hane = toplam nüfus / tahmini hane sayısı; yaşlı payı nüfus ağırlıklı;
ev ve bos sayı toplamı / nüfus toplamı; tdh için Türkiye serisi olmadığından il medyanı gösterilir."""
import os, sys, csv, json, statistics as st
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tuik_oku as T
KOK = T.KOK; DEPO = os.path.dirname(os.path.dirname(KOK)); t = lambda a: os.path.join(KOK, 'tuik', a)
A = {}
for r in csv.DictReader(open(os.path.join(KOK, 'arsiv_seriler.csv'), encoding='utf-8')):
    for k in ('hane', 'tdh', 'yasli', 'nufus'):
        if r[k] != '': A[(int(r['plaka']), int(r['yil']), k)] = float(r[k])
IL = sorted(T.IL.values())
def orta(p, y): return (A[(p, y, 'nufus')] + A[(p, y - 1, 'nufus')]) / 2
ev = T.ng(t('_l_ve__l_e_Evlenme_Say_s__TRDF_EVLENME_IL_ILCE1.0.xlsx'), ['Zaman'])
bo = T.ng(t('_l_ve__l_e_Bo_anma_Say_s__TRDF_BOSANMA_IL_ILCE1.0.xlsx'), ['Zaman'])
X = T.satirlar(t('_llere_G_re_Kaba_Bo_anma_H_z_.xls')); hy = [str(c)[:4] for c in X[4]]
RESMI = {}
for r in X:
    p = 0 if str(r[0]).startswith('Toplam') else T.plaka(r[0])
    if p is None: continue
    for j, c in enumerate(r[1:], 1):
        v = T.sayi(c)
        if v is not None and hy[j].isdigit(): RESMI[(p, int(hy[j]))] = v
I = T.satirlar(t('_l_ve_cinsiyete_g_re_ortalama_ilk_evlenme_ya__.xls')); iy = I[3]; ILK = {}
for r in I:
    p = 0 if str(r[0]).strip() == 'Türkiye' else T.plaka(r[0])
    if p is None: continue
    for j, c in enumerate(iy):
        y = str(c)[:4]
        if y.isdigit(): ILK[(p, int(y))] = T.sayi(r[j + 1])
TDH25 = {int(r['plaka']): float(r['tdh']) for r in csv.DictReader(open(os.path.join(KOK, 'dogum_verisi.csv'), encoding='utf-8'))}

def yuv(x, d=2): return None if x is None else round(x, d)
S = {
    'hane': (list(range(2008, 2026)), lambda p, y: A[(p, y, 'hane')], 2),
    'ilkK': (list(range(2010, 2026)), lambda p, y: ILK[(p, y)], 1),
    'ev': (list(range(2014, 2026)), lambda p, y: ev[p][(str(y),)] / orta(p, y) * 1000, 2),
    'bos': (list(range(2012, 2026)), lambda p, y: RESMI[(p, y)] if y < 2014 else bo[p][(str(y),)] / orta(p, y) * 1000, 2),
    'tdh': (list(range(2011, 2026)), lambda p, y: TDH25[p] if y == 2025 else A.get((p, y, 'tdh')), 2),
    'yasli': (list(range(2009, 2025)), lambda p, y: A[(p, y, 'yasli')], 1),
}
iller = {p: {} for p in IL}
tr = {}
for k, (yl, fn, d) in S.items():
    for p in IL: iller[p][k] = [yuv(fn(p, y), d) for y in yl]
    if k == 'hane':
        tr[k] = [round(sum(A[(p, y, 'nufus')] for p in IL) / sum(A[(p, y, 'nufus')] / A[(p, y, 'hane')] for p in IL), 2) for y in yl]
    elif k == 'yasli':
        tr[k] = [round(sum(A[(p, y, 'nufus')] * A[(p, y, 'yasli')] for p in IL) / sum(A[(p, y, 'nufus')] for p in IL), 1) for y in yl]
    elif k == 'ilkK':
        tr[k] = [round(ILK[(0, y)], 1) for y in yl]
    elif k == 'ev':
        tr[k] = [round(sum(ev[p][(str(y),)] for p in IL) / sum(orta(p, y) for p in IL) * 1000, 2) for y in yl]
    elif k == 'bos':
        tr[k] = [round(RESMI[(0, y)], 2) if y < 2014 else round(sum(bo[p][(str(y),)] for p in IL) / sum(orta(p, y) for p in IL) * 1000, 2) for y in yl]
    elif k == 'tdh':
        tr[k] = [None if all(iller[p][k][j] is None for p in IL) else round(st.median(iller[p][k][j] for p in IL), 2) for j in range(len(yl))]
H = {'yillar': {k: v[0] for k, v in S.items()}, 'tr': tr, 'iller': [{'p': p, **iller[p]} for p in IL]}
yol = os.path.join(DEPO, 'oyunlar', 'hikaye', 'veri.js'); os.makedirs(os.path.dirname(yol), exist_ok=True)
open(yol, 'w', encoding='utf-8').write('/* otomatik: _kaynak/harita/hikaye_isle.py — kaynaklar dosyanın başındaki açıklamada */\nwindow.HIKAYE=' + json.dumps(H, ensure_ascii=False, separators=(',', ':')) + ';\n')
print('yazıldı', os.path.getsize(yol))
for k in S: print(k, S[k][0][0], tr[k][0], '→', S[k][0][-1], tr[k][-1])
