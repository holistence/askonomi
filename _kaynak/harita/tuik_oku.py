# -*- coding: utf-8 -*-
"""TÜİK il tablolarını okur (eski .xls ve yeni veri portalı .xlsx biçimleri)."""
import os, csv, re, warnings
warnings.filterwarnings('ignore')
import openpyxl, xlrd
KOK = os.path.dirname(os.path.abspath(__file__))
IL = {r['il']: int(r['plaka']) for r in csv.DictReader(open(os.path.join(KOK, 'il_verisi.csv'), encoding='utf-8'))}
ES = {'Afyon': 'Afyonkarahisar', 'K.Maraş': 'Kahramanmaraş', 'Kahramanmaras': 'Kahramanmaraş', 'Içel': 'Mersin', 'İçel': 'Mersin'}
def plaka(ad):
    ad = str(ad).strip().replace('\n', ' ')
    ad = re.split(r'\s*[-–(]\s*', ad)[0].strip() if ad not in IL else ad
    ad = ES.get(ad, ad)
    return IL.get(ad)
def sayi(x):
    if x is None or x == '' or isinstance(x, str) and not re.match(r'^-?\d+([.,]\d+)?$', x.strip()): return None
    return float(str(x).replace(',', '.'))
def satirlar(yol):
    if yol.endswith('.xls'):
        sh = xlrd.open_workbook(yol).sheet_by_index(0)
        return [[sh.cell_value(r, c) for c in range(sh.ncols)] for r in range(sh.nrows)]
    ws = openpyxl.load_workbook(yol, data_only=True).worksheets[0]
    return [list(r) for r in ws.iter_rows(values_only=True)]
def ng(yol, baslik_satirlari):
    """Yeni portal biçimi: başlık satırları (ör. Zaman, Cinsiyet) ileri doldurulur; değer sütunları 'Gözlem Durumu' sütunlarını atlar.
    Döndürür: {plaka: {(etiket1, etiket2, ...): değer}}"""
    R = satirlar(yol)
    bas = {}
    for r in R:
        if r and str(r[0]).strip() in baslik_satirlari:
            dol, son = [], None
            for c in r[1:]:
                if c not in (None, ''): son = str(c).strip()
                dol.append(son)
            bas[str(r[0]).strip()] = dol
    durum = next((r for r in R if r and str(r[0]).strip() in ('Coğrafi Kapsam', 'Yaş Grubu')), None)
    out = {}
    for r in R:
        p = plaka(r[0]) if r and r[0] else None
        if str(r[0]).strip() == 'Türkiye': p = 0
        if p is None: continue
        d = {}
        for j, c in enumerate(r[1:]):
            if durum is not None and j + 1 < len(durum) and str(durum[j + 1] or '').strip() == 'Gözlem Durumu': continue
            v = sayi(c)
            if v is None: continue
            anahtar = tuple(bas[b][j] if j < len(bas[b]) else None for b in baslik_satirlari)
            d[anahtar] = v
        out[p] = d
    return out
