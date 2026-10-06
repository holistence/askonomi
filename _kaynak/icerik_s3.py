# -*- coding: utf-8 -*-
# Aşkonomi test serisi — Sezon 3 "Kriz" (test 21–30). Kaynak: kitap v45, Bölüm 22–28 ve Giriş.
# Sayfa dayanakları: /home/claude/askonomi_in/rapor_s3.md

ICERIK = {}

# 21 — hesap — Bölüm 28
ICERIK["beklenti-enflasyonu"] = {
    "kanca": "Sevgili, en iyi arkadaş, sırdaş, kariyer danışmanı: Bir insana kaç iş tanımı sığar?",
    "sorular": [
        ("Sevgili, en iyi arkadaş, sırdaş, ev arkadaşı, tatil arkadaşı, kriz desteği, kariyer danışmanı, kişisel gelişim destekçisi… Bu rollerden kaçını partnerinden beklersin?", [
            (0, "Üç dört tanesini, gerisi için hayatımda başka insanlar var"), (1, "Yaklaşık yarısını"),
            (2, "Çoğunu"), (3, "Hepsini, partner dediğin zaten bu")]),
        ("Uzun süredir seni zorlayan bir sorunla boğuşuyorsun. Destek için kime yaslanırsın?", [
            (0, "Partnerime, arkadaşlarıma, gerekirse bir uzmana"), (1, "Önce partnerime, sonra başkalarına da"),
            (2, "Çoğunlukla partnerime, başkasına pek anlatmam"), (3, "Yalnızca partnerime, beni ondan iyi kimse anlayamaz")]),
        ("Doğum günün yaklaşıyor. Ne istediğini partnerine söyler misin?", [
            (0, "Açıkça söylerim, tahmin oyununu sevmem"), (1, "İpucu veririm, gerisi ona kalmış"),
            (2, "Söylemem, beni tanıyorsa bilir"), (3, "Söylemek zorunda kalırsam hediyenin anlamı kalmaz")]),
        ("Yıllar sonra partnerinden ne beklersin?", [
            (0, "Güven versin, heyecanı da arada birlikte yaratırız"), (1, "Güven versin, ara sıra da beni şaşırtsın"),
            (2, "Hem hep güven versin hem hep heyecanlandırsın"), (3, "İlk günkü heyecan hiç sönmesin, sönerse bir şey yanlıştır")]),
        ("İdeal partner listende kaç madde “olmazsa olmaz”?", [
            (0, "Birkaç tane: saygı, dürüstlük, güven gibi"), (1, "Beş altı tane"),
            (2, "Listenin çoğu"), (3, "Hepsi, birinden vazgeçersem razı olmuşum demektir")]),
        ("Hangi cümle sana daha yakın?", [
            (0, "“Seninle hayatımın bazı alanları daha zengin.”"), (1, "“Sen benim en yakın insanımsın.”"),
            (2, "“Sen benim her şeyimsin.”"), (3, "“Sen beni tamamlıyorsun.”")]),
    ],
    "seviyeler": [
        (0, "Fiyat istikrarı", "Partnerinden beklediklerini sıraya koymuşsun: Bir çekirdek var, gerisi hayatındaki başka insanlarla paylaşılıyor. Kitap bunu beklentiyi düşürmek değil, dağıtmak olarak anlatır: Güçlü romantik bağ ile zengin sosyal ağ birbirinin rakibi değildir. Ama düşük endeks “az iste” demek değildir. Kitaba göre şiddetsizlik, rıza, temel saygı ve dürüstlük gibi beklentiler ne dağıtılabilir ne düşürülmelidir. Bu bir ölçüm değil, bir düşünme aracıdır."),
        (26, "Ilımlı enflasyon", "Beklentilerin yüksek ama çoğu makul. Kitap standart sahibi olmanın sorun olmadığını söyler: Standartlar kötü eşleşmeleri fark etmemize yardım eder. Asıl çizgi standart ile kusursuzluk talebi arasındadır ve listende birkaç madde bu çizgiye yaklaşıyor olabilir. Kitabın sorduğu sorular işine yarayabilir: “Bu beklenti partner tarafından biliniyor mu, karşılıklı mı, kaynaklarımızla uyumlu mu ve gerçekten benim için vazgeçilmez mi?”"),
        (51, "Yüksek enflasyon", "Partnerinin iş tanımı uzun: sevgili, sırdaş, kriz desteği, belki biraz da danışman. Kitap bunu bir iş ilanına benzetir: Aynı kişiden bütün görevleri eşit iyilikte yapmasını bekleriz. Her beklenti tek başına makul olabilir, toplam paket ise ağırlaşır. Bedeli şu: Tek kişiden her şeyi beklediğinde, onun yetersiz kaldığı her alan bütün ilişkinin başarısızlığı gibi görünebilir. Kitaba göre partner, profesyonel desteğin yerini almak zorunda da değildir."),
        (76, "Hiperenflasyon", "Senin gözünde partner, her ihtiyacın tek tedarikçisi gibi. Kitap Finkel ve arkadaşlarının benzetmesini aktarır: Dağın yükseklerinde manzara daha etkileyicidir, fakat oksijen daha azdır. Bu kadar yüksek beklenti ancak ilişkiye o düzeyde zaman ve enerji ayrıldığında karşılanabilir. Kitap “beklentini düşür” demez, beklenti ile kaynak arasındaki uyuma bakar. Kitabın sorusu: “Partnerimden istediğim şey gerçekten ilişkim için temel mi?”"),
    ],
    "bolum": "28",
    "birim": "Beklenti Enflasyonu Endeksi",
}

# 22 — hesap — Bölüm 25
ICERIK["iliski-getirisi"] = {
    "kanca": "Para yatırmadın ama zaman, emek ve dikkat yatırdın, peki karşılığında ne birikiyor?",
    "sorular": [
        ("İyi bir haber aldın: bir terfi, bir kabul, bir başarı. Partnerinin tepkisi genellikle nasıl olur?", [
            (3, "Sevinir, ayrıntıları sorar, kutlamak ister"), (2, "İçtenlikle tebrik eder, sonra gündem değişir"),
            (1, "“Güzel” der ama aklı başka yerdedir"), (0, "Hemen olası sorunları ya da eksikleri sıralar")]),
        ("Yaptığın küçük şeyler (haber vermek, bir ayrıntıyı hatırlamak, bir yükü paylaşmak) fark ediliyor mu?", [
            (3, "Çoğu zaman fark edilir ve dile getirilir"), (2, "Fark edilir ama pek söylenmez"),
            (1, "Ancak yapmadığımda fark edilir"), (0, "Görünmez kalır, sanki kendiliğinden oluyor")]),
        ("Kendi hedeflerin (eğitim, sağlık, iş, bir uğraş) açısından bu ilişki seni nereye taşıyor?", [
            (3, "Olmak istediğim kişiye yaklaştırıyor"), (2, "Destekliyor ama pek bir etkisi yok"),
            (1, "Hedeflerim ilişkinin gölgesinde kaldı"), (0, "Hedeflerimi “ilişkimiz için” bıraktım")]),
        ("En son birlikte yeni bir şey (bir yer, bir uğraş, bir deneyim) ne zaman yaptınız?", [
            (3, "Son birkaç hafta içinde"), (2, "Son birkaç ay içinde"),
            (1, "Hatırlamakta zorlanıyorum"), (0, "Ortak anılarımızın hepsi eskide kaldı")]),
        ("Uzun vadede bakınca ilişkide kim ne veriyor?", [
            (3, "Dönem dönem değişse de denge kuruluyor"), (2, "Biraz dengesiz ama ikimiz de bunu görüyoruz"),
            (1, "Genellikle aynı taraf veriyor"), (0, "Hep aynı taraf veriyor ve bu konuşulamıyor")]),
        ("İlişkiye harcanan enerjinin çoğu nereye gidiyor?", [
            (3, "Yeni şeyler kurmaya, birlikte plan yapmaya"), (2, "Gündelik düzeni sürdürmeye"),
            (1, "Aynı tartışmaları yatıştırmaya"), (0, "Hasar onarımına, başka şeye enerji kalmıyor")]),
    ],
    "seviyeler": [
        (0, "Uyarı ışığı", "Cevapların, ilişkiye harcanan emeğin büyük kısmının onarıma gittiğini ya da verilenin görünmez kaldığını düşündürüyor. Kitap burada bir eşik koyar: Ortak hayatın bilançosu tam denk olmayabilir, fakat sürekli tek tarafa zarar yazıyorsa yatırım metaforu uyarı vermeye başlar. Bu bir hüküm değil, bir düşünme aracı. Kitabın bölüm başındaki sorusu: Hangi yatırımlar ilişkiyi gerçekten besler?"),
        (26, "Bakım bekleyen hesap", "İlişkin işliyor ama getirisi azalıyor gibi. Kitaba göre ilişki sona ermeden önce bazen dramatik bir kriz değil, uzun süreli ihmal yaşanır. Faturalar ödenir, işler yürür, ama ortak hayat giderek bir lojistik şirkete dönüşebilir. Bedeli şu: İlişki işlevini yerine getirirken yakınlık sessizce azalabilir. Kitap çözümü büyük jestlerde değil, yüzlerce kez tekrarlanan küçük davranışlarda arar."),
        (51, "Düzenli getiri", "İlişkin sana değer katıyor: Küçük katkılar görülüyor, denge büyük ölçüde korunuyor. Kitap ilişki bakımını sürekli harcama olarak değil, ortaklığın kullanım değerini koruyan düzenli yatırım olarak anlatır. Bir uyarı var: İlişkinin bazı getirileri kendiliğinden yenilenmez. Yeni ortak deneyim üretilmediğinde bütün hatıralar giderek geçmiş zamana ait hale gelebilir. Yatırım bazen ilişkiye yeni malzeme eklemektir."),
        (76, "Bileşik getiri", "İlişkin hem zor günde bir sigorta hem iyi günde getiriyi çoğaltan bir ortaklık gibi çalışıyor. Kitabın deyişiyle iyi ortak yalnız yükümüzü taşımaya değil, büyümemize de dayanabilen insandır. Yine de yüksek puan bir garanti değildir. Kitaba göre romantik ilişkide en yüksek getirilerin bazıları sayıya çevrilemez. Bu endeks de onları ölçmez, yalnızca üzerine düşünmeye çağırır."),
    ],
    "bolum": "25",
    "birim": "Getiri Endeksi",
}

# 23 — senaryo — Bölüm 25 / 26 (ve 22)
ICERIK["batik-maliyet"] = {
    "kanca": "Geçmişe verdiklerin bugünkü kararını ne kadar yönetiyor?",
    "sorular": [
        ("Arkadaşın yedi yıllık ilişkisini anlatıyor: “Mutlu değilim ama bunca yıl verdim.” Ona ne dersin?", [
            ("G", "“Yedi yıl az değil, hemen vazgeçme.”"), ("S", "“Geçen yıllar geçti, onları hesaba katma.”"),
            ("A", "“Yılların hangisi bugün hâlâ bir şey taşıyor, ona bak.”"), ("Y", "“Önümüzdeki yedi yılı nasıl geçirmek istiyorsun?”")]),
        ("Aylar önce birlikte pahalı bir tatil planladınız ve parasını ödediniz. Şimdi aranız gergin ve tarih yaklaşıyor.", [
            ("G", "Para ödendi, gidilir, boşa gitmesin"), ("S", "Para zaten gitti, kararı hiç etkilememeli"),
            ("A", "Geri alınabilen bir kısım var mı, önce ona bakarım"), ("Y", "O haftayı başka nasıl geçirebileceğimi de tartarım")]),
        ("Bir ilişkinin bitmesine dair en çok neden korkardın?", [
            ("G", "Verdiğim her şeyin boşa gitmiş olmasından"), ("S", "Geçmişe takılıp yeni sayfayı açamamaktan"),
            ("A", "Ortak evin, çevrenin, düzenin dağılmasından"), ("Y", "Yanlış hayatta kalıp başka fırsatları kaçırmaktan")]),
        ("Uzun süredir birlikte olduğun biri için başka şehre taşındın. Şimdi işler eskisi gibi değil. Aklından ne geçer?", [
            ("G", "“Onun için bu kadar şeyi bıraktım, geri adım atamam.”"), ("S", "“Taşınmak geçmişte kaldı, bugünkü kararı etkilemez.”"),
            ("A", "“Kaybettiğim iş geçmişte, ama bugünkü gelirim ve çevrem gerçek.”"), ("Y", "“Gitmeseydim bugün nerede olurdum, düşünmeden edemem.”")]),
        ("“Bunca yılını vermişsin, şimdi bırakılır mı?” cümlesi sana ne ifade ediyor?", [
            ("G", "Haklı bir soru, emek kolay harcanmaz"), ("S", "Anlamsız, geçmiş yıllar karar ölçüsü olamaz"),
            ("A", "Yarı doğru, yılların bir kısmı bugünü hâlâ etkiler"), ("Y", "Asıl soru verilen yıllar değil, verilecek yıllar")]),
        ("Bir ilişki bitse, o yıllar için ne düşünürdün?", [
            ("G", "Bunca emek bir sonuca ulaşmalıydı"), ("S", "Bir sayfa kapandı, geriye bakmam"),
            ("A", "Bitse de iyi yanları ve öğrendiklerim benimle kalır"), ("Y", "Başka bir yolu seçseydim ne olurdu, merak ederdim")]),
    ],
    "sonuclar": {
        "G": ("Geçmişin bekçisi", "Senin için verilen emek kolay silinmez ve bu sadakatin bir parçası. İktisat bunun bir kısmına batık maliyet der: Bugün ne karar verirsen ver geri gelmeyecek olan. Bedeli şu: Kararı yalnız “bunca yıl boşa gitmesin” diye vermek, bugün için kötü bir seçeneği geçmişi kurtarmak için seçmek olabilir. Bu, kalmanın yanlış olduğu anlamına gelmez. Kitabın sorusu: Devam etmek zorunda hissediyorsam, bu “yalnız geçmişte çok şey verdiğim için” mi?", "25"),
        "S": ("Temiz sayfa", "Sen geçmişe takılmıyorsun: Olan olmuştur, karar bugüne göre verilir. Bu, batık maliyet yanılgısına karşı güçlü bir bağışıklık. Ama kitap öbür uca da dikkat çeker: İlişkinin bütün tarihini “batık maliyet, unut gitsin” diye silmek de en az geçmişe teslim olmak kadar yanıltıcıdır. Ortak çocuklar, konut, sosyal ağlar geçmişte kurulmuş olsa da bugünü etkiler. Risk, gerçek bağları da hesaptan düşmek.", "25"),
        "A": ("Ayırt eden", "Sen geçmişi ne put yapıyor ne çöpe atıyorsun. Neyin geri gelmeyecek batık maliyet, neyin bugünü hâlâ etkileyen ilişkiye özgü sermaye olduğunu ayırmaya çalışıyorsun. Kitabın önerdiği ayrım tam olarak bu. Zorluğu şu: Kitap bu ikisini hayatta kusursuz biçimde ayırmanın kolay olmadığını da kabul eder. Ve bir şeyi hatırlatır: Sona eren yatırım ile değersiz geçmiş aynı şey değildir.", "22"),
        "Y": ("Yarına bakan", "Sen kararı geçmişe değil, önündeki yıllara göre tartıyorsun. İktisadın diliyle fırsat maliyetine bakıyorsun: Bu seçimle hangi hayatlardan vazgeçiyorum? Bu, batık maliyet tuzağına karşı iyi bir pusula. Ama bir riski var: Seçilmemiş hayatlar hep daha parlak görünür, çünkü maliyetlerini yaşamamışızdır. Kitabın uyarısı: “Gerçek hayat bütün maliyetleriyle, hayali hayat ise seçilmiş sahneleriyle yarışır.”", "26"),
    },
}

# 24 — hesap — Bölüm 26
ICERIK["neye-mal-oldu"] = {
    "kanca": "Her “evet” birkaç sessiz “hayır” taşır, seninkiler neydi?",
    "sorular": [
        ("Bu ilişki için işinde ya da eğitiminde bir fırsattan vazgeçtin mi?", [
            (0, "Hayır, hiç gerekmedi"), (1, "Küçük bir fırsattan"),
            (2, "Önemli bir tekliften"), (3, "İş yönümü büyük ölçüde değiştirdim")]),
        ("Yaşadığın şehir ve ev nasıl belirlendi?", [
            (0, "Zaten kendi seçeceğim yer"), (1, "Birlikte seçtik, ikimiz de biraz esnedik"),
            (2, "Daha çok onun ihtiyaçlarına göre"), (3, "Onun için taşındım, tek başıma olsam gitmezdim")]),
        ("İlişkiden önceki arkadaş çevren ve uğraşların ne durumda?", [
            (0, "Olduğu gibi duruyor"), (1, "Biraz seyreldi"),
            (2, "Büyük ölçüde ortak çevreye dönüştü"), (3, "Çoğunu geride bıraktım")]),
        ("Bir haftada yalnız kendine kalan saatler…", [
            (0, "İlişkiden önceki kadar"), (1, "Biraz azaldı"),
            (2, "Belirgin biçimde azaldı"), (3, "Neredeyse hiç kalmadı")]),
        ("Ortak kararlarda (taşınma, tatil, büyük harcama) kimin tercihi varsayılan oluyor?", [
            (0, "Gerçekten birlikte karar veriyoruz"), (1, "Dönem dönem değişiyor"),
            (2, "Çoğu zaman onunki"), (3, "Neredeyse her zaman onunki")]),
        ("Vazgeçtiğin şeyler ilişkide konuşuluyor mu?", [
            (0, "Vazgeçtiğim önemli bir şey yok"), (1, "Evet, görülüyor ve takdir ediliyor"),
            (2, "Pek konuşulmuyor"), (3, "Hiç görülmüyor, doğal sayılıyor")]),
    ],
    "seviyeler": [
        (0, "Hafif bagaj", "Bu ilişki için şimdiye kadar büyük bir şeyden vazgeçmemişsin ya da vazgeçtiklerin seni pek zorlamıyor. Yine de fırsat maliyeti hiçbir zaman sıfır değildir. Kitabın deyişiyle her “evet” başka bazı ihtimallere sessizce “hayır” der. Düşük bir bedel ilişkinin değersiz olduğunu göstermez, belki yalnızca iki hayatın iyi örtüştüğünü gösterir. Bu bir ölçüm değil, bir düşünme aracıdır."),
        (26, "Görünür bedel", "Bu ilişki sana bazı şeylere mal olmuş: biraz zaman, biraz esneklik, belki bir fırsat. Kitaba göre bir seçimin maliyetli olması onun yanlış olduğu anlamına gelmez. Tersine, neyin uğruna neyi gözden çıkardığımız neye değer verdiğimizi gösterir. Dikkat edilecek nokta, bedellerin hep aynı tarafta birikmemesi. Kitabın sorusu: “Kim hangi fırsattan vazgeçti ve bu kayıp zaman içinde nasıl telafi edildi?”"),
        (51, "Yüksek bedel", "Bu ilişki için ciddi şeylerden vazgeçmişsin: bir şehir, bir iş, bir çevre ya da kendine ait zaman. Kitap hatırlatır: Vazgeçilen iş maaş bordrosunda görünmez, ama ilişkinin hafızasında kalabilir. Yüksek bedel yanlış seçim demek değildir. Risk, görülmeyen fedakârlığın zamanla kırgınlığa dönüşmesidir. Kitap çözümü her fedakârlığa fiyat etiketi koymakta değil, büyük kararların görünmeyen kaybedenlerini konuşabilmekte görür."),
        (76, "Ağır bedel", "Bu ilişki hayatının yönünü büyük ölçüde belirlemiş ve vazgeçtiklerin büyük. Kitap bunun kendi başına yanlış seçim olmadığını söyler: İyi hayat, fırsat maliyeti olmayan hayat değil, vazgeçtiklerine rağmen seçtiği hayatı yaşamaya değer bulan hayattır. Ama maliyet hep aynı kişide toplanıyorsa bu bir dağılım sorunudur. Kitabın ölçütü: Ortak hayatın maliyetleri kadar kaçırılan fırsatlar da görünür olmalıdır."),
    ],
    "bolum": "26",
    "birim": "Fırsat Maliyeti Endeksi",
}

# 25 — profil — Bölüm 27 (ve 26)
ICERIK["cok-secenek"] = {
    "kanca": "Seçenekler çoğaldıkça sen daha mı iyi seçiyorsun, yoksa daha mı zor?",
    "sorular": [
        ("Bir flört uygulamasında elli yeni profil gördün. Ne yaparsın?", [
            ("M", "Hepsine bakarım, belki en iyisi sondadır"), ("Y", "İlk içimi ısıtan birkaçıyla konuşmaya başlarım"),
            ("F", "Önce olmazsa olmazlarıma göre elerim"), ("A", "Birkaçıyla yazışırım, hiçbirini kapatmam"),
            ("B", "Her birinde beğendiğim bir özelliği aklımda tutarım")]),
        ("Restoranda menü sayfalarca uzun.", [
            ("M", "Hepsini okurum, en iyisini bulmadan karar vermem"), ("Y", "İlk göze hoş gelende dururum"),
            ("F", "Yemeyeceklerimi eler, kalanlardan seçerim"), ("A", "Paylaşmak için birkaç tane söyleriz, sonra bakarız"),
            ("B", "Sipariş verdikten sonra yan masanınkine bakarım")]),
        ("İyi giden bir ilişkin var. Aklından en çok ne geçer?", [
            ("M", "“Acaba daha iyisi var mı?”"), ("Y", "“İyi ki bu kadar kolay oldu.”"),
            ("F", "“Benim için önemli olan her şey yerinde.”"), ("A", "“Şimdilik iyi, bakalım ne olacak.”"),
            ("B", "“Keşke onda şu özellik de olsaydı.”")]),
        ("Önemli bir karar verdikten sonra (ev, iş, partner)…", [
            ("M", "Diğer seçenekleri düşünmeye devam ederim"), ("Y", "Konu kapanır, önüme bakarım"),
            ("F", "Ölçütlerime uyuyorsa içim rahattır"), ("A", "Geri dönebileceğimi bilmek beni rahatlatır"),
            ("B", "Başkalarının seçimleriyle kıyaslarım")]),
        ("Bir arkadaşın sana birini tanıştırmak istiyor.", [
            ("M", "Önce başka kimler var, onları da duymak isterim"), ("Y", "Olur, iyi biriyse neden olmasın"),
            ("F", "Önce birkaç temel şey sorarım: yaşı, şehri, hayattan beklentisi"), ("A", "Tanışırım ama kimseye söz vermem"),
            ("B", "Dinlerken onu önceki sevgililerimle kıyaslarım")]),
        ("Hangi cümle sana daha yakın?", [
            ("M", "En iyisi varken ikincisine razı olmam."), ("Y", "Yeterince iyi, çoğu zaman en iyisidir."),
            ("F", "Ne istediğini bilen az yorulur."), ("A", "Kapılar açık kaldıkça özgürüm."),
            ("B", "Her insanda başka bir şey eksik.")]),
    ],
    "sonuclar": {
        "M": ("En iyinin peşinde", "Sen yeterince iyiyle yetinmiyor, ulaşılabilecek en iyiyi arıyorsun. Kitap buna maksimize etme eğilimi der. Schwartz ve arkadaşlarının çalışmalarında bu eğilim daha fazla pişmanlık ve daha düşük seçim doyumuyla ilişkiliydi, ama kitap bu bulguların tartışıldığını da not eder. Romantik seçimde iş daha zordur, çünkü “en iyi partner”in tek boyutlu bir sıralaması yoktur. Risk şu: Her yeni seçenek aramanın bitişini biraz daha erteleyebilir.", "27"),
        "Y": ("Yeterince iyi", "Sen “benim için uygun” olanı bulduğunda aramayı bırakabiliyorsun. Her yeni adayı yeniden yarışmaya sokmadığın için seçenek bolluğu seni pek yormaz. Kitabın anlattığı karar yükünden en az etkilenen tarz bu olabilir. Yine de kitap bir uyarı yapar: Kolay karar ile iyi hayat aynı şey değildir. Kitaba göre bir insanın bazı özellikleri ancak zaman içinde öğrenilebilir.", "27"),
        "F": ("Filtreci", "Sen ne istediğini biliyorsun ve uymayanları erkenden eliyorsun. Kitaba göre tercihlerin netliği arama maliyetini azaltır, bu yüzden geniş bir seçenek kümesi sana fayda bile sağlayabilir. Riski şu: Filtre sayısı arttıkça henüz tanımadığın insanlarla beklenmedik uyum ihtimali de erkenden yok olabilir. Boy, yaş, meslek gibi kolay filtrelenen özellikler, mizah ya da duyarlılık gibi zamanla görülenlerin önüne geçebilir.", "27"),
        "A": ("Açık kapı", "Sen seçeneklerini açık tutmayı seviyorsun. Bu esnekliğin bir değeri var, iktisatta buna opsiyon değeri denir. Ama kitabın uyarısı şu: Romantik hayatta bütün opsiyonları korumanın bedeli, partnerin de sana aynı ölçüde yatırım yapmaması olabilir, çünkü o da ilişkinin her an başka seçeneğe değiştirilebileceğini düşünür. Kitabın sözüyle: “Özgürlük, kapıyı kapatmanın kendi kararımız olmasıdır.”", "26"),
        "B": ("Hayali rakip", "Sen seçtikten sonra da karşılaştırmayı bırakmıyorsun: birinin mizahı, ötekinin romantikliği, bir başkasının başarısı. Karşılaştırma bazen işe yarar, başka çiftlerde görülen iyi bir davranış kendi ilişkini geliştirebilir. Ama kitap bir tuzağa dikkat çeker: Herkesin en güçlü yanından kafanda bir bileşik partner kurarsan gerçek insanın kazanması mümkün değildir. Bolluk böylece en güçlü rakibi yaratır: hiç var olmamış kusursuz alternatif.", "27"),
    },
}

# 26 — hesap — Bölüm 24
ICERIK["guven-sermayesi"] = {
    "kanca": "Güven iyi çalıştığında görünmez, peki seninki ne kadar birikmiş?",
    "sorular": [
        ("Partnerin küçük sözlerini (“ararım”, “gelirim”, “hallederim”) ne sıklıkla tutar?", [
            (3, "Neredeyse her zaman"), (2, "Çoğu zaman"),
            (1, "Yarı yarıya"), (0, "Nadiren")]),
        ("Ona anlattığın bir sır ya da zayıf bir anın ne oldu?", [
            (3, "Korudu, hiç gündeme getirmedi"), (2, "Korudu ama bir kez ima ettiği oldu"),
            (1, "Bir tartışmada kullandığı oldu"), (0, "Başkalarıyla paylaştığını öğrendim")]),
        ("Bir sorun çıktığında partnerin genellikle…", [
            (3, "Ortada olur, sorumluluğunu alır"), (2, "Biraz gecikse de gelir"),
            (1, "Ortadan kaybolur, sonra döner"), (0, "Hatayı başkasının üzerine atar")]),
        ("Bir hata yaptığında partnerin…", [
            (3, "Kendiliğinden söyler"), (2, "Sorulunca dürüstçe anlatır"),
            (1, "Önce küçültür, sonra kabul eder"), (0, "Kanıt çıkana kadar inkâr eder")]),
        ("Bir gecikme ya da belirsiz bir mesaj karşısında sen ne yaparsın?", [
            (3, "Pek düşünmem, bir açıklaması vardır"), (2, "Merak eder, sorarım, geçer"),
            (1, "Kafama takılır, kontrol etme isteği duyarım"), (0, "Doğrulamadan rahat edemem")]),
        ("Önemli konularda (para, sağlık, ortak gelecek) birbirinize bilgi veriyor musunuz?", [
            (3, "Açıkça veririz"), (2, "Çoğunlukla, bazı şeyler zamanla söylenir"),
            (1, "Bazı önemli şeyleri sonradan öğrendiğim oldu"), (0, "Kararlarımı eksik bilgiyle verdiğimi hissediyorum")]),
    ],
    "seviyeler": [
        (0, "Ekside", "Cevapların güven hesabının şu an ekside olduğunu düşündürüyor: Doğrulama ihtiyacı yüksek, verilen sözler az bilgi taşıyor. Kitap bunu kişisel bir kusur saymaz: Hak edilmiş kuşku da sağlıklı bilgi işleme olabilir. Düşük güvenin bedeli sürekli kontrol, doğrulama ve savunmadır. Kitaba göre güveni bozan davranışsa, onaran da davranış olmalıdır. Güvenliğin tehdit altında olduğu yerde ise kitap önceliği kişinin korunmasına verir."),
        (26, "Kırılgan bakiye", "Güven hesabın açık ama kırılgan: Bazı sözler tutuluyor, bazı konularda şüphe kalıyor. Kitap güveni tek bir puan değil, alanlara göre değişen beklentiler bütünü olarak görür. Sadakatine güvendiğin birinin dakikliğine güvenmemen mümkündür. Risk, küçük tekrarların örüntüye dönüşmesidir. O zaman soru “Bu kez ne oldu?”dan “Bu kişinin sözü geleceğe ilişkin ne kadar bilgi taşıyor?” sorusuna kayar."),
        (51, "Artıda", "Güven hesabın artıda: Sözler çoğunlukla tutuluyor, sorun çıktığında kimse ortadan kaybolmuyor. Kitap bunun değerini işlem maliyetiyle anlatır: Birbirine güvenen çift her bilgiyi doğrulamak ya da her gecikmeyi soruşturmak zorunda kalmaz. Yine de bu sermaye bankadaki para gibi mekanik işlemez. Küçük bir gecikme yılların güvenini yok etmeyebilir, ama tek bir büyük ihanet geçmişin bütün yorumunu değiştirebilir."),
        (76, "Güçlü sermaye", "Güven sermayen güçlü: Davranışlar sözleri destekliyor, kırılganlığın korunuyor. Kitap güvenin en büyük getirisini huzurdan çok hareket alanı olarak görür. Sürekli savunmada kalmadan işine, arkadaşlarına ve kendine zaman ayırabilirsin. Tek uyarı: Kitabın hedefi maksimum güven değil, davranışla uyumlu güven düzeyidir. Kitabın deyişiyle iyi güven, kanıta rağmen değil kanıt sayesinde güçlenir. Bu endeks de bir düşünme aracıdır."),
    ],
    "bolum": "24",
    "birim": "Güven Sermayesi Endeksi",
}

# 27 — mit — Bölüm 23
ICERIK["aldatma-mitleri"] = {
    "kanca": "Herkesin aldatma hakkında kesin bir fikri var ama veriler o kadar kesin konuşmuyor.",
    "sorular": [
        ("Bir kez aldatan, sonraki ilişkisinde de mutlaka aldatır.", False,
         "Yanlış. Knopp ve arkadaşlarının 484 yetişkini iki ardışık ilişki boyunca izlediği çalışmada, ilk ilişkisinde sadakatsizlik bildirenlerin sonraki ilişkide de bildirme olasılığı yaklaşık üç kat yüksekti. Ama kitap bunun bir risk farkı olduğunu, kader olmadığını vurgular: Üç kat yüksek olasılık yüzde yüz kesinlik demek değildir."),
        ("Mutlu bir ilişkide aldatma olmaz, aldatıldıysa ilişki zaten kötüydü.", False,
         "Yanlış. Düşük ilişki doyumu bazı çalışmalarda sadakatsizlikle birlikte görülür, ama nedensellik ters de işleyebilir: Sadakatsizliğin kendisi doyumu düşürebilir. Kitaba göre memnun olmadığı halde hiç aldatmayan çok sayıda insan vardır ve mutlu olduğunu bildirenlerin bir bölümü de ilişki dışı davranış yaşayabilir."),
        ("İnsanlar neyin aldatma sayılacağı konusunda her zaman aynı çizgiyi çekmez.", True,
         "Doğru. Wilson ve arkadaşlarının ölçeğinde davranışlar “açık”, “aldatıcı” ve “belirsiz” olarak gruplanmış, belirsiz davranışlarda görüşler daha fazla ayrışmıştır. Kitabın özeti: İnsanlar aldatma kavramının merkezinde büyük ölçüde uzlaşabilir, fakat sınırlarında ciddi farklılık gösterebilir."),
        ("Partnerden kasıtlı olarak gizlenen bir borç ya da harcama da bir tür sadakatsizlik sayılabilir.", True,
         "Doğru. Garbinsky ve arkadaşları buna finansal sadakatsizlik der: Partnerin onaylamayacağı beklenen bir finansal davranışı yapıp kasıtlı olarak ondan saklamak. Kitaba göre her kişisel harcamayı açıklamamak bu kapsama girmez, anahtar unsur beklenen ortak kural ile kasıtlı gizlilik arasındaki farktır."),
        ("Aldatma ortaya çıktıktan sonra ilişki artık onarılamaz.", False,
         "Yanlış. Kitabın aktardığı terapi araştırmalarında, sadakatsizlik yaşayan çiftlerin başlangıçtaki yüksek sıkıntısı ile diğer çiftler arasındaki fark tedavi sonunda ve altı aylık izlemde büyük ölçüde kapanabilmiştir. Kitap bunun “aldatmadan sonra mutlaka birlikte kalınmalıdır” anlamına gelmediğini de ekler: Gösterilen yalnızca, sadakatsizliğin ilişkiyi otomatik olarak onarılamaz hale getirmediğidir."),
        ("Aldatmanın arkasında tek bir neden değil, birbirinden farklı motivasyonlar olabilir.", True,
         "Doğru. Selterman ve arkadaşlarının sadakatsizlik deneyimi yaşamış 495 kişiyle yaptığı çalışmada öfke, ihmal edilme, sevginin azalması, düşük bağlılık, özsaygıyı güçlendirme arzusu ve stres gibi durumsal etkenler ayrı motivasyonlar olarak ortaya çıktı. Örneklemin önemli bölümü genç yetişkinlerdi, yani dağılım genellenemez. Kitap bunun sorumluluğu ortadan kaldırmadığını da vurgular: Açıklama, mazeret değildir."),
    ],
    "seviyeler": [
        (0, "Atasözlerine güvenen", "İnançlarının çoğu gündelik dilin kesin cümlelerine yakın: “Bir kez aldatan hep aldatır”, “Mutlu olan aldatmaz.” Kitap bu cümlelerin bazılarında bir gerçek payı olduğunu ama verilerin bu kesinliği taşımadığını gösterir. Araştırmalar çoğu zaman risk farkından söz eder, kaderden değil. Geçmiş davranış bir risk bilgisi taşıyabilir, ama insanın üzerine ömür boyu sabit bir etiket yapıştırmaz. Kitabın uyarısı: “Risk değerlendirmesi ile insanı mahkûm etmek aynı şey değildir.”"),
        (3, "Gri alanı gören", "Bazı inançlarında verilerle aynı yerdesin, bazılarında atasözlerine yakınsın. Aldatma konusu tam da bu yüzden zor: İnsanlar merkezde büyük ölçüde uzlaşır, sınırlarda ise ciddi biçimde ayrışır. Kitaba göre iki insan “tek eşliyiz” dediğinde mutlaka aynı sözleşmeye imza atmış olmayabilir. Sadakat yalnız yasakların listesi değil, sınırlar konusunda ortak beklentidir. Dijital iletişim de bu gri alanı büyütür."),
        (5, "İhanet ekonomisti", "Aldatma hakkındaki yaygın inançları verilerden ayırt edebiliyorsun. Kitabın vardığı yer de bu: Aldatmanın ekonomik çekirdeği partner sayısından çok, üzerinde anlaşılmış kuraldan gizli sapmadır. Bu yüzden asıl maliyet yalnız kaybedilen ilişki değil, diğer insanın eksik bilgiyle verdiği kararlardır. Gizlilik bu yüzden davranışın üstüne ayrı bir maliyet ekler. Şimdi bölümün kapanış sorusu: “Bir kez bozulan güven yeniden kurulabilir mi ve kurulacaksa bunun bedelini hangi davranışlar, hangi zaman ve hangi karşılıklılık öder?”"),
    ],
    "bolum": "23",
}

# 28 — profil — Bölüm 24 (ve 23)
ICERIK["affetmek-guvenmek"] = {
    "kanca": "Üç ayrı karar çoğu zaman tek karar sanılır, sen hangisinde duruyorsun?",
    "sorular": [
        ("Yakın biri sana önemli bir konuda yalan söyledi ve özür diledi. İlk haftalarda sen?", [
            ("F", "Öfkem geçmiyor, özrü duymak bile zor geliyor"), ("G", "Özrü kabul ederim ama her sözünü tartarım"),
            ("U", "Kızgın değilim, ama nasıl devam edeceğimizi bilemem"), ("H", "Özür dilediyse konu kapanır, uzatmam")]),
        ("Sana göre affetmek…", [
            ("F", "Yapılanı kabul edilebilir saymak gibi gelir"), ("G", "Olabilir, ama güven ayrı bir hesaptır"),
            ("U", "İnsanı affetmek, ilişkiye devam etmek demek değildir"), ("H", "Unutup yola devam etmektir")]),
        ("Güveni sarsmış biri “Artık bana güvenmelisin” derse…", [
            ("F", "Bunu isteme hakkı olmadığını düşünürüm"), ("G", "Söz yetmez, davranışını görmem gerekir derim"),
            ("U", "Güvensem bile nasıl devam edeceğimizi konuşmamız gerekir"), ("H", "Haklı olabilir, ne kadar uzatabiliriz ki")]),
        ("Bir arkadaşın, partnerinin ondan gizlediği bir borcu öğrenmiş. Ona ne dersin?", [
            ("F", "“Kızgınlığın çok doğal, acele etme.”"), ("G", "“Bundan sonra hesapları birlikte görmek isteyebilirsin.”"),
            ("U", "“Affetmek ile birlikte kalmak ayrı kararlar.”"), ("H", "“Para bu, çözülür, büyütme.”")]),
        ("Böyle bir süreçte seni en çok ne zorlar?", [
            ("F", "Yaşananı içimde taşımaya devam etmek"), ("G", "Telefonu çaldığında aklıma kötü ihtimallerin gelmesi"),
            ("U", "Her şey yoluna girmiş gibi davranmak"), ("H", "Konunun tekrar tekrar açılması")]),
        ("Hangi cümle sana daha yakın?", [
            ("F", "Affetmek hak edilir."), ("G", "Affettim ama eskisi gibi değil."),
            ("U", "Affetmek bir şey, kalmak başka."), ("H", "Kin tutan önce kendini yorar.")]),
    ],
    "sonuclar": {
        "F": ("Affetmede takılan", "Senin için yaşanan şey kolay kapanmaz. Kitap affetmeyi unutmak ya da yapılanı kabul edilebilir saymak olarak görmez, daha çok sürekli misilleme ve öfke döngüsünden çıkabilmekle ilişkilendirir. Bazı çalışmalarda affetme eğilimi daha az olumsuz çatışmayla bağlantılı bulunmuştur. Ama kitap bunun “ne yapılırsa yapılsın affedin” anlamına gelmediğini vurgular. Onarımın takvimini de ihlali yapan kişi tek taraflı belirleyemez.", "23"),
        "G": ("Yeniden güvenmede takılan", "Sen affedebiliyorsun ama güvenin geri gelmesi zaman alıyor. Kitap bu ikisini zaten ayrı kararlar sayar. İhlalden sonra daha fazla bilgi istemek anlaşılırdır, ama geçici güvence ile kalıcı gözetim aynı şey değildir. Kitabın benzetmesiyle eğitim tekerlekleri bisiklet sürmeyi öğretir, beceri ancak onlarsız dengede durulduğunda yerleşir. Belki hedef eski güven değil, yeni bilgiyle kurulan yeni güvendir.", "24"),
        "U": ("Uzlaşmada takılan", "Sen insanı affedebiliyor, hatta ona yeniden güvenebiliyorsun. Takıldığın yer, ilişkinin hangi koşullarla devam edeceği. Kitap bunu çok net ayırır: Affetmek, güvenmek ve uzlaşmak üç ayrı karardır. Birlikte kalmak da tek başına gerçek affetmenin kanıtı değildir. Ekonomik dille söylersek bağışlama, geçmiş borcun kayıtlardan sihirli biçimde silinmesi değil, ilişkinin hangi koşullarla süreceğine dair yeni bir karardır.", "23"),
        "H": ("Hızlı kapatan", "Sen kırgınlığı uzatmayı sevmiyorsun, özür geldiyse sayfayı çeviriyorsun. Bu ilişkiye esneklik kazandırabilir. Ama kitap bir sınır hatırlatır: McNulty’nin yeni evli çiftlerle çalışmasında sorunlu davranış sık tekrarlanıyorsa yüksek affedicilik her koşulda olumlu sonuç vermemiştir. Kitabın deyişiyle affetmenin iyi olması, sınırların gereksiz olduğu anlamına gelmez. Özür bir sinyaldir, güvenilirliğini sonraki davranış belirler.", "24"),
    },
}

# 29 — senaryo (8 soru) — Bölüm 22–28
ICERIK["kriz-senaryolari"] = {
    "kanca": "Kriz geldiğinde herkesin gözü başka bir yere kayar, seninki nereye gidiyor?",
    "sorular": [
        ("Yıllardır birliktesiniz ve son zamanlarda hep aynı kavga dönüyor. Bir akşam yalnız kaldığında ilk ne düşünürsün?", [
            ("H", "Bu ilişkiye ne kadar emek verdiğimi"), ("G", "Onun neden değiştiğini, bir şey mi sakladığını"),
            ("A", "Başka bir hayatın nasıl olabileceğini"), ("B", "Birbirimizden ne beklediğimizi hiç konuşup konuşmadığımızı"),
            ("C", "Kendi ayaklarım üstünde nasıl bir hayat sürdüğümü")]),
        ("Partnerinin eski sevgilisiyle senden habersiz uzun uzun mesajlaştığını öğrendin.", [
            ("H", "“Bunca yılımızın üstüne bu mu?” diye düşünürüm"), ("G", "Önce bütün yazışmaları görmek isterim"),
            ("A", "Demek ki o da başka seçeneklere bakıyor, derim"), ("B", "Bunun bizim için aldatma sayılıp sayılmadığını konuşmak isterim"),
            ("C", "İlişkinin dışında kendime ait neyim var, ona bakarım")]),
        ("Partnerin ortak bütçeden habersiz büyük bir harcama yaptığını itiraf etti ve özür diledi.", [
            ("H", "Harcanan parayı ve şimdiye kadar verdiklerimi tartarım"), ("G", "Bundan sonra bütün harcamaları görmek isterim"),
            ("A", "Başka biri olsa böyle yapmazdı, diye düşünürüm"), ("B", "Para konusunda hangi kuralla yaşadığımızı yeniden konuşuruz"),
            ("C", "Kendi birikimimin ve gelirimin ne durumda olduğuna bakarım")]),
        ("Uzun zamandır ilişkiye emek veren hep senmişsin gibi hissediyorsun.", [
            ("H", "Kimin ne verdiğine dair aklımda bir liste oluşur"), ("G", "Onun gerçekte ne kadar istekli olduğunu anlamaya çalışırım"),
            ("A", "Başka biriyle bu kadar uğraşır mıydım, diye düşünürüm"), ("B", "Neyi beklediğimi açıkça söylemediğimi fark ederim"),
            ("C", "Kendi arkadaşlarımı ve uğraşlarımı ihmal ettiğimi fark ederim")]),
        ("Partnerine başka şehirde iyi bir iş teklifi geldi. Sen burada işinin en iyi yerindesin.", [
            ("H", "Şimdiye kadar kimin işi için kim fedakârlık etti, ona bakarız"), ("G", "Bu konuyu ne zamandır düşündüğünü merak ederim"),
            ("A", "Gitmek de kalmak da bir şeyden vazgeçmek, ikisini tartarım"), ("B", "İkimizin de bu ilişkiden ne beklediğini masaya koyarız"),
            ("C", "Hangi karar çıkarsa çıksın kendi işimi korumanın yolunu ararım")]),
        ("Zor bir dönemdesiniz. Bir arkadaşın flört uygulamasını gösterip “bak ne çok seçenek var” diyor.", [
            ("H", "Bunca yatırımı bırakıp sıfırdan başlamak bana pahalı gelir"), ("G", "Ekrandakilerin gerçekte nasıl biri olduğunu kim bilebilir, derim"),
            ("A", "Merakla bakarım, belki gerçekten daha iyisi vardır"), ("B", "Önce ben aslında ne istiyorum, onu bilmem gerek, derim"),
            ("C", "Seçenek olduğunu bilmek içimi rahatlatır ama acele etmem")]),
        ("Partnerin “Beni artık anlamıyorsun” dedi.", [
            ("H", "Ben de onun için yaptıklarımı sıralarım"), ("G", "Bunu neden şimdi söylediğini, arkasında ne olduğunu düşünürüm"),
            ("A", "Belki başka biriyle daha uyumlu olurdu, diye geçer aklımdan"), ("B", "Ondan ne beklediğimi, onun benden ne beklediğini sorarım"),
            ("C", "Hayatımın yalnız bu ilişkiden ibaret olmadığını hatırlarım")]),
        ("Bir krizi atlattınız ve çevreniz “artık eskisi gibisiniz” diyor. Sen?", [
            ("H", "Bu kriz bize neye mal oldu, hâlâ hesaplıyorum"), ("G", "Bir süre daha gözüm açık olacak"),
            ("A", "Başka yolu seçseydik ne olurdu, arada bir düşünürüm"), ("B", "Eskisi gibi değiliz, artık yeni kurallarımız var"),
            ("C", "Bu süreçte kendime ait alanı korumanın iyi geldiğini gördüm")]),
    ],
    "sonuclar": {
        "H": ("Hesap defteri", "Krizde ilk refleksin, verilenleri ve alınanları tartmak. Bu soğukluk değil: Kitap “gerçek aşk hesap yapmaz” cümlesinin bazen eşitsizliği görünmez kıldığını söyler. Ama defterin bir tuzağı var. Geçmişte verilenlerin bir kısmı geri alınamayacak batık maliyettir ve bugünkü karara gereğinden fazla ağırlık verebilir. Her davranışın anında eşdeğer karşılığını beklemek de ilişkiyi muhasebe defterine çevirebilir.", "25"),
        "G": ("Gözcü", "Kriz anında önce bilgiye ihtiyaç duyuyorsun: Ne oldu, neden oldu, başka ne var? Kitap ihlalden sonra daha fazla şeffaflık istemenin anlaşılır olduğunu söyler, ama geçici güvence ile kalıcı gözetimi ayırır. Denetimin bilgi talebinin doğal bir sonu yoktur: Telefon temiz çıkınca bu kez silinmiş mesajlar akla gelebilir. Kitabın sözüyle: Güvenin alternatifi kusursuz bilgi değildir.", "24"),
        "A": ("Alternatif tartan", "Kriz anında aklın seçilmemiş yollara gidiyor: başka biri, başka bir şehir, başka bir hayat. Bu, fırsat maliyetini görmenin doğal bir yolu ve kitaba göre bu farkındalık bazen gerçekten işe yarar. Ama kitap bu karşılaştırmanın adil olmadığını hatırlatır: Mevcut partnerin hatalarını biliyoruz, vazgeçtiğimiz kişinin yapacağı hataları bilmiyoruz. Kitabın sözüyle: Alternatif hayat maliyetsiz değildir, yalnız maliyetlerini henüz yaşamamışızdır.", "26"),
        "B": ("Beklenti yazarı", "Kriz anında sen sorunun kişide mi, beklentide mi olduğunu soruyorsun. Kitaba göre beklenti açığı her zaman partnerin hatası değildir: Beklenti çelişkili, kaynaklarla uyumsuz ya da hiç konuşulmamış olabilir. Bu güçlü bir tarz. Riski şu: Her krizi beklenti meselesi saymak, gerçekten vazgeçilmez olanı gözden kaçırabilir. Kitabın hatırlattığı gibi beklentileri yeniden düzenlemek, temel sınırları silmek değildir.", "28"),
        "C": ("Kendi ayağında", "Kriz anında sen kendi hayatının ayakta olduğundan emin olmak istiyorsun: işin, gelirin, arkadaşların. Kitap bunu kaçış hazırlığı saymaz: Gitme imkânının artması, gitme arzusunun artmasıyla aynı şey değildir. Kitaba göre gidebilme kapasitesi kalmanın anlamını bile güçlendirebilir. Riski şu: Bu dayanaklar ortak yatırımın yerini alırsa ilişki “seçilmiş seçenek” olmaktan çok “şimdilik tutulan seçenek” gibi hissedebilir.", "22"),
    },
}

# 30 — cift — Bölüm 24
ICERIK["kriz-aninda"] = {
    "kanca": "Ayrı ayrı çözün, sonra karşılaştırın: Kriz geldiğinde aynı yöne mi koşuyorsunuz?",
    "sorular": [
        ("Büyük bir tartışmadan sonra:", ["Aynı gün konuşmak", "Bir gece bekleyip konuşmak"]),
        ("Güveni sarsan bir olaydan sonra öncelik:", ["Neden olduğunu anlamak", "Bundan sonrasını konuşmak"]),
        ("Bir özür en çok neyle inandırıcı olur:", ["Hemen ve açıkça dile getirilmesiyle", "Zamanla davranışa yansımasıyla"]),
        ("Krizden sonra telefon ve şifreler:", ["Bir süre açık tutulur", "Herkesin alanı korunur"]),
        ("Para yüzünden bir kriz çıkarsa:", ["Kurallar açıkça yazılır", "Güvene dayalı esneklik korunur"]),
        ("Zor bir konu konuşulurken:", ["Her şey bir kerede masaya konur", "Adım adım, parça parça konuşulur"]),
        ("Affetmek:", ["Sayfayı tamamen kapatmaktır", "Kaydı tutup yola devam etmektir"]),
        ("Kriz atlatılınca ilişki:", ["Eski haline dönmeli", "Yeni kurallarla yeniden kurulmalı"]),
        ("Kalmak ya da gitmek tartışılırken ağır basan:", ["Birlikte geçirilen yıllar", "Önümüzdeki yıllar"]),
        ("Zor dönemde destek:", ["İki kişinin arasında kalır", "Arkadaş, aile ya da uzmanla da paylaşılır"]),
    ],
    "seviyeler": [
        (0, "Farklı kriz dilleri", "Kriz anında çoğu konuda farklı yerlerde duruyorsunuz. Bu ilişkinin zayıf olduğunu göstermez, krizi farklı dillerle yaşadığınızı gösterir. Kitap ilişkiyi bir eksik sözleşme olarak görür: Ortaya çıkacak her durumu önceden yazamazsınız, her şeyin yazılı kurala bağlanması da mümkün değildir. Yazılmayan yerleri birbirinizin iyi niyeti, adalet anlayışı ve geçmiş davranışları doldurur. Farklı cevap verdiğiniz maddeler, henüz konuşulmamış maddeler olabilir."),
        (4, "Kısmi uzlaşma", "Bazı konularda aynı taraftasınız, bazılarında değil. Kitaba göre güven tek bir puan değil, alanlara göre değişen beklentiler bütünüdür. Para konusunda aynı yerde durup konuşma biçiminde ayrışmanız mümkündür. Ayrıştığınız maddelere birlikte bakın. Kitabın sözüyle sağlam ilişki açık anlaşmalar ile hak edilmiş güveni birlikte kullanır. Güven sözleşmenin alternatifi değildir, ikisinden biri tek başına yetmez."),
        (7, "Aynı tarafta", "Kriz anında çoğu konuda aynı yerde duruyorsunuz. Bu, kitabın güven sermayesi dediği şeyin değerli yanı: Her küçük kararı yeniden müzakere etmek zorunda kalmadığınızda ilişkinin işlem maliyeti düşer. Yine de kitap bir uyarı yapar: Krizin kendisi ilişkiyi otomatik olarak güçlendirmez. Kâğıt üzerindeki uyum bir başlangıçtır, güven ise kitaba göre davranıştan beslenir."),
        (9, "Ortak kriz haritası", "Neredeyse her maddede aynı cevabı verdiniz. Kriz geldiğinde ne yapacağınız konusunda ortak bir haritanız var gibi. Kitabın deyişiyle güven belirsizliği ortadan kaldırmaz, belirsizlik içinde birlikte hareket etmenin maliyetini düşürür. Sizin cevaplarınız bu maliyetin düşük olabileceğini, eksik sözleşmenin boşluklarını benzer biçimde doldurduğunuzu düşündürüyor. Gerçek sınav yine davranışta: Kitaba göre özür bir sinyaldir. Güvenilirliğini sonraki davranış belirler."),
    ],
    "bolum": "24",
}
