# Sezon 1 (test 1–10) düzeltme raporu

Teslim dosyası: `/home/claude/askonomi/_kaynak/icerik_s1.py` (10 test, `ICERIK = {}` + atamalar, import yok).
Kontroller: `ast.parse` geçti. Anahtar tutarlılığı (her sonuç her soruda bir kez), soru ve seçenek sayıları, sonuç metni 50–90 kelime (hepsi 51–71), noktalı virgül yok, kanca tek cümle, yasak bölüm (10–14, 20, 21) yönlendirmesi yok, mit testinde 3 doğru / 3 yanlış, mit ve çift `bolum` alanı LISTE ile aynı.

Sayfa numaraları `bolum/NN.txt` dosyalarındaki `[s. NNN]` işaretlerinden alındı. Not: `dizin.txt`'teki sayfa numaraları bu işaretlerle uyuşmuyor (ör. dizin "Kıskançlık, 243" diyor, bölüm 19 s. 271'de başlıyor). Dizin eski bir dizgiden kalmış olabilir.

Genel değişiklikler (bütün testlerde):
- Taslaktaki bütün noktalı virgüller kaldırıldı (sorularda ve sonuçlarda).
- Birden çok cümleli kancalar tek cümleye indirildi.
- Kitapta hiç geçmeyen iktisat terimleri çıkarıldı: "azalan marjinal fayda", "esnek olmayan talep", "risk sever", "tamamlayıcı mallar (çay-şeker)", "denk eşleşme", "açığa vurulan tercih" (kitap "açıklanmış tercih" diyor, s. 68). Tüm kitapta arandı, hiçbiri yok.
- Kitap "fiyat" dilini eleştirdiği için ("Aşk piyasası vardır; sevgilinin fiyat etiketi yoktur.", s. 82) sonuç metinlerinde insanlara fiyat biçen ifadeler kullanılmadı. Başlıklar onaylı olduğu için olduğu gibi kaldı.

---

## 1. fiyatin-ne — "Aşk piyasasında fiyatın ne?" (profil)
Dayanak: Bölüm 05 s. 74, 82, Bölüm 03 s. 49–50, Bölüm 06 s. 96–97, Bölüm 01 s. 20, Bölüm 24 s. 348–350, Bölüm 25 s. 367–368.

Değişenler:
- Kanca "Herkesin bir fiyatı var" kitapla çelişiyordu (s. 81: "Bir insanın fiyatı yoktur."). Yerine: "Sevgilinin fiyat etiketi yok, ama senin gözünde aşkın bir bedeli var." (s. 82'ye dayanıyor).
- Sonuç adları "Senin fiyatın" yerine "Senin bedelin" oldu. Beş sonuç kitabın listesine yaslanıyor: "Zaman, dikkat, bağlılık, güven ve vazgeçilen alternatifler çoğu romantik seçimin içinde çok daha doğrudan yer alır." (s. 74)
- H sonucu "Heyecan" yerine "Yenilik" oldu. Taslaktaki "azalan marjinal fayda" kitapta yok, 27'ye yönlendirmesi de yanlıştı. Artık Bölüm 25 "Yenilik de Yatırım mıdır?" bölümüne dayanıyor.
- O sonucu Bölüm 19'dan 24'e yönlendirildi (mahremiyet ve kişisel alan s. 350'de işleniyor). Bölüm 19 sorusu bu testten çıkarıldı.
- Soru 2 H seçeneği ("Hiç beklemediğin anda bir sürpriz") ve soru 4 Z seçeneği yenilik ve zaman temasına göre güncellendi. Diğer sorulara dokunulmadı.

Olgusal iddialar:
- Z: zaman temel kıt kaynak → s. 49: "hiçbirimiz günün sonuna yirmi beşinci saati ekleyemeyiz". Zamanın anlamı koşula bağlı → s. 50: "hangi koşullarda ve hangi alternatiflerden vazgeçilerek verildiğiyle birlikte düşünülmelidir". Alıntı → s. 49: "“Bana zaman ayırmıyor, demek ki beni sevmiyor” çıkarımı her durumda doğru değildir." (birebir)
- D: para dışı kaynaklar da sinyal, dikkat başta → s. 97: "Romantik ilişkide para dışındaki kıt kaynaklar da sinyal taşıyabilir. Dikkat, zaman, emek ve tutarlılık bunların başında gelir." Kişisiz pahalı hediye ve ayrıntıyı hatırlayan ucuz hediye → s. 96: "Ucuz fakat kişinin aylar önce söylediği küçük bir ayrıntıyı hatırlatan hediye ise … dikkat hakkında güçlü bilgi taşıyabilir."
- G: güven sermayesi ve işlem maliyeti → s. 348: "Böylece ilişkinin günlük işlem maliyetleri azalır." Banka benzetmesinin sınırı → s. 349: "Küçük bir gecikme yılların güvenini yok etmeyebilir, ama tek bir büyük ihanet kişinin geçmiş hakkındaki yorumunu tamamen değiştirebilir." Sürekli kanıt istemek → s. 97: "Sürekli yeni kanıt isteyen ilişki, aslında hiçbir sinyalin yeterince güvenilir kabul edilmediği ilişkiye dönüşebilir."
- O: sık görüşme ve kişisel alan → s. 20: "Biri için sık görüşmek ilişkinin kalitesinin temel göstergesiyken başka biri için kişisel alanın korunması aynı derecede değerli olabilir." Mahremiyet → s. 350: "Mahremiyet, partnerden gizli ikinci bir hayat sürdürmekle aynı şey değildir."
- H: yenilik araştırması (Aron vd., 2000) → s. 367: "Birlikte yeni ve uyarıcı deneyimler yaşamak bazı çiftlerde ilişki kalitesini geçici veya daha uzun süreli biçimde destekleyebilir". Harcama değil nitelik → s. 368: "Yenilik harcamanın büyüklüğü değil, rutin dışı ortak deneyimin niteliğiyle ilgilidir." Alışma → s. 368: "İnsan yeni deneyimlere de alışabilir ve yaşamın tamamını sürekli uyarılma arayışına çevirmek sürdürülebilir değildir."

Çıkarılanlar: "azalan marjinal fayda" (kitapta yok). "İktisatta değer kıtlıktan doğar" (kitap tersini söylüyor, s. 57: kıtlık tek başına değer yaratmaz).

## 2. kacan-mi-kovalanan-mi — "Kaçan mısın, kovalanan mı?" (profil)
Dayanak: Bölüm 03 s. 57, Bölüm 05 s. 75, 82, Bölüm 06 s. 90, 98, 100, Bölüm 04 s. 71, Bölüm 02 s. 43, Bölüm 26.

Değişenler:
- K sonucu kitapla çelişiyordu ("İşe yarıyor"). Kitap "elde edilmesi zoru oyna" tavsiyesine mesafeli. Metin s. 57'ye göre yeniden yazıldı.
- V sonucundaki "bolca arz edilen şeyin değeri karşı tarafın gözünde düşer" kitapta yok. Yerine iki taraflı eşleşme kuralı (s. 75) ve fedakârlığın karşılığı garanti etmemesi (s. 82) kondu.
- D sonucunun adı "Açık fiyat" yerine "Açık sinyal" oldu. Ucuz söz ve tutarlılık üzerine kitap metnine göre yazıldı.
- S sonucu ("Seyirci: Kenarda bekleyen") reddedilme maliyeti (s. 71) ve "karar vermemek de karardır" (s. 43) üzerine kuruldu. Yönlendirme 26 olarak kaldı.
- Sorulara dokunulmadı, yalnız noktalı virgül temizlendi.

Olgusal iddialar:
- K: s. 57: "Kıtlık tek başına değer yaratmaz; kıt olan şeyin aynı zamanda istenmesi gerekir." (metinde virgülle verildi, tırnaksız). s. 57: "Cevap vermemek, sürekli uzak durmak veya karşı tarafı belirsizlik içinde tutmak bazı durumlarda ilgiyi artırmak yerine ilişkiyi sona erdirebilir." Kitap sezgiyi bütünüyle reddetmiyor → s. 57: "Kıtlık romantik algıyı etkileyebilecek unsurlardan biri olabilir; fakat aşkın evrensel stratejisi değildir."
- V: s. 75: "Romantik ilişkide ise aynı anda iki tercih sistemi çalışır." Alıntı → s. 75: "Çok istemek, tek başına eşleşme üretmez." (birebir). s. 82: "Romantik ilişkide yaptığınız harcama veya fedakârlık karşı tarafın sizi seçmesini garanti etmez." ve "sevgilinin fiyat etiketi yoktur."
- D: s. 90: "Aynı cümleyi samimi olmayan kişinin de kolayca söyleyebilmesi, sözün ayırt edici gücünü sınırlar." s. 98: "Uzun ilişkinin güçlü sinyallerinden biri bu nedenle gösteriş değil, tutarlılıktır." s. 100: aynı davranış "bir insan için güçlü ilginin göstergesi olabilirken başka biri için sınır ihlali olarak algılanabilir."
- S: s. 71: "Reddedilme riski, zaman, hareket özgürlüğü, kariyer fırsatı ve duygusal kırılganlık da kararın maliyetleri arasındadır." Alıntı → s. 43: "Karar vermemek de zaman geçtiği için fiilen bir karardır." (birebir)

## 3. kalp-mi-akil-mi — "Kalbin mi hesap yapıyor, aklın mı?" (senaryo)
Dayanak: tamamen Bölüm 02 (s. 32, 36–44). Bütün sonuçlar 02'ye yönlendirildi (önceden 25, 01, 04 de vardı).

Değişenler:
- İki soru bölümden gelen örneklerle değiştirildi. Eski "Bir ilişkinin bitmesi gerektiğini nasıl anlarsın?" yerine "Gece ikide büyük bir kavga" senaryosu geldi (Aşkonomi Kutusu "Gece İki Kararı ile Sabah On Kararı", s. 39). Eski "Hediye alırken…" yerine "Kâğıt üzerinde bütün kriterlerine uyuyor ama hiçbir şey hissetmedin" senaryosu geldi ("Listeye Uyan Kişi Neden Bazen Hiçbir Şey Hissettirmez?", s. 35–36). Diğer dört soru korundu.
- R: "Gelecek planı yapmak yatırımdır" (25'e yönlendiriyordu) yerine bölüm 02'nin rasyonellik tanımı ve muhasebe uyarısı kondu.
- T: "risk sever" terimi çıkarıldı (kitapta yok). Fedakârlık ve yoğun duygu anı üzerine kuruldu.
- S: "zihinsel kestirmeler" kitapta Bölüm 02'de, 04'te değil. Yönlendirme düzeltildi.
- D: Bölüm 02'nin "farklı sorular" ayrımına dayandırıldı.

Olgusal iddialar:
- R: s. 32: "Ekonomik rasyonellik bu nedenle yalnız en fazla para kazandıran seçeneği bulmak değildir. Bireyin değer verdiği farklı amaçlar arasında tercih yapabilmesiyle ilgilidir." Bağlılığı ertelemek → s. 43 ("ortak hayat kurmak için gerekli bağlılığı sürekli erteleyebilir"). Alıntı → s. 40–41: "Rasyonellik ilişkinin sürekli muhasebesini yapmak değil, önemli yeni bilgi geldiğinde eski hükmü değiştirebilme kapasitesini korumaktır." (birebir)
- T: s. 40: "Ortak hayat onun için gelir farkından daha değerliyse bu seçim kendi tercihleri içinde anlaşılabilir." s. 39: "Yoğun özlem sırasında “Onsuz yaşayamam” hissi son derece gerçek olabilir; fakat o anda gelecekte nasıl hissedeceğimizi kusursuz tahmin ettiğimiz anlamına gelmez." s. 39: "Rasyonellik burada duygusuzluk değildir. Geri dönüşü zor kararları mümkün olduğunda birden fazla duygusal durumda değerlendirebilme kapasitesidir."
- S: s. 36: "Tversky ve Kahneman’ın (1974) klasik çalışmalarında bu sezgisel kestirmeler, belirsizlik altında karar vermeyi kolaylaştıran fakat bazı durumlarda sistematik hatalara yol açabilen yöntemler olarak ele alınmıştır." s. 36: "Yakın zamanda yaşanan kötü ayrılık yeni insanlara ilişkin risk algısını büyütebilir." s. 37: "hangi durumda sezginin ne kadar iyi rehber olduğunu fark edebilmek olabilir."
- D: s. 44: "“Onu seviyor muyum?” ile “Onunla yaşayabilir miyim?” farklı sorulardır." (birebir). s. 43: "Duygu neyi önemsediğimizi bildirir. Akıl sonuçları düşünmemize yardım eder." s. 43: "Karar vermemek de zaman geçtiği için fiilen bir karardır."

## 4. ilk-bulusma-sinyali — "İlk buluşmada verdiğin sinyal aslında ne diyor?" (profil)
Dayanak: Bölüm 06 s. 88, 90–93, 98–101, Bölüm 08 s. 121, Bölüm 02 s. 38.

Değişenler:
- E: "pahalı sinyal = inandırıcı" kitapta ihtiyatla veriliyor. "Maliyet tek başına samimiyet sertifikası değildir" uyarısı eklendi.
- V: "vitrin en çok vitrine bakanları çeker" çıkarıldı (kitapta yok). Veblen ve servet sinyalinin birden çok yorumu eklendi. Yönlendirme 08 olarak kaldı.
- D: kitabın "ucuz söz" ve "ilk buluşmadaki nezaket küçük bir veridir" örneğiyle yeniden yazıldı. Yönlendirme 24 olarak kaldı.
- G: "bilgi eksikliği kısa vadede çekim yaratır" iddiası Bölüm 02'nin ihtiyatlı ifadesine çekildi. Yönlendirme 03'ten 02'ye alındı (dayandığı cümle orada).
- Sorulara dokunulmadı (noktalı virgüller virgüle çevrildi).

Olgusal iddialar:
- E: s. 90: "Romantik ilişkide bazı güçlü sinyallerin cüzdandan değil, takvimden gelmesinin nedeni budur." s. 92: "bazı özelliklerin taklit edilmesinin güç olması onları daha bilgilendirici hale getirebilir." Alıntı → s. 91: "Maliyet tek başına samimiyet sertifikası değildir." (birebir)
- V: Veblen ve gösterişçi tüketim → s. 93. Görünür tüketim ve kapasite → s. 93: "Gelir banka hesabında görünmezken otomobil, tatil, ev, kıyafet veya restoran tercihi ekonomik kapasite hakkında kolayca gözlenen işaretlere dönüşebilir." s. 121: "Ancak servet sinyalinin birden fazla yorumu olabilir." s. 100: "Pahalı restoran bir kişi için cömertlik, başka biri için gösteriş olabilir." s. 121: "Paranın görünür olması, herkesin gördüğünden hoşlanacağı anlamına gelmez."
- D: s. 88: "Gerçekten güvenilir insan da güvenilmez insan da kendisini güvenilir olarak tanıtabilir." s. 101: "İlk buluşmadaki nezaket küçük bir veridir. Altı ay boyunca gözlenen tutarlılık daha fazla bilgi sağlar."
- G: s. 38: "Belirsizlik, ulaşılmazlık veya tutarsızlık bazen duygusal yoğunluğu artırabilir." Alıntı → s. 38: "Yoğunluk ile ilişkinin kalitesi aynı değişken değildir." (birebir). s. 92: "İnsanlar görünmeyen nitelikler hakkında gözlenebilir özelliklerden çıkarım yapar".

## 5. guzellik-mitleri — "Güzellik hakkında inandığın 6 şeyden kaçı doğru?" (mit, bolum 07)
Dayanak: Bölüm 07 s. 104–107, 110–111, 114, 116.

Kaynak kontrolü:
- Hamermesh ve Biddle (1994): kitapta var (s. 105–106). Kitabın rakamıyla yazıldı.
- Langlois vd. (2000): kitapta var (s. 103–105). Hem uzlaşma hem halo etkisi için kitabın ifadesi kullanıldı.
- Dion, Berscheid ve Walster (1972): kitapta YOK. Halo etkisi iddiası Langlois meta-analizine (s. 105) bağlandı.
- Feingold (1988): kitapta YOK. Çekicilik benzerliği iddiası Webster vd. (2024, s. 111) ile değiştirildi.
- Hunt, Eastwick ve Finkel (2015): kitapta YOK. İddia çıkarıldı. Yerine kitaptaki Eastwick vd. (2014) bulgusu kondu (s. 110).
- Taslağın 2. iddiası ("Güzellik primi yalnız modellik gibi mesleklerde vardır" → Yanlış, "aynı çalışmalar başka mesleklerde de buluyor") kitapta desteklenmiyor. Kitabın aktardığı Deryugina ve Shurchkov deneyi primin bağlama bağlı olduğunu söylüyor. İddia "Güzellik primi her işte aynı büyüklükte ortaya çıkar" (Yanlış) olarak yeniden yazıldı.

İddialar (3 doğru, 3 yanlış):
1. Doğru. Ortalamanın altındakiler daha az kazanabilir → s. 105–106: "görüşmeciler tarafından ortalamanın altında çekici değerlendirilen kişilerin ortalama görünümlülere göre yaklaşık yüzde 5–10 daha düşük kazanç elde ettiğini". Uyarı alıntısı → s. 106: "Fakat bu bulguyu “Güzel olursanız yüzde şu kadar daha fazla kazanırsınız” formülüne çevirmemek gerekir." (birebir). İddia kitabın ihtiyatına uygun olarak "kazanabilir" diye kuruldu.
2. Yanlış. Prim her işte aynı → s. 106–107: "çekici çalışanlara daha yüksek ücret teklif edilmesi, görünüşün performansla ilişkili olmasının beklendiği görevde ortaya çıkarken analitik ve veri girişi görevlerinde benzer prim görülmemiştir." ve s. 107: "başlangıçtaki görünüş temelli değerlendirmelerin etkisi azalabilmiştir."
3. Yanlış. İnsanlar çok farklı düşünür → s. 104: "Langlois ve arkadaşlarının (2000) on bir meta-analizden oluşan kapsamlı çalışması, insanların kimin çekici bulunduğu konusunda hem aynı kültür içinde hem farklı kültürler arasında belirli düzeyde görüş birliği gösterebildiğini ortaya koymuştur." Evrensel standart değil → s. 104: "Bu sonuç “Dünyada tek ve evrensel güzellik standardı vardır” anlamına gelmez."
4. Doğru. Halo etkisi → s. 105: "çekicilik stereotipi veya daha geniş anlamıyla halo etkisi" ve "çekici bulunan çocuk ve yetişkinlerin daha olumlu değerlendirilebildiği". Sınır → s. 105: "o kişilerin gerçekten bütün alanlarda daha iyi olduğu anlamına gelmez."
5. Doğru. Çekicilikte benzerlik → s. 111: "karma cinsiyetli çiftlerde iki partnerin dış gözlemciler tarafından değerlendirilen fiziksel çekicilikleri arasında pozitif ilişki bulunduğunu … yaklaşık r = 0,39 düzeyindedir". s. 111: "Aşk piyasasının düzenlilikleri bireyin kaderi değildir."
6. Yanlış. Etki erkeklerde çok daha büyük → s. 110: "gerçek romantik değerlendirmelerde çekiciliğin etkisindeki cinsiyet farkı oldukça küçüktü ve anlamlı bulunmadı." ve "Fiziksel çekicilik her iki taraf için de romantik değerlendirmede anlamlı rol oynayabilir."

Seviyeler:
- 0 "Vitrine kanan": alıntı s. 110: "İnsan davranışı sloganlardan daha karmaşıktır." s. 116: "Güzellik önemlidir." ve "Fakat güzellik tek ve nesnel bir değer değildir." Taslaktaki "Görünüş sandığından daha fazla ödüllendiriliyor" çıkarıldı (kitapta bu genellik yok).
- 3 "Göz kararı": alıntı s. 105: "Güzel yüz, laboratuvar raporu değildir." (birebir)
- 5 "Piyasa analisti": s. 114: "Toplum hangi alanlarda güzelliği ödüllendiriyor ve bu ödül ne ölçüde işlevsel olarak ilgili?" (birebir)

Kanca "Veriler aynı şeyi söylemiyor" kitabın ara yolunu (s. 104: "Daha gerçekçi sonuç ikisinin arasında yer alır.") yansıtmıyordu. Yerine: "“Güzellik bakanın gözündedir” derler ama araştırmalar o kadar emin değil."

## 6. para-konusulunca — "Para konuşulunca ilişkinde ne oluyor?" (senaryo)
Dayanak: tamamen Bölüm 08 (s. 119, 124–125, 127–129, 132–133). Bütün sonuçlar 08'e yönlendirildi (önceden 15, 29, 31 vardı).

Değişenler:
- Soru 4 ("Gelirleriniz arasında büyük fark var") kitabın Aşkonomi Kutusu'ndaki örnekle somutlaştırıldı: "Biri ayda 100, diğeri 40 birim kazanıyor" (s. 133). Soru 2 A seçeneği soru 4 ile çakışmasın diye sadeleştirildi.
- O: "Aşk yetiyorsa neden evleniyoruz?" (Bölüm 15'e gönderme) yerine Gladstone vd. (2022) ortak hesap bulgusu ve kitabın uyarısı kondu.
- A: "Modern ilişkiler bu yöne kayıyor" (Bölüm 29) iddiası çıkarıldı, kitapta Bölüm 08 bağlamında böyle bir eğilim iddiası yok. Ayrı hesap ve özgürlük ilişkisi konuldu.
- K: tasarruf ve harcama çatışması kitabın kendi örneğine bağlandı (s. 128), Papp vd. (2009) bulgusu kitabın ihtiyatıyla eklendi.
- C: aşk endüstrisi (31) yerine "para sevginin yerine geçebilir mi" bölümü (s. 128–129) kondu.
- Senaryolar ekonomik kontrolü normalleştirmiyor. Kitap bu ayrımı s. 129'da yapıyor, sonuçlar buna aykırı bir şey söylemiyor.

Olgusal iddialar:
- O: s. 128: Gladstone vd. (2022) "mali kaynaklarını tamamen birleştiren çiftlerin … ortalama olarak daha yüksek ilişki doyumu bildirdiklerini". Evrensel reçete değil → s. 128: "“İyi evlilik için ortak banka hesabı açın” biçiminde evrensel reçeteye dönüştürülemez" ve "ortak hesap da kendiliğinden güven yaratmaz."
- A: s. 128: "Ayrı hesap kullanan çift kötü ilişkiye mahkûm olmadığı gibi". s. 125: "birlikte kalmayı daha özgür seçim haline getirir." Para dışı katkı → s. 133: "birinin parası, diğerinin zamanı veya bakım emeği daha büyük olabilir." Alıntı → s. 133: "Aşk bütçesinin bütün satırları para cinsinden yazılmaz." (birebir)
- K: s. 128: "Bir eş için tasarruf güvenlik, diğeri için yaşamın ertelenmesi olabilir." Bütçe ve değerler → s. 128: "Bütçe rakamlardan oluşur; para kavgası çoğu zaman değerlerden." (noktalı virgül yasağı nedeniyle tırnaksız aktarıldı). Papp vd. (2009) → s. 127: "para tartışmaları en sık yaşanan çatışma türü değildi; ancak diğer tartışmalara göre daha tekrarlayıcı, daha önemli ve çözülmesi daha zor olma eğilimi gösteriyordu."
- C: s. 129: "para “Seni seviyorum” cümlesinin davranışa dönüşme yollarından biri olabilir." s. 129: "Fakat para sevginin yerine de konabilir." s. 129: "Bir taraf para üreterek katkıda bulunurken diğeri zaman ve duygusal varlık beklemektedir." s. 129: "para her zaman zamanın, dikkatin ve bakımın tam ikamesi değildir."

## 7. benzer-mi-zit-mi — "Kendine benzeyeni mi seçiyorsun, zıttını mı?" (profil)
Dayanak: Bölüm 09 s. 137–139, 145, 147–149, Bölüm 15 s. 225–226.

Değişenler:
- B: "denk eşleşme" yerine kitabın terimleri "seçici eşleşme / homogami" kullanıldı. "Eşitsizlik büyüyebilir" iddiası kitabın ihtiyatlı ifadesine çekildi ("bazen … yoğunlaştırabilir"). Kitap, eşleşmenin eşitsizlik artışını açıklama gücünün sınırlı olduğunu vurguluyor (s. 144).
- Z: yönlendirme 04'ten 09'a alındı (zıt kutuplar tartışması Bölüm 09'da). "Araştırmalar desteklemiyor" yerine kitabın kendi ifadesi kullanıldı.
- Y: "yatırım mantığı" çıkarıldı. Kitabın "yukarı evlenmek" diline itirazı (s. 148) eklendi. Yönlendirme 05'ten 09'a alındı.
- T: "tamamlayıcı mallar, çay ile şeker" kitapta yok, çıkarıldı. Kitabın benzerlik ve tamamlayıcılık tartışması ile uzmanlaşmanın maliyeti kondu (Bölüm 15'e yönlendirme korunuyor, uzmanlaşma s. 225–226'da).
- Sorulara dokunulmadı.

Olgusal iddialar:
- B: s. 137: "İnsanlar birçok özellik bakımından kendilerine benzeyen kişilerle beklenenden daha sık eşleşir." Terimler → s. 137: "assortative mating, yani seçici eşleşme … homogami". Karşılaşma kanalı → s. 139 (Kalmijn, üniversite örneği). s. 145: "Aşk eşitsizliği tek başına yaratmaz; fakat bazen mevcut eşitsizlikleri aynı hanede yoğunlaştırabilir."
- Z: s. 137 (yukarıdaki cümle). s. 139: "“zıt kutuplar çeker” ile “benzer benzeri bulur” sözlerinin ikisi de tek başına ilişki teorisi değildir." s. 149: "Müzik zevkinizin farklı olması kolayca yönetilebilirken çocuk isteği konusunda tamamen ters beklentileriniz bulunması çok daha temel çatışma yaratabilir."
- Y: s. 148: "Bu dil, çok boyutlu insan özelliklerini tek bir sıralamaya indirger." ve "Böyle çiftin hangisi “yukarı” evlenmiştir?"
- T: s. 139: "benzerlik ile tamamlayıcılık birbirinin alternatifi değildir." s. 138: "biri planlamada, diğeri sosyal ilişkilerde daha güçlü olabilir." s. 147: "Kariyerleri farklı sektörlerdeyse ekonomik riskleri çeşitlenebilir" ve "tamamlayıcılık zaman zaman çok katı toplumsal cinsiyet uzmanlaşmasına bağlanmıştır". s. 226: "Üstelik uzmanlaşmanın uzun dönemli maliyeti olabilir. … ayrılık halinde maliyeti taraflardan birinin üzerinde biriken ilişkiye özgü yatırım haline gelebilir."

## 8. ihtiyac-arzu-tercih — "Sevgilin ihtiyaç mı, arzu mu, tercih mi?" (profil)
Dayanak: Bölüm 04 s. 63, 66, 68, 70–71, Bölüm 01 s. 16, Bölüm 05 s. 83, Bölüm 22 s. 311, 314.

Değişenler:
- I: "esnek olmayan talep" kitapta yok, çıkarıldı. Kitabın ihtiyaç tanımı (Aşkonomi Kutusu, s. 70) ve ihtiyaç ile bağımlılık ayrımı (s. 70–71) kondu.
- A: "azalan marjinal fayda" kitapta yok, çıkarıldı. Kitabın arzu tanımı kondu. Yönlendirme 01 olarak kaldı ("Arzu, Aşk ve Sevgi Aynı Şey mi?" s. 16–17).
- T: "açığa vurulan tercih" yerine kitabın terimi "açıklanmış tercih" ve kitabın ihtiyat notu kondu.
- L: kitabın uzun ilişki ve ilişkiye özgü sermaye anlatımı ile Bölüm 22'nin uyarısı kondu. Bölüm 22 sorusu (başlık) korundu.
- Sorularda yalnız noktalı virgüller temizlendi. Soru 5'te I seçeneği ("Panik") diğerleriyle eşit uzunluğa getirildi: "Paniğe kapılırım, onsuz eksik kalırım".

Olgusal iddialar:
- I: s. 70: "İhtiyaç, iyi oluş için önemli olabilecek daha genel koşulu anlatır. Aidiyet, yakınlık veya güven bunlara örnek olabilir. Bunların mutlaka romantik ilişki içinde karşılanması gerekmez." İki anlam → s. 71: "Birinde insanlar birbirlerinin hayatını zenginleştirdiği için karşılıklı bağ vardır; diğerinde kişinin başka gerçek seçeneği olmadığı için bağımlılık bulunur." Alıntı → s. 71: "Bağlılık, çıkış imkânının tamamen yokluğu değildir." (birebir)
- A: s. 70: "Arzu, bu genel ihtiyacın belirli nesneye, kişiye veya ilişki biçimine yönelmiş halidir." Alıntı → s. 66: "İnsan yakınlığa ihtiyaç duyabilir ama herhangi birine âşık olmaz." (birebir). s. 63: "Çok güçlü cinsel çekim yaratan kişiyle yaşam tarzımız uyuşmayabilir." (metinde "çok güçlü çekim hissedilen kişi" diye verildi)
- T: s. 70: "Tercih ise birden fazla arzu aynı anda gerçekleştirilemediğinde hangisine daha fazla ağırlık verdiğimizi gösterir." s. 68: "İktisat burada açıklanmış tercih fikrinden yararlanır." İhtiyat → s. 68: "Seçtiğimiz şey her zaman en çok istediğimiz şey değildir; bazen yalnız ulaşabildiğimiz seçenek olabilir."
- L: s. 16: "güven, bakım, alışkanlık ve ortak kimlik daha büyük yer tutabilir." s. 83: "Birlikte kurulan tarih başka bir partnerle anında yeniden üretilemez." Alıntı → s. 314: "Bir ilişkide uzun süre kalmış olmak tek başına kalmaya devam etmek için yeterli neden değildir" (birebir). Soru → s. 311 (Bölüm 22 alt başlığı) ve s. 324.

## 9. askin-alti-tanimi — "Aşkın 6 tanımından hangisi senin?" (profil)
Kontrol sonucu: John Alan Lee Bölüm 01'de geçiyor (s. 19–20, ayrıca s. 25'te Lee 1973 ölçek olarak anılıyor). Test Lee'nin altı tarzı üzerinde kaldı, ama tanımlar kitabın Bölüm 01'deki ifadelerine göre yeniden yazıldı. Başlık değişmedi.

Değişenler:
- Kanca: "1973’te … öne sürdü" yerine kitabın ifadesine yakın: "aşkı renkler gibi altı temel tarza ayırdı" (s. 19).
- Her sonuçta Lee'nin tarzı kitabın tanımıyla veriliyor. Agape sonucunda kitabın "değişmez kişilik tipleri değildir" uyarısı da yer alıyor.
- Yönlendirmeler: E→01, S→24 (güven sermayesi), L→26 (taslakta 27 idi; "Her Kapıyı Açık Tutmak" Bölüm 26'da), P→09 (taslakta 15 idi; uyumluluk ve benzerlik Bölüm 09'da), M→19, A→16.
- P sonucundan "Aşk tek başına yetiyorsa neden sözleşme yapıyoruz?" çıkarıldı. M sonucundan "kaybetme korkusu büyüdükçe kıskançlık büyür" genellemesi çıkarıldı, yerine kitabın kıskançlık-sevgi ayrımı kondu.
- Sorular iyi, dokunulmadı.

Olgusal iddialar:
- Lee ve renk analojisi → s. 19: "Lee (1973), aşk biçimlerini renkler analojisiyle sınıflandırarak altı temel tarz tanımlamıştır."
- Tanımlar → s. 19: "Eros, güçlü romantik ve fiziksel çekimin ağır bastığı aşkı; storge, arkadaşlık ve zaman içinde gelişen yakınlığı; ludus, oyunsu ve düşük bağlılıklı ilişki tarzını anlatır. … pragma, daha pratik ve uyumluluk odaklı; mania, yoğun bağımlılık ve kıskançlıkla ilişkili; agape ise özgeci ve verici aşk biçimleri olarak tarif edilir."
- Kişilik tipi uyarısı (A) → s. 19: "Bu sınıflandırmayı insanların değişmez kişilik tipleri gibi okumamak gerekir."
- E: s. 17: "ödül ve motivasyon sistemleriyle ilişkili beyin bölgelerinin erken dönem romantik aşkta etkinleşebildiğini". s. 18: "“aşk uyuşturucu gibidir” cümlesine fazla hızlı geçmemek gerekir." s. 16: otuz yıllık evlilikte "güven, bakım, alışkanlık ve ortak kimlik daha büyük yer tutabilir."
- S: s. 98: güven "farklı koşullarda gözlenen davranışların birbirine eklenmesiyle oluşur." s. 101: "Geçmiş davranışlardan oluşan bir güven sermayesi birikmiştir."
- L: s. 386: "Fakat hiçbir seçeneğe bağlanmamanın da fırsat maliyeti vardır." s. 387: "o da ilişkinin her an başka seçeneğe değiştirilebileceğini düşünür." Alıntı → s. 387: "Özgürlük, kapıyı kapatmanın kendi kararımız olmasıdır." (birebir)
- P: s. 149 (müzik zevki ve çocuk isteği, yukarıda). s. 149: "Romantik uyum, benzerlik sayısını topladığımız bir puan değildir."
- M: s. 274–275: "Kıskançlığın varlığı ilişkinin değerli olduğunu gösterebilir; kıskançlığın şiddeti sevginin miktarını ölçmez." (noktalı virgül yerine virgülle, tırnaksız). Soru → s. 271 (Bölüm 19 alt başlığı: "Neyi Kaybetmekten Korkuyoruz?").
- A: s. 242: bakım ve zihinsel yük "iyi yapıldıklarında tam tersine görünmez hale gelebilir." s. 242: "Bir kişinin bakım vermeyi sevmesi, bu sorumluluğun sonsuza kadar yalnız ona ait olması gerektiği anlamına gelmez".

## 10. birbirinizi-fiyatlamak — "Birbirinizi ne kadar doğru “fiyatlıyorsunuz”?" (çift)
Dayanak: Bölüm 05 s. 75, 82, Bölüm 08 s. 128, 132, Bölüm 09 s. 147, 149, Bölüm 04 s. 69.

Değişenler:
- `bolum` alanı "09" idi, LISTE'deki "05" yapıldı. Seviye metinleri ch05'in iki taraflı eşleşme fikrine göre yeniden kuruldu.
- Seviyelerdeki "denk eşleşme" (kitapta yok) ve "doğru takasla ikisi de kazançlı çıkar" (kitapta bu bağlamda yok) çıkarıldı.
- 9+ seviyesindeki "bu kadar benzer iki kişi birbirine yeni şeyler katmayı unutabilir" kitapta yok, çıkarıldı. Yerine benzerliğin ve tercihlerin değişebileceği kondu.
- Soru 6 "Hediye" yerine "Ortak giderler: Yarı yarıya / Gelire göre" oldu (s. 132, iki seçenek eşit çekici). "Bir akşam: " sonundaki boşluk düzeltildi. Diğer sorular korundu.
- Kanca iki cümleydi, tek cümleye indirildi.

Seviye iddiaları:
- 0: s. 75: "Ekonomik açıdan baktığımızda eşleşme, iki ayrı sıralamanın kesişmesidir."
- 3: s. 128: "Bir eş için tasarruf güvenlik, diğeri için yaşamın ertelenmesi olabilir."
- 6: s. 149: "Romantik uyum, benzerlik sayısını topladığımız bir puan değildir." ve müzik zevki ile çocuk isteği örneği (s. 149).
- 9: s. 82: "Aşk piyasası vardır; sevgilinin fiyat etiketi yoktur." (metinde virgülle verildi). s. 147: "Benzerlik ayrıca değişebilir." s. 69: "Aynı insan farklı yaşlarda aynı partner özelliklerine aynı ağırlığı vermek zorunda değildir."

---

## Emin olunamayan veya karar gerektiren noktalar
- Test 10'un `bolum` alanı: İçerik (tercih benzerliği) hem Bölüm 05 hem Bölüm 09 ile ilişkili. LISTE'ye uyularak 05 yapıldı. 09 tercih edilirse yalnız `bolum` alanı değişir, seviye metinleri iki bölümle de uyumlu.
- Birebir alıntılarda kitabın noktalı virgülü olan cümleleri (s. 57, 82, 128, 274–275) tırnak kullanmadan, virgüllü açıklama olarak verdim. Böylece hem noktalı virgül yasağına hem "birebir kopyala" kuralına aykırı düşmüyor.
- Sonuçlardaki "Bedeli şu" cümlelerinin bir kısmı (ör. test 1 D, test 4 D, test 9 S) olgusal iddia değil, yorum. Kitapta doğrudan karşılıkları yok ama kitapla çelişmiyorlar.
- Test 9 yönlendirmeleri tarzla ilişkili bölümlere dağıtıldı (24, 26, 09, 19, 16). Tarzların hepsi yalnız Bölüm 01'de tanımlanıyor. Hepsinin "01" olması isteniyorsa yalnız üçüncü alan değişir.
