# -*- coding: utf-8 -*-
# Aşkonomi test serisi — içerik kaynağı.
# DURUM: Sezon 1 TASLAK. Kitabın son metniyle karşılaştırılıp doğrulanmadan yayına alınmaz.
# tur: profil | senaryo | mit | cift | hesap | nesil | karne

import datetime as _dt

SEZONLAR = [
    {"no": 1, "ad": "Piyasaya Giriş", "alt": "Kim, kimi, neden seçer?"},
    {"no": 2, "ad": "Sözleşme", "alt": "Evlilik, ev ve emek"},
    {"no": 3, "ad": "Kriz", "alt": "İlişki sarsılınca"},
    {"no": 4, "ad": "Dijital Çağ", "alt": "Kaydırılan kalpler"},
]

TUR_AD = {"profil": "Profil", "senaryo": "Ne yapardın?", "mit": "Mit mi, gerçek mi?", "cift": "Çift testi",
          "hesap": "Hesaplayıcı", "nesil": "Nesil testi", "karne": "Final"}

BOLUM = {
    "01": "Aşk Nedir?", "02": "Aşk ve Rasyonalite", "03": "Kıtlık", "04": "İhtiyaç, Arzu ve Tercih",
    "05": "Aşk Piyasası", "06": "Sinyaller", "07": "Güzellik Ekonomisi", "08": "Para ve Servet",
    "09": "Denklik ve Benzerlik", "15": "Evliliğin Ekonomisi", "16": "Görünmeyen Emek",
    "17": "Çocukların Ekonomisi", "18": "Çok Eşlilik", "19": "Kıskançlık Ekonomisi",
    "22": "Boşanmanın Ekonomisi", "23": "Aldatma ve İhanet Ekonomisi", "24": "Güven Sermayesi",
    "25": "İlişkiye Yatırım", "26": "Fırsat Maliyeti", "27": "Seçenek Bolluğu", "28": "Beklenti Enflasyonu",
    "29": "Modern Evlilik", "30": "Tinder’dan Önce ve Sonra", "31": "Aşkın Endüstrisi",
    "32": "Küreselleşen Mahremiyet", "33": "Yalnızlığın Ekonomisi", "34": "Geleceğin Aşk Ekonomisi",
}

# ---- Başlık listesi (onaylı) ----
LISTE = [
    # no, slug, başlık, tür, bölüm
    (1, "fiyatin-ne", "Aşk piyasasında fiyatın ne?", "profil", "05"),
    (2, "kacan-mi-kovalanan-mi", "Kaçan mısın, kovalanan mı?", "profil", "03"),
    (3, "kalp-mi-akil-mi", "Kalbin mi hesap yapıyor, aklın mı?", "senaryo", "02"),
    (4, "ilk-bulusma-sinyali", "İlk buluşmada verdiğin sinyal aslında ne diyor?", "profil", "06"),
    (5, "guzellik-mitleri", "Güzellik hakkında inandığın 6 şeyden kaçı doğru?", "mit", "07"),
    (6, "para-konusulunca", "Para konuşulunca ilişkinde ne oluyor?", "senaryo", "08"),
    (7, "benzer-mi-zit-mi", "Kendine benzeyeni mi seçiyorsun, zıttını mı?", "profil", "09"),
    (8, "ihtiyac-arzu-tercih", "Sevgilin ihtiyaç mı, arzu mu, tercih mi?", "profil", "04"),
    (9, "askin-alti-tanimi", "Aşkın 6 tanımından hangisi senin?", "profil", "01"),
    (10, "birbirinizi-fiyatlamak", "Birbirinizi ne kadar doğru “fiyatlıyorsunuz”?", "cift", "05"),
    (11, "evlilik-ne", "Evlilik senin için yatırım mı, sigorta mı, ortaklık mı?", "profil", "15"),
    (12, "gorunmeyen-emek", "Görünmeyen Emek Hesaplayıcı: Evde kimin mesaisi yazılmıyor?", "hesap", "16"),
    (13, "ev-isini-kim-yapiyor", "Ev işini kim yaptığını sanıyor, kim yapıyor?", "cift", "16"),
    (14, "cocugun-maliyeti", "Bir çocuğun gerçek maliyeti: 6 iddia", "mit", "17"),
    (15, "kiskanclik", "Kıskançlığın koruma mı, sahiplenme mi?", "profil", "19"),
    (16, "cok-eslilik-mitleri", "Çok eşlilik tarihi: Mit mi, gerçek mi?", "mit", "18"),
    (17, "iliski-sozlesmesi", "İlişkin bir sözleşme olsaydı hangi maddesi bozuk olurdu?", "senaryo", "15"),
    (18, "bosanmanin-faturasi", "Boşanmanın gerçek faturası", "mit", "22"),
    (19, "evliligin-yuzyili", "Evliliğin hangi yüzyıldan?", "nesil", "29"),
    (20, "ayni-evlilik", "İkiniz aynı evliliği mi hayal ediyorsunuz?", "cift", "15"),
    (21, "beklenti-enflasyonu", "Beklenti Enflasyonu Endeksin kaç?", "hesap", "28"),
    (22, "iliski-getirisi", "İlişki Yatırım Getirisi hesaplayıcı", "hesap", "25"),
    (23, "batik-maliyet", "Batık maliyet: Bitmesi gereken bir ilişkide misin?", "senaryo", "25"),
    (24, "neye-mal-oldu", "Bu ilişki sana neye mal oldu?", "hesap", "26"),
    (25, "cok-secenek", "Çok seçenek seni mutsuz mu ediyor?", "profil", "27"),
    (26, "guven-sermayesi", "Güven Sermayen artıda mı, ekside mi?", "hesap", "24"),
    (27, "aldatma-mitleri", "Aldatma hakkında 6 yaygın inanç: Kaçı doğru?", "mit", "23"),
    (28, "affetmek-guvenmek", "Affetmek, güvenmek, uzlaşmak: Hangisinde takılıyorsun?", "profil", "24"),
    (29, "kriz-senaryolari", "Ne yapardın? 8 kriz senaryosu", "senaryo", "22"),
    (30, "kriz-aninda", "Kriz anında aynı tarafta mısınız?", "cift", "24"),
    (31, "tinder-oncesi-sonrasi", "Tinder öncesi mi aşıksın, sonrası mı?", "nesil", "30"),
    (32, "hangi-on-yil", "Aşk hayatın hangi on yıla ait?", "nesil", "29"),
    (33, "kaydirma-ekonomisi", "Kaydırma ekonomisi: Uygulamalar hakkında 6 iddia", "mit", "30"),
    (34, "ask-endustrisi", "Aşk endüstrisi seni ne kadar satın aldı?", "hesap", "31"),
    (35, "yalnizligin-fiyati", "Yalnızlığın fiyatı hakkında ne biliyorsun?", "mit", "33"),
    (36, "yalniz-misin", "Yalnız mısın, yalnızlığı mı seçtin?", "profil", "33"),
    (37, "ask-icin-ulke", "Aşk için ülke değiştirir miydin?", "senaryo", "32"),
    (38, "goruldu-ekonomisi", "“Görüldü” ekonomisi: Mesajların ne sinyal veriyor?", "senaryo", "06"),
    (39, "2040-aski", "2040’ın aşkına hazır mısın?", "profil", "34"),
    (40, "karne", "Aşkonomi Karnesi", "karne", ""),
]

# ---- Yayın takvimi: ilk 6 test hemen, sonra her Pazartesi ve Perşembe ----
ILK_ACILIS = _dt.date(2026, 10, 6)
def takvim():
    d = {}
    for no in range(1, 7):
        d[no] = ILK_ACILIS
    gun = _dt.date(2026, 10, 12)  # Pazartesi
    no = 7
    while no <= 39:
        if gun.weekday() in (0, 3):
            d[no] = gun; no += 1
        gun += _dt.timedelta(days=1)
    d[40] = d[39]
    return d

# ---- Sezon 1 içerikleri ----
# profil/senaryo: "sorular": [(soru, [(anahtar, seçenek), ...]), ...], "sonuclar": {anahtar: (ad, metin, bölüm)}
# mit: "sorular": [(iddia, dogru_mu, açıklama)], "seviyeler": [(min_puan, ad, metin)]
# cift: "sorular": [(soru, [seçenek1, seçenek2])], "seviyeler": [(min_eslesme, ad, metin)]

ICERIK = {}

ICERIK["fiyatin-ne"] = {
    "kanca": "Herkesin bir fiyatı var. Seninki para değil.",
    "sorular": [
        ("Bir ilk buluşmada seni en çok ne soğutur?", [
            ("Z", "Son dakika iptal etmesi"), ("D", "Sürekli telefonuna bakması"),
            ("G", "Anlattıklarının birbirini tutmaması"), ("O", "İkinci buluşmayı hemen planlamaya kalkması"),
            ("H", "Her şeyin fazla sıradan geçmesi")]),
        ("Hangi jest seni kazanır?", [
            ("Z", "En yoğun haftasında sana bir akşam ayırması"), ("D", "Bir ay önce söylediğin küçük bir ayrıntıyı hatırlaması"),
            ("G", "Söylediği saatte, söylediği yerde olması"), ("O", "“Bu hafta sonu kendine zaman ayır” demesi"),
            ("H", "Hiç beklemediğin anda bir sürpriz")]),
        ("Bir ilişkide neyi “zarar” hanesine yazarsın?", [
            ("Z", "Hep bir sonraki haftaya ertelenen planları"), ("D", "Yarım kulakla dinlenmeyi"),
            ("G", "Küçük de olsa yalanları"), ("O", "Her adımının sorgulanmasını"),
            ("H", "Her günün bir öncekinin kopyası olmasını")]),
        ("Arkadaşın yeni sevgilisini anlatıyor. Hangi cümle seni ikna eder?", [
            ("Z", "“Her gün mutlaka görüşüyoruz.”"), ("D", "“Beni gerçekten dinliyor.”"),
            ("G", "“Ne dediyse yaptı.”"), ("O", "“Kıskanç değil, beni rahat bırakıyor.”"),
            ("H", "“Onunla hiç sıkılmıyorum.”")]),
        ("Hangi cümle sana daha yakın?", [
            ("Z", "Sevgi, birine ayrılan saatlerle ölçülür."), ("D", "Görülmek, sevilmekten önce gelir."),
            ("G", "Söz, sözleşmeden sağlamdır."), ("O", "Sevmek tutmak değil, bırakabilmektir."),
            ("H", "Rutin, aşkın sessiz katilidir.")]),
        ("Bir tartışmadan sonra barışmanın en hızlı yolu?", [
            ("Z", "Hemen gelip yüz yüze konuşmak"), ("D", "Ne hissettiğimi gerçekten anlamaya çalışmak"),
            ("G", "Tutulabilecek bir söz vermek"), ("O", "Biraz zaman tanıyıp sonra konuşmak"),
            ("H", "Beni bir anda güldürecek çılgın bir fikir")]),
    ],
    "sonuclar": {
        "Z": ("Senin fiyatın: Zaman", "Seni kazanmak için çiçek de pahalı hediye de yetmez; takvimde yer açılması gerekir. Senin gözünde sevginin gerçek bedeli ayrılan saatlerdir, çünkü zaman kimsenin çoğaltamadığı tek kaynaktır. İktisatta değer kıtlıktan doğar; senin aşk piyasanda en kıt mal da zaman.", "03"),
        "D": ("Senin fiyatın: Dikkat", "Sen sevilmekten önce görülmek istiyorsun. Telefon masaya ters konmadıkça teklif geçersiz. Dikkat, verenin başka her şeyden vazgeçtiği için pahalı bir sinyaldir; sen de tam olarak bu bedeli ödeyeni ciddiye alıyorsun.", "06"),
        "G": ("Senin fiyatın: Güven", "Senin para birimin tutarlılık: Söylenen saatte orada olmak, verilen sözü tutmak. Güven yavaş biriken, hızlı harcanan bir sermayedir ve sen hesabını çok dikkatli tutuyorsun. Bir yalan, senin piyasanda iflas sebebidir.", "24"),
        "O": ("Senin fiyatın: Alan", "Seni kazanmanın yolu seni tutmaya çalışmamaktan geçiyor. Sen sevildiğini, özgür bırakıldığında hissediyorsun. Kıskançlık ve kontrol senin için fiyatı anında ikiye katlayan şeyler. Kitabın sorusu tam sana göre: Neyi kaybetmekten korkuyoruz?", "19"),
        "H": ("Senin fiyatın: Heyecan", "Senin için en büyük maliyet sıkılmak. Aynı şeyin her tekrarı bir öncekinden biraz daha az haz verir; iktisatçılar buna azalan marjinal fayda der. Sen bunu herkesten çabuk hissediyorsun. Riskin şu: Seçenekler bollaştıkça, yenisini aramak bir alışkanlığa dönüşebilir.", "27"),
    },
}

ICERIK["kacan-mi-kovalanan-mi"] = {
    "kanca": "“Kaçan kovalanır” derler. Peki sen hangisisin?",
    "sorular": [
        ("Hoşlandığın biri mesajına 6 saat sonra cevap verdi. Sen?", [
            ("K", "Ben de en az 7 saat beklerim"), ("V", "Hemen yazarım, belki bir şey olmuştur"),
            ("D", "Ne zaman müsaitsem o zaman yazarım"), ("S", "Hiç yazmam, zaten bir şey çıkmazdı")]),
        ("İlk buluşmanın sonunda…", [
            ("K", "“Ararım” derim, birkaç gün aramam"), ("V", "Eve varmadan “çok güzeldi” yazarım"),
            ("D", "Hoşlandıysam bunu açıkça söylerim"), ("S", "Bir sonraki adımı ona bırakırım")]),
        ("Seni en çok kim cezbeder?", [
            ("V", "Kolay ulaşılamayan, gizemli biri"), ("K", "Benim için çabalayan, emek veren biri"),
            ("D", "Ne istediğini açıkça söyleyen biri"), ("S", "Beni hiç zorlamayan, yavaş ilerleyen biri")]),
        ("Bir ilişkide hep ulaşılabilir olmak sana nasıl hissettirir?", [
            ("K", "Değerimin düştüğünü hissederim"), ("V", "Huzurlu; ben zaten hep oradayım"),
            ("D", "Karşılıklıysa güzel"), ("S", "Biraz boğucu")]),
        ("Arkadaşların seni nasıl tarif eder?", [
            ("K", "“Onu yakalamak zor.”"), ("V", "“Sevince her şeyini verir.”"),
            ("D", "“Ne istediğini bilir.”"), ("S", "“Hep izler, nadiren adım atar.”")]),
        ("Hangi cümleye katılırsın?", [
            ("K", "Değer, ulaşılmazlıktan doğar."), ("V", "Sevgi saklanmaz, gösterilir."),
            ("D", "Oyun oynayan kaybeder."), ("S", "Hiç başlamayan ilişki bitmez de.")]),
    ],
    "sonuclar": {
        "K": ("Kaçan: Kıtlık stratejisi", "Arzını bilerek kısıyorsun. İktisatta kıt olan mal pahalıdır; sen de ulaşılmaz kalarak değerini yüksek tutuyorsun. İşe yarıyor, ama bir bedeli var: Kıtlıkla yükselen fiyat güven kurmayı zorlaştırır. Hep kaçan biri, bir gün yakalanmaktan korkmaya başlar.", "03"),
        "V": ("Kovalayan: Güçlü talep", "Talebin güçlü ve fiyata pek duyarlı değil; sevdiğinde hesabı kitabı bırakıyorsun. Bu cömertlik güzel, ama piyasanın acı bir kuralı var: Bolca arz edilen şeyin değeri karşı tarafın gözünde düşebilir. Sorun sevmen değil, karşılığına bakmadan sevmen.", "05"),
        "D": ("Dengede: Açık fiyat", "Oyun oynamıyorsun. Ne istediğini söylüyor, karşılığını bekliyorsun. İki tarafın da istekli olduğu yerde eşleşme kurulur; sen o noktayı tahmin oyunlarıyla değil, açık sinyallerle arıyorsun. Bazen “fazla açık” bulunabilirsin ama seninle kimse kâhinlik yapmak zorunda kalmaz.", "06"),
        "S": ("Seyirci: Piyasanın dışında", "Risk almaktansa hiç oynamamayı seçiyorsun; reddedilme ihtimali kazanma ihtimalinden ağır basıyor. Ama iktisadın en sert dersi şu: Hiç seçmemek de bir seçimdir ve onun da bir maliyeti vardır. Kaçırdığın fırsatlar hiçbir faturada görünmez.", "26"),
    },
}

ICERIK["kalp-mi-akil-mi"] = {
    "kanca": "Kalple akıl gerçekten düşman mı? 6 zor seçimde kendini dene.",
    "sorular": [
        ("İki seçenek var: Seni heyecanlandıran ama düzensiz yaşayan biri, ya da güvenilir ama “kıvılcım”ı olmayan biri.", [
            ("R", "Güvenilir olan. Kıvılcım sonradan gelir, istikrar gelmez."), ("T", "Heyecan. Hayat bir kere."),
            ("S", "İlk andaki hissim neyse o."), ("D", "İkisiyle birer kez daha buluşur, sonra karar veririm.")]),
        ("Sevgilin başka bir şehirde iş teklifi aldı.", [
            ("R", "Kira, ulaşım, kariyer… artı-eksi listesi yaparım."), ("T", "Nereye giderse peşinden giderim."),
            ("S", "İçime ne doğarsa onu yaparım."), ("D", "Önce ne istediğimizi konuşur, sonra hesap yaparız.")]),
        ("Bir ilişkinin bitmesi gerektiğini nasıl anlarsın?", [
            ("R", "Verdiklerimle aldıklarım arasındaki fark büyüdüğünde"), ("T", "Kalbim artık çarpmadığında"),
            ("S", "Bir sabah kalkıp “tamam” dediğimde"), ("D", "Hissettiğim ve gördüğüm şeyler aynı yeri gösterdiğinde")]),
        ("Hediye alırken…", [
            ("R", "Bütçe belirler, işe yarar bir şey alırım"), ("T", "Bütçeyi aşsam da onu en çok mutlu edecek şeyi alırım"),
            ("S", "Vitrinde gözüme çarpanı alırım"), ("D", "Ne istediğini çaktırmadan öğrenir, makul fiyata bulurum")]),
        ("“Aşk kördür” sözü için ne dersin?", [
            ("R", "Kör değil, hesabı sonra yapar."), ("T", "Kördür ve iyi ki öyledir."),
            ("S", "Kör değil, sadece çok hızlıdır."), ("D", "Başta kördür, zamanla gözlüğünü takar.")]),
        ("Evlilik kararı ne zaman verilir?", [
            ("R", "Ekonomik ve pratik koşullar hazır olunca"), ("T", "Doğru kişiyi bulduğun an"),
            ("S", "Bir gün “işte bu” diye hissettiğinde"), ("D", "Hem içinden geldiğinde hem şartlar elverdiğinde")]),
    ],
    "sonuclar": {
        "R": ("Kalbin bir muhasebeci", "Sen sevmiyor değilsin; sadece sevginin hesabını da tutuyorsun. Bu sanıldığı kadar soğuk bir şey değil: Gelecek planı yapmak, birine ciddi yatırım yapmak demektir. Riskin şu: Her şeyin hesaplanabildiğine inanınca, hesaba girmeyen şeyler görünmez olur.", "25"),
        "T": ("Kalbin bir kumarbaz", "Sen büyük oynarsın. Olasılıkları bilsen de kalbinin sesine uyarsın. Hayatın en güzel hikâyeleri böyle yazılır, en pahalı faturaları da. İktisatçılar buna “risk sever” der; sen ise sadece “yaşamak” diyorsun.", "01"),
        "S": ("Kalbin bir kestirme yol", "Sen hesap yapmıyorsun ama rastgele de karar vermiyorsun: Sezgilerin, yaşadıklarından süzülmüş hızlı kurallar. Davranışsal iktisat bunlara “zihinsel kestirmeler” der. Çoğu zaman şaşırtıcı derecede isabetlidirler; ama yanıldığında nedenini bulmak zordur.", "04"),
        "D": ("Kalp ile akıl ortaklığı", "Ne körü körüne atlıyorsun ne de her şeyi tabloya döküyorsun: Önce hissediyor, sonra kontrol ediyorsun. Kitabın ikinci bölümü tam bu soruyla açılır: Kalp ile akıl gerçekten düşman mı? Senin cevabın belli: Hayır, ortak.", "02"),
    },
}

ICERIK["ilk-bulusma-sinyali"] = {
    "kanca": "Sen bir şey söylüyorsun. Karşındaki başka bir şey duyuyor.",
    "sorular": [
        ("İlk buluşmanın yerini nasıl seçersin?", [
            ("E", "Onun sevdiği şeyleri araştırıp ben seçerim"), ("V", "Şık, adı bilinen bir yer"),
            ("D", "“Ben şurayı severim, sen ne dersin?” diye sorarım"), ("G", "Son ana kadar söylemem, sürpriz olsun")]),
        ("Ne giyersin?", [
            ("E", "Özenle hazırlanırım, emek belli olsun"), ("V", "En iyi, en göz önündeki parçamı"),
            ("D", "Her zaman nasılsam öyle"), ("G", "Biraz farklı bir şey; çözmeye çalışsın")]),
        ("Kendinden ne kadar bahsedersin?", [
            ("E", "Az; daha çok onu dinlerim"), ("V", "Başarılarımdan, gezdiğim yerlerden"),
            ("D", "İyisiyle kötüsüyle ne varsa"), ("G", "Çok az; merak etsin")]),
        ("Hesap geldi.", [
            ("E", "Ben öderim, bu benim jestim"), ("V", "Kartımı hemen çıkarırım"),
            ("D", "Bölüşmeyi teklif ederim"), ("G", "Gülümser, ne yapacağına bakarım")]),
        ("Buluşmadan sonra…", [
            ("E", "Konuştuklarımıza gönderme yapan uzun bir mesaj"), ("V", "Bir fotoğraf ya da story"),
            ("D", "“Çok keyif aldım, tekrar görüşelim.”"), ("G", "Ertesi güne kadar hiçbir şey")]),
        ("Karşındaki hangi cümleyi kurarsa etkilenirsin?", [
            ("E", "“Bunun için uğraştığın belli.”"), ("V", "“Çok etkileyicisin.”"),
            ("D", "“Seninle rahat hissediyorum.”"), ("G", "“Seni çözemedim.”")]),
    ],
    "sonuclar": {
        "E": ("Emek sinyali", "Sen “seni seviyorum” demek yerine bedeli olan şeyler yapıyorsun: Zaman, özen, araştırma. İktisatta buna pahalı sinyal denir; kolay taklit edilemediği için inandırıcıdır. Karşındaki büyük ihtimalle şunu duyuyor: “Bu insan ciddi.”", "06"),
        "V": ("Vitrin sinyali", "Sen gücünü ve imkânlarını görünür kılıyorsun. Bazı piyasalarda işe yarar; ama vitrin en çok vitrine bakanları çeker. Karşındaki “Neyin var?” sorusunun cevabını aldı. “Kimsin?” sorusununkini henüz almadı.", "08"),
        "D": ("Şeffaflık sinyali", "Sen kartlarını açık oynuyorsun. Söz söylemek bedavadır, bu yüzden ucuz bir sinyal gibi görünür; ama tutarlılık onu pahalı hâle getirir. Söylediğin gibi davrandıkça her buluşma güven hesabına küçük bir yatırım olur.", "24"),
        "G": ("Gizem sinyali", "Sen bilgiyi kısarak merak üretiyorsun. Bilgi eksikliği kısa vadede çekim yaratır; uzun vadede ise karşı tarafı “acaba” sorusuyla baş başa bırakır. Gizem ilk buluşmayı kazandırır, ilişkiyi ise güven.", "03"),
    },
}

# Mit testi: açıklamalar kitaptan değil, yayımlanmış araştırmalardan; kitapla karşılaştırılacak.
ICERIK["guzellik-mitleri"] = {
    "kanca": "Herkes güzelliğin göreceli olduğunu söyler. Veriler aynı şeyi söylemiyor.",
    "sorular": [
        ("Güzel bulunan insanlar iş hayatında ortalamada daha fazla kazanır.", True,
         "Doğru. İktisatçı Daniel Hamermesh ile Jeff Biddle’ın 1994’teki çalışmasından bu yana birçok araştırma, görünüşe bağlı bir “güzellik primi” bulunduğunu gösteriyor."),
        ("Güzellik primi yalnızca modellik, oyunculuk gibi görünüşün önemli olduğu mesleklerde vardır.", False,
         "Yanlış. Aynı çalışmalar, görünüşün işle doğrudan ilgisi olmayan mesleklerde de benzer bir fark buluyor."),
        ("Kimin güzel olduğu konusunda insanlar birbirinden çok farklı düşünür.", False,
         "Yanlış, en azından sanıldığı kadar değil. Langlois ve arkadaşlarının 2000 yılındaki kapsamlı incelemesi, insanların kimi çekici bulduğu konusunda hem kendi kültürleri içinde hem de kültürler arasında belirgin bir uzlaşma buluyor."),
        ("Çekici bulunan insanların daha nazik, daha zeki ve daha başarılı olduğu sanılır.", True,
         "Doğru. Psikologlar buna “güzel olan iyidir” önyargısı der; ilk kez 1972’de Dion, Berscheid ve Walster tarafından gösterildi."),
        ("Çiftler genellikle çekicilik bakımından birbirine yakın kişilerden oluşur.", True,
         "Doğru. Gerçek çiftler üzerindeki çalışmalar (ör. Feingold’un 1988 tarihli meta-analizi) eşler arasında çekicilikte belirgin bir benzerlik buluyor."),
        ("Bir insanı uzun süre tanıdıkça onu ne kadar çekici bulduğumuz değişebilir.", True,
         "Doğru. Hunt, Eastwick ve Finkel’in 2015 tarihli çalışmasına göre birbirini uzun süre tanıdıktan sonra çift olanlarda görünüş benzerliği daha zayıf. Tanıdıkça “güzel” algısı da değişiyor."),
    ],
    "seviyeler": [
        (0, "Vitrine kanan", "Güzellik hakkındaki inançlarının çoğu, verilerin söylediğinden farklı. Rahatsız edici ama önemli bir gerçek: Görünüş, piyasada sandığından daha fazla ödüllendiriliyor."),
        (3, "Göz kararı", "Bazı şeyleri doğru tahmin ettin, bazılarında yanıldın. Güzelliğin ekonomisi tam da bu yüzden ilginç: Herkesin bir fikri var, ama veriler çoğu zaman sürpriz yapıyor."),
        (5, "Piyasa analisti", "Güzelliğin piyasada nasıl fiyatlandığını çok iyi okuyorsun. Şimdi zor soru: Bu primi adil buluyor musun?"),
    ],
    "bolum": "07",
}

ICERIK["para-konusulunca"] = {
    "kanca": "Aşk parayla satın alınmaz. Peki faturayı kim ödüyor?",
    "sorular": [
        ("İlk buluşmada hesap?", [
            ("O", "Davet eden öder, sonra sıra değişir"), ("A", "Herkes kendi payını öder"),
            ("K", "Zaten pahalı olmayan bir yer seçerim"), ("C", "Ben öderim, tartışmaya gerek yok")]),
        ("Birlikte yaşamaya başladınız. Kira ve faturalar?", [
            ("O", "Hepsi tek, ortak hesaptan"), ("A", "Gelire göre paylaşılır ama hesaplar ayrı kalır"),
            ("K", "Önce bütçe tablosu, sonra karar"), ("C", "Kim daha rahatsa o öder, saymayız")]),
        ("Partnerin sana sormadan büyük bir alışveriş yaptı.", [
            ("O", "Bozulurum; o bizim ortak paramız"), ("A", "Kendi parasıysa söz hakkım yok"),
            ("K", "Birikim planımızı bozdu mu, ona bakarım"), ("C", "Mutlu olduysa sorun değil")]),
        ("Gelirleriniz arasında büyük fark var.", [
            ("O", "Fark etmez, hepsi bizim"), ("A", "Herkes gücü oranında katkı verir"),
            ("K", "Fazlası birikime gider"), ("C", "Çok kazanan öbürünü şımartsın")]),
        ("Para yüzünden hangi kavga tanıdık geliyor?", [
            ("O", "“Bunu neden bana sormadın?”"), ("A", "“Benim paramla ilgili konuşma.”"),
            ("K", "“Yine mi harcadın?”"), ("C", "“Neden bu kadar hesapçısın?”")]),
        ("Hangi cümle seni anlatır?", [
            ("O", "Evlilik ortaklıksa kasa da ortaktır."), ("A", "Ayrı cüzdan, sağlam ilişki."),
            ("K", "Bugünün aşkı, yarının güvencesiyle büyür."), ("C", "Para harcamak içindir, hele sevdiğin için.")]),
    ],
    "sonuclar": {
        "O": ("Ortak kasa", "Senin için ilişki bir ortaklık, ortaklığın da tek bir kasası olur. Güzel tarafı: “Benim param, senin paran” hesabı yok. Riskli tarafı: Ortak kasada harcama kararları da ortak olmak zorunda. Kitabın sorusu: Aşk yetiyorsa neden evleniyoruz? Cevabın bir kısmı tam burada, ortak bütçede.", "15"),
        "A": ("Ayrı cüzdan", "Sen aşkı paylaşıyorsun, cüzdanı değil. Bu bencillik değil, bağımsızlığı korumanın bir yolu. Modern ilişkiler bu yöne kayıyor: Zorunlu kurumdan seçilebilir ortaklığa. Tek uyarı: Hesaplar ayrı olunca, parasal olmayan emeğin kimde kaldığı görünmez olabilir.", "29"),
        "K": ("Tasarruf eden kalp", "Senin için para harcanacak değil, korunacak bir şey: Yarının güvencesi. Bu ilişkiye istikrar getirir. Ama tasarruf eden biriyle harcayan biri eşleşince kavga paradan değil, paranın ne anlama geldiğinden çıkar: Senin için güvenlik, onun için özgürlük.", "08"),
        "C": ("Cömert kalp", "Sen sevgiyi biraz da harcayarak gösteriyorsun: Hediye, davet, sürpriz. Cömertlik güzel bir sinyaldir; ama koca bir endüstri de tam bu duygunun üzerine kurulu, çiçekten pırlantaya, düğünden balayına. Sorman gereken soru: Bu harcama ona mı, yoksa bir beklentiye mi?", "31"),
    },
}

ICERIK["benzer-mi-zit-mi"] = {
    "kanca": "Zıt kutuplar gerçekten birbirini çeker mi? Senin seçimlerin ne diyor?",
    "sorular": [
        ("İdeal partnerin hangi konuda sana benzemeli?", [
            ("B", "Neredeyse her konuda"), ("Z", "Hiçbir konuda; yoksa sıkılırım"),
            ("Y", "Benden biraz daha ileride olsun"), ("T", "Değerlerde aynı, yeteneklerde farklı")]),
        ("Eğitim düzeyi?", [
            ("B", "Benimkine yakın olmalı"), ("Z", "Hiç önemli değil"),
            ("Y", "Benden yüksekse daha iyi"), ("T", "Birbirimizle konuşabildiğimiz sürece fark etmez")]),
        ("Hafta sonu planı…", [
            ("B", "İkimizin de sevdiği aynı şeyi yaparız"), ("Z", "Ben onun dünyasını keşfederim, o benimkini"),
            ("Y", "Onun çevresine girer, yeni insanlar tanırım"), ("T", "Biri planlar, öbürü uygular")]),
        ("Tartıştığınızda…", [
            ("B", "Nadiren tartışırız, aynı düşünürüz"), ("Z", "Sık ama heyecanlı"),
            ("Y", "Onun bakış açısından öğrenirim"), ("T", "Biri sakinleştirir, öbürü çözer")]),
        ("Ailesiyle tanışınca neye bakarsın?", [
            ("B", "Benim aileme benzeyip benzemediğine"), ("Z", "Ne kadar farklı olduklarına"),
            ("Y", "Nasıl bir çevreden geldiğine"), ("T", "Birbirleriyle nasıl anlaştıklarına")]),
        ("“Tencere yuvarlanmış, kapağını bulmuş.”", [
            ("B", "Tam olarak böyle"), ("Z", "Ben başka bir tencere ararım"),
            ("Y", "Kapak, tencereyi biraz yukarı taşımalı"), ("T", "Tencere ile kapak aynı değil, birbirine uygun")]),
    ],
    "sonuclar": {
        "B": ("Ayna: Benzerini seçen", "Sen kendine benzeyeni seçiyorsun ve yalnız değilsin. Araştırmalar çiftlerin eğitim, yaş ve değerler bakımından birbirine benzeme eğiliminde olduğunu gösteriyor; iktisatçılar buna denk eşleşme diyor. Konforlu bir seçim. Bedeli ise toplum düzeyinde: Benzerler eşleştikçe haneler arasındaki eşitsizlik büyüyebilir.", "09"),
        "Z": ("Zıt kutup", "Sen farklılıktan besleniyorsun; tanımadığın dünya seni çekiyor. Romantik, ama araştırmalar “zıtlar birbirini çeker” sözünü pek desteklemiyor: Kalıcı çiftler daha çok benzerlerden oluşuyor. Senin işin daha zor ama sıkıcı değil: Farkı kavgaya değil heyecana çevirmek.", "04"),
        "Y": ("Bir basamak yukarı", "Sen partnerinde biraz ileride olanı arıyorsun: Daha bilgili, daha deneyimli, daha geniş çevreli. Bunu çıkarcılık sanmak kolay; aslında bir yatırım mantığı, ilişkinin seni büyütmesini istiyorsun. Ama aşk piyasası iki taraflıdır: Yukarı bakan biri, karşısına ne kattığını da hesaba katmalı.", "05"),
        "T": ("Tamamlayıcı", "Sen aynılık değil uyum arıyorsun: Değerler ortak, beceriler farklı. İktisatta buna tamamlayıcı mallar denir; çay ile şeker gibi, birlikte daha değerlidirler. İş bölümünden doğan bu kazanç, iktisatçıların evliliği açıklarken başvurduğu en eski gerekçelerden biri.", "15"),
    },
}

ICERIK["ihtiyac-arzu-tercih"] = {
    "kanca": "Onu seviyor musun, yoksa ona ihtiyacın mı var?",
    "sorular": [
        ("Bir hafta hiç görüşemeseniz?", [
            ("I", "Eksik ve huzursuz hissederim"), ("A", "Özlemden yanarım"),
            ("T", "Kendi işlerime bakarım; döndüğünde yine o"), ("L", "Bir şey değişmez, düzenim bozulur sadece")]),
        ("Onu ilk neden seçtin?", [
            ("I", "Yanımdayken kendimi güvende hissettim"), ("A", "Ondan gözümü alamadım"),
            ("T", "Tanıdığım herkes arasında bana en çok o uydu"), ("L", "Bir şekilde hayatımdaydı, devam etti")]),
        ("Kâğıt üzerinde daha “uygun” biri çıksa?", [
            ("I", "Korkarım ama onu bırakamam"), ("A", "Uygunluk değil, çekim önemli"),
            ("T", "Karşılaştırırım; yine de onu seçerdim diye düşünüyorum"), ("L", "Değiştirmek zahmetli gelir")]),
        ("Onunla ilgili en çok neyi seversin?", [
            ("I", "Hep orada olmasını"), ("A", "Bana hissettirdiklerini"),
            ("T", "Kim olduğunu"), ("L", "Her şeyi bilmesini, açıklamak zorunda kalmamayı")]),
        ("Ayrılık düşüncesi sana ne hissettirir?", [
            ("I", "Panik"), ("A", "Acı ama yaşanmaya değmiş bir tutku"),
            ("T", "Üzüntü; ama hayat devam eder"), ("L", "Bütün düzenin değişmesi; yorucu")]),
        ("Hangi cümle daha yakın?", [
            ("I", "“O olmadan eksiğim.”"), ("A", "“Onu istemekten vazgeçemiyorum.”"),
            ("T", "“Her sabah onu yeniden seçiyorum.”"), ("L", "“Onunla her şey kolay.”")]),
    ],
    "sonuclar": {
        "I": ("İhtiyaç: Vazgeçilmez mal", "Senin için o, fiyatı ne olursa olsun talep ettiğin bir mal. İktisatçılar buna esnek olmayan talep der. Derin bir bağın işareti, ama riskli bir yanı var: Vazgeçemediğin şeyin fiyatını karşı taraf belirler. Sağlıklı ilişki, ihtiyacın karşılıklı olduğu yerde kurulur.", "04"),
        "A": ("Arzu: Yanan motor", "Senin bağın çekim üzerine kurulu: İstemek, özlemek, yanmak. Arzu ilişkinin motorudur ama yakıtı yenilenmeli. Aynı şeyin her tekrarı bir öncekinden biraz daha az haz verir; iktisatta buna azalan marjinal fayda denir. Arzuyu canlı tutan, ilişkiye yeni şeyler katmaktır.", "01"),
        "T": ("Tercih: Her gün yeniden", "Sen onu seçtin; ihtiyaçtan ya da alışkanlıktan değil, alternatifleri görüp yine de onu tercih ettiğin için. İktisatçılar buna açığa vurulan tercih der: Ne söylediğimiz değil, neyi seçtiğimiz neyi değerli bulduğumuzu gösterir. Her gün yeniden seçmek, belki de aşkın en olgun hâli.", "04"),
        "L": ("Alışkanlık: Rahat koltuk", "Rahatsız edici ama dürüst bir sonuç: Bağında alışkanlığın payı büyük. Bu kötü değil; birlikte kurulan düzen bir ilişkinin en değerli birikimlerinden biridir. Ama değiştirmenin maliyeti yüksek olduğunda kalmak ile seçmek aynı şey değildir. Kitabın sorusu: Kalmak ne zaman gitmekten pahalıdır?", "22"),
    },
}

ICERIK["askin-alti-tanimi"] = {
    "kanca": "Kanadalı sosyolog John Alan Lee, 1973’te aşkın altı ayrı tarzı olduğunu öne sürdü. Seninki hangisi?",
    "sorular": [
        ("Aşk sana en çok neyi hatırlatır?", [
            ("E", "İlk görüşte çarpılmayı"), ("L", "Keyifli bir oyunu"), ("S", "Yavaş yavaş derinleşen bir dostluğu"),
            ("P", "Doğru kişiyle kurulan bir hayatı"), ("M", "Uykusuz geceleri"), ("A", "Karşılık beklemeden vermeyi")]),
        ("İdeal başlangıç?", [
            ("E", "Tek bir bakış"), ("L", "Flört, şaka, hafiflik"), ("S", "Yıllardır tanıdığın biri"),
            ("P", "Ortak hedefleri konuşmak"), ("M", "Aklından çıkaramadığın biri"), ("A", "Ona yardım ederken tanışmak")]),
        ("Bir ilişkide neye dayanamazsın?", [
            ("E", "Kıvılcımın sönmesine"), ("L", "Fazla ciddiyete"), ("S", "Güvenin sarsılmasına"),
            ("P", "Plansızlığa"), ("M", "Belirsizliğe, cevapsız mesaja"), ("A", "Sevdiğimin mutsuz olmasına")]),
        ("Sevgilin sana nasıl hissettirmeli?", [
            ("E", "Büyülenmiş"), ("L", "Özgür"), ("S", "Evinde"),
            ("P", "Güvende ve yolunda"), ("M", "Vazgeçilmez"), ("A", "Ona iyi gelen biri")]),
        ("Ayrılık…", [
            ("E", "Tutku bittiyse biter"), ("L", "Hayat devam ediyor, başkaları da var"), ("S", "Dostluk kalır"),
            ("P", "Mantıklı değilse bitirmek gerekir"), ("M", "Kabullenmesi çok zor"), ("A", "O mutluysa ben de razıyım")]),
        ("Hangi cümle seni anlatır?", [
            ("E", "Aşk, kalbin hızlanmasıdır."), ("L", "Aşk, ciddiye alınmayacak kadar güzel bir oyundur."),
            ("S", "Aşk, en iyi arkadaşınla yaşlanmaktır."), ("P", "Aşk, doğru ortağı seçmektir."),
            ("M", "Aşk, ya hep ya hiçtir."), ("A", "Aşk, vermektir.")]),
    ],
    "sonuclar": {
        "E": ("Eros: Tutku", "Senin için aşk, kalbin hızlanmasıyla başlar. Çekim, güzellik ve yoğunluk senin aşk dilin. Kıvılcım olmadan bir ilişkiye adım atmıyorsun. Tutkulu başlangıçlar unutulmaz; asıl soru, kıvılcımın günlük hayata nasıl taşınacağı.", "01"),
        "L": ("Ludus: Oyun", "Sen aşkı bir oyun gibi yaşıyorsun: Hafif, keyifli, bağlayıcı olmayan. Seçeneklerin açık kalmasını seviyorsun. Bu özgürlük güzel, ama seçenek bolluğunun bir bedeli var: Her şeyin bir alternatifi olduğunda hiçbir şeye tam bağlanmak zorlaşır.", "27"),
        "S": ("Storge: Dostluk", "Senin aşkın yavaş yanar ama uzun sürer. Önce dostluk, sonra güven, en son aşk. Gösterişli başlangıçlara pek inanmıyorsun; zamanla biriken ortak geçmişe inanıyorsun. İlişkinin en değerli varlığı senin için görünmez olan: Güven.", "24"),
        "P": ("Pragma: Akıllı seçim", "Sen aşkı doğru ortağı seçmek olarak görüyorsun: Değerler, hedefler, hayat planı. Bu soğukluk değil, geleceği ciddiye almak. İktisatçıların evliliği bir ortaklık sözleşmesi olarak incelemesinin nedeni de bu: Aşk tek başına yetiyorsa, neden sözleşme yapıyoruz?", "15"),
        "M": ("Mania: Yoğunluk", "Senin aşkın yoğun: Ya hep ya hiç. Mesaj gelmediğinde huzursuzlanıyor, belirsizlikte zorlanıyorsun. Bu kadar derin hissedebilmek bir zenginlik; ama kaybetme korkusu büyüdükçe kıskançlık da büyüyebilir. Kitabın sorusu: Neyi kaybetmekten korkuyoruz?", "19"),
        "A": ("Agape: Vermek", "Senin için aşk karşılık beklemeden vermek. Sevdiğinin iyiliği senin iyiliğinden önce geliyor. Bu, en cömert aşk tarzı; ama bir uyarı: Verenin emeği çoğu zaman görünmez kalır. Bakım ve özen de bir emektir ve görülmeyi hak eder.", "16"),
    },
}

ICERIK["birbirinizi-fiyatlamak"] = {
    "kanca": "İkiniz de aynı şeyleri mi değerli buluyorsunuz? Ayrı ayrı çözün, sonra karşılaştırın.",
    "sorular": [
        ("Bir akşam: ", ["Evde baş başa", "Arkadaşlarla dışarıda"]),
        ("Beklenmedik bir para geldi:", ["Tatile", "Birikime"]),
        ("Tartışınca:", ["Hemen konuşalım", "Soğuyunca konuşalım"]),
        ("Sevgi en çok böyle gösterilir:", ["Sözle", "Davranışla"]),
        ("Yaşanacak yer:", ["Büyükşehir", "Sakin bir kasaba"]),
        ("Hediye:", ["Sürpriz olsun", "İstediğim şey olsun"]),
        ("Telefonlar:", ["Şifreler paylaşılır", "Herkesin kendi alanı"]),
        ("Bayram ve tatiller:", ["Ailelerle", "İkimiz"]),
        ("Gelecek:", ["Planlı", "Akışına"]),
        ("Ev işleri:", ["Görev listesiyle", "Kim müsaitse"]),
    ],
    "seviyeler": [
        (0, "Takas ekonomisi", "Neredeyse her konuda farklı şeylere değer veriyorsunuz. Bu bir felaket değil, bir pazarlık davetidir: Farklı tercihleri olan iki taraf, doğru takasla ikisini de kazançlı çıkarabilir. Ama bunun için konuşmanız gerekecek, hem de çok."),
        (3, "Farklı para birimleri", "Aynı dili konuşuyor ama farklı para birimleri kullanıyorsunuz. Bazı konularda kur farkı var. Uyumsuz sandığınız şeyler çoğu zaman tercihlerin değil, beklentilerin farklı olmasından kaynaklanır."),
        (6, "Yakın kur", "Çoğu konuda aynı şeylere değer veriyorsunuz; ayrıldığınız birkaç nokta ise ilişkinin baharatı. Farklı olduğunuz maddelere bakın: Kavgaların çoğu buradan çıkıyor olabilir."),
        (9, "Aynı fiyat listesi", "Neredeyse her şeyi aynı fiyattan değerlendiriyorsunuz. İktisatçıların denk eşleşme dediği şey bu. Tek uyarı: Bu kadar benzer iki kişi, birbirine yeni şeyler katmayı unutabilir."),
    ],
    "bolum": "09",
}


def tum_testler():
    t = takvim()
    out = []
    for no, slug, ad, tur, bolum in LISTE:
        sezon = (no - 1) // 10 + 1
        d = {"no": no, "slug": slug, "ad": ad, "tur": tur, "bolum": bolum, "sezon": sezon,
             "acilis": t[no].isoformat()}
        if slug in ICERIK:
            d.update(ICERIK[slug])
        out.append(d)
    return out
