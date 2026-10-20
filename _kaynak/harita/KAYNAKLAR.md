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

## dogum_verisi.csv

- **Yıl:** 2025. Kaynak, TÜİK "Doğum İstatistikleri, 2025" bülteni (21.05.2026). Bülten bağlantısı: https://veriportali.tuik.gov.tr/tr/press/58018
- **Sütunlar:** plaka, il, tdh (toplam doğurganlık hızı, kadın başına çocuk), kaba_dogum (kaba doğum hızı, ‰). Ondalık ayırıcı nokta.
- **Durum:** İki sütun da 81 il için dolu. Eksik il yok.

### Birincil kaynak: erişilemedi
- veriportali.tuik.gov.tr ve data.tuik.gov.tr adreslerine erişilemedi. WebFetch izni alınamadı, shell proxy'si de bağlantıyı reddetti (403).
- Bu yüzden il değerleri TÜİK tablosundan doğrudan alınmadı.

### İkincil kaynak (81 ilin tamamı için)
- **Kaynak:** nufusune.com il sayfaları, `https://www.nufusune.com/<il>-nufusu` biçiminde. Örnekler: https://www.nufusune.com/sanliurfa-nufusu, https://www.nufusune.com/bartin-nufusu, https://www.nufusune.com/canakkale-nufusu
- Her sayfa değerleri "TÜİK Doğum, Evlenme ve Boşanma İstatistikleri" kaynağıyla, 2025 yılı için veriyor. Nüfus tabanı ADNKS 2025.
- 81 sayfanın her biri tek tek okundu. Her sayfada yıl "2025" görünüyordu.
- Sitenin kendi notu: resmi kullanım öncesinde değerlerin TÜİK'ten teyit edilmesi gerekiyor.

### Türkiye geneli (2025)
- TDH 1,42 (2024: 1,49). Kaba doğum hızı ‰10,4. Canlı doğum 895.374.
- Kaynaklar:
  - https://www.ekonomigazetesi.com/ekonomi/dogurganlik-hizi-2025te-142-79771
  - https://www.alomaliye.com/2026/05/21/dogurganlik-hizi-2025te-1-42ye-geriledi/
  - https://www.haberturk.com/dogurganlik-hizi-tarihi-dusuk-seviyede-3886214-ekonomi

### Kontroller
1. **TDH uç iller:** 10 il, bağımsız haber kaynaklarıyla karşılaştırıldı ve hepsi birebir tuttu.
   - En yüksekler: Şanlıurfa 3,15; Şırnak 2,53; Mardin 2,23; Diyarbakır 2,14; Siirt 2,11.
   - En düşükler: Bartın 1,09; İzmir 1,10; Ankara, Eskişehir ve Zonguldak 1,11.
   - Karşılaştırma kaynakları:
     - https://www.ahaber.com.tr/viral/galeri/liste/2025-tuik-dogum-istatistikleri-dogurganlik-hizi-en-yuksek-ve-en-dusuk-iller-hangileri
     - https://www.haberler.com/guncel/yeni-veriler-aciklandi-iste-cumhurbaskani-19867436-haberi/
     - https://t24.com.tr/gundem/turkiyenin-nufus-yapisi-degisiyor-dogum-oranlari-gerilemeye-devam-ediyor,1323548
     - https://www.habergalerisi.com/haber-dogum-istatistikleri-2025-140316.html
   - CSV'deki sıralamada da ilk 5 ve son 5 il haberlerdekiyle aynı.
2. **TDH dağılımı:** Bültende verilen sayımlar CSV ile birebir tutuyor.
   - TDH < 2,10 olan il: 76.
   - TDH < 1,50 olan il: 59.
   - TDH ≥ 3 olan il: 1 (Şanlıurfa).
   - Bu sayımların kaynakları: alomaliye ve habergalerisi (yukarıda).
3. **Kaba doğum hızı:** İl düzeyinde bağımsız doğrulama yalnızca 1 ilde yapılabildi.
   - Sinop ‰7,2 (TDH 1,25). Kaynak "Türkiye'nin en düşük 4'üncü ili" diyor. CSV'de Sinop ‰7,2 ile Edirne'yle birlikte 4. sırada; altında Zonguldak 6,6, Bartın 6,8 ve Giresun 6,9 var. Kaynak: https://www.kastamonugundemgazetesi.com/sinop-kaba-dogum-hizinda-turkiye-nin-en-dusuk-4-uncu-ili-oldu/116953
   - Ulusal haberlerde il bazında kaba doğum hızı bulunamadı.
   - En yüksek il CSV'de de Şanlıurfa (‰23,8). Bu değer TDH sıralamasıyla tutarlı.
   - **Not:** kaba_dogum sütununun bağımsız teyidi, tdh sütununa göre daha zayıf.
4. **İl adları:** CSV'deki il adları il_verisi.csv ile birebir eşleşiyor (script ile kontrol edildi). 81 il var, tekrar eden yok.

### Eksikler ve yapılacaklar
- Eksik il yok.
- Yayından önce önerilen: TÜİK bülten tablosu "İllere göre toplam doğurganlık hızı ve kaba doğum hızı, 2025" indirilip iki sütunun birebir karşılaştırılması. Özellikle kaba_dogum sütunu için.
