# -*- coding: utf-8 -*-
# Aşkonomi test serisi — Sezon 4 "Dijital Çağ" (test 31–39) içerikleri.
# Kaynak: kitap metni v45, bölüm 06, 15, 29–34. Sayfa dayanakları: /home/claude/askonomi_in/rapor_s4.md

ICERIK = {}

# 31 — nesil — Bölüm 30
ICERIK["tinder-oncesi-sonrasi"] = {
    "kanca": "Aşkı mahalle mi tanıştırırdı, arkadaş mı, ekran mı? Senin refleksin hangi çağdan?",
    "sorular": [
        ("Hayatının aşkıyla nasıl tanışmak isterdin?", [
            ("M", "Aynı sokakta, aynı okulda ya da bir düğünde"),
            ("A", "Bir arkadaşın “Sizi tanıştırmalıyım” demesiyle"),
            ("I", "Uzun yazışmalarla başlayan bir tanışıklıkla"),
            ("K", "Birkaç kilometre ötede, ekranda karşıma çıkarak"),
            ("Y", "Beni iyi tanıyan bir uygulamanın önerisiyle")]),
        ("Yeni biriyle tanıştın. Güvenmeden önce neye bakarsın?", [
            ("M", "Ailesini ve çevresini kimlerin tanıdığına"),
            ("A", "Ortak arkadaşımızın onun hakkında ne dediğine"),
            ("I", "Yazdıklarının zamanla birbirini tutup tutmadığına"),
            ("K", "Profilinin doğrulanmış olup olmadığına"),
            ("Y", "Uygulamanın uyum yorumuna ve önerisine")]),
        ("Aday havuzun ne kadar geniş olmalı?", [
            ("M", "Tanıdığım çevre yeter, uzağı bilmem"),
            ("A", "Arkadaşlarımın arkadaşları kadar"),
            ("I", "Şehrimin, hatta ülkemin sınırını aşabilmeli"),
            ("K", "Ne kadar çok profil, o kadar iyi"),
            ("Y", "Geniş olsun ama birkaç iyi adaya indirilsin")]),
        ("Seni en çok ne yorar?", [
            ("M", "Herkesin her şeyi bilmesi"),
            ("A", "Ayrılınca arkadaşların arada kalması"),
            ("I", "Yüz yüze görüşmenin hep ertelenmesi"),
            ("K", "Sonu gelmeyen profil kaydırmak"),
            ("Y", "Mesajın ne kadarının bana ait olduğunu düşünmek")]),
        ("İlk adım nasıl atılır?", [
            ("M", "Mesaja gerek yok, yüz yüze selam verilir"),
            ("A", "Arkadaşım aracılığıyla haber gönderirim"),
            ("I", "Uzun, özenli, birkaç paragraflık bir mesajla"),
            ("K", "Kısa bir espri yazar, hemen gönderirim"),
            ("Y", "Taslağı önce bir yapay zekâya düzelttiririm")]),
        ("Hangi cümle sana yakın?", [
            ("M", "Kısmet, yakınında olandır."),
            ("A", "Güvendiğin birinin önerisi altın değerindedir."),
            ("I", "Mesafe, iyi bir yazışmayla kısalır."),
            ("K", "Seçenek çoksa doğruyu bulma şansı da çoktur."),
            ("Y", "Doğru veri, doğru kişiyi getirir.")]),
    ],
    "sonuclar": {
        "M": ("Mahalle çağı", "Senin aşk haritan yakın çevreyle çizili: Aynı sokak, aynı okul, bir düğün masası. Kitaba göre tarih boyunca bir insanın karşılaşabileceği partner sayısını büyük ölçüde coğrafya belirledi. Bu dünyada aile ve mahalle hem karşılaşma alanı hem dolaylı bir güven kontrolüydü. Bedeli şu: Varlığından haberdar olmadığın biriyle ne kadar uyumlu olabileceğinin pratikte hiçbir önemi yoktu. Havuz dar, güven sağlam.", "30"),
        "A": ("Arkadaş köprüsü çağı", "Sen tanışmanın en güvenilir yolunu bir arkadaşın kefaletinde görüyorsun. Kitap bunu şöyle anlatır: “Onu yıllardır tanıyorum” cümlesi kusursuz garanti değildi, ama iki yabancı arasındaki bilgi problemini azaltabilirdi. İktisatta bu bir aracılık hizmetidir. ABD verilerine göre çevrim içi tanışma yaklaşık 2013 civarında bu yolu geride bıraktı. Senin bedelin, havuzun arkadaş çevren kadar kalması.", "30"),
        "I": ("İnternet çağı", "Sen coğrafyayı aşmaya hazırsın ama aceleci değilsin. Kitaba göre tren, otomobil, üniversite ve büyük şehirler partner havuzunu genişletti. Ama aşk piyasasının sınırları uzun süre büyük ölçüde fiziksel dünyanın sınırlarıydı. Senin çağında yabancılar birbirine bağlanıyor ama henüz telefonda sıraya dizilmiyordu. Güçlü yanın, yazışmaların zamanla biriktirdiği bilgi. Bedeli: Profil ne kadar ayrıntılı olursa olsun ses tonunu, hareketleri ve iki insan arasındaki kimyayı taşıyamaz.", "30"),
        "K": ("Kaydırma çağı", "Sen Tinder sonrasının insanısın: Geniş havuz, hızlı karar, sağa ya da sola. Kitaba göre değişen yalnız parmak hareketi değil. Eskiden aile, arkadaş ve mahallenin yaptığı eşleştirmenin bir bölümünü artık platformlar yapıyor. Avantajın, başka türlü hiç karşılaşmayacağın insanlara ulaşmak. Bedeli: Milyonlarca profil milyonlarca gerçek seçenek demek değil, çünkü karşı tarafın da seni seçmesi gerekir. Kıt olan artık dikkat.", "30"),
        "Y": ("Yapay zekâ çağı", "Sen bir adım öndesin: Partner aramanın emeğini yazılıma devretmeye hazırsın. Kitap bunun çoktan başladığını yazar: Tinder Mart 2026’da “Chemistry” adlı yapay zekâ destekli kişiselleştirme katmanını duyurdu. Kazanç açık, arama maliyeti düşer. Bedeli daha sinsi: Geçmiş tercihlerinden öğrenen bir sistem sana hep benzerini getirebilir ve tesadüfen iyi biriyle karşılaşma ihtimalini azaltabilir.", "34"),
    },
}

# 32 — nesil — Bölüm 29/30
ICERIK["hangi-on-yil"] = {
    "kanca": "Bazı insanlar takvimle değil, aşk anlayışıyla yaşar. Seninki hangi yılda kaldı?",
    "sorular": [
        ("Evlilik teklifi denince aklına ne gelir?", [
            ("P", "Ömür boyu sürecek bir taş, bir yüzük"),
            ("U", "İki hayatın birlikte bir düzen kurması"),
            ("D", "Genç yaşta, heyecanla verilen bir söz"),
            ("O", "Önce mesaj, sonra buluşma, sonra karar"),
            ("Z", "Her şey oturduktan sonra konan son taş")]),
        ("Evlenmek için doğru zaman ne zaman?", [
            ("P", "Sonsuza kadar süreceğine emin olunca"),
            ("U", "Kimin neyi üstleneceği belli olunca"),
            ("D", "Yirmili yaşlarda, hayatı birlikte kurmak için"),
            ("O", "Birbirimizi yeterince tanıyınca, yaş fark etmez"),
            ("Z", "İş, ev ve birikim tamamlanınca")]),
        ("İlişkide en çok neyi değerli bulursun?", [
            ("P", "Kalıcılığı, sonsuza kadar sürmesini"),
            ("U", "İş bölümünü, herkesin işini bilmesini"),
            ("D", "Birlikte sıfırdan başlamayı"),
            ("O", "Geniş bir havuzdan seçmiş olmayı"),
            ("Z", "Birlikte kendimizi geliştirmeyi")]),
        ("Partnerinle nasıl tanışmış olmayı isterdin?", [
            ("P", "Benden çok farklı bir çevreden gelen biriyle"),
            ("U", "Hayat düzenime uyacak biriyle, tanıdık aracılığıyla"),
            ("D", "Ortak bir arkadaşın tanıştırmasıyla"),
            ("O", "Bir uygulamada, hiç ortak tanıdık olmadan"),
            ("Z", "Yapay zekânın önerdiği birkaç aday arasından")]),
        ("Para konusunda ilişkide…", [
            ("P", "Büyük jest, büyük bağlılık demektir"),
            ("U", "Biri kazanır, biri evi çevirir, ikisi de emektir"),
            ("D", "Az parayla başlanır, birlikte büyütülür"),
            ("O", "Herkes kendi hesabını bilir, ortak gider konuşulur"),
            ("Z", "Önce ekonomik eşik aşılır, sonra nikâh kıyılır")]),
        ("Hangi cümle sana yakın?", [
            ("P", "Bazı şeyler sonsuza kadardır."),
            ("U", "İyi evlilik, iyi bir iş bölümüdür."),
            ("D", "Önce evlenilir, sonra kurulur."),
            ("O", "Aşkı artık arkadaş değil, ekran tanıştırıyor."),
            ("Z", "Önce kurulur, sonra evlenilir.")]),
    ],
    "sonuclar": {
        "P": ("1940’ların aşkı: Sonsuza kadar", "Sen aşkı kalıcılıkla ölçüyorsun. Kitaba göre 1939’dan itibaren pırlanta romantik bağlılıkla sistematik biçimde ilişkilendirildi. Frances Gerety’nin 1947’de yazdığı “A Diamond Is Forever” sloganı ertesi yıldan itibaren kampanyanın merkezine yerleşti. Aynı yıllarda ABD’de benzer eğitimlilerin evlenme eğilimi düşüyordu. Bedeli şu: Yakın tarihte üretilmiş bir norm, birkaç kuşak sonra “eskiden beri böyle” gibi görünebilir.", "31"),
        "U": ("1950’lerin aşkı: İş bölümü", "Sen ilişkiyi iyi işleyen bir ortaklık gibi görüyorsun: Herkes bir alanda uzmanlaşır, birlikte daha çok üretilir. Gary Becker’ın 1973’te yayımladığı evlilik modeli tam bunu anlatır. Kitaba göre bu model yirminci yüzyılın ortasındaki birçok hanenin gerçek yapısını iyi betimleyen unsurlar taşıyordu. Bedeli: Betimlenen yapı değişmez bir yasa değildir. Eğitim, istihdam ve ev teknolojileri değiştikçe uzmanlaşmanın getirisi de değişti.", "15"),
        "D": ("1990’ların aşkı: Önce evlen, sonra kur", "Sen hayatı birlikte sıfırdan kurmaya inanıyorsun. Kitapta aktarılan OECD karşılaştırmasına göre 1990’ların başında OECD ülkelerinde ilk evlilik yaşı kadınlarda 22–27, erkeklerde 24–30 arasındaydı. Senin modelin kitabın “temel taşı” dediği eski evlilik modeline yakın: Önce evlenilir, ev ve birikim sonra birlikte kurulur. Riskin, ekonomik olarak kırılgan bir başlangıç. Kazancın, birlikte kurulan şeyin ortak hikâyesi.", "29"),
        "O": ("2010’ların aşkı: Aracısız tanışma", "Sen tanışmak için aracıya ihtiyaç duymuyorsun. Rosenfeld ve arkadaşlarının ABD verilerine göre heteroseksüel çiftler arasında çevrim içi tanışma, yaklaşık 2013 civarında arkadaşlar aracılığıyla tanışmayı geride bıraktı. Araştırmacılar buna aracıların devreden çıkması dedi. Kazancın geniş havuz. Bedeli: Arkadaşın sağladığı küçük güven bilgisi de devreden çıkar. Bu bulgu ABD’ye ait, her ülke aynı hızda değişmiyor.", "30"),
        "Z": ("2020’lerin aşkı: Kapak taşı", "Sen önce hayatını kurup sonra evlenmekten yanasın. Kitaptaki OECD verisine göre 2021’de ilk evlilik yaşı ortalaması kadınlarda yaklaşık 31, erkeklerde yaklaşık 33,4’e yükseldi. Sosyologlar buna kapak taşı evlilik der: Nikâh, zaten kurulmuş hayatın üzerine konur. Bedeli: Eşik yükseldikçe ekonomik olarak kırılgan olanlar nikâha daha geç ulaşabilir ya da hiç ulaşamayabilir. Evlilik değersizleşmedi, ön koşulları ağırlaştı.", "29"),
    },
}

# 33 — mit — Bölüm 30
ICERIK["kaydirma-ekonomisi"] = {
    "kanca": "Herkesin flört uygulamaları hakkında bir teorisi var. Hangileri veriyle uyuşuyor?",
    "sorular": [
        ("ABD’de çevrim içi tanışma, arkadaşlar aracılığıyla tanışmayı geride bıraktı.", True,
         "Doğru. Rosenfeld ve arkadaşlarının (2019) ulusal temsilî 2017 verilerine göre ABD’de heteroseksüel çiftler arasında çevrim içi tanışma, yaklaşık 2013 civarında arkadaş aracılığını geride bıraktı. Kitap uyarıyor: Bu bulgu ABD’ye ait, bütün dünyada tanışma biçimlerinin aynı hızda değiştiği anlamına gelmez."),
        ("Uygulamada başlayan ilişkiler, çevrim dışı başlayanlardan daha mutsuz ve daha geçicidir.", False,
         "Yanlış. Potarca’nın (2020) İsviçre’de 3.245 kişiyle yaptığı çalışmada, mobil uygulamada tanışan çiftlerde ilişki ve yaşam doyumu bakımından belirgin bir dezavantaj bulunmadı. Birlikte yaşama niyeti de daha güçlüydü. Bu, uygulama ilişkilerinin daha iyi olduğunu da kanıtlamaz. Daha güvenli sonuç, tanışma aracının tek başına ilişkinin kalitesini belirlemediği."),
        ("Ekranda milyonlarca profil varsa, elinde milyonlarca seçenek var demektir.", False,
         "Yanlış. Flört uygulaması süpermarket değildir. Süpermarkette ürünün sizi seçmesi gerekmez, flörtte ise karşı tarafın da sizi kabul etmesi gerekir. Kitabın ifadesiyle her kullanıcı aynı anda seçen ve seçilendir."),
        ("Uygulamalarda insanlar ortalamada kendilerinden daha “arzu edilir” sıradaki kullanıcılara yazma eğilimindedir.", True,
         "Doğru. Bruch ve Newman’ın (2018) dört büyük ABD kentindeki çalışmasında kadınlar da erkekler de ortalamada kendilerinden yaklaşık yüzde 25 daha yüksek sıradaki kullanıcılara mesaj gönderdi. Aradaki mesafe büyüdükçe yanıt alma olasılığı azaldı. Bu sıralama insanın değerini değil, yalnız platformdaki konumunu gösterir."),
        ("Boost gibi ücretli özelliklerle aşkın kendisi satın alınabilir.", False,
         "Yanlış. Para, profilin daha çok kişiye gösterilmesini etkileyebilir. Ama karşı tarafın ilgilenmesini, eşleşmeyi, konuşmayı ve ilişkiyi garanti etmez. Kitaba göre ücretli görünürlük sevgiyi değil, seçilme fırsatına erişimi etkileyebilir."),
        ("Bir saha deneyinde, iki tarafın ilgisini birlikte hesaba katan algoritma, yalnız tıklanmayı artırmaya çalışan sistemden daha çok karşılıklı eşleşme üretti.", True,
         "Doğru. Chen ve arkadaşlarının (2023) Tayvan’da 690.857 hesapla yaptığı deneyde iki taraflı mantığı kullanan algoritma görünürlüğü daha geniş dağıttı ve daha fazla karşılıklı eşleşme üretti. Sınır da açık: Ölçülen şey karşılıklı beğeniydi, mutlu ilişki değil."),
    ],
    "seviyeler": [
        (0, "Ekran yanılgısı", "Uygulamalar hakkındaki sezgilerinin çoğu verilerle uyuşmadı. Şaşırtıcı değil: Kaydırma arayüzü romantik seçimi alışverişe benzetmeye çok elverişli. Ama kitabın vurguladığı gibi, Tinder’dan sonra aşk piyasasında kıtlık ortadan kalkmadı, yalnız kıt olan şeylerin bir bölümü değişti. Artık kıt olan profil değil, dikkat ve karşılıklılık. Bir dahaki kaydırmada şunu hatırla: Ekrandaki herkes aynı anda seçen ve seçilendir."),
        (3, "Bilinçli kaydırıcı", "Bazı mekanizmaları doğru okudun, bazılarında sezgi seni yanılttı. Dijital flörtün büyük paradoksu tam burada: Bolluk ile kıtlık aynı anda büyüyor. Tarihte hiç olmadığı kadar çok potansiyel partner görebiliyoruz, ama kitabın hatırlattığı gibi günümüz hâlâ yirmi dört saat. Arama ucuzladı, ama değerlendirme ve duygusal emek ortadan kalkmadı. Alternatif sayısı büyüdü, karşılıklılık şartı ise hâlâ yerinde."),
        (5, "Platform ekonomisti", "Platformların nasıl çalıştığını iyi okuyorsun: Karşılıklılık şartı, dikkatin eşitsiz dağılımı, görünürlüğün fiyatı. Şimdi kitabın sorduğu zor soru geliyor. “En çok eşleşme”, “en uzun kullanım” ve “en iyi uzun dönemli ilişki” aynı hedef değil. Bir algoritma bunlardan hangisini başarı saymalı? Kitabın önerisi, “Ne kadar doğru tahmin ediyor?” sorusundan önce “Neyi doğru tahmin etmeye çalışıyor?” diye sormak."),
    ],
    "bolum": "30",
}

# 34 — hesap — Bölüm 31
ICERIK["ask-endustrisi"] = {
    "kanca": "Çiçek, yüzük, düğün, paylaşım. Sevgini kendi cümlelerinle mi kuruyorsun, hazır bir senaryoyla mı?",
    "sorular": [
        ("14 Şubat’ta partnerin hiçbir şey yapmadı. Ne düşünürsün?", [
            (0, "Sıradan bir gün, bir şey düşünmem"),
            (1, "Biraz garip ama önemli değil"),
            (2, "Kırılırım, o gün bir şey bekliyordum"),
            (3, "İlişkide bir sorun var demektir")]),
        ("Bir hediyenin değerini en çok ne belirler?", [
            (0, "Beni ne kadar tanıdığını göstermesi"),
            (1, "Düşünülmüş olması, fiyatı ikinci planda"),
            (2, "Özenli ve iyi bir markadan olması"),
            (3, "Onun için ne kadar harcandığı")]),
        ("Evlilik teklifi ve yüzük?", [
            (0, "Yüzük şart değil, söz yeter"),
            (1, "Aileden kalma ya da sade bir yüzük"),
            (2, "Pırlanta olmalı ama makul fiyatta"),
            (3, "Pırlanta, gelirin hakkını veren bir fiyatta")]),
        ("Düğün bütçesi konuşulurken hangi cümle sana yakın?", [
            (0, "Küçük bir nikâh, gerisi bizim hayatımız"),
            (1, "Sevdiklerimiz gelsin, gösteriş olmasın"),
            (2, "Bir kere evleniyoruz, biraz fazlası olabilir"),
            (3, "Çevremizdeki düğünlerden geri kalamayız")]),
        ("Yıldönümünüzü sosyal medyada paylaşmadınız.", [
            (0, "Zaten paylaşmayız"),
            (1, "Paylaşmak hoş ama gerekmez"),
            (2, "Paylaşmayınca bir şey eksik kalır"),
            (3, "Paylaşmazsak çevremiz ne düşünür diye düşünürüm")]),
        ("Bir arkadaşının nişan yüzüğünü gördün.", [
            (0, "Mutlu olsunlar, kıyaslamam"),
            (1, "Güzelmiş derim, geçerim"),
            (2, "Beklentimi biraz yukarı çeker"),
            (3, "Partnerimin bana alacağıyla karşılaştırırım")]),
    ],
    "seviyeler": [
        (0, "Kendi sözlüğü", "Sevgini büyük ölçüde kendi cümlelerinle kuruyorsun. Kitaba göre bu, piyasadan kaçtığın anlamına gelmek zorunda değil, çünkü piyasanın karşıtı parasızlık değildir. Riskin şu: “Ben sevgiyi parayla ölçmem” derken partnerinin önem verdiği ritüelleri küçümseyebilirsin. Asıl mesele para değil, karşındakinin anlam dünyasına dikkat etmek. Bu endeks kesin bir ölçüm değil, kendine soru sormak için bir düşünme aracıdır."),
        (25, "Seçici tüketici", "Piyasanın sunduğu sembolleri kullanıyorsun ama hepsini değil. Aynı kırmızı gül biri için klişe, başka biri için ilk buluşmanın hatırası olabilir. Kitabın vurgusu bu: Standart ürün, standart duygu üretmek zorunda değildir. Sorman gereken, kullandığın sembollerden hangi beklentinin gerçekten sana ait olduğu. Bu endeks bir teşhis değil, kendi tercihlerine bakmak için bir düşünme aracıdır."),
        (50, "Ritüel müşterisi", "Aşkı görünür kılmak senin için önemli: Doğru gün, doğru jest, doğru hediye. Ritüeller ilişkiye gerçekten anlam katabilir. Ama kitap ortak ritüel ile zorunlu performansı ayırır. “Bunu yapmazsak çevremiz ilişkimizi başarısız sanacak” düşüncesi devreye girdiğinde aynı jest sosyal değerlendirme baskısına dönüşebilir. Piyasa ritüelin araçlarını sunar, ritüelin kime ait olduğunu çiftin verdiği anlam belirler. Bu endeks bir düşünme aracıdır, hüküm değildir."),
        (75, "Senaryoya abone", "Sevginin nasıl görünmesi gerektiğine dair hazır senaryo sende güçlü çalışıyor. Yalnız değilsin: ABD’de 2026 Sevgililer Günü için planlanan harcama 29,1 milyar dolar olarak tahmin edildi. Ama kitabın uyarısı net: Fiyatı duygunun kusursuz termometresi sanmak bir hatadır. Kitabın sorusu: Harcamayı kendi tercihinle mi yapıyorsun, yoksa toplumsal bir tabanı yakalamaya mı çalışıyorsun? Bu bir düşünme aracıdır."),
    ],
    "bolum": "31",
    "birim": "Aşk Endüstrisi Endeksi",
}

# 35 — mit — Bölüm 33
ICERIK["yalnizligin-fiyati"] = {
    "kanca": "Tek başına yaşamak, yalnız olmak, yalnız hissetmek. Bunlar aynı şey mi?",
    "sorular": [
        ("Türkiye’de tek kişilik hanelerin payı son on yılda belirgin biçimde arttı.", True,
         "Doğru. TÜİK verilerine göre tek kişilik hanelerin toplam haneler içindeki payı 2014’te yüzde 13,9 iken 2025’te yüzde 20,5’e yükseldi. Yani bugün yaklaşık her beş haneden biri tek kişilik."),
        ("Bu rakam, Türkiye’de yaklaşık her beş kişiden birinin yalnız olduğunu gösterir.", False,
         "Yanlış. TÜİK burada yalnızlık ölçmüyor, aynı hanede kaç kişinin yaşadığını ölçüyor. Tek başına yaşamak bir hane düzenidir. Yalnızlık ise sahip olunan ilişkilerle arzulanan ilişkiler arasındaki farktan doğan öznel bir deneyimdir. Kalabalık bir evde yalnız olunabilir, tek başına yaşayıp güçlü bağlara sahip olunabilir."),
        ("Yalnızlık esas olarak yaşlılığın sorunudur.", False,
         "Yanlış. WHO’nun 2025 değerlendirmesine göre genç gruplarda yaklaşık her beş kişiden biri yalnızlık yaşıyor. OECD de 2018–2022 döneminde sosyal bağlantı göstergelerindeki en belirgin kötüleşmelerin bazılarını 16–24 yaş grubunda buldu."),
        ("Dünya Sağlık Örgütü’ne göre dünyada yaklaşık her altı kişiden biri yalnızlık yaşıyor.", True,
         "Doğru. WHO’nun 2025’te yayımladığı küresel değerlendirme bu tahmini veriyor ve oranın gençler arasında daha yüksek olabildiğini belirtiyor."),
        ("Bir yapay zekâ arkadaşıyla konuşmak, hemen ardından yalnızlık hissini azaltabiliyor.", True,
         "Doğru, ama dikkatli okunmalı. De Freitas ve arkadaşlarının (2026) araştırmasında kullanımın hemen ardından yalnızlık hissinde azalma görüldü. En önemli mekanizmalardan biri kendini dinlenmiş ve duyulmuş hissetmekti. Bu sonuç yapay zekânın arkadaşın yerini aldığını göstermez ve uzun dönemli etkiyi ölçmez."),
        ("Telefonla geçirilen sürenin insanları yalnızlaştırdığı kesin olarak kanıtlandı.", False,
         "Yanlış. OECD’nin 2025 değerlendirmesine göre çevrim içi etkileşim ile yalnızlık arasındaki birçok ilişki korelasyon. Yalnız insanların platformları farklı kullanması da bu ilişkiyi açıklayabilir. Önemli olan sürenin kendisinden çok nasıl geçtiği: Uzaktaki annenle görüntülü konuşmak ile başkalarının hayatını sessizce kaydırmak aynı davranış değil."),
    ],
    "seviyeler": [
        (0, "Kalabalık yanılgısı", "Yalnızlık hakkındaki sezgilerinin çoğu verilerle uyuşmadı. En yaygın hata, üç farklı şeyi tek kelimeyle anlatmak: Sosyal izolasyon, yalnızlık ve tek başına yaşamak. Kitabın deyişiyle hane istatistiği kapının içinde kaç kişi bulunduğunu söyler. Kapı çalındığında dışarıda kimin bulunduğunu söylemez. Yalnızlığı anlamak için kaç kişiyle yaşadığına değil, hayatında kimlerin gerçekten bulunduğuna bakmak gerekir."),
        (3, "Dikkatli gözlemci", "Bazı ayrımları doğru yaptın, bazılarında kolay bir hikâyeye kapıldın. Yalnızlık hakkında en çekici açıklamalar genellikle en temiz olanlardır, “telefon bizi yalnızlaştırdı” gibi. Kitap daha zor bir soru soruyor: “Hangi dijital kullanım, hangi insan için, hangi ilişki biçiminin yerine veya yanına geliyor?” Cevap kişiden kişiye değişir ve verilerin söylediği de tam olarak bu."),
        (5, "Yalnızlık ekonomisti", "Yalnızlığın ekonomisini iyi okuyorsun: Hane düzeni ile duygu arasındaki farkı, gençlerdeki tabloyu, verinin sınırlarını. Kitabın vardığı yer şu: Kıt olan insan sayısı değil. Kıt olan zaman, dikkat, karşılıklılık, güven, erişilebilir sosyal alan ve tekrar eden karşılaşma. Kitabın deyişiyle bağlantı bolluğu, ilişki bolluğu değildir. İletişimin fiyatı sıfıra yaklaşabilir, dikkatin kıtlığı ise devam eder."),
    ],
    "bolum": "33",
}

# 36 — profil — Bölüm 33
ICERIK["yalniz-misin"] = {
    "kanca": "Tek başına olmak bir eksiklik mi, bir tercih mi, yoksa bir takvim sorunu mu?",
    "sorular": [
        ("Cuma akşamı hiçbir planın yok. İlk düşüncen?", [
            ("B", "Harika, ev benim, akşam benim"),
            ("Z", "Mahalledeki kafeye inerim, tanıdık biri çıkar"),
            ("F", "Keşke arkadaşlarla bir kez denk gelebilsek"),
            ("P", "En yakınımı ararım, başka kimseye gerek yok"),
            ("D", "Telefonu açar, kimin ne yaptığına bakarım")]),
        ("Araban yolda kaldı. Kimi ararsın?", [
            ("B", "Çekiciyi ararım, işi kendim çözerim"),
            ("Z", "Yakındaki tanıdıklardan birini, mutlaka biri çıkar"),
            ("F", "Aradığım herkes o saatte işte olur, yine de denerim"),
            ("P", "Partnerimi ya da tek en yakınımı"),
            ("D", "Bir gruba “Yakında olan var mı?” diye yazarım")]),
        ("Sosyal hayatını en çok ne daraltıyor?", [
            ("B", "Hiçbir şey, istediğim kadar sosyalim"),
            ("Z", "Bakkalın, sabah selamlarının azalması"),
            ("F", "Çalışma saatlerimin kimseyle uyuşmaması"),
            ("P", "Her şeyi tek bir kişiyle paylaşıyor olmam"),
            ("D", "Çok mesajlaşıp az buluşmamız")]),
        ("Hangisi seni daha iyi anlatır?", [
            ("B", "Kendi başıma olmayı seçiyorum ve keyif alıyorum"),
            ("Z", "Simitçiden komşuya herkesle iki çift lafım var"),
            ("F", "İnsanları seviyorum ama takvimim izin vermiyor"),
            ("P", "Bir kişim var, o bana yeter"),
            ("D", "Yüzlerce kişiye bir tıkla ulaşabilirim")]),
        ("Bir arkadaşın doğum günü…", [
            ("B", "Az ama önemli insanlar için hatırlarım"),
            ("Z", "Herkese kısa bir tebrik, keyifli bir alışkanlık"),
            ("F", "Hatırlarım ama aramaya fırsat bulamam"),
            ("P", "Benim için tek önemli doğum günü belli"),
            ("D", "Bildirim gelirse yazarım")]),
        ("Hangi cümle sana yakın?", [
            ("B", "Sessizlik benim lüksüm."),
            ("Z", "Küçük selamlar büyük farklar yaratır."),
            ("F", "Dostluk da zaman ister."),
            ("P", "Ruh eşini bulunca başka kimseye gerek kalmaz."),
            ("D", "Herkes bir mesaj uzaklıkta.")]),
    ],
    "sonuclar": {
        "B": ("Seçilmiş sessizlik", "Sen tek başınalığı bir eksiklik olarak değil, bilinçli bir tercih olarak yaşıyorsun. Kitap bunu açıkça kabul eder: Kişisel alan, özerklik, sessizlik ve zaman üzerinde tam kontrol birçok insan için son derece değerli kazançlardır. Tek kişilik hane bazen bilinçli biçimde satın alınmış bir özgürlüktür. Bedeli ekonomik: Kira, faturalar ve evin bütün işleri paylaşılmaz. İktisatçılar buna ölçek ekonomisinin kaybı der.", "33"),
        "Z": ("Zayıf bağların ustası", "Sen sosyal hayatını yalnız birkaç yakın ilişkiyle değil, gündelik küçük temaslarla da kuruyorsun: Simitçi, komşu, spor salonundaki tanıdık. Sandstrom ve Dunn’ın (2014) araştırmasında insanlar alışılmıştan daha fazla tanıdıkla etkileşim kurdukları günlerde daha yüksek mutluluk ve aidiyet bildirdi. Bedeli şu: Bu ağ bedava göründüğü için kolayca kaybolur. Kapanan bir bakkal, her gün yaşanan yirmi saniyelik bir selamı da götürebilir.", "33"),
        "F": ("Zaman fakiri", "Sen insanları istemediğin için değil, ortak boş zaman bulamadığın için uzak kalıyorsun. Kitap bunu açıkça söyler: Bazen insan ilişkilerinin en büyük engeli konuşma becerisi değil, koordinasyon maliyetidir. Vardiyalar, uzun yollar ve bakım yükü sosyal hayatı yasaklamadan daraltır. Arkadaşlığın da bakım maliyeti var: Sosyal sermaye kendi kendine faiz üreten bir mevduat değildir. Riskin, bağların sessizce aşınması.", "33"),
        "P": ("Tek hisseli portföy", "Senin sosyal dünyan büyük ölçüde tek bir insanda toplanıyor. Bu bağ çok değerli olabilir. Ama kitap finans diliyle uyarır: Arkadaşlar, kardeşler ve komşular ortadan kalktığında bütün sosyal risk tek kişide yoğunlaşır, bu da son derece konsantre bir portföydür. Bir kişiden sevgili, sırdaş, ortak ve bütün çevre olmasını beklemek ilişkiye olağanüstü yük bindirir. Aşk yalnızlığın değerli bir koruyucusu olabilir ama evrensel sigortası değildir.", "33"),
        "D": ("Bağlantı zengini", "Sen yüzlerce kişiye birkaç saniyede ulaşabiliyorsun. Kitabın çağımız için kurduğu paradoks seni anlatıyor: İletişimin işlem maliyeti düştü ama anlamlı ilişkinin kıtlığı ortadan kalkmadı. Telefon tek başına suçlu değil. Görüntülü konuşmak ile başkalarının hayatını sessizce kaydırmak aynı davranış değil. Riskin, ulaşılabilir kişi sayısını güvenceyle karıştırmak. Kitabın deyişiyle dijital görünürlük ile sosyal güvence aynı para birimi değildir.", "33"),
    },
}

# 37 — senaryo — Bölüm 32
ICERIK["ask-icin-ulke"] = {
    "kanca": "Aşk sınır tanımaz, derler. Pasaport, dil ve uçak bileti başka şeyler söyler.",
    "sorular": [
        ("Sevgilin başka bir ülkede iş teklifi aldı. İlk tepkin?", [
            ("G", "Bavulumu hazırlarım, gerisi çözülür"),
            ("P", "Giderim, ama kariyer kaybımı birlikte nasıl telafi edeceğimizi konuşuruz"),
            ("K", "Burada kurulu bir hayatım var, o hayat kalmalı"),
            ("U", "Gitsin, bir süre uzaktan idare ederiz"),
            ("M", "İkimiz için de yeni olan üçüncü bir ülke ararız")]),
        ("Taşındın ve yerel dili bilmiyorsun. Ne yaparsın?", [
            ("G", "Hemen kursa yazılır, sokağın dilini öğrenirim"),
            ("P", "Ben onun dilini öğrenirim, o da benimkini"),
            ("K", "Böyle bir duruma düşmemek için taşınmazdım"),
            ("U", "Uzun kalmayacağım, idare ederim"),
            ("M", "Evde ikimizin de anadili olmayan ortak bir dil konuşuruz")]),
        ("Bayram da var, Noel de. Bu yıl nerede?", [
            ("G", "Partnerimin ailesinde, yeni gelenekler öğrenirim"),
            ("P", "Bir yıl onlarda, bir yıl bizde"),
            ("K", "Bizde, bayramı ailemsiz düşünemem"),
            ("U", "Herkes kendi ailesinde, sonra buluşuruz"),
            ("M", "İkisinden de bir parça alıp kendi geleneğimizi kurarız")]),
        ("Bir tartışmada partnerin “Bizim kültürde böyle yapılır” dedi.", [
            ("G", "Onun kültürüne uyum sağlamaya çalışırım"),
            ("P", "Bir konuda onun, bir konuda benim dediğim olsun"),
            ("K", "Benim kültürümde başka türlü yapıldığını söylerim"),
            ("U", "Uzaktayken pek sorun olmuyor, görüşünce konuşuruz"),
            ("M", "“Bizim evde nasıl olacak?” diye sorarım")]),
        ("Çocuğunuz olursa evde hangi dil konuşulur?", [
            ("G", "Yaşadığımız ülkenin dili"),
            ("P", "Herkes kendi anadilini konuşsun"),
            ("K", "Benim dilim, kökünü bilsin"),
            ("U", "Önce aynı ülkede yaşamayı çözmeliyiz"),
            ("M", "Üç dil birden, biri de bizim ortak dilimiz")]),
        ("Aşk için taşınmanın en büyük bedeli sence ne?", [
            ("G", "Yok, aşk her bedele değer"),
            ("P", "Faturanın tek kişinin kariyerine yazılması"),
            ("K", "Ailemden ve dostlarımdan kopmak"),
            ("U", "Uçak biletleri, izin günleri ve saat farkı"),
            ("M", "İki tarafın da alışkanlıklarından vazgeçmesi")]),
    ],
    "sonuclar": {
        "G": ("Göçebe kalp", "Sen aşk için sınırı geçmeye hazırsın. Cesur, ama kitabın hatırlattığı bir bilanço var: Dil, diploma, mesleki lisans ve profesyonel çevre ülke değiştirince aynı değeri korumayabilir. Başlangıçta ekonomik olarak eşit iki kişi birkaç yıl içinde belirgin gelir farkına sahip olabilir. Taşınma ortak karar olduğu halde maliyet yalnız bir kişinin kariyerine yazılırsa romantik fedakârlık zamanla ekonomik bağımlılığa dönüşebilir.", "32"),
        "P": ("Adil pazarlıkçı", "Sen fedakârlığı hesapsız bir jest değil, ortak bir bütçe kalemi olarak görüyorsun. Kitabın ölçüsü de bu: Uzun ilişkinin adaleti her gün eşit fedakârlık yapmak değil, maliyetlerin ortak kararın ortak sonucu olarak görülüp görülmemesidir. Bir partner ilk yıllarda taşınabilir, yıllar sonra roller değişebilir. Riskin şu: Kariyer ve para kolay hesaplanır, uyum emeği kolay görünmez. Kitap, bu emeği kimin taşıdığına da bakmayı önerir.", "32"),
        "K": ("Kökleri derin", "Sen hayatını kurduğun yerden kopmak istemiyorsun. Anlaşılır bir tercih: Dil, çevre ve iş piyasası senin sermayen. Kitap bunun öbür yüzünü gösterir: Yerel dili, hukuku ve iş piyasasını iyi bilen partner ilişkinin dış dünyayla bağlantısını kontrol ederken göçmen partner ona daha bağımlı hale gelebilir. Aynı evde iki dil zenginliktir. Hangisinin varsayılan sayıldığı ise güç dengesi hakkında da bilgi verir.", "32"),
        "U": ("Uzak mesafe yatırımcısı", "Sen hem kariyerini hem ilişkini korumak için mesafeyi göze alıyorsun. Teknoloji senden yana: Görüntülü görüşme ve anlık mesaj, geçmişte haftalarla ölçülen haberleşmeyi gündelik hale getirdi. Ama kitap uyarır: İletişim maliyeti düşerken erişilebilir olma beklentisi yükseldi. Birkaç saat cevap vermemek bile ilgisizlik sayılabilir. Uçak bileti, vize, izin günü ve zaman farkı da hâlâ gerçek. Mesafe kalkmaz, maliyet yapısı değişir.", "32"),
        "M": ("Üçüncü kültürün mimarı", "Sen ne onun kültürünü ne kendininkini olduğu gibi kopyalamak istiyorsun. Kitaba göre sağlıklı müzakere “Bizde böyle yapılır” cümlesinden “Bizim ilişkimizde nasıl yapılacak?” sorusuna geçildiğinde başlar. Naeimi ve Impett’in (2025) 592 kişilik çalışmasında bazı çiftler iki kültürden unsurları birleştirip kendilerine özgü pratikler oluşturdu. Bedeli: Başka çiftlerin hiç konuşmadan uyguladığı kurallar sizde açıkça konuşulmak zorunda kalır. Yorucu, ama görünmeyen varsayımları da açığa çıkarır.", "32"),
    },
}

# 38 — senaryo — Bölüm 06 ve 30
ICERIK["goruldu-ekonomisi"] = {
    "kanca": "“Görüldü” yazıyor, cevap yok. Bu bir sinyal mi, yoksa sadece uzun bir toplantı mı?",
    "sorular": [
        ("Mesajın “Görüldü” oldu ama üç saattir cevap yok. Sen?", [
            ("Z", "Müsait olunca uzun bir cevap yazacağını bilirim"),
            ("T", "Hep böyle mi yapıyor, ona bakarım"),
            ("S", "Bir mesaj daha atarım, belki yanlış anlaşıldım"),
            ("M", "Ben de bir o kadar bekler, sonra yazarım"),
            ("C", "Bir sonraki mesajımı daha iyi yazmaya çalışırım")]),
        ("Seni en çok hangi mesaj etkiler?", [
            ("Z", "Yoğun gününde bile ayırdığı uzun bir sesli mesaj"),
            ("T", "Her akşam aynı saatte gelen kısa bir “Günün nasıldı?”"),
            ("S", "Duygularını açıkça anlattığı uzun bir paragraf"),
            ("M", "Az ama yerinde, beklemediğim anda gelen bir cümle"),
            ("C", "Esprili, kusursuz kurulmuş bir mesaj")]),
        ("Hoşlandığın birine ilk mesajı yazıyorsun.", [
            ("Z", "Profilini dikkatle okuduğumu belli eden özel bir soru"),
            ("T", "Basit bir selam, asıl iş devamında"),
            ("S", "Ne hissettiğimi hiç saklamadan yazarım"),
            ("M", "Kısa tutarım, fazla hevesli görünmeyeyim"),
            ("C", "Defalarca yazıp siler, en etkileyici hâlini gönderirim")]),
        ("“Seni çok özledim” mesajı geldi. Ne düşünürsün?", [
            ("Z", "Güzel, ama görüşmek için zaman ayırıyor mu?"),
            ("T", "Bunu son haftalarda davranışlarıyla da gösterdi mi?"),
            ("S", "Çok mutlu olurum, söylemek önemlidir"),
            ("M", "Biraz bekletir, sonra cevap veririm"),
            ("C", "Cevabımı özenle, güzel bir cümleyle kurarım")]),
        ("Mesajlarını yazarken yapay zekâdan yardım alır mısın?", [
            ("Z", "Hayır, zaman ayırıp kendim yazmak işin özü"),
            ("T", "Hayır, nasıl yazıyorsam öyle bilinmeliyim"),
            ("S", "Duygumu anlatacak kelimeyi bulamazsam belki"),
            ("M", "Gerek yok, zaten az yazıyorum"),
            ("C", "Evet, mesajlarım daha akıcı ve esprili oluyor")]),
        ("Hangi cümle sana yakın?", [
            ("Z", "Zaman, geri alınamayan hediyedir."),
            ("T", "Bir kez değil, her gün."),
            ("S", "Söylenmeyen söz, hiç var olmaz."),
            ("M", "Az olan değerlidir."),
            ("C", "İyi yazılmış bir mesaj kapıyı açar.")]),
    ],
    "sonuclar": {
        "Z": ("Zaman sinyali", "Sen ilgiyi mesajın uzunluğuyla değil, ayrılan zamanla ölçüyorsun. Kitaba göre zaman güçlü bir sinyal olabilir, çünkü geri alınamaz: Para yeniden kazanılabilir, geçen saat geri getirilemez. Çok yoğun birinin ayırdığı zaman yüksek fırsat maliyeti taşıyabilir. Riskin şu: Zaman miktarından duygunun büyüklüğünü çıkarmak. Kişinin alternatiflerini ve yaşam koşullarını bilmeden bu hesap kolayca yanılır.", "06"),
        "T": ("Tutarlılık sinyali", "Sen tek bir mesaja değil, örüntüye bakıyorsun. Kitap buna gündelik bir Bayesçi hesap der: Yeni bilgi geldikçe karşımızdaki insan hakkındaki inançlarımızı güncelleriz. Tek bir davranışın yorumu her zaman belirsizdir, davranış tekrarlandıkça rastlantısal açıklamalar zayıflar. Kitaba göre uzun ilişkinin güçlü sinyallerinden biri gösteriş değil, tutarlılıktır. Riskin şu: Örüntünün oluşmasını beklerken ilk heyecanı ve ilk cesur adımları ıskalamak.", "06"),
        "S": ("Söz sinyali", "Sen duygunu söylemekten çekinmiyorsun ve söyleneni önemsiyorsun. Bu açıklık değerli. Ama oyun teorisindeki “ucuz konuşma” kavramı bir sınır çizer: Ucuz konuşma yalan demek değildir, ama aynı cümleyi samimi olmayan biri de kolayca kurabildiği için sözün ayırt edici gücü sınırlıdır. Kitabın formülü şu: Söylenen, davranışla ve geçmişle desteklendikçe güvenilir hale gelir.", "06"),
        "M": ("Kıtlık sinyali", "Sen ulaşılabilirliğini bilerek kısıyorsun: Kısa mesaj, gecikmeli cevap. Ama sinyalin anlamını yalnız gönderen belirlemez. Kitaba göre gönderenin istediği anlam ile alıcının çıkardığı anlam aynı olmak zorunda değildir. Üstelik iletişim ucuzladıkça erişilebilir olma beklentisi yükseldi: Birkaç saat cevap vermemek bile ilgisizlik olarak okunabilir. Senin “değerliyim” mesajın karşı tarafta “ilgilenmiyor” diye çözülebilir.", "06"),
        "C": ("Cyrano sinyali", "Sen mesajın iyi yazılmasını önemsiyorsun ve yardım almaktan çekinmiyorsun. Kitap bunu başlı başına hile saymaz: Fotoğrafçı, kuaför ve arkadaş tavsiyesi de kendini sunmanın eski yardımcılarıdır. Ama yapay zekâ bazı sinyallerin taklit maliyetini düşürür. Ante’nin (2026) çalışmasında öne çıkan kaygılardan biri, desteklenmiş çevrim içi personadan yüz yüze buluşmadaki desteksiz kişiye geçişti. Soru şu: Yazdığın kişi gerçekten sen misin?", "34"),
    },
}

# 39 — profil — Bölüm 34
ICERIK["2040-aski"] = {
    "kanca": "Algoritma seçiyor, yapay zekâ yazıyor, bazen karşıda insan bile yok. Sen bu geleceğin neresindesin?",
    "sorular": [
        ("Bir uygulama sana “Bu kişi yüzde 92 uyumlu” diyor.", [
            ("S", "Güvenirim, veriler genelde haklı çıkar"),
            ("Y", "Profili açar, ona nasıl yazacağımı düşünürüm"),
            ("A", "Ön görüşmeyi yapay zekâ asistanıma bırakırım"),
            ("P", "Benimle konuşan yapay zekâ zaten tam bana göre"),
            ("I", "Yüzdeyi değil, yüz yüze buluşmayı ciddiye alırım")]),
        ("Gece yarısı içini dökmek istiyorsun.", [
            ("S", "Uygulamanın önerdiği biriyle konuşmayı denerim"),
            ("Y", "Arkadaşıma yazarım, ama önce cümlelerimi bir yapay zekâyla toparlarım"),
            ("A", "Asistanım o saatte kimin müsait olduğunu bulsun"),
            ("P", "Yapay zekâ arkadaşımla konuşurum, o hep oradadır"),
            ("I", "Sabahı beklerim, bir dostumu ararım")]),
        ("Senin için hangisi daha romantik?", [
            ("S", "Algoritmanın bulduğu, hiç tanımadığım uyumlu biri"),
            ("Y", "Kusursuz kurulmuş, esprili bir mesaj"),
            ("A", "Önceden elenmiş üç adayla, zaman kaybetmeden buluşmak"),
            ("P", "Beni hiç reddetmeyen, her zaman anlayan biri"),
            ("I", "Kusurlu ama gerçekten insana ait, el yazısı bir not")]),
        ("Seni en çok ne rahatsız eder?", [
            ("S", "Gözümden kaçmış uyumlu bir aday"),
            ("Y", "Kötü yazılmış bir ilk mesaj"),
            ("A", "Boşa geçen ilk buluşmalar"),
            ("P", "Birinin beni günün birinde reddetmesi"),
            ("I", "Yazıştığım kişinin aslında bir yapay zekâ olması")]),
        ("Partnerin sana yazdığı mektubu bir yapay zekâya yazdırmış.", [
            ("S", "Sorun değil, önemli olan beni seçmiş olması"),
            ("Y", "Ben de yapıyorum, gayet normal"),
            ("A", "Verimli, zamanını başka bir şeye ayırmış"),
            ("P", "Fark etmez, güzel cümleler güzeldir"),
            ("I", "Kırılırım, kendi kelimelerini isterdim")]),
        ("Hangi cümle sana yakın?", [
            ("S", "Doğru veri, doğru eşleşme getirir."),
            ("Y", "Duygu benim, kelimeler yardımcı."),
            ("A", "Zamanım değerli, elemeyi başkası yapsın."),
            ("P", "Beni dinleyen, beni anlayandır."),
            ("I", "Seçilmenin değeri, seçilmeme ihtimalindedir.")]),
    ],
    "sonuclar": {
        "S": ("Algoritmaya güvenen", "Sen partner arama emeğini yazılıma devretmeye hazırsın. Kitabın yapay zekâ basamaklarında bu ilk basamaktır: Adayları sıralayan ve öneren sistem. Kazancı, arama maliyetinin düşmesi. Ama kitabın uyarısı önemli: Daha önce kimi seçtiğini öğrenen bir sistem sana geçmiş tercihlerinin giderek daha iyi kopyalarını sunabilir. Ne yapacağını tahmin etmek ile ne yapmanın iyi olacağını bilmek aynı problem değildir.", "34"),
        "Y": ("Cyrano kuşağı", "Sen duyguyu kendinde, kelimeyi yardımcıda görüyorsun. Kitaba göre yapay zekâ kullanmak başlı başına hile değildir. Ama Ante’nin (2026) çalışmasında karşı taraf yapay zekâ kullanımını sonradan öğrendiğinde aldatılmışlık hissi yaşayabiliyordu. Güzel mesaj yazmak ucuzladıkça güzel mesajın sinyal değeri de düşebilir. Kitabın önerdiği soru “Yapay zekâ kullandı mı?” değil, “Yapay zekâ ne yaptı?”", "34"),
        "A": ("Ajanını gönderen", "Sen zamanını korumak için ön elemeyi bir yapay zekâ ajanına bırakmaya açıksın. Kitap bunu ekonomik olarak son derece çekici bulur: Yüz profil yerine beş aday, on başarısız ilk buluşma yerine önceden filtrelenmiş üç kişi. Bedeli ise romantik serendipity, yani tesadüfen iyi bir insanla karşılaşma ihtimalinin azalması. Asıl soru da açık: Ajanına neyi başarı saymasını söyledin?", "34"),
        "P": ("Sentetik yakınlığa açık", "Sen her zaman erişilebilir, seni hiç bekletmeyen bir muhatabın değerini görüyorsun. Kitap bu çekiciliği ciddiye alır: Yapay partner ret riskini ve koordinasyon maliyetini olağanüstü ölçüde düşürür. Ama bir soru bırakır: İnsan ilişkisinde karşı tarafın özgürce “hayır” diyebilmesi, “evet”inin değerinin bir bölümünü oluşturur. Üstelik yapay partner bir şirketin ürünüyse tek bir güncelleme ilişkiyi değiştirebilir.", "34"),
        "I": ("Analog romantik", "Sen geleceğe karşı değilsin, ama aşkta insanın kendisini istiyorsun. Kitaba göre yapay zekâ çağında doğrulanabilir insanlık sinyalleri daha değerli hale gelebilir: Yüz yüze buluşma, tutarlı davranış, ortak arkadaşlar. El yazısı mektubun e-posta çağında daha romantik görünmesi gibi, kusurlu ama gerçekten insana ait bir cümle daha kıymetli olabilir. Riskin, işe yarayan araçları da toptan reddetmek.", "34"),
    },
}
