# Türkiye'nin Aşk Haritası — Veri ve Geometri Kaynakları

Derleme tarihi: 21.10.2026

## Önemli not: TÜİK sitesine doğrudan erişilemedi
Bu çalışma sırasında data.tuik.gov.tr ve veriportali.tuik.gov.tr adreslerine yapılan WebFetch istekleri izin onayı alınamadığı için engellendi:
- https://data.tuik.gov.tr/Kategori/GetKategori?p=nufus-ve-demografi-109&dil=1
- https://veriportali.tuik.gov.tr/tr/press/54196

Bu yüzden bu dosyadaki il verilerinin TAMAMI **ikincil kaynaktan** alındı. Değerler TÜİK'e dayanıyor ama yayından önce TÜİK'in il tablosuyla (Evlenme ve Boşanma İstatistikleri, 2025, il tablosu) birebir karşılaştırılması gerekir.

## il_verisi.csv sütunları

### kaba_evlenme (‰) ve kaba_bosanma (‰): TAM, 81/81 il
- **Yıl:** 2025. Kaynak bülten: TÜİK, "Evlenme ve Boşanma İstatistikleri, 2025", 24.02.2026.
- **Kaynak türü:** İKİNCİL.
- **Ana kaynak (81 ilin tablosu):** https://www.erdemvarol.com.tr/turkiye-evlenme-bosanma-oranlari/ (Av. Erdem Varol hukuk bürosu. Tablo TÜİK 2025'e atfediliyor; il sayıları, kaba hızlar ve Türkiye toplamı veriliyor.)
- **Hassasiyet:** Hızlar tabloda **tek ondalıklı**. TÜİK bülteni iki ondalık veriyor (ör. Gaziantep 7,76), tablo bunu yuvarlıyor (7,8). İki ondalıklı 81 il değeri bulunamadı.
- **Tutarlılık kontrolleri:**
  1. Tablodaki 81 ilin evlenme sayılarının toplamı 552.237, boşanma sayılarının toplamı 193.793. İkisi de bültenin Türkiye toplamıyla birebir aynı.
  2. Boşanma sayıları ikinci ve bağımsız bir kaynakla 81/81 il birebir eşleşiyor: https://www.kocatepegazetesi.com/2025-te-193-bin-793-cift-bosandi-afyonkarahisar-26-sirada/410458
  3. Bültenin en yüksek ve en düşük ilk üç il değerleri (iki ondalık) tablodaki yuvarlanmış değerlerle uyumlu:
     - Evlenme: Gaziantep 7,76; Osmaniye 7,68; Şanlıurfa 7,50; Tunceli 4,18; Gümüşhane 4,58; Ardahan 4,67.
     - Boşanma: İzmir 3,28; Antalya 3,21; Denizli 3,14; Hakkari 0,51; Şırnak 0,52; Bitlis 0,63.
     - Bu değerlerin kaynakları: https://www.alomaliye.com/2026/02/24/evlenme-ve-bosanma-istatistikleri-2025/ ve https://www.turkiyegazetesi.com.tr/ekonomi/turkiyenin-evlilik-karnesi-belli-oldu-her-100-gelinden-5i-yabanci-1773005
  4. Trakya illeri (Tekirdağ, Edirne, Kırklareli) ayrıca şu kaynakla eşleşiyor: https://www.babaeskisozgazetesi.com/trakyada-2025-yilinda-evlilik-ve-bosanma-verileri-aciklandi/58804
- **Türkiye geneli (2025):** kaba evlenme hızı ‰6,43 (552.237 evlenme), kaba boşanma hızı ‰2,26 (193.793 boşanma).

### ilk_evlenme_erkek, ilk_evlenme_kadin: BOŞ (81 ilin 81'i eksik)
- 81 il için tam liste bulunamadı. Haberler yalnızca en uç illeri veriyor ve çoğunda veri yılı açıkça yazmıyor. Bu yüzden sütun boş bırakıldı.
- **Türkiye geneli (2025):** erkek 28,5, kadın 26,0 (alomaliye, aynı bülten).
- **Bilgi için, CSV'ye girmeyen kısmi değerler:** Kaynaklar haberturk (https://www.haberturk.com/turkiyenin-evlilik-haritasi-netlesti-en-erken-ve-en-gec-evlenen-iller-belli-oldu-zirvede-bakin-hangi-sehir-var-3885128) ve yenisafak, 20.05.2026; ikisi de "TÜİK son veriler" diyor, yıl belirtmiyor.
  - Tunceli: erkek 32,4, kadın 29,6
  - Rize: erkek 29,9, kadın 27,4
  - Muğla: erkek 29,7, kadın 26,8
  - Ağrı: erkek 27,5, kadın 23,8
  - Muş: kadın 24,1
  - Gaziantep: erkek 26,9, kadın 24,1
  - Şanlıurfa: erkek 26,4
- **Gerekli birincil kaynak:** TÜİK "Evlenme ve Boşanma İstatistikleri" il tablosu (ortalama ilk evlenme yaşı, il ve cinsiyete göre) veya "İstatistiklerle Aile 2025".

### hane_buyuklugu: BOŞ (81 ilin 81'i eksik)
- 2025 için 81 ilin tam listesi bulunamadı.
- **Türkiye geneli (2025, ADNKS, "İstatistiklerle Aile 2025"):** 3,08 kişi. Kaynak: https://bigpara.hurriyet.com.tr/haberler/genel-haberler/ortalama-hane-halki-buyuklugu-3-08-kisi-oldu_ID100701416/
- **Bilgi için, CSV'ye girmeyen kısmi 2025 değerleri:** Şırnak 4,84; Şanlıurfa 4,63; Batman 4,43; Tunceli 2,49; Giresun 2,50; Çanakkale 2,51. Kaynaklar bigpara ve https://www.risalehaber.com/hane-halki-buyuklugu-en-yuksek-iller-sirnak-ve-sanliurfa-452231h.htm
- **Gerekli birincil kaynak:** TÜİK ADNKS il tablosu, "İllere göre ortalama hanehalkı büyüklüğü".

## İl adları ve plakalar
81 plaka (1–81) var ve her biri tek kez geçiyor. CSV ile iller.json il adlarıyla birebir eşleşiyor (script ile kontrol edildi). Kaynak GeoJSON'da "Afyon" yazan il adı "Afyonkarahisar" olarak düzeltildi.

## Geometri (iller.json)
- **Kaynak:** https://github.com/alpers/Turkey-Maps-GeoJSON, dosya `tr-cities.json` (ham kopya: `ham/tr-cities.json`).
- **Lisans:** Apache License 2.0 (`ham/LICENSE_alpers_Turkey-Maps-GeoJSON.txt`). Lisans, sitede atıf yapılmasını ve lisans metninin korunmasını gerektiriyor.
- **İşleme:**
  - Basit Web Mercator projeksiyonu uygulandı.
  - Harita 1000 genişliğe ölçeklendi; viewBox "0 0 1000 429".
  - shapely ile topolojiyi koruyarak sadeleştirildi (tolerans 0,3 px).
  - 1 px²'den küçük adacıklar atıldı.
  - cx, cy değerleri il centroidi. Centroid ilin dışında kalırsa iç nokta (representative point) kullanıldı.
- **Boyut:** 58.088 bayt (yaklaşık 57 KB).
- **Kontrol:** Harita PNG'ye render edilip gözle kontrol edildi.
