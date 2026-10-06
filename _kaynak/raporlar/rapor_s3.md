# Sezon 3 "Kriz" (test 21–30): kaynak raporu

Dosya: `/home/claude/askonomi/_kaynak/icerik_s3.py` (10 test).
Okunan metinler (baştan sona): Giriş, Bölüm 22, 23, 24, 25, 26, 27, 28 (`/home/claude/askonomi_in/bolum/`).
Sayfa numaraları dosyalardaki `[s. NNN]` işaretlerine göredir. Alıntılarda satır sonu tirelemesi kaldırılmıştır.

Yapılan kontroller: `ast.parse` sorunsuz. Ayrı bir betik şunları denetledi: başlık listesiyle (veri.LISTE 21–30) slug eşleşmesi; her profil/senaryo sorusunda her sonuç anahtarının tam bir kez geçmesi; soru sayıları (6, test 29 için 8, test 30 için 10 ikili soru); seçenek sayısı (4–6); hesap puanlarının 0–3 arası tam sayı olması; seviyelerin 0'dan başlaması; mit testinde "Doğru./Yanlış." önekleri (3 doğru, 3 yanlış); sonuç ve seviye metinlerinin 50–90 kelime aralığında olması; noktalı virgül bulunmaması; Bölüm 10–14, 20, 21'e yönlendirme yapılmaması; test 30 seçeneklerinde ben/sen gibi kişiye bağlı sözcük bulunmaması. Sonuç: hata yok.

Genel not: Hiçbir sonuç metni "ayrıl" ya da "kal" demiyor. Şiddet/istismar içeren senaryo yok. Kitabın şiddet ve güvenlik konusundaki sınır cümlesi yalnızca güven endeksinin en düşük seviyesinde (s. 356) ve beklenti endeksinin en düşük seviyesinde (s. 414) koruyucu bir not olarak kullanıldı.

---

## 21 beklenti-enflasyonu (hesap, Bölüm 28, birim "Beklenti Enflasyonu Endeksi")

Dayanak: Bölüm 28, s. 403–416.

**"Koç" ve "tutkulu sevgili" kitapta geçmiyor.** Kitap bu fikri s. 409'da şöyle veriyor: "Aynı insanın sevgili, en iyi arkadaş, cinsel partner, ekonomik ortak, ev arkadaşı, ebeveynlik ortağı, sırdaş, tatil arkadaşı, kriz desteği, kariyer danışmanı ve kişisel gelişim destekçisi olması beklenebilir." Soru 1 bu listeyi kullanıyor ("cinsel partner", "ekonomik ortak" ve "ebeveynlik ortağı" çıkarıldı, cinsellik kuralı nedeniyle ve listeyi kısa tutmak için). "Koç" yerine kitaptaki "kariyer danışmanı" kullanıldı. "Terapist" fikri ise kitabın s. 410–411'deki "Aşk Terapinin Yerini Tutabilir mi?" alt başlığından alındı (soru 2 ve "Yüksek enflasyon" seviyesi). Grep ile doğrulandı: "koç" kitapta yalnızca Bölüm 34'te (romantik koçluk) geçiyor.

Soruların dayanağı:
- S1 roller listesi → s. 409 (yukarıdaki cümle).
- S2 destek için tek kişiye yaslanmak → s. 410 kutu ("Bir ihtiyacımızı arkadaş, kardeş, meslektaş, terapist, spor grubu veya başka sosyal ilişkiler de karşılayabiliyorsa bunu yalnız partnerin sorumluluğu haline getirmek zorunlu değildir."), s. 411.
- S3 söylemeden anlamak → s. 408 ("“Söylemek zorunda kalıyorsam anlamı kalmıyor” cümlesi doğum günlerinden duygusal desteğe kadar pek çok konuda karşımıza çıkar."). Seçenek 3 bu cümlenin uyarlaması.
- S4 güvenlik ile heyecan → s. 411 ("aynı insandan hem güvenlik hem yenilik istememizdir"), s. 411–412 (yeniliği çiftlerin aktif biçimde yaratabilmesi).
- S5 olmazsa olmaz sayısı → s. 406 ("Beklenti enflasyonu standart sahibi olmak değil, her tercihimizin vazgeçilmez şarta dönüşmesidir."), s. 407 (portföy problemi).
- S6 "beni tamamlıyorsun" → s. 414–415 ("Belki daha gerçekçi romantik cümle “Beni tamamlıyorsun” değil, “Seninle hayatımın bazı alanları daha zengin hale geliyor”dur."). Seçenekler kısaltılmış uyarlamadır, doğrudan alıntı olarak sunulmadı.

Seviye metinlerindeki iddialar:
- Beklentiyi düşürmek değil, dağıtmak → s. 414 alt başlık "Beklentiyi Düşürmek mi, Dağıtmak mı?".
- "Güçlü romantik bağ ile zengin sosyal ağ birbirinin rakibi değildir" → s. 410 kutu, aynı cümle.
- Şiddetsizlik, rıza, temel saygı, dürüstlük ne dağıtılabilir ne düşürülmeli → s. 414 ("Bazı beklentiler ise dağıtılamaz ve düşürülmemelidir. Şiddetsizlik, rıza, temel saygı ve dürüstlük gibi konular...").
- Standartlar kötü eşleşmeleri fark etmeye yardım eder → s. 406 ("Standartlar kötü eşleşmeleri fark etmemize ... yardım eder.").
- Standart ile kusursuzluk talebi → s. 406 ("Sorun, standart ile kusursuzluk talebinin birbirine karıştığı yerde başlar.").
- Doğrudan alıntı "Bu beklenti partner tarafından biliniyor mu, karşılıklı mı, kaynaklarımızla uyumlu mu ve gerçekten benim için vazgeçilmez mi?" → s. 413 (birebir).
- İş ilanı benzetmesi → s. 410 kutu "Partnerin İş Tanımı Kaç Sayfa?".
- Yetersiz kalınan her alanın genel başarısızlık gibi algılanması → s. 410 ("onun yetersiz kaldığı her alan ilişkinin genel başarısızlığı gibi algılanabilir").
- Partner profesyonel desteğin yerini almak zorunda değil → s. 411, s. 414 ("profesyonel psikolojik yardımın yerini almak zorunda değildir").
- Finkel, dağ ve oksijen → s. 412 ("Dağın yükseklerinde manzara daha etkileyicidir; fakat oksijen daha azdır."). Metinde noktalı virgül yerine virgül kullanıldı ve tırnaksız aktarıldı.
- "Beklentinizi düşürün" dememesi, beklenti ile kaynak uyumu → s. 412.
- Alıntı "Partnerimden istediğim şey gerçekten ilişkim için temel mi?" → s. 416. **Kısaltıldı.** Kitapta cümle şöyle sürüyor: "..., yoksa “doğru insan böyle olmalı” diye öğrendiğim uzun listenin başka bir maddesi mi?" Tam alıntı istenirse eklenebilir (kelime sınırı içinde kalır).

## 22 iliski-getirisi (hesap, Bölüm 25, birim "Getiri Endeksi")

Dayanak: Bölüm 25, s. 361–375. Endeks para getirisi ölçmüyor. Kitabın parasal olmayan yatırım ve getiri kalemlerini kullanıyor (s. 362, s. 372: "güven, yakınlık, aidiyet, bakım, ortak deneyimler...").

Soruların dayanağı:
- S1 iyi habere tepki (capitalization) → s. 365–366 (Gable vd., aktif-yapıcı tepkiler).
- S2 küçük katkıların görülmesi → s. 365 (Algoe vd. 2010, Gordon vd. 2012, "İlişkiye yatırım yalnız vermek değil, verilen şeyi görebilme kapasitesidir").
- S3 hedefler, Michelangelo olgusu → s. 366–367, s. 371 ("yatırım büyümüş, fakat yatırımcının kendisi küçülmüş olabilir"). Seçenek "“ilişkimiz için” bıraktım" → s. 367.
- S4 ortak yenilik → s. 367–368 (Aron vd. 2000).
- S5 karşılıklılık → s. 372–373.
- S6 üretken ile telafi edici emek → s. 373–374.

Seviye metinleri:
- "Ortak hayatın bilançosu tam denk olmayabilir; fakat sürekli tek tarafa zarar yazıyorsa yatırım metaforu uyarı vermeye başlar." → s. 373 (noktalı virgül virgüle çevrildi).
- "hangi yatırımlar ilişkiyi gerçekten besler" → s. 362, bölüm sorusu.
- Ani kriz değil uzun süreli ihmal → s. 364 ("İlişki sona ermeden önce bazen dramatik kriz değil, uzun süreli ihmal yaşanır.").
- Lojistik şirkete dönüşmek, yakınlığın sessizce azalması → s. 364.
- Yüzlerce kez tekrarlanan küçük davranışlar → s. 365.
- Bakım, ortaklığın kullanım değerini koruyan düzenli yatırım → s. 364.
- Getirilerin kendiliğinden yenilenmemesi, hatıraların geçmişe ait hale gelmesi, yeni malzeme eklemek → s. 368.
- Zor günde sigorta, iyi günde getiriyi çoğaltma → s. 366.
- "İyi ortak yalnız yükümüzü taşımaya değil, büyümemize de dayanabilen insandır." → s. 366.
- En yüksek getirilerin bazıları sayıya çevrilemez → s. 374.

## 23 batik-maliyet (senaryo, Bölüm 25 / 26 / 22)

Dayanak: s. 369–370 (Bölüm 25), s. 313–314 (Bölüm 22), s. 381, 385, 389 (Bölüm 26). Sonuçlar karar vermiyor. Dört düşünme tarzı tanımlıyor ve her birinin kitaptaki riskini gösteriyor. Şiddet ya da istismar ima eden senaryo yok. Senaryolar mutsuzluk, gerginlik, taşınma, ödenmiş tatil gibi gündelik durumlar.

Soruların dayanağı:
- S1, S5 "bunca yıl" → s. 313 ("Bu ilişkiye on beş yılımı verdim."), s. 369 kutu ("“Bunca yılını vermişsin, şimdi bırakılır mı?” cümlesi tek başına ekonomik olarak da doğru değildir.").
- S2 ödenmiş tatil → s. 313 (geçmiş tatiller ve düğün masrafları batık maliyet örneği).
- S4 taşınma → s. 313–314 ("Kariyerini eşinin işi için başka şehre taşımış kişinin kaybettiği mesleki fırsatlar geçmiştedir, fakat düşük bugünkü geliri ve emeklilik birikimi bugünün gerçeğidir."). Y seçeneği → s. 385 ("“Onun için gitmeseydim bugün nerede olurdum?”").
- S6 A seçeneği → s. 370 ("Sona eren yatırım ile değersiz geçmiş aynı şey değildir.").

Sonuç metinleri:
- G: batık maliyet tanımı → s. 370, s. 313. "bugün için kötü seçeneği geçmişi kurtarmak amacıyla tercih etmek" → s. 370. Alıntı “yalnız geçmişte çok şey verdiğim için” → s. 370 (birebir parça). "Kalmanın yanlış olduğu anlamına gelmez" → s. 369 ("Yatırım bize neden kalmanın cazip olabileceğini açıklar; kalmanın her zaman doğru olduğunu kanıtlamaz.").
- S: alıntı “batık maliyet, unut gitsin” ve "en az geçmişe teslim olmak kadar yanıltıcıdır" → s. 370. Ortak çocuklar, konut, sosyal ağlar → s. 370.
- A: batık maliyet ile ilişkiye özgü sermaye ayrımı → s. 314 ("batık maliyet ile ilişkiye özgü sermaye birbirinden ayrılmalıdır"). Kusursuz ayırmanın kolay olmaması → s. 370 ("İnsan hayatında bu ikisini kusursuz biçimde ayırmak kolay değildir."). "Sona eren yatırım ile değersiz geçmiş aynı şey değildir." → s. 370. Bölüm yönlendirmesi 22 (ayrım ilk kez s. 314'te kuruluyor). Cümle Bölüm 25'ten olsa da konu iki bölümde ortak.
- Y: "hayali hayat"ın kusursuz görünmesi → s. 381. Birebir alıntı "Gerçek hayat bütün maliyetleriyle, hayali hayat ise seçilmiş sahneleriyle yarışır." → s. 381. "maliyetlerini henüz yaşamamışızdır" fikri → s. 389.

## 24 neye-mal-oldu (hesap, Bölüm 26, birim "Fırsat Maliyeti Endeksi")

Dayanak: Bölüm 26, s. 377–390, Giriş s. 8–9. Endeks bedelin büyüklüğünü ölçüyor. Seviyelerin hiçbiri yüksek bedeli yanlış seçim olarak yorumlamıyor.

Soruların dayanağı:
- S1 iş/eğitim fırsatı → s. 378 (iş teklifini reddeden kişi).
- S2 şehir → s. 382 (tied mover: "tek başına olsaydı taşınmayı seçmeyecek “bağlı göçmen”"). Seçenek 3 bu tanımın uyarlaması.
- S3 arkadaşlar → s. 384 (mesleki ağ), s. 371 (dış dayanaklar, Bölüm 25).
- S4 zaman → s. 378 ("Hayatın kıt kaynağı yalnız para değil, geri dönmeyen zamandır.").
- S5 varsayılan tercih → s. 384 ("bir tarafın isteği ... varsayılan seçenek haline gelir").
- S6 görünürlük → s. 384–385.

Seviye metinleri:
- "her “evet” başka bazı ihtimallere sessizce “hayır” der" → s. 377 (birebir yakın: "Her “evet” başka bazı ihtimallere sessizce “hayır” der.").
- Maliyetli seçim yanlış seçim değildir, neye değer verdiğimizi gösterir → Giriş s. 8–9 ("Bir seçimin maliyetli olması onun yanlış olduğu anlamına gelmez. Bazen tam tersine, neyin uğruna neyi gözden çıkarabildiğimiz, neye gerçekten değer verdiğimiz hakkında güçlü bilgi verir."), ayrıca s. 386.
- Alıntı "Kim hangi fırsattan vazgeçti ve bu kayıp zaman içinde nasıl telafi edildi?" → s. 383 (birebir).
- "Vazgeçilen iş maaş bordrosunda görünmez, ama ilişkinin hafızasında kalabilir." → s. 384.
- Kırgınlık, fiyat etiketi değil görünmeyen kaybedenleri konuşmak → s. 385.
- "İyi hayat, fırsat maliyeti olmayan hayat değil; vazgeçtiklerine rağmen seçtiği hayatı yaşamaya değer bulan hayattır." → s. 386 (noktalı virgül virgüle çevrildi).
- Aynı kişide toplanması bir dağılım sorunu → s. 383 ("gerçek bir dağılım problemi"), s. 388.
- "Ortak hayatın maliyetleri kadar kaçırılan fırsatlar da görünür olmalıdır." → s. 388 (birebir).

## 25 cok-secenek (profil, Bölüm 27, ayrıca 26)

Dayanak: Bölüm 27, s. 391–402, Bölüm 26, s. 379–380 ve 386–387.

Sonuç metinleri:
- M: maksimize etme, Schwartz vd. 2002, pişmanlık ve düşük seçim doyumu → s. 395. Bulguların tartışılmış olması → s. 395 ("Bu bulgular daha sonra ölçüm ve kavram açısından geniş biçimde tartışılmıştır"). "en iyi partner"in tek boyutlu sıralamasının olmaması → s. 395–396. Yeni seçeneklerin aramanın bitişini ertelemesi → s. 395.
- Y: "yeterince iyi ve benim için uygun" → s. 395. "Kolay karar ile iyi hayat aynı şey değildir." → s. 401. Zamanla öğrenilen özellikler → s. 401 ("insan hakkında ancak zaman içinde öğrenilebilecek özelliklere zaman tanımak").
- F: tercih netliğinin arama maliyetini azaltması → s. 394. Filtre sayısı arttıkça beklenmedik uyumun yok olması → s. 401. Kolay filtrelenen özellikler (boy, yaş, meslek) ile mizah ve duyarlılık → s. 398.
- A: opsiyon değeri, partnerin aynı ölçüde yatırım yapmaması → s. 387. Birebir alıntı "Özgürlük, kapıyı kapatmanın kendi kararımız olmasıdır." → s. 387. Yönlendirme Bölüm 26.
- B: başka çiftteki iyi davranışı fark edip ilişkiyi geliştirmek → s. 400. Hayali bileşik partner → s. 400. "hiç var olmamış kusursuz alternatif" → s. 400.

Kullanılmayanlar: D'Angelo & Toma (6 ve 24 profil), Pronk & Denissen (yaklaşık %27 düşüş), Lenton & Francesconi rakamları. Sonuç metinlerine sığmadı, uydurma riski de yok.

## 26 guven-sermayesi (hesap, Bölüm 24, birim "Güven Sermayesi Endeksi")

Dayanak: Bölüm 24, s. 345–360. Endeks kör güveni değil, davranış kaydını ölçüyor (söz tutma, sır koruma, sorumluluk alma, kendiliğinden açıklama, doğrulama ihtiyacı, önemli bilgiyi paylaşma). Bu, kitabın "maksimum güven değil, davranışla uyumlu güven" ilkesine uygun (s. 352–353).

Soruların dayanağı: s. 348 (küçük sözlerin tutulması, ortadan kaybolmamak, hatayı başkasının üzerine atmamak, mahremiyeti korumak), s. 347 (sırrın paylaşılması, zayıflığın silah olarak kullanılması), s. 353 (kendiliğinden açıklama ile kanıt çıkana kadar inkâr), s. 348 (her bilgiyi doğrulamak, her gecikmeyi soruşturmak), s. 350–351 (karşı tarafın kararını etkileyen bilgi).

Seviye metinleri:
- "Hak edilmiş kuşku da sağlıklı bilgi işleme olabilir." → s. 352.
- Düşük güvenin kontrol, doğrulama ve savunma maliyeti → s. 357.
- "Güveni bozan davranışsa, güveni onaran da eninde sonunda davranış olmalıdır" → s. 354.
- Güvenlik tehdit altındaysa öncelik kişinin korunması → s. 356 ("Güvenliğin tehdit altında olduğu durumda öncelik ilişkinin yeniden kurulması değil kişinin korunması ve gerçek çıkış seçeneklerine erişmesidir.").
- Alanlara göre değişen güven, sadakat ve dakiklik örneği → s. 346.
- Tek olaydan örüntüye, iki alıntı "Bu kez ne oldu?" ve "Bu kişinin sözü geleceğe ilişkin ne kadar bilgi taşıyor?" → s. 353 (birebir).
- İşlem maliyeti, doğrulama ve soruşturma → s. 348.
- Mekanik olmayan sermaye, küçük gecikme ile büyük ihanet → s. 349.
- Getiri olarak hareket alanı → s. 358.
- Maksimum değil davranışla uyumlu güven → s. 352–353.
- "İyi güven, kanıta rağmen değil kanıt sayesinde güçlenir." → s. 357 (birebir).

## 27 aldatma-mitleri (mit, Bölüm 23)

Dayanak: Bölüm 23, s. 327–344. 3 doğru, 3 yanlış.

1. "Bir kez aldatan ... mutlaka aldatır." **Yanlış.** → s. 337: Knopp vd. (2017), 484 yetişkin, "yaklaşık üç kat daha yüksekti". s. 337: "Üç kat daha yüksek olasılık, yüzde yüz kader anlamına gelmez". s. 338 kutu: "Bu bir risk farkıdır."
2. "Mutlu ilişkide aldatma olmaz ..." **Yanlış.** → s. 330: "Fakat nedenselliği ters çevirmemek gerekir... sadakatsizliğin kendisi ... doyumu düşürebilir", "memnun olmadığı halde hiç aldatmayan çok sayıda insan vardır ve mutlu olduğunu bildiren insanların bir bölümü de ilişki dışı davranış yaşayabilir".
3. "Herkes aynı çizgiyi çekmez." **Doğru.** → s. 328: Wilson vd. (2011), "“açık”, “aldatıcı” ve “belirsiz”", "merkezinde büyük ölçüde uzlaşabilir, fakat sınırlarında ciddi farklılık gösterebilirler".
4. "Gizli borç ya da harcama sadakatsizlik sayılabilir." **Doğru.** → s. 334: Garbinsky vd. (2020), tanım, "Burada her kişisel harcamayı açıklamamak finansal sadakatsizlik değildir", "beklenen ortak kural ile kasıtlı gizlilik arasındaki farktır".
5. "Aldatmadan sonra ilişki onarılamaz." **Yanlış.** → s. 339: Atkins vd. (2010), "tedavi sonunda ve altı aylık izlemde aradaki farkın büyük ölçüde kapanabildiğini". Alıntı "aldatmadan sonra mutlaka birlikte kalınmalıdır" ve "sadakatsizliğin ilişkiyi otomatik olarak onarılamaz hale getirmediğidir" → s. 339 (birebir).
6. "Farklı motivasyonlar olabilir." **Doğru.** → s. 329: Selterman vd. (2019), 495 kişi. Motivasyon listesi kitaptakinin **kısaltılmış** hali ("cinsel arzu" ve "cinsel çeşitlilik" cinsellik kuralı nedeniyle çıkarıldı). Genç yetişkin örneklem uyarısı → s. 329. "Bilimsel açıklama ile ahlaki mazeret birbirine karıştırılmamalıdır" → s. 329.

Seviye metinleri:
- Risk farkı, kader değil → s. 338. Geçmiş davranışın ömür boyu etiket olmaması → s. 337 ("geçmiş davranış bir risk bilgisi taşıyabilir ama insanın üzerine ömür boyu sabit etiket yapıştırmaz"). Birebir alıntı "Risk değerlendirmesi ile insanı mahkûm etmek aynı şey değildir." → s. 338.
- "tek eşliyiz" ve aynı sözleşme → s. 328. Sadakat yasak listesi değil ortak beklenti → s. 328. Dijital iletişimin gri alanı büyütmesi → s. 333.
- "Aldatmanın ekonomik çekirdeği ... üzerinde anlaşılmış kuraldan gizli sapmadır" → s. 333. Eksik bilgiyle verilen kararlar → s. 344. Gizliliğin ayrı maliyeti → s. 335 alt başlık "Gizlilik Neden Ayrı Bir Maliyet Yaratır?". Alıntı "Bir kez bozulan güven yeniden kurulabilir mi" → s. 344 (birebir parça).

Kullanılmayanlar: Munsch (2015), çünkü kitap çalışmanın düzeltildiğini ve sonuçların zayıfladığını söylüyor (s. 335). Conley vd. (2012), cinsel sağlık konusu. "Parası çok olan daha çok aldatır" iddiası da kullanılabilirdi (s. 334–335: "basit bir ekonomik yasa beklemek için neden yoktur"), yedek mit olarak duruyor.

## 28 affetmek-guvenmek (profil, Bölüm 24 ve 23)

Dayanak: s. 355–356 (Bölüm 24), s. 340 (Bölüm 23). Senaryolar yalan, gizli borç ve sarsılmış güven gibi şiddet içermeyen ihlaller.

Sonuç metinleri:
- F: affetmenin unutmak ya da kabul edilebilir saymak olmaması, misilleme ve öfke döngüsü → s. 340. Affetme eğilimi ve daha az olumsuz çatışma (Braithwaite vd. 2011) → s. 356. “ne yapılırsa yapılsın affedin” → s. 356 (birebir). Onarım takvimi → s. 355 ("Onarım, ihlali yapanın affedilme takvimini tek taraflı belirlemesiyle gerçekleşmez.").
- G: affetmek ile güvenmenin ayrı kararlar olması → s. 355. Geçici güvence ile kalıcı gözetim → s. 355. Eğitim tekerlekleri benzetmesi → s. 355. Eski güven değil, yeni bilgiyle yeni güven → s. 356.
- U: "affetmek, güvenmek ve uzlaşmak üç ayrı karardır" → s. 355. Birlikte kalmanın affetmenin kanıtı olmaması → s. 355. "bağışlama geçmiş borcun kayıtlardan sihirli biçimde silinmesi değildir" → s. 340. Yönlendirme 23.
- H: McNulty (2008), yeni evliler, sık tekrarlanan davranışta yüksek affedicilik → s. 356. "affetmenin iyi olması, sınırların gereksiz olduğu anlamına gelmez" → s. 356. "Özür bir sinyaldir; güvenilirliğini sonraki davranış belirler" → s. 354 (noktalı virgül virgüle çevrildi).

## 29 kriz-senaryolari (senaryo, 8 soru, Bölüm 22–28)

Senaryolar ve bölümleri: S1 tekrarlayan kavga (22), S2 eski sevgiliyle gizli mesajlaşma (23, s. 328 ve 333), S3 gizli harcama (23, 24, s. 334), S4 tek taraflı emek (25, s. 372–373), S5 iş teklifi ve taşınma (26, s. 382–384), S6 seçenek bolluğu (27, s. 395), S7 "beni anlamıyorsun" (28, s. 408), S8 kriz sonrası "eskisi gibi" (24, s. 356). Sonuçlar beş kriz tarzı ve her biri ilgili bölüme yönleniyor (25, 24, 26, 28, 22).

Sonuç metinleri:
- H (→25): “gerçek aşk hesap yapmaz” ve eşitsizliği görünmez kılması → s. 372–373. Batık maliyetin gereğinden fazla ağırlık kazanması → s. 370. Anında eşdeğer karşılık ve muhasebe defteri → s. 372 ("Her davranışın anında eşdeğer karşılığını talep etmek ilişkiyi muhasebe defterine çevirebilir.").
- G (→24): şeffaflık isteğinin anlaşılır olması, geçici güvence ile kalıcı gözetim → s. 354–355. Denetimin bilgi talebinin doğal sonu olmaması, silinmiş mesajlar → s. 351. "Güvenin alternatifi kusursuz bilgi değildir" → s. 351.
- A (→26): farkındalığın bazen işe yaraması → s. 389. Mevcut partnerin hatalarını bilip vazgeçilen kişinin hatalarını bilmemek → s. 381. "Alternatif hayat maliyetsiz değildir; yalnız maliyetlerini henüz yaşamamışızdır." → s. 389.
- B (→28): beklenti açığının kaynakları (çelişkili, kaynaklarla uyumsuz, karşılıklı anlaşma yok) → s. 413. "Beklentileri yeniden düzenlemek, temel sınırları silmek değildir." → s. 414.
- C (→22): "Gitme imkânının artması, gitme arzusunun artmasıyla aynı şey değildir." → s. 313. "gidebilme kapasitesi, kalmanın anlamını güçlendirebilir" → s. 371 (Bölüm 25). “seçilmiş seçenek” ve “şimdilik tutulan seçenek” → s. 396–397 (Bölüm 27).

## 30 kriz-aninda (cift, Bölüm 24, 10 ikili soru)

Seçenekler kişiden bağımsız yazıldı. Hiçbirinde ben/sen/bana/sana yok, iki partner aynı seçeneği aynı anlamda seçebilir. Dayanaklar: s. 353–354 (özür ve davranış), s. 351 ve 354–355 (telefon, şeffaflık), s. 349–350 (açık anlaşma ile güven), s. 339 (ayrıntıların paylaşılma biçimi, Bölüm 23), s. 340 (affetme), s. 356 (eski haline dönmek ile yeni yapı), s. 370 (geçmiş yıllar ile gelecek, Bölüm 25), s. 414 (desteği dağıtmak, Bölüm 28).

Seviye metinleri:
- Eksik sözleşme, iyi niyet, adalet anlayışı ve geçmiş davranışlar → s. 349 kutu. Her şeyin yazılı kurala bağlanamaması → s. 349–350.
- Alanlara göre değişen güven → s. 346. "Sağlam ilişki açık anlaşmalar ile hak edilmiş güveni birlikte kullanır." → s. 350. "güven sözleşmenin alternatifi değildir" → s. 349.
- Her kararı yeniden müzakere etmemek, işlem maliyeti → s. 348. Krizin kendisinin ilişkiyi otomatik güçlendirmemesi → s. 357. "güven davranıştan beslenmelidir" → s. 357.
- "Güven belirsizliği ortadan kaldırmaz; belirsizlik içinde birlikte hareket etme maliyetini düşürür" → s. 347. Özür bir sinyal, güvenilirliği sonraki davranış belirler → s. 354.

---

## Kitapta bulunamadığı için çıkarılan ya da değiştirilenler
- "Partnerden hem en iyi arkadaş, hem tutkulu sevgili, hem koç, hem terapist... beklemek": Kitapta bu kalıp yok. "Koç" ve "tutkulu sevgili" geçmiyor. Kitabın s. 409 listesi (sevgili, en iyi arkadaş, sırdaş, kariyer danışmanı, kişisel gelişim destekçisi...) ve s. 410–411 terapist tartışması kullanıldı.
- Kriz anında çift uyumunun "nadir" olduğu, benzer çiftlerin "kör noktalarını paylaştığı" gibi ilk taslakta düşündüğüm cümleler kitapta karşılığı olmadığı için yazılmadı.
- Affetmenin "kişinin kendisine verdiği hediye" olduğu fikri kitapta yok, kullanılmadı.
- Hiçbir sonuçta kitap dışı araştırma, rakam ya da isim yok. Geçen tüm isimler (Finkel, Schwartz, Knopp, Wilson, Garbinsky, Selterman, McNulty) ve rakamlar (484, 495, "üç kat") yukarıdaki sayfalarda bulunuyor.

## Emin olunamayan noktalar
- Test 23'te "A" sonucu Bölüm 22'ye yönleniyor, ama sonuçtaki kapanış cümlesi Bölüm 25'ten (s. 370). Ayrım iki bölümde de işlendiği için 22 seçildi. İstenirse 25 yapılabilir.
- Test 29'da "C" sonucu 22'ye yönleniyor, ama Bölüm 25 (s. 371) ve Bölüm 27'den (s. 396–397) de cümle alıyor.
- Test 21'in son seviyesindeki alıntı kısaltılmış (yukarıya bakın).
- Hesap testlerinde (22, 24, 26) sorular kişinin kendi ilişkisini değerlendirmesini istiyor. İlişkisi olmayan kullanıcı için bir "ilişkim yok" seçeneği tasarımda yok (şartnamede de istenmiyor).
- Test 25 "Yeterince iyi" sonucunun riski kitapta doğrudan bu tarza bağlanmıyor. Kitabın genel cümlesi ("Kolay karar ile iyi hayat aynı şey değildir", s. 401) uyarlandı.
