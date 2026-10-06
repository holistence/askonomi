# Sezon 2 "Sözleşme" (test 11–20): kaynak raporu

Dosya: `/home/claude/askonomi/_kaynak/icerik_s2.py`
Kaynak: v45 bölüm metinleri (`bolum/NN.txt`), sayfa numaraları `[s. NNN]` işaretlerinden alındı.
Baştan sona okunan bölümler: 15, 16, 17, 18, 19, 22, 24, 25, 28, 29. Bölüm 01'den yalnız s. 21–22 (aşkın tarihi) okundu.
Bölüm 10–14, 20, 21'e yönlendirme yok, bu konulardan soru yok. Bölüm 20'deki çeyiz ve görücü usulü malzemesi bilerek kullanılmadı.

Kontroller:
- `ast.parse` geçti. Dosyada import yok.
- Tutarlılık betiği geçti: her sonuç anahtarı her soruda bir kez geçiyor. Mit testlerinde 3 doğru, 3 yanlış var. Çift testlerinde 10 ikili soru var. Hesaplayıcı puanları 0–3 arası tam sayı ve ilk seviye 0.
- Noktalı virgül yok.
- Bütün sonuç ve seviye metinleri 50–90 kelime arasında.
- Doğrudan alıntılar normalize edilmiş kitap metninde birebir arandı. Hepsi bulundu.

---

## 11 evlilik-ne (profil): Bölüm 15, s. 223–232

Sonuçlar: Y Yatırım, S Sigorta, O Ortaklık, T Yol arkadaşlığı, H Sözleşme. Sonuçların hepsi Bölüm 15'e yönleniyor.

| Metindeki iddia | Sayfa | Kitaptaki cümle (kısa) |
|---|---|---|
| İlişkiye özgü yatırım, ilişki bitince başka yerde aynı değeri taşımaz | s. 227–228 | "Bu yatırımların önemli bölümü ilişki sona erdiğinde başka yerde aynı değeri taşımayabilir. Ekonomide bu tür yatırımların ilişkiye özgü olması…" |
| Alıntı: “Yarın hiçbir şey olmamış gibi çekip gitmeyeceğim” | s. 228 | "hukuken tanınmış uzun dönemli ortaklığın “Yarın hiçbir şey olmamış gibi çekip gitmeyeceğim” mesajını daha inandırıcı hale getirerek…" (Matouschek & Rasul) |
| Uzmanlaşma, ayrılıkta maliyeti tek kişide biriken yatırıma dönüşebilir | s. 226 | "ayrılık halinde maliyeti taraflardan birinin üzerinde biriken ilişkiye özgü yatırım haline gelebilir." |
| Eş küçük bir dayanışma ağıdır, iş kaybında diğerinin geliri sürer | s. 227 | "Bir partner işini kaybettiğinde diğerinin geliri devam edebilir… eş… hayatın belirsizliklerine karşı oluşturulan küçük bir dayanışma ağıdır." |
| “İyi günde kötü günde” karşılıklı dayanışma taahhüdüdür | s. 227 | "“İyi günde kötü günde” sözü bu açıdan yalnız romantik vaat değil, belirsiz geleceğe karşı karşılıklı dayanışma taahhüdüdür." |
| Aile kusursuz sigorta şirketi değildir, Kenya deneyi | s. 227 | "Ancak aile kusursuz sigorta şirketi değildir… Robinson'ın (2012) Kenya'da evli çiftlerle yaptığı deneysel çalışma, eşler arasındaki risk paylaşımının eksik kalabildiğini göstermiştir." |
| Becker 1973, evlilik kazanç üreten ortaklık | s. 223 | "Gary Becker'ın 1973 tarihli A Theory of Marriage… evliliği romantik duygunun karşıtı olarak değil… bir ortaklık biçimi olarak incelemekti." |
| Hane zamanı kullanarak kendi içinde değer üretir | s. 224 | "Hane yalnız piyasadan mal satın alan bir tüketici değildir; zaman ve piyasa mallarını kullanarak kendi içinde de değer üretir." |
| Piyasa geliri yalnız bir kişinin adına yazılır | s. 230 | "toplam hane üretimi yüksek olabilir; fakat piyasa geliri yalnız bir kişinin adına yazılır." |
| Stevenson ve Wolfers, tüketim tamamlayıcılığı | s. 226 | "birlikte tüketmekten ve ortak zevklerden elde edilen tüketim tamamlayıcılığı daha önemli hale gelmiş olabilir." Metinde de "olmuş olabilir" diye ihtiyatlı verildi. |
| “Bu insanla neden kalıyorum?” sorusunda gönüllülük payı artar | s. 226 | "klasik ekonomik zorunlulukların azalması kişinin “Bu insanla neden kalıyorum?” sorusundaki gönüllülük payını artırabilir." |
| Nikâh önceden hazırlanmış haklar ve yükümlülükler paketidir | s. 228 (kutu) | "Nikâhın eklediği temel unsur… önceden hazırlanmış bir haklar ve yükümlülükler paketi sunmasıdır. Miras, ortak mülkiyet…" |
| Nikâh hukuki koordinasyon mekanizmasıdır | s. 228 | "belirsiz geleceğe ilişkin önceden hazırlanmış hukuki bir koordinasyon mekanizmasıdır." |
| Bağlılık ile hapis farkı, bağlılığın özgür seçim olarak kalması | s. 228 | "Bağlılık ile hapis arasında ise temel fark vardır… iyi kurum… bağlılığın özgür seçim olmasını koruyan yapıyı aramak zorundadır." |

## 12 gorunmeyen-emek (hesap): Bölüm 16, s. 233–243

Birim: "Görünmeyen Emek Endeksi". Seviyeler 0, 30, 55 ve 80'de başlıyor. Her seviye metni "düşünme aracı" ibaresiyle bitiyor.
Soruların dayanağı: ihtiyacı fark etmek (s. 236, deterjan ve diş macunu), tarihleri hatırlamak (s. 236), ikinci vardiya (s. 235), duygu işi (s. 237), takip etmek (s. 236–237) ve bakım için çalışma düzenini değiştirmek (s. 239–240).

| İddia | Sayfa | Kitaptaki cümle |
|---|---|---|
| Deterjanı kim fark etti, listeye kim ekledi | s. 237 (kutu) | "Fakat deterjanın azaldığını kim fark etti, alışveriş listesine kim ekledi…" |
| Zihinsel yük iyi yapıldığında fark edilmez | s. 237 | "iyi yapıldığında sorun ortaya çıkmaz ve dolayısıyla yapılan iş fark edilmez." |
| Adalet her şeyi yarı yarıya bölmek değildir | s. 238 | "Bir ilişkinin adil olabilmesi için bütün görevlerin matematiksel olarak yüzde 50–50 paylaşılması gerekmez… Çalışma saatleri… farklıysa eşit sayıda görev bile adil olmayabilir." |
| Algılanan hakkaniyet ilişki doyumuyla bağlantılı | s. 238 | "yalnız nesnel görev dağılımının değil, algılanan hakkaniyetin ilişki açısından önemli olduğunu gösterir… daha düşük ilişki doyumuyla ilişkilendirilmiştir." |
| Daminger'in dört aşaması | s. 236 | "Allison Daminger (2019)… bilişsel emek… dört aşama: ihtiyaçları önceden fark etmek, seçenekleri belirlemek, karar vermek ve sonuçları izlemek." |
| “Söyleseydin yapardım”: fiziksel iş paylaşılmış, yönetim yükü paylaşılmamış | s. 236 | "Bir kişi “Söyleseydin yapardım” diyebilir… fiziksel iş paylaşılmış, yönetim yükü paylaşılmamış olabilir." |
| Dikkat de zaman kadar kıt bir kaynaktır | s. 237 | "Çünkü zaman kadar dikkat de kıt kaynaktır" |
| Hochschild ve Machung, ikinci vardiya | s. 235 | "Arlie Hochschild ve Anne Machung'un The Second Shift… ikinci çalışma gününü anlatır." |
| Günün 24 saati değişmez, fazladan ücretsiz saat başka şeylerden eksilir | s. 235 | "Günün yirmi dört saati değişmediği için ücretsiz işe ayrılan fazladan saat, ücretli çalışma, eğitim, uyku, dinlenme… ayrılamayan saattir." |
| Alıntı: “Ücretsiz olmak ile maliyetsiz olmak aynı şey değildir.” | s. 234 | Birebir. |

Bilerek kullanılmayan: ILO (%76) ve OECD (Türkiye 5,2 kat) cinsiyet oranları. Bunlar kitapta var (s. 234–235). Ama kullanıcının kendi sonucuna cinsiyetli bir istatistik eklemek kalıp yargı gibi okunabileceği için koymadım.

## 13 ev-isini-kim-yapiyor (çift): Bölüm 16

Tasarım: Her soru için seçenekler ["Hep aynı kişi", "Sırayla ya da birlikte"]. Seçenekler kişiden bağımsız. Eşleşme, iki partnerin iş bölümünü aynı algılaması demek. Cinsiyetli ifade yok.
Maddelerin dayanağı: fark edip listeye eklemek (s. 236–237), faturalar (s. 238), yemek kararı (s. 235), doğum günü hediyesi (s. 233), bulaşık makinesi ve tabakları kaldırmak (s. 237 kutu), doktor randevuları (s. 230, 233), tatil seçeneklerini araştırmak (s. 236), akrabalarla ilişkiyi sürdürmek ve tartışma sonrası ortamı yumuşatmak (s. 237, duygu işi), işin yapılıp yapılmadığını kontrol etmek (s. 236–237).

| İddia (seviye metinleri) | Sayfa | Kitaptaki cümle |
|---|---|---|
| Bir işi “yapmak” zincirin yalnızca bir halkasıdır | s. 237 | "Bir işi “yapmak”, bazı durumlarda ihtiyacı fark etmekten sonuçlanıp sonuçlanmadığını kontrol etmeye kadar uzanan zincirin yalnız bir halkasıdır." |
| Zihinsel yük iyi yapıldığında fark edilmez | s. 237 | yukarıdaki gibi |
| Eşitsiz dağılım bile “normal” ya da “adil” kabul edilebilir | s. 238 | "eşitsiz bir dağılım taraflarca yine de “normal” veya “adil” kabul edilebilir (Gillespie vd., 2019)." |
| İş bölümü birinin gelecekteki eğitim, gelir ve boş zaman imkânlarını değiştiriyor mu | s. 238–239 | "İş bölümü yalnız bugünkü rahatlığı mı paylaştırıyor, yoksa taraflardan birinin gelecekteki eğitim, gelir, boş zaman ve ekonomik bağımsızlık imkânlarını da…" |

Seviye 4'teki soru ("Hep aynı kişi" dediğiniz işlerde o kişinin kim olduğu konusunda da anlaşıyor musunuz?) motorun kör noktasını açıkça söylüyor. İki kişi de "hep aynı kişi" diyebilir ama farklı kişileri kastediyor olabilirler.

## 14 cocugun-maliyeti (mit): Bölüm 17, s. 245–256

Dağılım: D, Y, D, Y, D, Y (3 doğru, 3 yanlış).

| İddia | D/Y | Sayfa | Kitaptaki cümle |
|---|---|---|---|
| Her yerde geçerli tek bir maliyet rakamı vardır | Y | s. 246 | "maliyet ülkeye, gelir grubuna, kamu hizmetlerinin kapsamına… göre büyük ölçüde değişir… tek rakamlar… ancak belirli ülke, yıl ve varsayımlar altında anlam taşır." |
| En büyük maliyetlerin bir kısmı bütçede görünmez | D | s. 246 | "Daha büyük maliyetlerin bir bölümü bütçede hiç görünmez… para, zaman ve vazgeçilen alternatifler." Esnek çalışma için daha düşük ücret kabul etmek de aynı sayfada geçiyor. |
| Kalabalık aile, daha az eğitimin nedenidir | Y | s. 248–249 | Black vd. (2005), Norveç: "doğum sırası hesaba katıldığında ve ikiz doğumları… kullandıklarında… nedensel etkisi büyük ölçüde ortadan kalkıyordu." s. 249: "korelasyon görmek, birincinin ikincisine neden olduğunu kanıtlamaz." |
| Gelir ve doğurganlık arasındaki negatif ilişki zayıfladı, kimi yerde tersine döndü | D | s. 250 | Doepke vd. (2023): "“yeni bir döneme” girmiştir… negatif ilişki zayıflamış, bazı bağlamlarda tersine dönmüş… kariyer ile aileyi birlikte sürdürmenin ne kadar mümkün olduğudur." |
| Nakit teşvikler doğurganlığı güçlü ve kalıcı artırır | Y | s. 254 | OECD (2024b): "nakit transferlerin doğurganlık üzerinde çoğunlukla yok, küçük veya geçici olumlu etkiler gösterdiğini…" ve "Tek seferlik ödeme, yirmi yıl sürebilecek çocuk yetiştirme maliyetinin küçük bir bölümünü karşılar." Metinde "OECD (2024)" yazıldı, kaynakçadaki etiket 2024b. |
| Danimarka'da yaklaşık %20 çocuk cezası | D | s. 240–241 (Bölüm 16, Bölüm 17 s. 246'da atıf) | Kleven vd. (2019): "uzun dönemli yaklaşık yüzde 20'lik bir çocuk cezası… Bu oran Danimarka'ya özgüdür." s. 241: "ekonomik bedelinin yalnız bir ebeveyne yazılması toplumsal bir düzenlemedir." |

Seviye metinleri:
- Maliyet hesaplanabilir, değer fiyatlandırılamaz; uykusuz gece örneği: s. 253 (kutu). Kitaptaki cümle noktalı virgül içerdiği için alıntı yapılmadı, açımlandı.
- "İnsanlar maliyetini bildikleri halde neden…" sorusu: s. 243.
- Faydaların topluma yayılması, maliyetin aileye kalması: s. 252.
- "üreme hakkı bireye aittir": s. 253.

## 15 kiskanclik (profil): Bölüm 19, s. 271–281 (G sonucu için Bölüm 24)

Sonuçlar:
- R Sınır bekçisi (reaktif kıskançlık)
- D Kaybetme korkusu (duygusal kıskançlık)
- S Sürekli alarm (bilişsel ve şüpheci kıskançlık)
- K Sahiplenme (kontrol)
- T Kıskandıran
- G Güvenli liman

Kontrol davranışı içeren seçenekler (şifreyi bilip kontrol etmek, konum istemek, görüşmeleri azaltmasını istemek) K sonucuna gidiyor. K sonuç metni bunları normalleştirmiyor ve kitaptan alıntıyla sınır çiziyor.

| İddia | Sayfa | Kitaptaki cümle |
|---|---|---|
| Reaktif ve şüpheci kıskançlık ayrımı | s. 275 | "Gerçek ve açık bir sınır ihlaline verilen kıskançlık tepkisi ile yeterli kanıt olmadan sürekli tehdit arayan kıskançlık aynı değildir." |
| Neyin ihlal sayılacağı kültüre ve ilişkiye göre değişir | s. 280 | "Toplumlar hangi davranışın flört, sadakatsizlik veya uygunsuz yakınlık sayılacağı konusunda farklı sınırlar çizebilir… duyguyu tetikleyen olayın anlamı, ilişkinin ve kültürün kurallarından bağımsız değildir." |
| Kaybetme korkusu | s. 271–272 | "elimizde bulunan değerli bir ilişkiyi üçüncü kişiye karşı kaybetmekten korkarız." |
| Pfeiffer ve Wong: duygusal kıskançlıkla romantik sevgi arasında pozitif ilişki | s. 274 | "Pfeiffer ve Wong'un ilk çalışmalarında duygusal kıskançlık ile romantik sevgi arasında belirli pozitif ilişkiler bulunmuştur" |
| Varlığı değeri gösterebilir, şiddeti sevgiyi ölçmez | s. 274–275 | "Kıskançlığın varlığı ilişkinin değerli olduğunu gösterebilir; kıskançlığın şiddeti sevginin miktarını ölçmez." Metinde "şiddet" sözcüğü fiziksel şiddetle karışmasın diye "yoğunluk" diye yazıldı. |
| “Neyi kaybetmekten korkuyoruz?” | s. 271 (bölüm alt başlığı) | Birebir. |
| Bilişsel kıskançlık sevgiyle aynı yönde hareket etmez | s. 274 | "bilişsel kıskançlığın, yani sürekli şüphe ve kuşkunun sevgiyle aynı yönde hareket etmediği görülmüştür." |
| Kalp emojisi arkadaşlık da olabilir, flört de | s. 276 | "bir kalp emojisi arkadaşlık da olabilir, flört de." |
| Kıskançlık alarmdır, alarmın çalması yangını kanıtlamaz | s. 281 | "Kıskançlık ilişkinin alarmıdır; alarmın çalması yangın olduğunu kanıtlamadığı gibi…" (açımlandı) |
| Alıntı: “Bir duygunun anlaşılabilir olması…” | s. 278 | Birebir. |
| Kontrol karşı tarafın davranış alanını sınırlandırır | s. 278 | "diğer kişinin davranış alanını sınırlandırmaya başlar." |
| Sevgi bağlılık yaratır, mülkiyet hakkı yaratmaz | s. 281 | "Sevgi bağlılık yaratabilir; mülkiyet hakkı yaratmaz." (Noktalı virgül yüzünden alıntı yapılmadı, açımlandı.) |
| İspanya, düşük bağlılık ve bilinçli kıskançlık yaratma | s. 277 | "İspanya örnekleminde daha düşük ilişki bağlılığı bildiren kişilerin partnerlerinde bilinçli kıskançlık yaratmayı daha sık kullandığı bulunmuştur (de Miguel & Buss, 2011)." |
| Sinyal alıcının yorumladığı anlamı taşır | s. 277 | "Bir sinyal göndericinin niyetini değil, alıcının yorumladığı anlamı taşır." |
| Güven arttıkça tehdidin algılanışı azalabilir | s. 273 | "güven arttıkça aynı tehdidin algılanışı azalabilir." Bölüm 24, s. 352'de de benzer anlatım var. |
| Güvenin bir bölümü sınırlara saygıdır | s. 277 (kutu) | "Güvenin bir bölümü doğrulanabilir bilgiden, bir bölümü ise belirsizliğe rağmen partnerin sınırlarına saygı göstermeyi kabul etmekten oluşur." |
| Hiç kıskanmayan biri ilgisiz sanılabilir | s. 274 | "Partnerimiz hiç kıskanmıyorsa bizi yeterince önemsemediğini düşünebilir" |

## 16 cok-eslilik-mitleri (mit): Bölüm 18, s. 257–270

Dağılım: D, Y, D, Y, D, Y. Cinsellik içeren malzeme (açık ilişki, cinsel doyum meta-analizi) kullanılmadı.

| İddia | D/Y | Sayfa | Kitaptaki cümle |
|---|---|---|---|
| Toplumların büyük çoğunluğu polijiniye izin vermiştir (%85) | D | s. 258 | "Henrich ve arkadaşlarının (2012)… incelenen insan toplumlarının yaklaşık yüzde 85'i erkeklerin birden fazla eş edinmesine en azından izin vermiştir." |
| Erkeklerin çoğu çok eşliydi | Y | s. 258 | "bu rakam “tarih boyunca erkeklerin yüzde 85'i birden fazla kadınla evliydi” anlamına kesinlikle gelmez… toprak, hayvan, gelir, statü veya siyasi güce bağlı…" |
| Dünya nüfusunun yaklaşık %2'si poligamik hanelerde yaşıyor | D | s. 259 | "Pew Research Center'ın 130 ülke ve bölgeyi kapsayan araştırmasında… yaklaşık yüzde 2'sinin… Batı ve Orta Afrika'nın bazı bölgelerinde çok daha yüksektir." |
| Poliandri hiç görülmemiştir | Y | s. 262–263 | "Starkweather ve Hames (2012)… poliandriye izin veren 53 toplum belirlemiş… sanıldığından daha geniş coğrafi dağılıma sahip" |
| Himalaya kardeş poliandrisi araziyi bölünmekten korur | D | s. 263 | "bölünebilir tarım arazisinin kıt olduğu yerlerde aile mülkünün her kuşakta daha küçük parçalara ayrılmasını önleyebilir… bütün poliandri örneklerini… formüle sıkıştırmamak gerekir." |
| Polijin hanelerde kadınlar her konuda daha az kontrole sahip | Y | s. 260 | Eissler vd. (2025), Burkina Faso: "karar alma genellikle hiyerarşik kalmış… bazı polijin hanelerde kadınlar kendi kazançları üzerinde tek eşli hanelerdeki kadınlardan daha fazla kontrol de sürdürebilmiştir." |

Seviye metinleri:
- Etnografik kayıtların ima ettiğinden çok daha tek eşli bir dünya: s. 259.
- Servet ve statünün aile yapısına çevrildiği kurum: s. 259.
- Nadir kurumların bile tek bir nedeni yok: s. 263.
- İnsan doğası esnek: s. 270.
- Kim karar veriyor, kaynaklar nasıl paylaşılıyor, isteyen çıkabiliyor mu: s. 269.
- Hukuki izin ile eşit pazarlık gücü farklıdır: s. 269.
- "kaç kişi?" sorusuyla bitmez: s. 269.

## 17 iliski-sozlesmesi (senaryo): Bölüm 15 (+16, 22, 24, 25)

Sonuçlar ilişkinin "bozuk maddeleri":

| Anahtar | Madde | Yönlendirme |
|---|---|---|
| K | Kasa | 15 |
| E | Emek | 16 |
| G | Güven | 24 |
| B | Bakım | 25 |
| C | Çıkış | 15 |

| İddia | Sayfa | Kitaptaki cümle |
|---|---|---|
| Haneyi tek karar verici gibi görmek yanıltıcıdır, tercihler kısmen ortak ama özdeş değil | s. 229 | "tercihleri kısmen ortak ama tamamen özdeş olmayan bireylerin oluşturduğu ortaklık" |
| “Bizim paramız” kolay, nasıl paylaşıldığı ayrı soru | s. 230 | "“Bizim paramız” ve “bizim zamanımız” ifadeleri… bunların nasıl paylaşıldığı hâlâ ayrı bir ekonomik sorudur" |
| Pastanın büyüklüğü ve bölünmesi | s. 230 | "evliliğin kazancını yalnız toplam pastanın büyüklüğüyle değerlendiremeyiz. Pastanın nasıl bölündüğünü de bilmemiz gerekir." |
| Zihinsel yük ve “Söyleseydin yapardım” | s. 236 | yukarıda (test 12) |
| İlişki eksik bir sözleşmedir, beş yıl sonraki hastalık ve iş kaybı yazılamaz | s. 349 (kutu) | "beş yıl sonra ortaya çıkacak hastalığı, iş kaybını… önceden eksiksiz yazamayız… eksik sözleşme denir." |
| Yazılamayan durumda iyi niyete ve geçmiş davranışa dayanılır | s. 349 | "birbirlerinin iyi niyetine, adalet anlayışına ve geçmiş davranışlarına dayanırlar." |
| Güven sözleşmenin alternatifi değil, ulaşamadığı yerlerin koşuludur | s. 349 | "güven sözleşmenin alternatifi değildir; sözleşmenin ulaşamadığı alanlarda birlikte yaşayabilmenin koşullarından biridir." (açımlandı) |
| Güvenin hammaddesi tekrar eden tutarlılıktır | s. 348 | "Güvenin asıl hammaddesi bu nedenle büyük romantik jestlerden çok tekrar eden tutarlılık olabilir." |
| Ortak hayat lojistik şirkete dönüşebilir | s. 364 | "ortak hayat giderek yalnız lojistik şirkete dönüşebilir." |
| Ogolsky ve Bowers, 35 çalışma; ilişki süresi bakım davranışlarıyla sürekli pozitif ilişkili değil | s. 364 | "Ogolsky ve Bowers'ın (2013) 35 çalışma ve 12.273 katılımcıyı kapsayan meta-analizinde… ilişki süresinin kendisi bu bakım davranışlarıyla sürekli pozitif ilişki göstermiyordu. Uzun süre birlikte olmak, ilişkinin aktif biçimde iyi korunduğunun kanıtı değildir." |
| Bağlılık ve hapis; ayrılık imkânsızlaşınca kötü ilişkiden çıkış engellenir | s. 228 | "Ayrılığın imkânsız hale gelmesi ilişkiye yatırımı korurken aynı zamanda kötü veya şiddetli ilişkiden çıkışı da engelleyebilir." |
| Sürekli ayrılık tehdidi manipülasyon olabilir | s. 313 | "Partnerini sürekli “Bunu yapmazsan boşanırım” diyerek korkutmak ilişkisel manipülasyon olabilir" |
| Alıntı: “Gitme imkânının artması…” | s. 313 | Birebir. |

## 18 bosanmanin-faturasi (mit): Bölüm 22, s. 311–325

Dağılım: D, Y, Y, D, Y, D. Bölüm 22, s. 321'deki "şiddet ve intihar sonuçları" atfına dokunulmadı.

| İddia | D/Y | Sayfa | Kitaptaki cümle |
|---|---|---|---|
| Toplam gelir değişmese bile kişi başı maliyet artabilir | D | s. 314–315 | "toplam aile geliri hiç değişmese bile kişi başına yaşam maliyeti artabilir… Bir insan eşinden ayrılırken aynı zamanda hane ölçeği ekonomisinden de ayrılır." |
| Tek taraflı boşanma yasaları boşanmayı kalıcı olarak artırdı | Y | s. 320–321 | Wolfers (2006): "geçici artış görülmüş, fakat bu artışın büyük bölümü yaklaşık on yıl içinde tersine dönmüş" |
| "Evliliklerin yarısı boşanmayla biter" evrenseldir | Y | s. 321 | "“evliliklerin yarısı boşanmayla biter” türü tek oranlar bütün ülkeler ve kuşaklar için geçerli evrensel gerçekler değildir… Boşanmayı anlamak için payda en az pay kadar önemlidir." |
| 50 yaş üstünde servet yaklaşık yarıya düştü | D | s. 317, 322 | Lin & Brown (2021): "kadınların yaşam standardı göstergesi… yaklaşık yüzde 45, erkeklerinki yaklaşık yüzde 21 düşmüş; her iki grubun serveti ise yaklaşık yarıya gerilemiştir… evrensel oranlar değildir." |
| Boşanma artışı kalite düşüşünü gösterir | Y | s. 317 (kutu) | "bazı kötü evlilikler boşanma istatistiklerine hiç girmemiş olabilir… kötü evliliklerin sona erdirilebilir hale geldiğini de gösterebilir (Stevenson & Wolfers, 2006)." |
| Almanya: kadınlarda gelir kaybı ve yoksulluk riski daha büyük ve kalıcı | D | s. 316 | Leopold (2018): "Erkekler… daha keskin kısa dönemli düşüşler… kadınların hane gelirindeki kayıpları ve yoksulluk riskindeki artış daha büyük ve daha kalıcıdır… hangi sonuçtan söz ettiğimizi sormamız gerekir." |

Seviye metinleri:
- İlk şok romantik değil ama gerçek, sabit maliyetler iki haneye dağılır: s. 315.
- Kira, ısınma, taşınma, mobilya: s. 314.
- Sonuç hangi evlilikten çıkıldığına bağlıdır: s. 316.
- "Kalmak ne zaman gitmekten pahalıdır?": s. 311 (alt başlık).
- "kim hangi maliyetleri taşıyor?": s. 322.
- İyi boşanma acısız değildir, gereksiz çatışmayla büyütülen maliyetler: s. 324.

## 19 evliligin-yuzyili (nesil): Bölüm 29, 28, 15 (+ s. 21–22)

Sonuçlar ve dayanaklar:
- K Kurumsal evlilik: s. 22, 404, 418
- R 18. ve 19. yüzyıl romantik ideal: s. 21, 404
- U 20. yüzyıl ortası iş bölümü evliliği: s. 225–226
- A 20. yüzyıl arkadaşlık evliliği: s. 405, 419
- B Bugün, kapak taşı evlilik: s. 419–421

| İddia | Sayfa | Kitaptaki cümle |
|---|---|---|
| Tarihsel evlilik mülkiyet, soy, bakım, üretim emeği ve ittifakı topluyordu | s. 418 | "Mülkiyetin aktarılması, çocukların meşru soy hattına yerleştirilmesi, bakımın örgütlenmesi, üretim emeğinin paylaşılması ve aileler arasında ittifak kurulması…" |
| Romantik sevgi bulunabilirdi ama temel meşruiyet kaynağı değildi | s. 22 | "Romantik sevgi evlilikte bulunabilirdi, fakat eş seçiminin tek veya temel meşruiyet kaynağı olmak zorunda değildi." |
| Uzun süren evlilik yüksek doyumun kanıtı değildir, çıkış yoksa çift birlikte kalır | s. 404 | "evliliklerin uzun sürmesi yüksek duygusal doyumun kanıtı değildir… çift birlikte kalır." |
| 18. ve 19. yüzyılda biçimlenen romantik idealler | s. 21 | "on sekizinci ve on dokuzuncu yüzyıllarda biçimlenen romantik idealler" |
| Coontz'un “aşk devrimi” | s. 404 | "sevmedikleri biriyle aile çıkarı için evlenmenin meşruiyetini zayıflatmış ve evlilikten duygusal tatmin beklemeyi normalleştirmiştir… yeni bir başarı ölçütü… “Onu seviyor muyum ve onunla mutlu muyum?”" |
| Becker'ın modeli 20. yüzyıl ortasındaki haneleri betimliyordu | s. 225 | "Bu model yirminci yüzyılın ortasındaki birçok hanenin gerçek yapısını iyi betimleyen unsurlar taşıyordu" |
| Betimleme ile yasa farkı; eğitim, ücretli istihdam ve piyasa hizmetleri getiriyi değiştirdi | s. 225 | "betimlenen yapı ile değişmez ekonomik yasa aynı şey değildir. Kadınların eğitim ve ücretli istihdamının yükselmesi… klasik uzmanlaşmanın getirisini değiştirmiştir." |
| Uzmanlaşmanın uzun dönemli maliyeti | s. 226 | "uzmanlaşmanın uzun dönemli maliyeti olabilir" |
| Cherlin: 20. yüzyılda arkadaşlık temelli evlilik | s. 405 | "yirminci yüzyıl içinde arkadaşlık/companionate marriage modeli öne çıkmış ve sevgi, arkadaşlık… daha merkezi hale gelmiştir" (Cinsel yakınlık metinde kullanılmadı.) |
| Evlilik yalnız görevlerin birlikteliği olmaktan çıkar | s. 419 | "evlilik yalnız görevlerin gerçekleştirildiği birliktelik değil…" |
| Temel taşı ve kapak taşı | s. 420 | "cornerstone–capstone… Eski modelde evlilik ortak hayatın temel taşıdır… nikâh zaten kurulmuş hayatın üzerine konan kapak taşı" |
| OECD 2021 ilk evlilik yaşı: kadın ~31, erkek ~33,4 | s. 419 | "2021'de OECD ortalaması kadınlarda yaklaşık 31, erkeklerde yaklaşık 33,4'e yükselmiştir" |
| Kırılgan olanlar nikâha daha geç ulaşabilir | s. 421 (kutu) | "ekonomik olarak daha kırılgan olanlar nikâha daha geç ulaşabilir veya hiç ulaşamayabilir." |

Dikkat edilmesi gereken nokta: Kitap Coontz'un "aşk devrimi"ne tarih vermiyor. R sonucunda iki ayrı cümle yan yana duruyor: s. 21'deki "18. ve 19. yüzyıl romantik idealleri" ve s. 404'teki "aşk devrimi". Sonuç adı ("18. ve 19. yüzyıl") s. 21'e dayanıyor. Metinde ikisi "de" bağlacıyla bağlandı ama aynı dönem oldukları iddia edilmedi. Daha temkinli bir yazım istenirse sonuç adı "Romantik ideal" olarak kısaltılabilir.

## 20 ayni-evlilik (çift): Bölüm 15 / 29 (`bolum: "15"`, LISTE ile aynı)

| Madde | Dayanak |
|---|---|
| Temel taşı / kapak taşı | s. 420 |
| Hukuki güvence / kamusal ilan | s. 228, 422 |
| Üretim / tüketim tamamlayıcılığı | s. 226 |
| Tek kasa / ayrı hesap | s. 229–230 |
| Kariyerde uzmanlaşma / eşitlik | s. 225–226, 425 |
| Önce ekonomik hazırlık / sonra | s. 421 kutu |
| Birlikte yaşama: prova mı, ayrı kurum mu | s. 421–422 |
| Boş zaman: birlikte / bağımsız | s. 413 |
| Yük paylaşımı / kişisel gelişim desteği | s. 405 |
| Görkemli / sade düğün | s. 423 |

| İddia (seviye metinleri) | Sayfa | Kitaptaki cümle |
|---|---|---|
| Biri evliliği bağımsız iki insanın ortaklığı, öbürü boş zamanın birlikte geçtiği birliktelik olarak görebilir. Sorun aynı kurumdan farklı şey beklemek | s. 413 (Bölüm 28) | "Her iki model kendi başına patolojik değildir; sorun tarafların aynı kurumdan farklı şey beklemesi olabilir." |
| Gelenek az cevap verdikçe müzakere artar, çift kendi kurumunu tasarlar | s. 419 | "çift kendi kurumunu kendisi tasarlamak zorunda kalır. Gelenek daha az cevap verdiğinde daha fazla müzakere gerekir. Özgürlük artar; koordinasyon ihtiyacı da artabilir." |
| Devlet aynı nikâhı verir, çiftler farklı hikâyeler yükler | s. 423 | "Devlet aynı nikâhı verir; çiftler o nikâha farklı hikâyeler yükler." (açımlandı) |
| Evliliğin anlamını çiftler yazıyor | s. 431 | "evliliğin anlamını çiftlerin kendileri daha fazla yazmaktadır." |
| Eşitlikçi idealle başlayıp geleneksel düzene sürüklenmek | s. 425 | "çocuk geldiğinde ücret farkı, izin sistemi, işyeri beklentileri veya toplumsal normlar onları daha geleneksel iş bölümüne sürükleyebilir." |

Not: s. 413'teki dayanak Bölüm 28'de. Test için `bolum` alanı LISTE'yle tutarlı kalsın diye "15" bırakıldı. Testin büyük bölümü Bölüm 29'a dayandığı için "29" da savunulabilir. Karar sizin.

---

## Kitapta bulunamadığı için ya da bilerek çıkarılanlar
- Bölüm 20'deki çeyiz, başlık parası ve görücü usulü (nesil testi için cazipti). Bölüm 20 yasaklı yönlendirme listesinde olduğu için kullanılmadı.
- Orta Çağ saray aşkı (s. 21). Bir evlilik anlayışı değil, bir aşk anlayışı olduğu için nesil testinde sonuç yapılmadı.
- ILO ve OECD'nin cinsiyete göre ev işi oranları (s. 234–235). Kitapta var ama kişisel sonuç metinlerinde kalıp yargı gibi okunmasın diye kullanılmadı.
- Bölüm 18'deki rızaya dayalı tek eşli olmayan ilişki ve cinsel doyum bulguları. Cinsellik konusu olduğu için kullanılmadı.
- Bölüm 22'deki çocuk sonuçları (Frimmel 2024, Tan 2026). Mit testine eklenebilirdi ama test 3 doğru, 3 yanlış dengesinde tamamlandığı için alınmadı.
- Hiçbir metinde kitap dışı araştırma, rakam ya da isim kullanılmadı.
