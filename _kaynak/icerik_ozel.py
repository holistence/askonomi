# -*- coding: utf-8 -*-
# Aşkın Kimyası özel bölümü — 40 testlik serinin dışında, numarasız iki test.
# Kitap bölümüne yönlendirme yok (10–14 yasak bölüm kuralı gereği Bölüm 10'a da bağlanmıyor).
# Kaynaklar /kimya/ sayfasının sonunda APA biçiminde listeleniyor.

ICERIK = {}

ICERIK["ask-evresi"] = {
    "kanca": "Arzu, çekim ve bağ beyinde ayrı sistemler gibi çalışır, sen hangisinin içindesin?",
    "sorular": [
        ("Onu düşündüğünde aklına ilk ne geliyor?", [
            ("A", "Yakınlık, dokunma isteği"), ("C", "Bir sonraki mesaj, bir sonraki buluşma"),
            ("B", "Birlikte kurduğumuz gündelik düzen")]),
        ("Bir gün ondan hiç haber alamasan ne hissedersin?", [
            ("A", "Özlerim ama hayatım akmaya devam eder"), ("C", "Telefona dakikada bir bakarım"),
            ("B", "Merak ederim ama endişelenmem, güvenirim")]),
        ("Son zamanlarda uykun ve iştahın nasıl?", [
            ("A", "Normal, sadece onu görünce enerjim yükseliyor"), ("C", "Uykum kaçıyor, yemek aklıma gelmiyor"),
            ("B", "Düzenli, hatta yanında daha rahat uyuyorum")]),
        ("Onun kusurları hakkında ne düşünüyorsun?", [
            ("A", "Pek düşünmedim, çekim daha baskın"), ("C", "Kusur mu? Şimdilik göremiyorum"),
            ("B", "Hepsini biliyorum, çoğuyla barıştım")]),
        ("Birlikteyken en çok neyi seviyorsun?", [
            ("A", "Tensel yakınlığı"), ("C", "Kalbimin hızlanmasını, o heyecanı"),
            ("B", "Hiç konuşmadan yan yana olabilmeyi")]),
        ("Aranızda bir sorun çıkınca ilk tepkin ne olur?", [
            ("A", "Biraz mesafe alırım, çekim sürerse dönerim"), ("C", "Dünyam yıkılır, hemen çözmek isterim"),
            ("B", "Konuşuruz, birlikte bir yol buluruz")]),
        ("Gelecekten söz ederken neler konuşuyorsunuz?", [
            ("A", "Pek konuşmuyoruz, şimdiyi yaşıyoruz"), ("C", "Her şeyi hayal ediyorum ama hiçbiri somut değil"),
            ("B", "Ev, iş, tatil gibi somut planlar yapıyoruz")]),
        ("Bir arkadaşın ilişkini tek kelimeyle anlatsa hangisini seçerdi?", [
            ("A", "Tutkulu"), ("C", "Sırılsıklam"), ("B", "Huzurlu")]),
    ],
    "sonuclar": {
        "A": ("Arzu evresi", "Seni şu an en çok yakınlık ve beden çekiyor. Araştırmacılar cinsel arzuyu romantik çekimle bağlantılı ama ayrı bir sistem olarak ele alır. Arzuda testosteron gibi hormonların payı büyüktür, hem kadınlarda hem erkeklerde. Arzu tek başına bir ilişkinin geleceğini söylemez. Ama çoğu hikâyenin ilk kıvılcımıdır. Asıl soru şu: Bu yakınlık zamanla merak ve bağa dönüşüyor mu?", ""),
        "C": ("Çekim evresi", "Sen tam ortasındasın. Uykusuz geceler, sürekli kontrol edilen telefon, kusursuz görünen biri. Beyin görüntüleme çalışmaları bu evrede dopaminle çalışan ödül ve istek sisteminin belirgin biçimde etkinleştiğini gösteriyor. Sevilen kişiye yönelik eleştirel yargıyla ilişkili bazı bölgelerde ise etkinlik azalabiliyor. Keyfini çıkar. Ama büyük kararları biraz bekletmek akıllıca olabilir, çünkü beynin şu an sana tarafsız bir rapor sunmuyor.", ""),
        "B": ("Bağ evresi", "Heyecanın yerini huzur almış görünüyor. Bu bir düşüş değil, başka bir sistemin devreye girmesi. Bağlanmada oksitosin ve vazopresinin rol oynadığı düşünülüyor, ancak en güçlü kanıt hayvan çalışmalarından geliyor. İyi haber şu: Uzun evliliklerde bile ödül sisteminin etkin kalabildiğini gösteren çalışmalar var. Bağın sermayesi güvendir. Bakımı ise birlikte yaşanan yeni deneyimlerdir.", ""),
    },
}

ICERIK["askin-kimyasi-mitleri"] = {
    "kanca": "Aşkın kimyası hakkında her yerde duyduğun altı cümle, kaçı bilime dayanıyor?",
    "sorular": [
        ("Oksitosin “aşk hormonu”dur, burna sıkılan oksitosin insanları birbirine bağlar.", False,
         "Yanlış. Oksitosin doğum, emzirme, dokunma ve sosyal bağlanmada rol oynar. Ama burun spreyiyle verilen oksitosinin davranışa etkisini inceleyen çalışmaların önemli bir kısmı küçük örneklemliydi ve sonuçlar tutarlı biçimde tekrarlanamadı (Walum, Waldman ve Young, 2016). Tek bir “aşk hormonu” yoktur."),
        ("Terk edilmiş ama hâlâ âşık birinin beyni, bağımlılıkla ilişkili bölgelerde etkinlik gösterir.", True,
         "Doğru. Yakın zamanda terk edilmiş ama hâlâ âşık olan kişilerin beyin taramalarında ödül, motivasyon ve bağımlılıkla ilişkili bölgelerde etkinlik görüldü (Fisher vd., 2010). Bu, aşkın bir hastalık olduğu anlamına gelmez. Ama vazgeçmenin neden bu kadar zor olduğunu açıklamaya yardım eder."),
        ("Aşk en fazla üç yıl sürer, bu biyolojik bir kuraldır.", False,
         "Yanlış. Bu cümlenin ünü bilimden çok popüler kültürden gelir. Ortalama yirmi bir yıldır evli olup hâlâ yoğun romantik aşk bildiren kişilerin beyin taramalarında, yeni âşıklardakine benzer ödül sistemi etkinliği görüldü (Acevedo vd., 2012). Aşkın biçimi değişebilir. Ama biyolojik bir son kullanma tarihi yoktur."),
        ("Kalp kırıklığı gerçek bir kalp sorununa yol açabilir.", True,
         "Doğru. Ani ve yoğun duygusal stres, “kırık kalp sendromu” olarak bilinen geçici bir kalp kası işlev bozukluğuna yol açabilir. Bu hastalarda stres hormonlarının belirgin biçimde yüksek olduğu bulundu (Wittstein vd., 2005). Çoğu vakada tablo geçicidir. Ama göğüs ağrısı her zaman acil tıbbi değerlendirme gerektirir."),
        ("Âşıkken sevilen kişiye yönelik eleştirel yargı zayıflayabilir.", True,
         "Doğru. Sevdiklerinin fotoğrafına bakan âşıkların beyninde, olumsuz duygular ve sosyal yargıyla ilişkili bazı bölgelerde etkinliğin azaldığı görüldü (Bartels ve Zeki, 2004). Halk arasında buna “aşk körlüğü” denir. Bilimsel bulgu daha sınırlıdır, ama yönü aynıdır."),
        ("Cinsel arzu ile romantik bağ aynı şeydir, aynı kimyayla çalışır.", False,
         "Yanlış. Antropolog Helen Fisher arzu, romantik çekim ve bağlanmayı birbiriyle bağlantılı ama ayrı beyin sistemleri olarak tanımladı (Fisher, 1998). Bu yüzden insan, bağ hissetmediği birine arzu, arzu duymadığı birine derin bağ hissedebilir. İkisi aynı ilişkide buluşabilir ama aynı şey değildir."),
    ],
    "seviyeler": [
        (0, "Slogan avcısı",
         "Aşk kimyası hakkındaki popüler cümlelerin çoğu sana inandırıcı gelmiş. Yalnız değilsin, bu sloganlar her yerde. Gerçek tablo daha karmaşık. Tek bir “aşk hormonu” yok, beynin birkaç sistemi aynı anda çalışıyor. Ve hiçbir kimyasal, kiminle hayat kuracağına senin yerine karar vermiyor."),
        (3, "Meraklı gözlemci",
         "Bazılarını bildin, bazılarında popüler anlatıya kandın. Aşkın kimyasında en sık yapılan hata, karmaşık bir süreci tek bir moleküle indirgemek. Beyin, kalp ve hormonlar birlikte çalışır. Ama arzu, çekim ve bağ birbirinden ayrı da işleyebilir."),
        (5, "Nörobilim okuru",
         "Aşkın kimyasını sloganlardan ayırmayı biliyorsun. Bir adım ötesi şu soru: Kimya bize ne hissettiğimizi anlatıyorsa, kiminle hayat kuracağımıza nasıl karar veriyoruz? Aşkonomi tam bu sorudan başlıyor."),
    ],
}
