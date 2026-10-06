# -*- coding: utf-8 -*-
# Aşkonomi test serisi — Sezon 2 "Sözleşme" (test 11–20) içerikleri.
# Kaynak: Aşkonomi v45, bölüm 15, 16, 17, 18, 19, 22, 24, 25, 28, 29 (+ s. 21–22).
# Sayfa dayanakları: /home/claude/askonomi_in/rapor_s2.md

ICERIK = {}

# ---------------------------------------------------------------- 11
ICERIK["evlilik-ne"] = {
    "kanca": "Nikâh masasında herkes aynı imzayı atar ama herkes aynı şeyi imzalamaz.",
    "sorular": [
        ("Biri sana “Neden evlenmek?” diye sorsa ilk cümlen ne olur?", [
            ("Y", "Birlikte kalıcı bir şey inşa etmek için"),
            ("S", "Zor günde yanımda biri olsun diye"),
            ("O", "İki kişi bir ekip olunca hayat daha iyi işler"),
            ("T", "Hayatı onunla paylaşmak daha keyifli"),
            ("H", "İlişkimizin resmî bir güvencesi olsun diye")]),
        ("Evlilikte en çok neyin “ortak” olduğunu düşünürsün?", [
            ("Y", "Evin, birikimin, uzun vadeli planların"),
            ("S", "Kötü günlerin ve sürprizlerin"),
            ("O", "Günlük işlerin ve sorumlulukların"),
            ("T", "Tatillerin, zevklerin, boş zamanın"),
            ("H", "Hakların ve yükümlülüklerin")]),
        ("Partnerin işini kaybetti. Aklından ilk ne geçer?", [
            ("Y", "Ortak planlarımızı nasıl koruruz?"),
            ("S", "Bunun için varız, bir süre benim gelirim yeter."),
            ("O", "Evdeki iş bölümümüzü yeniden düzenleriz."),
            ("T", "Birlikte geçireceğimiz zaman arttı, iyi değerlendirelim."),
            ("H", "Resmî haklarımızı ve güvencelerimizi gözden geçiririm.")]),
        ("Nikâh sence bir ilişkiye ne ekler?", [
            ("Y", "Ortak yatırımlara cesaret"),
            ("S", "Geleceğe karşı bir dayanışma sözü"),
            ("O", "Rollerin ve görevlerin netleşmesi"),
            ("T", "Birlikte kurulan hayatın kutlaması"),
            ("H", "Hukuken tanınan bir haklar paketi")]),
        ("Bir evlilikte seni en çok ne yıpratırdı?", [
            ("Y", "Ortak bir geleceğe yatırım yapamamak"),
            ("S", "Zor anda yalnız bırakılmak"),
            ("O", "İşlerin hep birinin üstünde kalması"),
            ("T", "Birlikte keyif alacak bir şey bulamamak"),
            ("H", "Kuralların ve hakların belirsiz kalması")]),
        ("Hangi cümle sana daha yakın?", [
            ("Y", "Evlilik, geleceğe birlikte yapılan bir yatırımdır."),
            ("S", "Evlilik, iyi günde de kötü günde de bir güvencedir."),
            ("O", "Evlilik, iyi işleyen bir iş bölümüdür."),
            ("T", "Evlilik, hayatı birlikte yaşamayı seçmektir."),
            ("H", "Evlilik, iki kişinin yazılı sözüdür.")]),
    ],
    "sonuclar": {
        "Y": ("Evlilik senin için: Yatırım",
              "Senin için evlilik, geleceğe birlikte yapılan bir yatırım: ortak ev, ortak plan, uzun vade. Kitap bunlara ilişkiye özgü yatırım der, çünkü ilişki bitince çoğu başka yerde aynı değeri taşımaz. Hukuken tanınan ortaklık, “Yarın hiçbir şey olmamış gibi çekip gitmeyeceğim” mesajını daha inandırıcı kılabilir. Bedeli de var: Birinin kariyerinden vazgeçtiği bir uzmanlaşma, ayrılık hâlinde maliyeti tek kişinin üstünde biriken bir yatırıma dönüşebilir.",
              "15"),
        "S": ("Evlilik senin için: Sigorta",
              "Senin için eş, hayatın belirsizliklerine karşı kurulan küçük bir dayanışma ağı. Biri işini kaybedince öbürünün geliri sürer, hastalıkta zaman ve kaynak yeniden dağıtılır. Kitap “iyi günde kötü günde” sözünü tam böyle okur: belirsiz geleceğe karşı karşılıklı bir taahhüt. Ama bir uyarı da ekler: Aile kusursuz bir sigorta şirketi değildir. Kenya’da evli çiftlerle yapılan bir deney, eşler arasındaki risk paylaşımının eksik kalabildiğini gösterdi.",
              "15"),
        "O": ("Evlilik senin için: Ortaklık",
              "Sen evliliği iyi işleyen bir ekip olarak görüyorsun: Herkes iyi yaptığı işi üstlenir, hane birlikte üretir. Gary Becker’ın 1973 tarihli evlilik teorisi de evliliği romantizmin karşıtı olarak değil, kazanç üreten bir ortaklık olarak inceledi. Hane yalnız tüketmez, zamanı kullanarak kendi içinde değer üretir. Riskli tarafı şu: Toplam üretim yüksek olsa da piyasa geliri yalnız bir kişinin adına yazılabilir ve evdeki emek görünmez kalabilir.",
              "15"),
        "T": ("Evlilik senin için: Yol arkadaşlığı",
              "Senin için evlilik, tek başına yapamadığın işleri bölüşmek değil, birlikte yapmayı sevdiğin şeyleri ortaklaştırmak. İktisatçılar Stevenson ve Wolfers buna tüketim tamamlayıcılığı der: ortak zevkler, seyahatler, projeler. Kitaba göre modern evlilikte bu yön, klasik iş bölümünden daha önemli hâle gelmiş olabilir. Bedeli şu: Ekonomik zorunluluk azaldıkça “Bu insanla neden kalıyorum?” sorusunun cevabı giderek daha çok gönüllülüğe dayanır.",
              "15"),
        "H": ("Evlilik senin için: Sözleşme",
              "Senin için nikâh, sevginin yanında yazılı bir güvence. Kitap da nikâhı birçok hukuk sisteminde önceden hazırlanmış bir haklar ve yükümlülükler paketi olarak görür: miras, ortak mülkiyet, sosyal güvenlik, ayrılık kuralları. Yani belirsiz geleceğe karşı hukuki bir koordinasyon mekanizması. Ama kitap bir çizgi de çeker: Bağlılık ile hapis aynı şey değildir. İyi kurum, bağlılığı güçlendirirken onun özgür bir seçim olarak kalmasını da korur.",
              "15"),
    },
}

# ---------------------------------------------------------------- 12
ICERIK["gorunmeyen-emek"] = {
    "kanca": "Bazı işler kimsenin bordrosuna yazılmaz ama birinin gününden düşer.",
    "birim": "Görünmeyen Emek Endeksi",
    "bolum": "16",
    "sorular": [
        ("Evde deterjan, ekmek ya da diş macunu bitmek üzereyken bunu genelde kim fark eder?", [
            (0, "Neredeyse hiç ben değilim"), (1, "Bazen ben, bazen başkası"),
            (2, "Çoğunlukla ben"), (3, "Hep ben, listeyi de ben tutarım")]),
        ("Doktor randevuları, doğum günleri, ödeme tarihleri gibi şeyleri kim aklında tutar?", [
            (0, "Başkası hatırlatır, ben uyarım"), (1, "Herkes kendi işini hatırlar"),
            (2, "Çoğunu ben hatırlarım"), (3, "Evin takvimi benim kafamda")]),
        ("İşten ya da okuldan eve döndüğünde ne olur?", [
            (0, "Gün benim için biter, dinlenirim"), (1, "Arada bir küçük işler yaparım"),
            (2, "Çoğu akşam bir iki saat daha çalışırım"), (3, "Asıl yoğunluk eve gelince başlar")]),
        ("Evde biri kırgınsa ya da akrabalar arasında gerginlik varsa ortamı kim yumuşatır?", [
            (0, "Genelde başkası"), (1, "Kim müsaitse o"),
            (2, "Çoğunlukla ben"), (3, "Hep ben, herkes de bunu benden bekler")]),
        ("Bir iş birine verildi. Gerçekten yapılıp yapılmadığını kim takip eder?", [
            (0, "Takip eden başkası"), (1, "Takibe gerek kalmaz, yapılır"),
            (2, "Çoğu zaman ben kontrol ederim"), (3, "Ben sormasam yapılmaz")]),
        ("Evden biri hastalanınca ya da bakım gerekince kim işini veya planını değiştirir?", [
            (0, "Genelde başkası"), (1, "Sırayla ya da birlikte"),
            (2, "Çoğunlukla ben"), (3, "Hep ben, çalışma düzenim de buna göre şekillendi")]),
    ],
    "seviyeler": [
        (0, "Görünür mesai",
         "Sonuçlara göre evin görünmeyen işlerinin büyük bölümü sende birikmiyor. Bu, gerçekten paylaşılan bir düzen de olabilir, yükün başka birinde toplanması da. Kitabın kutusundaki soruyu düşün: Deterjanın azaldığını kim fark etti, alışveriş listesine kim ekledi? Zihinsel yük iyi yapıldığında sorun çıkmaz, bu yüzden yapılan iş de fark edilmez. Bu bir ölçüm değil, bir düşünme aracı."),
        (30, "Paylaşılan mesai",
         "Görünmeyen işlerin bir kısmı sende, bir kısmı başkasında. Kitaba göre adalet her şeyi yarı yarıya bölmek değildir: Biri yemeği, öbürü faturaları üstlenebilir, çalışma saatleri farklıysa eşit görev bile adil olmayabilir. Araştırmalar, nesnel dağılım kadar algılanan hakkaniyetin de ilişki doyumuyla bağlantılı olduğunu gösteriyor. Bu bir düşünme aracı: Hangi maddelerde yükün sende toplandığına bak."),
        (55, "Gizli yönetici",
         "Evde işler yapılıyor olabilir ama neyin yapılacağını fark eden, hatırlayan ve takip eden büyük ölçüde sensin. Allison Daminger bu bilişsel emeği dört aşamada inceler: ihtiyacı önceden fark etmek, seçenekleri belirlemek, karar vermek, sonucu izlemek. “Söyleseydin yapardım” cümlesi tam burada doğar: Fiziksel iş paylaşılmış, yönetim yükü paylaşılmamış olabilir. Bu bir düşünme aracı, ama dikkat de zaman kadar kıt bir kaynak."),
        (80, "İkinci vardiya",
         "Sonuçlara göre eve dönmek senin için ikinci bir çalışma gününün başlaması gibi. Arlie Hochschild ve Anne Machung’un kalıcı hâle getirdiği kavramın adı bu: ikinci vardiya. Günün yirmi dört saati değişmediği için ücretsiz işe ayrılan her fazladan saat dinlenmeden, eğitimden ya da ücretli işten eksilir. Kitabın cümlesiyle: “Ücretsiz olmak ile maliyetsiz olmak aynı şey değildir.” Bu bir teşhis değil, bir düşünme aracı."),
    ],
}

# ---------------------------------------------------------------- 13
_EV = ["Hep aynı kişi", "Sırayla ya da birlikte"]
ICERIK["ev-isini-kim-yapiyor"] = {
    "kanca": "Ayrı ayrı çözün, sonra karşılaştırın: Aynı evde yaşıyorsunuz ama aynı evi mi görüyorsunuz?",
    "sorular": [
        ("Bir şeyin bitmek üzere olduğunu fark edip listeye eklemek:", list(_EV)),
        ("Faturaları ve son ödeme tarihlerini takip etmek:", list(_EV)),
        ("Akşam ne yeneceğine karar vermek:", list(_EV)),
        ("Doğum günlerini hatırlayıp hediyeyi ayarlamak:", list(_EV)),
        ("Bulaşık makinesini boşaltıp tabakları kaldırmak:", list(_EV)),
        ("Aile üyelerinin doktor randevularını ayarlamak:", list(_EV)),
        ("Tatil için seçenekleri araştırmak:", list(_EV)),
        ("Akrabaları arayıp sormak, ilişkiyi sürdürmek:", list(_EV)),
        ("Bir tartışmadan sonra ortamı yumuşatmak:", list(_EV)),
        ("Bir işin gerçekten yapılıp yapılmadığını kontrol etmek:", list(_EV)),
    ],
    "seviyeler": [
        (0, "İki ayrı ev",
         "Aynı evde yaşıyorsunuz ama iş bölümünü çok farklı görüyorsunuz. Kitabın hatırlattığı gibi bir işi “yapmak”, ihtiyacı fark etmekten sonucunu kontrol etmeye uzanan zincirin yalnızca bir halkası olabilir. Biriniz son halkayı görürken diğeriniz bütün zinciri görüyor olabilir. Farklı cevap verdiğiniz maddeler, görünmeyen emeğin tam olarak nerede durduğunu gösteriyor. Algı farkı, işin bir kısmının hiç görünmemesinden doğabilir."),
        (4, "Yarım harita",
         "Bazı işlerde aynı tabloyu görüyorsunuz, bazılarında görmüyorsunuz. Ayrıştığınız maddeler büyük ihtimalle planlama, hatırlama ve takip gibi kolay gözden kaçan işler. Kitaba göre zihinsel yük iyi yapıldığında sorun çıkmaz, bu yüzden yapılan iş de fark edilmez. Bir soru: “Hep aynı kişi” dediğiniz işlerde, o kişinin kim olduğu konusunda da anlaşıyor musunuz?"),
        (7, "Ortak harita",
         "Evdeki iş bölümünü büyük ölçüde aynı görüyorsunuz. Bu değerli bir başlangıç: Neyin kimde olduğunu iki kişi aynı biçimde görüyorsa konuşmak da kolaylaşır. Yine de kitabın uyarısı geçerli: Aynı algı, adil dağılım demek değildir. Araştırmalara göre eşitsiz bir dağılım bile taraflarca “normal” ya da “adil” kabul edilebiliyor. Asıl soru, aynı gördüğünüz tablonun ikinize de uygun gelip gelmediği."),
        (9, "Aynı harita",
         "Neredeyse her işte aynı cevabı verdiniz: Evinizin haritası ikinizin zihninde aynı. Şimdi kitabın daha geniş sorusu ilginçleşiyor: İş bölümü yalnız bugünkü rahatlığı mı paylaştırıyor, yoksa birinizin gelecekteki eğitim, gelir ve boş zaman imkânlarını da değiştiriyor mu? Çok sayıda “hep aynı kişi” cevabınız varsa, bu soru en çok o maddeler için anlamlı."),
    ],
    "bolum": "16",
}

# ---------------------------------------------------------------- 14
ICERIK["cocugun-maliyeti"] = {
    "kanca": "Bebek bezi faturada görünür ama bir çocuğun asıl maliyeti başka yerlerde saklanır.",
    "sorular": [
        ("Bir çocuğun doğumdan yetişkinliğe kadar maliyeti için her yerde geçerli tek bir rakam vardır.", False,
         "Yanlış. Kitaba göre maliyet ülkeye, gelir grubuna, kamu hizmetlerinin kapsamına ve ailenin seçtiği yaşam standardına göre büyük ölçüde değişir. Tek rakamlar ancak belirli ülke, yıl ve varsayımlar altında anlam taşır."),
        ("Bir çocuğun en büyük maliyetlerinin bir kısmı aile bütçesinde hiç görünmez.", True,
         "Doğru. Kitap çocuk maliyetini üç katmanda düşünür: para, zaman ve vazgeçilen alternatifler. Çocuğa ayrılan saatlerde ücretli çalışamamak, eğitim alamamak ya da esnek çalışmak için daha düşük ücret kabul etmek faturada görünmez ama gerçek bir maliyettir."),
        ("Kalabalık ailelerde çocukların daha az eğitim alması, aile büyüklüğünün buna yol açtığını kanıtlar.", False,
         "Yanlış. Black ve arkadaşlarının (2005) Norveç verileriyle yaptığı çalışmada büyük ailelerdeki çocukların eğitimi ilk bakışta daha düşük görünüyordu. Ama doğum sırası hesaba katılıp ikiz doğumlar kullanıldığında aile büyüklüğünün nedensel etkisi büyük ölçüde ortadan kalktı. Korelasyon nedensellik değildir."),
        ("Yüksek gelirli ülkelerde “gelir arttıkça daha az çocuk” ilişkisi zayıfladı, bazı yerlerde tersine döndü.", True,
         "Doğru. Doepke ve arkadaşlarının (2023) değerlendirmesine göre doğurganlık ekonomisi “yeni bir döneme” girdi. Kadınların işgücüne katılımının yüksek olduğu kimi ülkeler görece yüksek doğurganlık gösterebiliyor. Belirleyici olan, kariyer ile aileyi birlikte sürdürmenin ne kadar mümkün olduğu."),
        ("Doğum yardımı gibi nakit teşvikler doğurganlığı güçlü ve kalıcı biçimde artırır.", False,
         "Yanlış. Kitabın aktardığı OECD (2024) değerlendirmesine göre ailelere yapılan nakit transferlerin doğurganlık üzerindeki etkisi çoğunlukla yok, küçük ya da geçici. Tek seferlik bir ödeme, yirmi yıl sürebilecek çocuk yetiştirme maliyetinin küçük bir bölümünü karşılar."),
        ("Danimarka’da ilk çocuktan sonra kadınların kazancında, erkeklere kıyasla uzun dönemli yaklaşık yüzde 20’lik bir fark açıldığı bulundu.", True,
         "Doğru. Kleven ve arkadaşlarının (2019) çalışması bu farka “çocuk cezası” der. Oran Danimarka’ya özgüdür ve başka ülkelere doğrudan taşınamaz. Kitaba göre bu biyolojik bir yasa da değildir: Ücretli izin, çocuk bakımı ve bakımın nasıl paylaşıldığı maliyetin kimde yoğunlaşacağını değiştirebilir."),
    ],
    "seviyeler": [
        (0, "Etiket fiyatı",
         "Çocuğun maliyeti hakkındaki inançlarının çoğu, kitabın aktardığı bulgulardan farklı. Şaşırtıcı değil: Maliyetin büyük kısmı faturada değil, zamanda ve vazgeçilen fırsatlarda saklı. Kitabın ilkesi de açık: Bir çocuğun maliyeti hesaplanabilir, ama değeri fiyatlandırılamaz. Bu iki muhasebeyi birbirine karıştırmamak, çocuk ekonomisinin belki de en temel kuralı. Uykusuz bir gece bir fırsat maliyetidir, o gecenin anlamı ise aynı birimle ölçülemez."),
        (3, "Bütçe okuru",
         "Bazı iddiaları doğru okudun, bazılarında yanıldın. Çocuk ekonomisi tam da bu yüzden zor: Sezgisel olarak güçlü fikirler, veriyle sınanınca her yerde aynı biçimde işlemeyebiliyor. Örneğin kalabalık ailelerle eğitim arasındaki ilişki, ilk bakışta göründüğü kadar basit değil. Kitabın sorusu hâlâ açık: İnsanlar maliyetini bildikleri hâlde neden hayatlarının en büyük yatırımlarından birini karşılıksız yapar?"),
        (5, "Aile ekonomisti",
         "Çocuk ekonomisini çok iyi okuyorsun: Görünmeyen maliyetleri, korelasyon tuzağını ve teşviklerin sınırını biliyorsun. Şimdi zor soru: Kitaba göre çocuk yetiştirmenin faydaları topluma yayılırken maliyetin önemli bölümünü aile taşıyor. Bu yükün ne kadarı ortak omuzlara düşmeli? Kitap bir sınır da çizer: Toplumsal faydanın varlığı, üreme hakkının bireye ait olduğu gerçeğini ortadan kaldırmaz."),
    ],
    "bolum": "17",
}

# ---------------------------------------------------------------- 15
ICERIK["kiskanclik"] = {
    "kanca": "Herkes biraz kıskanır, asıl mesele o duyguyla ne yaptığın.",
    "sorular": [
        ("Partnerin, senin tanımadığın bir iş arkadaşıyla sık sık mesajlaşıyor.", [
            ("R", "Açık bir kuralımızı çiğnemedikçe sorun etmem"),
            ("D", "Belli etmesem de içim burkulur"),
            ("S", "Aklıma bir sürü senaryo gelir"),
            ("K", "Kim olduğunu ve ne konuştuklarını sorarım"),
            ("T", "Ben de birinden söz ederek tepkisini ölçerim"),
            ("G", "Merak edersem sorarım, gerisi onun alanı")]),
        ("Partnerinin telefonu masada, ekranda bir bildirim yandı.", [
            ("R", "Bakmam, bir sorun sezersem açıkça konuşurum"),
            ("D", "Bakmam ama kimden geldiğini merak ederim"),
            ("S", "Çaktırmadan göz atarım, içim rahatlasın"),
            ("K", "Şifresini zaten bilirim, ara sıra kontrol ederim"),
            ("T", "Ben de kendi telefonumla meşgulmüş gibi yaparım"),
            ("G", "Bakmak aklıma bile gelmez")]),
        ("Kıskançlık sence çoğu zaman neyin işaretidir?", [
            ("R", "Bir sınırın aşıldığının"),
            ("D", "Ona çok değer verdiğimin"),
            ("S", "Bir şeylerin ters gittiğinin"),
            ("K", "Ona sahip çıktığımın"),
            ("T", "Hâlâ istendiğimin"),
            ("G", "Güvenin biraz sarsıldığının")]),
        ("Partnerin eski sevgilisiyle arkadaş kalmış.", [
            ("R", "Konuştuğumuz sınırlar içindeyse sorun yok"),
            ("D", "Kabul ederim ama bir yanım hep tetikte"),
            ("S", "Aralarında hâlâ bir şey olduğunu düşünürüm"),
            ("K", "Görüşmelerini azaltmasını isterim"),
            ("T", "Ben de eski sevgilimden söz etmeye başlarım"),
            ("G", "Geçmiş onun geçmişi, ben bugüne bakarım")]),
        ("Partnerin bir akşam arkadaşlarıyla dışarıda ve söylediğinden geç kaldı.", [
            ("R", "Haber vermeden çok gecikirse ararım"),
            ("D", "Özlerim, biraz da yalnız hissederim"),
            ("S", "Her geçen dakika aklımdan başka şeyler geçer"),
            ("K", "Konumunu benimle paylaşmasını isterim"),
            ("T", "Bir dahaki sefere ben de geç kalırım"),
            ("G", "Keyfine bakarım, gelince anlatır")]),
        ("Hangi cümle sana daha yakın?", [
            ("R", "Kurallar konuşulur, çiğnenince hesabı sorulur."),
            ("D", "Seven, kaybetmekten korkar."),
            ("S", "Hiç belli olmaz, tedbirli olmak lazım."),
            ("K", "Sevdiğin insanın nerede olduğunu bilmek hakkındır."),
            ("T", "Biraz kıskançlık ilişkiye tuz biber olur."),
            ("G", "Güven, kontrolden daha güçlü bir bağdır.")]),
    ],
    "sonuclar": {
        "R": ("Sınır bekçisi",
              "Sen kıskançlığı bir alarm gibi kullanıyorsun: Açık bir sınır aşılırsa çalar, aşılmazsa susar. Kitap bunu reaktif kıskançlık diye ayırır: Gerçek ve açık bir ihlale verilen tepki, kanıt olmadan sürekli tehdit arayan kıskançlıktan farklıdır. Senin riskin şurada: Neyin ihlal sayılacağı kültürden kültüre, ilişkiden ilişkiye değişir. Konuşulmamış bir sınıra tepki verdiğinde, karşı taraf o kuralı ilk kez o an öğreniyor olabilir.",
              "19"),
        "D": ("Kaybetme korkusu",
              "Sen kıskançlığı içinde yaşıyorsun: burukluk, özlem, biraz da kaygı. Bu duygu değer verdiğin bir ilişkiyi kaybetme korkusundan doğuyor. Pfeiffer ve Wong’un çalışmasında duygusal kıskançlık ile romantik sevgi arasında belirli pozitif ilişkiler bulunmuştu. Ama kitap bir sınır çizer: Kıskançlığın varlığı ilişkinin değerli olduğunu gösterebilir, yoğunluğu ise sevginin miktarını ölçmez. Kitabın sorusu tam sana göre: Neyi kaybetmekten korkuyoruz?",
              "19"),
        "S": ("Sürekli alarm",
              "Senin kıskançlığın daha çok zihninde dolaşıyor: senaryolar, ihtimaller, ipuçları. Kitap buna bilişsel kıskançlık der ve önemli bir bulgu aktarır: Sürekli şüphe ve kuşku, sevgiyle aynı yönde hareket etmez. Dijital çağ bu yakıtı bol bol üretir, bir kalp emojisi arkadaşlık da olabilir, flört de. Kitabın benzetmesiyle kıskançlık ilişkinin alarmıdır ama alarmın çalması yangın olduğunu kanıtlamaz.",
              "19"),
        "K": ("Sahiplenme",
              "Cevapların, kıskançlığın duygudan davranışa geçtiği yeri gösteriyor: sormak, kontrol etmek, sınırlamak. Bu davranışların kaynağı kaybetme korkusu olabilir. Ama kitaba göre kaynağı açıklamak davranışı haklı çıkarmaz. Ama kitap açık konuşur: “Bir duygunun anlaşılabilir olması, o duyguyla yapılan her davranışı kabul edilebilir hale getirmez.” Kontrol, karşı tarafın davranış alanını daraltmaya başlar. Kitabın en net fikirlerinden biri de şu: Sevgi bağlılık yaratabilir, ama mülkiyet hakkı yaratmaz.",
              "19"),
        "T": ("Kıskandıran",
              "Sen ilgiyi ölçmek için bazen terazinin öbür kefesine bir rakip koyuyorsun. Kitap bunu partneri ilişkide tutmaya yönelik stratejiler arasında anlatır. İspanya’daki bir çalışmada daha düşük ilişki bağlılığı bildirenlerin bilinçli kıskançlık yaratmayı daha sık kullandığı bulunmuştu. Kısa vadede ilgi artabilir. Ama kitabın sinyal kuralı burada da geçerli: Bir sinyal göndericinin niyetini değil, alıcının yorumladığı anlamı taşır.",
              "19"),
        "G": ("Güvenli liman",
              "Sen kıskançlığı nadiren hissediyorsun, hissettiğinde de sormayı tercih ediyorsun. Kitaba göre güven arttıkça aynı tehdidin algılanışı azalabilir. Güvenin bir bölümü doğrulanabilir bilgiden, bir bölümü de belirsizliğe rağmen partnerin sınırlarına saygı göstermekten oluşur. Tek bir risk var: Romantik kültür kıskançlığı sevginin işareti sayar, bu yüzden hiç kıskanmayan biri bazen ilgisiz sanılabilir. Rahatlık ile ilgisizlik aynı şey değildir.",
              "24"),
    },
}

# ---------------------------------------------------------------- 16
ICERIK["cok-eslilik-mitleri"] = {
    "kanca": "Çok eşlilik tarihi, çoğumuzun sandığından çok daha şaşırtıcı bir hikâye anlatıyor.",
    "sorular": [
        ("İncelenen insan toplumlarının büyük çoğunluğu, erkeklerin birden fazla eş edinmesine en azından izin vermiştir.", True,
         "Doğru. Henrich ve arkadaşlarının (2012) etnografik kayıtları değerlendiren çalışmasına göre bu oran yaklaşık yüzde 85."),
        ("Bu yüzden tarih boyunca erkeklerin çoğu birden fazla kadınla evliydi.", False,
         "Yanlış. Bir toplumun polijiniye izin vermesi ile nüfusun çoğunun öyle yaşaması aynı şey değildir. Kitaba göre çok eşli evlilik çoğu toplumda toprak, hayvan, gelir, statü ya da siyasi güce sahip belirli erkeklerin erişebildiği bir düzenlemeydi."),
        ("Bugün dünya nüfusunun yaklaşık yüzde 2’si poligamik hanelerde yaşıyor.", True,
         "Doğru. Bu, Pew Research Center’ın 130 ülke ve bölgeyi kapsayan araştırmasının tahmini. Oran Batı ve Orta Afrika’nın bazı bölgelerinde çok daha yüksek. Bugünkü dünya, etnografik kayıtların ima ettiğinden çok daha tek eşli."),
        ("Bir kadının birden fazla erkekle evli olduğu poliandri, insan toplumlarında hiç görülmemiştir.", False,
         "Yanlış. Poliandri çok daha seyrek ama gerçek. Starkweather ve Hames (2012), poliandriye izin veren 53 toplum belirledi ve bu evlilik biçiminin sanıldığından daha geniş bir coğrafyaya yayıldığını gösterdi."),
        ("Himalaya’daki kardeş poliandrisi, kıt tarım arazisinin kuşaktan kuşağa bölünmesini önleyebilir.", True,
         "Doğru. Kitaba göre birkaç erkek kardeşin aynı kadınla evlenmesi, bölünebilir arazinin kıt olduğu yerlerde aile mülkünün her kuşakta daha küçük parçalara ayrılmasını önleyebilir. Ama kitap bütün poliandri örneklerini bu tek formüle sıkıştırmamak gerektiğini de hatırlatır."),
        ("Polijin hanelerdeki kadınlar her konuda, tek eşli hanelerdeki kadınlardan daha az kontrole sahiptir.", False,
         "Yanlış, en azından her yerde değil. Burkina Faso’daki polijin haneleri inceleyen Eissler ve arkadaşları (2025), karar almanın genellikle hiyerarşik kaldığını ama bazı hanelerde kadınların kendi kazançları üzerinde tek eşli hanelerdekinden daha fazla kontrol sürdürebildiğini buldu."),
    ],
    "seviyeler": [
        (0, "Efsane okuru",
         "Çok eşlilik hakkındaki inançlarının çoğu, kitabın aktardığı bulgulardan farklı. En şaşırtıcı ayrım şu: Bir ilişki biçiminin çok sayıda toplumda meşru görülmesi, insanların çoğunun öyle yaşadığı anlamına gelmez. Bugünkü dünya, etnografik kayıtların ima ettiğinden çok daha tek eşli. Kitaba göre çok eşlilik, servet ve statü dağılımının aile yapısına çevrildiği bir kurum olarak da incelenebilir."),
        (3, "Tarih meraklısı",
         "Bazı iddiaları doğru okudun, bazılarında yanıldın. Çok eşlilik, hakkında en çok kalıp yargı dolaşan konulardan biri. Kitabın bu bölümdeki temel dersi işine yarayabilir: Aile biçimleri servetten, mirastan ve toprak kıtlığından bağımsız değildir. Nadir kurumların bile tek bir ekonomik nedeni yoktur. Kitabın ifadesiyle insan doğasının ayırt edici özelliklerinden biri, farklı ilişki kurumlarını kurabilecek kadar esnek olmasıdır."),
        (5, "Saha antropoloğu",
         "Çok eşlilik tarihini çok iyi okuyorsun. Şimdi kitabın sorduğu daha zor soru: Bir yapının adil olup olmadığını anlamak için kaç kişi olduğuna değil, kimin karar verebildiğine, kaynakların nasıl paylaşıldığına ve isteyenin ilişkiden çıkıp çıkamadığına bakmak gerekmez mi? Kitaba göre hukuki izin ile tarafların eşit pazarlık gücü farklı kavramlardır. Ölçü “kaç kişi?” sorusuyla bitmez."),
    ],
    "bolum": "18",
}

# ---------------------------------------------------------------- 17
ICERIK["iliski-sozlesmesi"] = {
    "kanca": "Hiçbir ilişki yazılı sözleşmeyle kurulmaz ama her birinin görünmez maddeleri vardır.",
    "sorular": [
        ("Akşam bir tartışma başladı. Büyük ihtimalle konu ne?", [
            ("K", "Sorulmadan yapılan bir harcama"),
            ("E", "Evdeki işlerin hep aynı kişide kalması"),
            ("G", "Söylenenle yapılanın tutmaması"),
            ("B", "Birlikte vakit geçirmeyi unutmamız"),
            ("C", "“Böyle giderse biter” cümlesinin kurulması")]),
        ("İlişkinize bir sözleşme yazılsa ilk hangi maddeyi eklemek isterdin?", [
            ("K", "Paranın nasıl bölüşüleceği"),
            ("E", "Ev işlerinin ve takibinin kimde olduğu"),
            ("G", "Önemli hiçbir şeyin saklanmayacağı"),
            ("B", "Haftada bir akşamın yalnız ikimize ait olduğu"),
            ("C", "İsteyen tarafın onurlu biçimde ayrılabileceği")]),
        ("Partnerin bir hafta iş seyahatine çıktı. Ne fark edersin?", [
            ("K", "Harcamaları kimin karşıladığını daha net görürüm"),
            ("E", "Evdeki her şeyi zaten ben takip ediyormuşum"),
            ("G", "Nerede, kiminle olduğunu merak ettiğimi"),
            ("B", "Birlikteyken de pek konuşmadığımızı"),
            ("C", "Tek başıma da gayet idare edebildiğimi")]),
        ("Bir arkadaşın ilişkini anlatmanı istedi. Hangi cümleyi kurma ihtimalin yüksek?", [
            ("K", "“Para konusu bizde hep biraz gergin.”"),
            ("E", "“Ben hatırlatmazsam hiçbir şey yapılmıyor.”"),
            ("G", "“Bazen bir şey sakladığını hissediyorum.”"),
            ("B", "“İyiyiz ama ev arkadaşı gibiyiz.”"),
            ("C", "“Ayrılmak istesem bile kolay olmazdı.”")]),
        ("Yıldönümünüz yaklaşıyor. Aklından ilk ne geçer?", [
            ("K", "Bütçemiz ne kadar, kim ödeyecek?"),
            ("E", "Planlamayı yine ben mi yapacağım?"),
            ("G", "Verdiği sözü bu kez tutacak mı?"),
            ("B", "En son ne zaman baş başa kaldık?"),
            ("C", "Gerçekten istediğimiz için mi birlikteyiz?")]),
        ("Hangi cümle ilişkine en çok lazım?", [
            ("K", "“Bizim paramız” gerçekten bizim olsun."),
            ("E", "Görünmeyen işler de görülsün."),
            ("G", "Söylenen yapılsın, saklanan olmasın."),
            ("B", "Rutinin içinde de birbirimizi bulalım."),
            ("C", "Kalmak zorunluluk değil, seçim olsun.")]),
    ],
    "sonuclar": {
        "K": ("Bozuk madde: Kasa",
              "Senin ilişkinde en çok gıcırdayan madde para. Sorun çoğu zaman paranın miktarı değil, nasıl paylaşıldığı. Kitap haneyi tek bir karar verici gibi düşünmenin yanıltıcı olduğunu söyler: Eşlerin tercihleri kısmen ortak ama tamamen aynı değildir. “Bizim paramız” demek kolaydır, nasıl bölündüğü ayrı bir sorudur. Kitaba göre evliliğin kazancı yalnız pastanın büyüklüğüyle değerlendirilemez, pastanın nasıl bölündüğünü de bilmek gerekir.",
              "15"),
        "E": ("Bozuk madde: Emek",
              "Senin ilişkinde zorlanan madde, kimsenin yazmadığı işler: fark etmek, hatırlamak, takip etmek. Kitap bunu zihinsel yük diye anlatır. “Söyleseydin yapardım” diyen kişi gerçekten söylenen her işi yapıyor olabilir. Ama ne yapılacağını fark etmek, görevi tanımlamak ve takip etmek hep diğerindeyse fiziksel iş paylaşılmış, yönetim yükü paylaşılmamış olabilir. Bu madde yazılmadıkça emeğin bedeli hep aynı hanede birikir.",
              "16"),
        "G": ("Bozuk madde: Güven",
              "Senin ilişkinde zorlanan madde, hiçbir sözleşmeye tam yazılamayan madde: güven. Kitap ilişkiyi eksik bir sözleşme olarak anlatır. Beş yıl sonra çıkacak hastalığı, iş kaybını, krizi önceden yazamayız. Yazılamayan her durumda iki kişi birbirinin iyi niyetine ve geçmiş davranışlarına dayanır. Kitaba göre güven sözleşmenin alternatifi değil, sözleşmenin ulaşamadığı yerlerde birlikte yaşamanın koşuludur ve hammaddesi tekrar eden tutarlılıktır.",
              "24"),
        "B": ("Bozuk madde: Bakım",
              "Senin ilişkinde zorlanan madde kriz değil, ihmal. Faturalar ödeniyor, işler dönüyor ama ilişkinin kendisine pek sıra gelmiyor. Kitap bu tehlikeyi açıkça adlandırır: Ortak hayat giderek yalnız lojistik bir şirkete dönüşebilir. Ogolsky ve Bowers’ın 35 çalışmayı kapsayan meta-analizinde ilişki süresi, bakım davranışlarıyla sürekli pozitif ilişki göstermiyordu. Yani uzun süre birlikte olmak, ilişkinin iyi korunduğunun kanıtı değildir.",
              "25"),
        "C": ("Bozuk madde: Çıkış",
              "Senin ilişkinde zorlanan madde, en az konuşulan madde: çıkış. Kalmanın bir seçim mi, bir zorunluluk mu olduğu bulanıklaşmış olabilir. Kitap bağlılık ile hapis arasında temel bir fark görür: Ayrılık imkânsızlaştığında yatırım korunur ama kötü ilişkiden çıkış da engellenir. Öte yandan sürekli bir ayrılık tehdidi de manipülasyon olabilir. Kitabın gözlemi: “Gitme imkânının artması, gitme arzusunun artmasıyla aynı şey değildir.”",
              "15"),
    },
}

# ---------------------------------------------------------------- 18
ICERIK["bosanmanin-faturasi"] = {
    "kanca": "Boşanmanın bedeli mahkeme kapısında başlamaz, orada da bitmez.",
    "sorular": [
        ("Ayrılan bir çiftin toplam geliri hiç değişmese bile kişi başına yaşam maliyeti artabilir.", True,
         "Doğru. Tek mutfak, tek internet bağlantısı, tek oturma odası iki haneye bölününce ölçek ekonomisi kaybolur. Kitabın deyişiyle insan eşinden ayrılırken aynı zamanda hane ölçeği ekonomisinden de ayrılır."),
        ("Boşanmayı tek tarafın başlatabilmesine izin veren yasalar, boşanmaları kalıcı olarak büyük ölçüde artırdı.", False,
         "Yanlış. Justin Wolfers’ın (2006) ABD eyaletlerini yeniden inceleyen çalışmasına göre reformlardan sonra geçici bir artış görüldü, ama bu artışın büyük bölümü yaklaşık on yıl içinde tersine döndü."),
        ("“Evliliklerin yarısı boşanmayla biter” her ülke ve kuşak için geçerli bir gerçektir.", False,
         "Yanlış. Kitaba göre bu tür tek oranlar evrensel gerçekler değildir. Yıllık boşanma sayısını nüfusa bölmek, mevcut evliliklerin ne kadarının sonunda boşanacağını söylemez. Boşanmayı anlamak için payda en az pay kadar önemlidir."),
        ("ABD’de 50 yaş üstü boşanmalarda hem kadınların hem erkeklerin serveti yaklaşık yarıya geriledi.", True,
         "Doğru. Lin ve Brown’ın (2021) çalışmasında servet her iki grupta yaklaşık yarıya düştü, yaşam standardı göstergesi ise kadınlarda yaklaşık yüzde 45, erkeklerde yaklaşık yüzde 21 geriledi. Bunlar belirli bir ülke, dönem ve yaş grubunun sonuçları, evrensel oranlar değil."),
        ("Boşanma oranının yükselmesi, evliliklerin kalitesinin düştüğünü gösterir.", False,
         "Yanlış, en azından her zaman değil. Kitaba göre ekonomik bağımlılığın yüksek olduğu dönemlerde bazı kötü evlilikler istatistiklere hiç girmemiş olabilir, çünkü taraflardan biri ayrılmayı göze alamıyordu. Çıkış maliyeti düşünce bu evlilikler görünür hâle gelir (Stevenson ve Wolfers, 2006)."),
        ("Almanya’daki uzun dönemli bir çalışmada boşanmanın gelir kaybı ve yoksulluk riski kadınlarda daha büyük ve kalıcı bulundu.", True,
         "Doğru. Thomas Leopold’un (2018) çalışmasında erkekler yaşam doyumu gibi bazı öznel göstergelerde daha keskin ama kısa dönemli düşüşler yaşadı. Kadınların hane geliri kaybı ve yoksulluk riskindeki artış ise daha büyük ve kalıcıydı. “Kim için daha kötü” sorusunun cevabı, hangi sonuçtan söz edildiğine bağlı."),
    ],
    "seviyeler": [
        (0, "Kolay hesap",
         "Boşanmanın ekonomisi hakkındaki inançlarının çoğu, kitabın aktardığı bulgulardan farklı. Belki de en önemlisi şu: Boşanmanın ilk ekonomik şoku romantik değildir ama gerçektir. Daha önce tek hanenin taşıdığı sabit maliyetler iki haneye dağılır. Kira, ısınma, mobilya ve taşınma aynı geliri iki kez zorlar. Toplam gelir değişmese bile kişi başına yaşam maliyeti artabilir."),
        (3, "Yarım fatura",
         "Bazı kalemleri doğru okudun, bazılarını gözden kaçırdın. Bu çok doğal, çünkü boşanma hakkında en çok tekrarlanan cümlelerin bir kısmı veriyle uyuşmuyor. Boşanma istatistikleri tam da bu yüzden yanıltıcı olabilir: Tek bir oran, kimin hangi bedeli ne kadar süre ödediğini göstermez. Kitaba göre boşanmanın sonucu, hangi evlilikten çıkıldığına ve sonrasında hangi hayata girildiğine bağlıdır. Kitabın sorusu hâlâ geçerli: Kalmak ne zaman gitmekten pahalıdır?"),
        (5, "Tam döküm",
         "Boşanmanın faturasını çok iyi okuyorsun: ölçek kaybını, yasa etkisinin sınırını ve kimin neyi kaybettiğini biliyorsun. Kitabın en zor sorusu şimdi senin: Bu evliliğin sürmesi ve sona ermesi hâlinde kim hangi maliyetleri taşıyor? Kitaba göre boşanmanın iyi olması acısız olması demek değildir. Daha anlamlı ölçüt, kaçınılmaz maliyetlerin gereksiz çatışmayla büyütülüp büyütülmediğidir."),
    ],
    "bolum": "22",
}

# ---------------------------------------------------------------- 19
ICERIK["evliligin-yuzyili"] = {
    "kanca": "Aşkla evlenmek sandığından daha yeni bir fikir, peki senin evlilik hayalin hangi döneme ait?",
    "sorular": [
        ("Eşini seçerken en çok neyin sözü geçmeli?", [
            ("K", "Ailemin, çünkü evlilik iki aileyi birleştirir"),
            ("R", "Kalbimin, aşk yoksa evlilik de yok"),
            ("U", "Kimin neyi üstleneceğinin netliğinin"),
            ("A", "En iyi arkadaşım olabilmesinin"),
            ("B", "Kendimi hazır hissettiğim zamanın")]),
        ("Evlilik hayatın neresinde durur?", [
            ("K", "Yetişkinliğin ve aile düzeninin başında"),
            ("R", "Büyük bir aşkın doğal sonunda"),
            ("U", "Ev kurulup roller paylaşıldığında"),
            ("A", "Bir arkadaşlığın ömür boyu sürdüğü yerde"),
            ("B", "Her şey yoluna girdikten sonra, en tepede")]),
        ("Evde para ve iş nasıl bölünmeli?", [
            ("K", "Geleneğin ve ailenin öngördüğü gibi"),
            ("R", "Aşk varsa gerisi kendiliğinden çözülür"),
            ("U", "Biri dışarıda kazanır, öbürü evi çevirir"),
            ("A", "Birlikte karar verir, birlikte yaparız"),
            ("B", "Her şeyi konuşur, kendi düzenimizi kurarız")]),
        ("İyi bir eşin en önemli özelliği ne?", [
            ("K", "Ailesine ve sorumluluklarına bağlı olması"),
            ("R", "Beni ilk günkü gibi heyecanlandırması"),
            ("U", "Üstlendiği işi aksatmadan yapması"),
            ("A", "Onunla saatlerce konuşabilmem"),
            ("B", "Kişisel gelişimimi desteklemesi")]),
        ("Düğün senin için ne demek?", [
            ("K", "İki ailenin ve çevrenin onayı"),
            ("R", "Aşkımızın herkese ilanı"),
            ("U", "Yeni bir hanenin kuruluş günü"),
            ("A", "En yakınlarımızla güzel bir kutlama"),
            ("B", "Birlikte başardıklarımızın taçlandığı gün")]),
        ("Evlilikte en büyük hayal kırıklığı ne olurdu?", [
            ("K", "Aileye ve çevreye mahcup olmak"),
            ("R", "Aşkın zamanla sönüp gitmesi"),
            ("U", "Birinin üstüne düşeni yapmaması"),
            ("A", "Birbirimize anlatacak bir şey kalmaması"),
            ("B", "İlişkinin beni büyütmemesi")]),
    ],
    "sonuclar": {
        "K": ("Yüzyıllar boyu: Kurumsal evlilik",
              "Senin evlilik anlayışın çok eski bir köke dayanıyor. Kitaba göre tarihsel evlilik mülkiyetin aktarılmasını, çocukların soy hattına yerleşmesini, bakımın örgütlenmesini, üretim emeğinin paylaşılmasını ve aileler arası ittifakı aynı kurumda topluyordu. Romantik sevgi bulunabilirdi ama eş seçiminin temel kaynağı olmak zorunda değildi. Kitabın uyarısı: Böyle evliliklerin uzun sürmesi yüksek duygusal doyumun kanıtı değildir, çıkış seçeneği yoksa çift zaten birlikte kalır.",
              "29"),
        "R": ("18. ve 19. yüzyıl: Romantik ideal",
              "Senin evlilik anlayışının merkezinde aşk var: Sevdiğinle evlenmek ve başka bir gerekçeye ihtiyaç duymamak. Kitap, on sekizinci ve on dokuzuncu yüzyıllarda biçimlenen romantik ideallerden söz eder. Stephanie Coontz’un “aşk devrimi” dediği dönüşüm de aile çıkarı için sevilmeyen biriyle evlenmenin meşruiyetini zayıflattı ve evlilikten duygusal tatmin beklemeyi normalleştirdi. Bedeli şu: Evlilik için yeni bir başarı ölçütü doğdu, “Onunla mutlu muyum?”",
              "28"),
        "U": ("20. yüzyıl ortası: İş bölümü evliliği",
              "Senin evlilik anlayışın net bir iş bölümüne dayanıyor: Biri dışarıda kazanır, öbürü evi ve bakımı yönetir. Kitaba göre Gary Becker’ın uzmanlaşma modeli, yirminci yüzyılın ortasındaki birçok hanenin gerçek yapısını iyi betimleyen unsurlar taşıyordu. Ama betimleme ile değişmez yasa aynı şey değildir. Eğitim, ücretli çalışma ve piyasadan alınabilen hizmetler bu modelin getirisini değiştirdi. Uzmanlaşmanın uzun dönemli maliyeti de tek kişide birikebilir.",
              "15"),
        "A": ("20. yüzyıl: Arkadaşlık evliliği",
              "Senin için eş her şeyden önce en yakın arkadaş. Kitap, sosyolog Andrew Cherlin’in şemasını aktarır: Yirminci yüzyıl içinde arkadaşlık temelli evlilik öne çıktı ve sevgi ile eşler arası arkadaşlık evliliğin merkezine yerleşti. Evlilik artık yalnız görevlerin yerine getirildiği bir birliktelik değildi. Bu model güçlü bir yakınlık vaat eder. Riski de buradan doğar: Konuşacak şey azaldığında evliliği taşıyan ana direk de zayıflar.",
              "29"),
        "B": ("Bugün: Kapak taşı evlilik",
              "Senin evlilik anlayışın tam bugünün: önce iş, birikim, ev ve kendini tanımak, sonra nikâh. Sosyoloji buna temel taşı ile kapak taşı ayrımı der. Eski modelde evlilik hayatın temel taşıydı, yeni modelde kurulmuş hayatın üzerine konan kapak taşı. OECD ortalamasında ilk evlilik yaşı 2021’de kadınlarda yaklaşık 31, erkeklerde yaklaşık 33,4’e yükseldi. Bedeli: Giriş çıtası yükseldikçe ekonomik olarak kırılgan olanlar nikâha daha geç ulaşabilir.",
              "29"),
    },
}

# ---------------------------------------------------------------- 20
ICERIK["ayni-evlilik"] = {
    "kanca": "Ayrı ayrı çözün, sonra karşılaştırın: “Evet” derken aynı evliliğe mi evet diyorsunuz?",
    "sorular": [
        ("Evlilik:", ["Hayatı birlikte kurmanın başlangıcı", "Kurulmuş bir hayatın tacı"]),
        ("Nikâh en çok:", ["Hukuki bir güvence", "Bağlılığın herkese ilanı"]),
        ("Evliliğin asıl kazancı:", ["İşleri ve yükleri bölüşmek", "Sevdiğimiz şeyleri birlikte yapmak"]),
        ("Para:", ["Tek kasa", "Ortak bütçe, ayrı hesaplar"]),
        ("Kariyerler:", ["Gerekirse biri öne çıkar, öbürü destekler", "İkisi de aynı ağırlıkta yürür"]),
        ("Evlenmeden önce:", ["Ekonomik olarak hazır olmalıyız", "Hazırlığı evlenince birlikte yaparız"]),
        ("Nikâhsız birlikte yaşamak:", ["Evliliğe bir hazırlık", "Kendi başına bir seçenek"]),
        ("Boş zaman:", ["Çoğunu birlikte geçiririz", "Herkesin kendi alanı da olur"]),
        ("Eşimden en çok beklediğim:", ["Hayatın yükünü paylaşması", "Kendimi geliştirmemi desteklemesi"]),
        ("Düğün:", ["Kalabalık ve görkemli", "Küçük ve sade"]),
    ],
    "seviyeler": [
        (0, "İki ayrı evlilik",
         "Aynı kurumdan çok farklı şeyler bekliyorsunuz. Kitap bunu kendi başına bir sorun saymaz: Biri evliliği iki bağımsız insanın ortaklığı, öbürü boş zamanın neredeyse tamamının birlikte geçtiği bir birliktelik olarak görebilir. Kitaba göre sorun modellerin kendisi değil, tarafların aynı kurumdan farklı şey beklemesi olabilir. Farklı cevap verdiğiniz maddeler, konuşulmamış beklentilerin haritası."),
        (4, "Aynı bina, farklı planlar",
         "Bazı temel konularda aynı evliliği hayal ediyorsunuz, bazılarında yollarınız ayrılıyor. Kitaba göre modern evlilikte gelenek daha az cevap verdikçe daha fazla müzakere gerekir: Çift kendi kurumunu kendisi tasarlamak zorunda kalır. Ayrıştığınız maddeler, o tasarımın henüz çizilmemiş kısımları. Kitabın deyişiyle özgürlük artar, koordinasyon ihtiyacı da artabilir. Farklı cevaplar bir uyumsuzluk kanıtı değil, konuşulacak gündemin listesi."),
        (7, "Ortak plan",
         "Evlilikten büyük ölçüde aynı şeyleri bekliyorsunuz. Kitabın gözlemiyle devlet herkese aynı nikâhı verir, çiftler o nikâha farklı hikâyeler yükler. Sizin hikâyeleriniz çoğu yerde örtüşüyor. Ayrıldığınız birkaç madde varsa, bunlar büyük ihtimalle hayat değiştikçe yeniden konuşulacak olanlar. Ortak bir plan, değişmeyen bir plan demek değildir. İş, çocuk ya da şehir değiştiğinde aynı sorular yeniden masaya gelir."),
        (9, "Aynı hikâye",
         "Neredeyse her maddede aynı evliliği hayal ediyorsunuz. Kitaba göre modern evliliğin ayırt edici özelliği, anlamını giderek çiftlerin kendilerinin yazması. Siz aynı satırları yazıyorsunuz. Kitaptan tek bir not: Çiftler eşitlikçi bir idealle başlayabilir, ama çocuk, ücret farkı ve iş hayatının beklentileri onları zamanla daha geleneksel bir düzene sürükleyebilir. Hayal aynı, hayat değişebilir."),
    ],
    "bolum": "15",
}
