# -*- coding: utf-8 -*-
# Aşkonomi test serisi, Sezon 1 (test 1-10). Kitabın v45 metniyle karşılaştırılıp düzeltildi.
# Kaynak sayfa numaraları: /home/claude/askonomi_in/rapor_s1.md

ICERIK = {}

# 1 ------------------------------------------------------------------
ICERIK["fiyatin-ne"] = {
    "kanca": "Sevgilinin fiyat etiketi yok, ama senin gözünde aşkın bir bedeli var.",
    "sorular": [
        ("Bir ilk buluşmada seni en çok ne soğutur?", [
            ("Z", "Son dakika iptal etmesi"), ("D", "Sürekli telefonuna bakması"),
            ("G", "Anlattıklarının birbirini tutmaması"), ("O", "İkinci buluşmayı hemen planlamaya kalkması"),
            ("H", "Her şeyin fazla sıradan geçmesi")]),
        ("Hangi jest seni kazanır?", [
            ("Z", "En yoğun haftasında sana bir akşam ayırması"), ("D", "Bir ay önce söylediğin küçük bir ayrıntıyı hatırlaması"),
            ("G", "Söylediği saatte, söylediği yerde olması"), ("O", "“Bu hafta sonu kendine zaman ayır” demesi"),
            ("H", "Hiç denemediğiniz bir şeyi birlikte yapmayı önermesi")]),
        ("Bir ilişkide neyi “zarar” hanesine yazarsın?", [
            ("Z", "Hep bir sonraki haftaya ertelenen planları"), ("D", "Yarım kulakla dinlenmeyi"),
            ("G", "Küçük de olsa yalanları"), ("O", "Her adımının sorgulanmasını"),
            ("H", "Her günün bir öncekinin kopyası olmasını")]),
        ("Arkadaşın yeni sevgilisini anlatıyor. Hangi cümle seni ikna eder?", [
            ("Z", "“Ne kadar yoğun olsa da bana vakit ayırıyor.”"), ("D", "“Beni gerçekten dinliyor.”"),
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
        "Z": ("Senin bedelin: Zaman",
              "Senin için sevginin en inandırıcı kanıtı takvimde açılan yerdir. Kitap zamanı aşkın en temel kıt kaynaklarından biri sayar: Kimse güne yirmi beşinci saati ekleyemez. Bir saatin anlamı da hangi koşulda ve neyden vazgeçilerek verildiğine bağlıdır. Bedeli şu: Yoğun bir dönemdeki partneri sevgisizlikle suçlamak kolaylaşır. Kitap uyarır: “Bana zaman ayırmıyor, demek ki beni sevmiyor” çıkarımı her durumda doğru değildir.",
              "03"),
        "D": ("Senin bedelin: Dikkat",
              "Sen sevilmeden önce görülmek istiyorsun. Aynı masada oturmak yetmez, zihnin de orada olmalı. Kitaba göre romantik ilişkide para dışındaki kıt kaynaklar da sinyal taşır ve dikkat bunların başında gelir. Pahalı ama kişisiz bir hediye seni etkilemez. Aylar önce söylediğin küçük bir ayrıntıyı hatırlayan ucuz bir hediye ise dikkat hakkında güçlü bilgi taşır. Bedeli şu: Dikkat her an ölçülebildiği için hayal kırıklığı da her an üretilebilir.",
              "06"),
        "G": ("Senin bedelin: Güven",
              "Senin para birimin tutarlılık: Söylenen saatte orada olmak, verilen küçük sözü tutmak. Kitap güveni bir sermayeye benzetir. Geçmiş davranışlardan birikir ve ilişkinin günlük işlem maliyetini düşürür. Ama banka hesabı gibi işlemez: Küçük bir gecikme yılların güvenini silmeyebilir, tek büyük ihanet ise bütün geçmişin yorumunu değiştirebilir. Bedeli şu: Kitaba göre sürekli yeni kanıt isteyen ilişki, hiçbir sinyalin yeterince güvenilir sayılmadığı ilişkiye dönüşebilir.",
              "24"),
        "O": ("Senin bedelin: Alan",
              "Seni kazanmanın yolu seni tutmaya çalışmamaktan geçiyor. Kitap insanların ilişkiden beklediklerinin farklı olduğunu söyler: Biri için sık görüşmek ilişkinin kalitesinin temel göstergesidir, başka biri için kişisel alanın korunması aynı derecede değerlidir. Sende ikincisi ağır basıyor. Kitaba göre mahremiyet, partnerden gizli ikinci bir hayat sürdürmekle aynı şey değildir. Bedeli şu: Sık temas isteyen biri, alan ihtiyacını ilgisizlik diye okuyabilir.",
              "24"),
        "H": ("Senin bedelin: Yenilik",
              "Senin için en büyük maliyet sıkılmak. Aynı hafta sonu düzeni sana güven değil durgunluk gibi gelir. Kitap bu konuda bir araştırma aktarır: Birlikte yeni ve uyarıcı deneyimler yaşamak bazı çiftlerde ilişki kalitesini destekleyebilir. Ama kitaba göre yenilik harcamanın büyüklüğüyle değil, rutin dışı ortak deneyimin niteliğiyle ilgilidir. Bedeli şu: İnsan yeni deneyimlere de alışabilir ve hayatı sürekli uyarılma arayışına çevirmek sürdürülebilir değildir.",
              "25"),
    },
}

# 2 ------------------------------------------------------------------
ICERIK["kacan-mi-kovalanan-mi"] = {
    "kanca": "“Kaçan kovalanır” derler, peki sen hangisisin?",
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
            ("K", "Değerimin düştüğünü hissederim"), ("V", "Huzurlu, ben zaten hep oradayım"),
            ("D", "Karşılıklıysa güzel"), ("S", "Biraz boğucu")]),
        ("Arkadaşların seni nasıl tarif eder?", [
            ("K", "“Onu yakalamak zor.”"), ("V", "“Sevince her şeyini verir.”"),
            ("D", "“Ne istediğini bilir.”"), ("S", "“Hep izler, nadiren adım atar.”")]),
        ("Hangi cümleye katılırsın?", [
            ("K", "Değer, ulaşılmazlıktan doğar."), ("V", "Sevgi saklanmaz, gösterilir."),
            ("D", "Oyun oynayan kaybeder."), ("S", "Hiç başlamayan ilişki bitmez de.")]),
    ],
    "sonuclar": {
        "K": ("Kaçan: Kıtlık stratejisi",
              "Arzını bilerek kısıyorsun: Geç cevap, belirsiz plan, biraz mesafe. Ulaşılmaz kalmanın değerini artıracağını düşünüyorsun. Kitap bu sezgiyi bütünüyle reddetmez ama sınırını çizer: Kıtlık tek başına değer yaratmaz, kıt olan şeyin aynı zamanda istenmesi gerekir. Bedeli şu: Kitaba göre cevap vermemek, sürekli uzak durmak veya karşı tarafı belirsizlik içinde tutmak bazı durumlarda ilgiyi artırmak yerine ilişkiyi sona erdirebilir.",
              "03"),
        "V": ("Kovalayan: Güçlü talep",
              "Sevdiğinde hesabı kitabı bırakıyorsun, ilk adımı atan çoğu zaman sen oluyorsun. Bu cömertlik güzel. Ama kitabın aşk piyasası bölümü bir kuralı hatırlatır: Romantik ilişkide aynı anda iki tercih sistemi çalışır ve karşındakinin de seni seçmesi gerekir. Kitabın deyişiyle “Çok istemek, tek başına eşleşme üretmez.” Bedeli şu: Yaptığın fedakârlık karşılığı garanti eden bir bedel değildir, çünkü sevgilinin fiyat etiketi yoktur.",
              "05"),
        "D": ("Dengede: Açık sinyal",
              "Oyun oynamıyorsun. Ne istediğini söylüyor, karşılığını bekliyorsun. Kitap burada bir ayrım yapar: Söz ucuzdur, çünkü samimi olmayan kişi de aynı cümleyi kolayca kurabilir. Senin açıklığını inandırıcı yapan, söylediklerinle yaptıklarının zaman içinde uyuşmasıdır. Kitaba göre uzun ilişkinin güçlü sinyallerinden biri gösteriş değil tutarlılıktır. Bedeli şu: Aynı davranış bir insan için güçlü ilgi, başka biri için sınır ihlali gibi görünebilir.",
              "06"),
        "S": ("Seyirci: Kenarda bekleyen",
              "Risk almaktansa beklemeyi seçiyorsun. Reddedilme ihtimali kazanma ihtimalinden ağır basıyor. Kitap romantik kararların fiyatının yalnız para olmadığını söyler: Reddedilme riski ve duygusal kırılganlık da kararın maliyetleri arasındadır. Senin için bu maliyet yüksek. Bedeli şu: Kitabın hatırlattığı gibi “Karar vermemek de zaman geçtiği için fiilen bir karardır.” Beklerken kaçan fırsatlar hiçbir faturada görünmez, ama fırsat maliyeti tam da orada durur.",
              "26"),
    },
}

# 3 ------------------------------------------------------------------
ICERIK["kalp-mi-akil-mi"] = {
    "kanca": "Kalple akıl gerçekten düşman mı, altı zor seçimde kendini dene.",
    "sorular": [
        ("İki seçenek var: Seni heyecanlandıran ama düzensiz yaşayan biri, ya da güvenilir ama “kıvılcım”ı olmayan biri.", [
            ("R", "Güvenilir olan. Kıvılcım sonradan gelir, istikrar gelmez."), ("T", "Heyecan. Hayat bir kere."),
            ("S", "İlk andaki hissim neyse o."), ("D", "İkisiyle birer kez daha buluşur, sonra karar veririm.")]),
        ("Sevgilin başka bir şehirde iş teklifi aldı.", [
            ("R", "Kira, ulaşım, kariyer… artı-eksi listesi yaparım."), ("T", "Nereye giderse peşinden giderim."),
            ("S", "İçime ne doğarsa onu yaparım."), ("D", "Önce ne istediğimizi konuşur, sonra hesap yaparız.")]),
        ("Gece ikide büyük bir kavga ettiniz. “Bitti” demek üzeresin.", [
            ("R", "Sakinleşince artı-eksi listesi yapar, öyle karar veririm."), ("T", "O an ne hissediyorsam söylerim, sonrası sonra."),
            ("S", "Bu tür kavgaların nereye gittiğini önceki ilişkilerimden bilirim."), ("D", "Kararı sabaha bırakırım, sabah da aynı görünüyorsa ciddiye alırım.")]),
        ("Arkadaşların seni biriyle tanıştırdı. Kâğıt üzerinde bütün kriterlerine uyuyor ama hiçbir şey hissetmedin.", [
            ("R", "Bir şans daha veririm, kriterlerimi boşuna koymadım."), ("T", "Kıvılcım yoksa yoktur, devam etmem."),
            ("S", "İlk izlenimim neyse odur, nadiren yanılır."), ("D", "Birkaç kez daha görüşürüm, his bir bilgi ama tek bilgi değil.")]),
        ("“Aşk kördür” sözü için ne dersin?", [
            ("R", "Kör değil, hesabı sonra yapar."), ("T", "Kördür ve iyi ki öyledir."),
            ("S", "Kör değil, sadece çok hızlıdır."), ("D", "Başta kördür, zamanla gözlüğünü takar.")]),
        ("Evlilik kararı ne zaman verilir?", [
            ("R", "Ekonomik ve pratik koşullar hazır olunca"), ("T", "Doğru kişiyi bulduğun an"),
            ("S", "Bir gün “işte bu” diye hissettiğinde"), ("D", "Hem içinden geldiğinde hem şartlar elverdiğinde")]),
    ],
    "sonuclar": {
        "R": ("Kalbin bir muhasebeci",
              "Sen sevmiyor değilsin, sadece sevginin hesabını da tutuyorsun. Kitaba göre bu soğukluk değil: Ekonomik rasyonellik en çok parayı getiren seçeneği bulmak değil, değer verdiğin farklı amaçlar arasında seçim yapabilmektir. Bedeli şu: Her şeyi sürekli tartmak bağlılığı erteleyebilir. Kitabın ölçüsü açık: “Rasyonellik ilişkinin sürekli muhasebesini yapmak değil, önemli yeni bilgi geldiğinde eski hükmü değiştirebilme kapasitesini korumaktır.”",
              "02"),
        "T": ("Kalbin bir kumarbaz",
              "Sen büyük oynarsın. Riskleri görürsün ama kalbinin sesine uyarsın. Kitap bunu otomatik olarak irrasyonel saymaz: Ortak hayat senin için vazgeçtiğin şeyden değerliyse seçimin kendi tercihlerin içinde anlaşılabilir. Ama yoğun özlem anındaki “Onsuz yaşayamam” hissinin geleceği kusursuz tahmin etmediğini de hatırlatır. Bedeli şu: Kitaba göre rasyonellik burada duygusuzluk değil, geri dönüşü zor kararları birden fazla duygusal durumda değerlendirebilmektir.",
              "02"),
        "S": ("Kalbin bir kestirme yol",
              "Sen uzun hesap yapmıyorsun ama rastgele de karar vermiyorsun. Sezgilerin, yaşadıklarından süzülmüş hızlı kurallar. Kitap Tversky ve Kahneman’ın klasik çalışmalarından yola çıkarak bu kestirmelerin belirsizlikte karar vermeyi kolaylaştırdığını, ama bazen sistematik hatalara yol açabildiğini anlatır. Bedeli şu: Yakın zamanda yaşanan kötü bir ayrılık yeni insanlara ilişkin risk algını büyütebilir. Kitabın ölçüsü, sezginin hangi durumda ne kadar iyi rehber olduğunu fark edebilmektir.",
              "02"),
        "D": ("Kalp ile akıl ortaklığı",
              "Ne körü körüne atlıyorsun ne de her şeyi tabloya döküyorsun. Önce hissediyor, sonra kontrol ediyorsun. Kitap tam bu ayrımı savunur: “Onu seviyor muyum?” ile “Onunla yaşayabilir miyim?” farklı sorulardır. Duygu neyi önemsediğini bildirir, akıl sonuçları düşünmene yardım eder. Bedeli şu: Bu yol yavaştır. Kararı fazla uzatırsan, kitabın dediği gibi karar vermemek de zaman geçtiği için fiilen bir karara dönüşür.",
              "02"),
    },
}

# 4 ------------------------------------------------------------------
ICERIK["ilk-bulusma-sinyali"] = {
    "kanca": "Sen bir şey söylüyorsun, karşındaki başka bir şey duyuyor.",
    "sorular": [
        ("İlk buluşmanın yerini nasıl seçersin?", [
            ("E", "Onun sevdiği şeyleri araştırıp ben seçerim"), ("V", "Şık, adı bilinen bir yer"),
            ("D", "“Ben şurayı severim, sen ne dersin?” diye sorarım"), ("G", "Son ana kadar söylemem, sürpriz olsun")]),
        ("Ne giyersin?", [
            ("E", "Özenle hazırlanırım, emek belli olsun"), ("V", "En iyi, en göz önündeki parçamı"),
            ("D", "Her zaman nasılsam öyle"), ("G", "Biraz farklı bir şey, çözmeye çalışsın")]),
        ("Kendinden ne kadar bahsedersin?", [
            ("E", "Az, daha çok onu dinlerim"), ("V", "Başarılarımdan, gezdiğim yerlerden"),
            ("D", "İyisiyle kötüsüyle ne varsa"), ("G", "Çok az, merak etsin")]),
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
        "E": ("Emek sinyali",
              "Sen “seni seviyorum” demek yerine bedeli olan şeyler yapıyorsun: Zaman, özen, araştırma. Kitap romantik ilişkide bazı güçlü sinyallerin cüzdandan değil takvimden geldiğini söyler. Taklit edilmesi güç davranışlar daha fazla bilgi taşıyabilir. Bedeli şu: Kitaba göre “Maliyet tek başına samimiyet sertifikası değildir.” Karşındaki emeğini görür, ama ne anlama geldiğine o karar verir.",
              "06"),
        "V": ("Vitrin sinyali",
              "Sen gücünü ve imkânlarını görünür kılıyorsun: Şık mekân, iddialı kıyafet, başarı hikâyeleri. Kitap bunu Veblen’in gösterişçi tüketim kavramıyla açıklar. Banka hesabı görünmez, ama mekân ve yaşam tarzı ekonomik kapasite hakkında işaret verebilir. Bedeli şu: Kitaba göre servet sinyalinin birden fazla yorumu olabilir. Pahalı restoran sana cömertlik, karşındakine gösteriş gibi görünebilir. Paranın görünür olması, herkesin gördüğünden hoşlanacağı anlamına gelmez.",
              "08"),
        "D": ("Şeffaflık sinyali",
              "Sen kartlarını açık oynuyorsun. Kitaba göre söz tek başına zayıf bir sinyaldir: Güvenilir insan da güvenilmez insan da kendini güvenilir diye tanıtabilir. Senin açıklığını değerli kılan, söylediğin gibi davranmaya devam etmen. Kitabın örneğiyle ilk buluşmadaki nezaket küçük bir veridir, altı ay boyunca gözlenen tutarlılık çok daha fazlası. Bedeli şu: Açıklık ilk anda göz kamaştırmayabilir. Getirisi zamanla birikir.",
              "06"),
        "G": ("Gizem sinyali",
              "Sen bilgiyi kısarak merak üretiyorsun. Kitap bunun işe yarayabileceğini kabul eder: Belirsizlik, ulaşılmazlık veya tutarsızlık bazen duygusal yoğunluğu artırabilir. Ama hemen ekler: “Yoğunluk ile ilişkinin kalitesi aynı değişken değildir.” Bedeli şu: Kitaba göre insanlar görünmeyen nitelikler hakkında gözlenebilir davranışlardan çıkarım yapar. Az veri verirsen çıkarımı karşındaki yapar. Gizem ilk buluşmayı kazandırabilir, ilişkiyi ise güven taşır.",
              "02"),
    },
}

# 5 ------------------------------------------------------------------
ICERIK["guzellik-mitleri"] = {
    "kanca": "“Güzellik bakanın gözündedir” derler ama araştırmalar o kadar emin değil.",
    "sorular": [
        ("Görünüşü ortalamanın altında değerlendirilen kişiler, iş hayatında ortalama görünümlülerden daha az kazanabilir.", True,
         "Doğru. Hamermesh ve Biddle’ın 1994 tarihli klasik çalışmasında, ortalamanın altında çekici bulunanların ortalama görünümlülere göre yaklaşık yüzde 5–10 daha düşük kazanç elde ettiği bulundu. Kitap yine de uyarır: Bu bulguyu “Güzel olursanız yüzde şu kadar daha fazla kazanırsınız” formülüne çevirmemek gerekir."),
        ("Güzellik primi her işte aynı büyüklükte ortaya çıkar.", False,
         "Yanlış. Kitabın aktardığı bir deneyde (Deryugina ve Shurchkov, 2015) çekici çalışanlara daha yüksek ücret teklifi, görünüşün performansla ilgili olmasının beklendiği görevde çıktı. Analitik ve veri girişi görevlerinde benzer prim görülmedi. Gerçek performans bilgisi ortaya çıktıkça görünüşün etkisi de azalabildi."),
        ("Kimin güzel olduğu konusunda insanlar birbirinden çok farklı düşünür.", False,
         "Yanlış, en azından sanıldığı kadar değil. Langlois ve arkadaşlarının (2000) on bir meta-analizden oluşan çalışması, insanların kimin çekici olduğu konusunda hem aynı kültür içinde hem kültürler arasında belirli düzeyde görüş birliği gösterebildiğini ortaya koydu. Kitap bunun tek ve evrensel bir güzellik standardı anlamına gelmediğini de ekler."),
        ("Çekici bulunan insanlar başka yönlerden de daha olumlu değerlendirilebilir.", True,
         "Doğru. Psikolojide buna çekicilik stereotipi, daha geniş anlamıyla halo etkisi denir. Langlois ve arkadaşlarının meta-analitik değerlendirmesinde çekici bulunan çocuk ve yetişkinlerin daha olumlu değerlendirilebildiği görüldü. Kitaba göre bu, onların gerçekten her alanda daha iyi olduğu anlamına gelmez."),
        ("Çiftler fiziksel çekicilik bakımından birbirine benzeme eğilimindedir.", True,
         "Doğru. Webster ve arkadaşlarının 2024’te eski meta-analitik verileri yeniden değerlendirdiği çalışmada, karma cinsiyetli çiftlerde iki partnerin dış gözlemcilerce değerlendirilen çekicilikleri arasında yaklaşık r = 0,39 düzeyinde pozitif ilişki bulundu. Kitap bunun ortalama bir örüntü olduğunu, bireyin kaderi olmadığını vurgular."),
        ("Gerçek romantik değerlendirmelerde fiziksel çekiciliğin etkisi erkeklerde kadınlardan çok daha büyüktür.", False,
         "Yanlış. Eastwick ve arkadaşlarının (2014) meta-analitik incelemesinde, varsayımsal partner sorularında verilen cevaplar farklılaşabilse de gerçek romantik değerlendirmelerde çekiciliğin etkisindeki cinsiyet farkı oldukça küçüktü ve anlamlı bulunmadı. Kitaba göre fiziksel çekicilik her iki taraf için de anlamlı rol oynayabilir."),
    ],
    "seviyeler": [
        (0, "Vitrine kanan",
         "Güzellik hakkındaki sezgilerinin çoğu, kitabın aktardığı araştırmalarla örtüşmedi. Kitabın deyişiyle “İnsan davranışı sloganlardan daha karmaşıktır.” Kitabın özeti iki cümle: Güzellik önemlidir. Fakat güzellik tek ve nesnel bir değer değildir."),
        (3, "Göz kararı",
         "Bazılarını doğru bildin, bazılarında yanıldın. Güzelliğin ekonomisi tam da bu yüzden ilginç: Görünüş ilk anda çok bilgi veriyormuş gibi gelir, ama kitabın deyişiyle “Güzel yüz, laboratuvar raporu değildir.”"),
        (5, "Piyasa analisti",
         "Güzelliğin nasıl ödüllendirildiğini iyi okuyorsun. Şimdi kitabın sorduğu zor soru sende: Toplum hangi alanlarda güzelliği ödüllendiriyor ve bu ödül ne ölçüde işlevsel olarak ilgili?"),
    ],
    "bolum": "07",
}

# 6 ------------------------------------------------------------------
ICERIK["para-konusulunca"] = {
    "kanca": "Aşk parayla satın alınmaz, peki faturayı kim ödüyor?",
    "sorular": [
        ("İlk buluşmada hesap?", [
            ("O", "Davet eden öder, sonra sıra değişir"), ("A", "Herkes kendi payını öder"),
            ("K", "Zaten pahalı olmayan bir yer seçerim"), ("C", "Ben öderim, tartışmaya gerek yok")]),
        ("Birlikte yaşamaya başladınız. Kira ve faturalar?", [
            ("O", "Hepsi tek, ortak hesaptan"), ("A", "Herkesin hesabı ayrı, giderler bölüşülür"),
            ("K", "Önce bütçe tablosu, sonra karar"), ("C", "Kim daha rahatsa o öder, saymayız")]),
        ("Partnerin sana sormadan büyük bir alışveriş yaptı.", [
            ("O", "Bozulurum, o bizim ortak paramız"), ("A", "Kendi parasıysa söz hakkım yok"),
            ("K", "Birikim planımızı bozdu mu, ona bakarım"), ("C", "Mutlu olduysa sorun değil")]),
        ("Biri ayda 100, diğeri 40 birim kazanıyor. Ortak giderler?", [
            ("O", "Kim ne kazanırsa ortak kasaya, giderler oradan"), ("A", "Gelir oranında, herkes kendi hesabından"),
            ("K", "Önce birikim payı ayrılır, kalanı paylaşılır"), ("C", "Çok kazanan rahatça üstlensin, saymayalım")]),
        ("Para yüzünden hangi kavga tanıdık geliyor?", [
            ("O", "“Bunu neden bana sormadın?”"), ("A", "“Benim paramla ilgili konuşma.”"),
            ("K", "“Yine mi harcadın?”"), ("C", "“Neden bu kadar hesapçısın?”")]),
        ("Hangi cümle seni anlatır?", [
            ("O", "Evlilik ortaklıksa kasa da ortaktır."), ("A", "Ayrı cüzdan, sağlam ilişki."),
            ("K", "Bugünün aşkı, yarının güvencesiyle büyür."), ("C", "Para harcamak içindir, hele sevdiğin için.")]),
    ],
    "sonuclar": {
        "O": ("Ortak kasa",
              "Senin için ilişki bir ortaklık, ortaklığın da tek kasası olur. Kitap bu konuda dikkat çekici bir araştırma aktarır: Gladstone ve arkadaşlarının (2022) çalışmasında parasını tamamen birleştiren çiftler ortalamada daha yüksek ilişki doyumu bildirdi. Ama kitap bunun evrensel bir reçete olmadığını vurgular: Ortak hesap kendiliğinden güven yaratmaz. Bedeli şu: Ortak kasada harcama kararları da ortak olmak zorunda, “Bunu neden bana sormadın?” sorusu buradan doğar.",
              "08"),
        "A": ("Ayrı cüzdan",
              "Sen aşkı paylaşıyorsun, cüzdanı ayrı tutuyorsun. Bu bencillik değil, özerkliği korumanın bir yolu. Kitaba göre ayrı hesap kullanan çift kötü ilişkiye mahkûm değildir. Kitap paranın özgürlükle bağını da vurgular: Kendi geliri olan kişi ilişkide zorunluluktan değil gönüllülükten kalabilir. Bedeli şu: Para dışındaki katkılar, yani zaman ve bakım, bu hesapta kolayca görünmez olur. Kitabın hatırlattığı gibi “Aşk bütçesinin bütün satırları para cinsinden yazılmaz.”",
              "08"),
        "K": ("Tasarruf eden kalp",
              "Senin için para harcanacak değil, korunacak bir şey: Yarının güvencesi. Bu ilişkiye istikrar getirebilir. Ama kitap para kavgalarının çoğu zaman rakamdan değil anlamdan çıktığını söyler: Bir eş için tasarruf güvenlik, diğeri için yaşamın ertelenmesi olabilir. Kitaba göre bütçe rakamlardan, para kavgası ise çoğu zaman değerlerden oluşur. Bedeli şu: Kitabın aktardığı bir çalışmada para tartışmaları en sık yaşanan tartışma değildi, ama diğerlerine göre daha tekrarlayıcı ve çözülmesi daha zor olma eğilimi gösterdi.",
              "08"),
        "C": ("Cömert kalp",
              "Sen sevgiyi biraz da harcayarak gösteriyorsun: Hediye, davet, sürpriz. Kitaba göre para “Seni seviyorum” cümlesinin davranışa dönüşme yollarından biri olabilir. Ama kitap aynı cümlenin tersini de yazar: Para sevginin yerine de konabilir. Bir taraf para üreterek katkı verirken diğeri zaman ve duygusal yakınlık bekleyebilir. Bedeli şu: Kitaba göre para her zaman zamanın, dikkatin ve bakımın tam ikamesi değildir.",
              "08"),
    },
}

# 7 ------------------------------------------------------------------
ICERIK["benzer-mi-zit-mi"] = {
    "kanca": "Zıt kutuplar birbirini çeker mi, yoksa senin seçimlerin başka bir şey mi söylüyor?",
    "sorular": [
        ("İdeal partnerin hangi konuda sana benzemeli?", [
            ("B", "Neredeyse her konuda"), ("Z", "Hiçbir konuda, yoksa sıkılırım"),
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
        "B": ("Ayna: Benzerini seçen",
              "Sen kendine benzeyeni seçiyorsun ve gerçek çiftlerin tablosu sana yakın. Kitaba göre insanlar eğitim, din ve yaşam tarzı gibi birçok özellikte benzerleriyle beklenenden daha sık eşleşir. Buna seçici eşleşme ya da homogami denir. Ama bunun tek nedeni tercih değildir: Aynı okul, işyeri ve mahalle benzer insanları zaten bir araya getirir. Bedeli şu: Kitaba göre benzer eşleşme bazen mevcut eşitsizlikleri aynı hanede yoğunlaştırabilir.",
              "09"),
        "Z": ("Zıt kutup",
              "Sen farklılıktan besleniyorsun, tanımadığın dünya seni çekiyor. Kitap “zıt kutuplar çeker” sözünün gerçek çiftlerin genel tablosuyla pek örtüşmediğini gösterir: İnsanlar birçok özellikte benzerleriyle beklenenden daha sık eşleşir. Ama kitaba göre “benzer benzeri bulur” da tek başına bir ilişki teorisi değildir. Bedeli şu: Bütün farklar aynı değildir. Müzik zevki kolay yönetilir, çocuk isteğinde zıtlık çok daha temel bir çatışma yaratabilir.",
              "09"),
        "Y": ("Bir basamak yukarı",
              "Sen partnerinde biraz ileride olanı arıyorsun: Daha bilgili, daha deneyimli, çevresi daha geniş. İlişkinin seni büyütmesini istiyorsun. Kitap burada yaygın bir dile itiraz eder: “Yukarı evlenmek” gibi ifadeler çok boyutlu insan özelliklerini tek bir sıralamaya indirger. Biri daha eğitimli, öteki daha varlıklı olabilir. Böyle bir çiftte hangisi yukarıda? Bedeli şu: Yukarı bakarken karşındakinin de kendi tercih sıralaması olduğunu unutmak kolaydır.",
              "09"),
        "T": ("Tamamlayıcı",
              "Sen aynılık değil uyum arıyorsun: Değerler ortak, beceriler farklı. Kitap benzerlik ile tamamlayıcılığı rakip değil, farklı boyutlarda birlikte işleyen ilkeler olarak görür. Bir partner planlamada, öteki sosyal ilişkilerde güçlü olabilir. Farklı sektörlerdeki kariyerler riski çeşitlendirebilir. Bedeli şu: Klasik aile ekonomisi tamamlayıcılığı zaman zaman katı bir iş bölümüne bağladı. Kitaba göre uzmanlaşmanın uzun dönemli maliyeti, ayrılık hâlinde taraflardan birinin üzerinde birikebilir.",
              "09"),
    },
}

# 8 ------------------------------------------------------------------
ICERIK["ihtiyac-arzu-tercih"] = {
    "kanca": "Onu seviyor musun, yoksa ona ihtiyacın mı var?",
    "sorular": [
        ("Bir hafta hiç görüşemeseniz?", [
            ("I", "Eksik ve huzursuz hissederim"), ("A", "Özlemden yanarım"),
            ("T", "Kendi işlerime bakarım, döndüğünde yine o"), ("L", "Bir şey değişmez, sadece düzenim bozulur")]),
        ("Onu ilk neden seçtin?", [
            ("I", "Yanımdayken kendimi güvende hissettim"), ("A", "Ondan gözümü alamadım"),
            ("T", "Tanıdığım herkes arasında bana en çok o uydu"), ("L", "Bir şekilde hayatımdaydı, devam etti")]),
        ("Kâğıt üzerinde daha “uygun” biri çıksa?", [
            ("I", "Korkarım ama onu bırakamam"), ("A", "Uygunluk değil, çekim önemli"),
            ("T", "Karşılaştırırım, yine de onu seçerdim diye düşünüyorum"), ("L", "Değiştirmek zahmetli gelir")]),
        ("Onunla ilgili en çok neyi seversin?", [
            ("I", "Hep orada olmasını"), ("A", "Bana hissettirdiklerini"),
            ("T", "Kim olduğunu"), ("L", "Her şeyi bilmesini, açıklamak zorunda kalmamayı")]),
        ("Ayrılık düşüncesi sana ne hissettirir?", [
            ("I", "Paniğe kapılırım, onsuz eksik kalırım"), ("A", "Acı ama yaşanmaya değmiş bir tutku"),
            ("T", "Üzüntü, ama hayat devam eder"), ("L", "Bütün düzenin değişmesi, yorucu")]),
        ("Hangi cümle daha yakın?", [
            ("I", "“O olmadan eksiğim.”"), ("A", "“Onu istemekten vazgeçemiyorum.”"),
            ("T", "“Her sabah onu yeniden seçiyorum.”"), ("L", "“Onunla her şey kolay.”")]),
    ],
    "sonuclar": {
        "I": ("İhtiyaç: Güvenli liman",
              "Senin bağının merkezinde güven ve aidiyet var. Kitaba göre ihtiyaç, iyi oluş için önemli olan genel koşuldur: Yakınlık, aidiyet, güven. Bunların mutlaka romantik ilişki içinde karşılanması gerekmez, ama sende büyük ölçüde onda toplanmış. Bedeli şu: Kitap “birbirimize ihtiyacımız var” cümlesinin iki anlamını ayırır. Birinde insanlar birbirinin hayatını zenginleştirir, diğerinde kişinin başka gerçek seçeneği kalmamıştır. Kitabın deyişiyle “Bağlılık, çıkış imkânının tamamen yokluğu değildir.”",
              "04"),
        "A": ("Arzu: Yanan motor",
              "Senin bağın çekim üzerine kurulu: İstemek, özlemek, gözünü alamamak. Kitaba göre arzu, genel bir ihtiyacın belirli bir kişiye yönelmiş hâlidir. “Yakınlık istiyorum” ile “Ayşe'yle birlikte olmak istiyorum” arasındaki fark tam burada ortaya çıkar. Kitabın deyişiyle “İnsan yakınlığa ihtiyaç duyabilir ama herhangi birine âşık olmaz.” Bedeli şu: Kitap çok güçlü çekim hissedilen kişiyle yaşam tarzının uyuşmayabileceğini de hatırlatır.",
              "04"),
        "T": ("Tercih: Her gün yeniden",
              "Sen onu alternatifleri görüp yine de seçtiğin için yanında tutuyorsun. Kitaba göre tercih, istekler çatıştığında hangisine daha fazla ağırlık verdiğini gösterir. İktisat buna açıklanmış tercih der: Söylediklerimiz kadar gerçek kısıtlar altında yaptığımız seçimler de neyi değerli bulduğumuzu anlatır. Bedeli şu: Kitap burada ihtiyatlıdır. Seçtiğimiz şey her zaman en çok istediğimiz şey değildir, bazen yalnız ulaşabildiğimiz seçenektir.",
              "04"),
        "L": ("Alışkanlık: Ortak tarih",
              "Bağında alışkanlığın payı büyük ve bu kötü bir şey değil. Kitaba göre uzun ilişkide güven, bakım, alışkanlık ve ortak kimlik daha büyük yer tutabilir. Birlikte kurulan tarih başka bir partnerle anında yeniden üretilemez. Bedeli şu: Kitap bir sınır da çizer: “Bir ilişkide uzun süre kalmış olmak tek başına kalmaya devam etmek için yeterli neden değildir.” Kitabın sorusu: Kalmak ne zaman gitmekten pahalıdır?",
              "22"),
    },
}

# 9 ------------------------------------------------------------------
ICERIK["askin-alti-tanimi"] = {
    "kanca": "Kanadalı sosyolog John Alan Lee aşkı renkler gibi altı temel tarza ayırdı, sana en yakın olanı hangisi?",
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
        "E": ("Eros: Tutku",
              "Senin için aşk güçlü romantik ve fiziksel çekimle başlar. Lee bu tarza eros der. Kitap erken romantik aşkta beynin ödül ve motivasyon sistemlerinin etkinleşebildiğini aktarır, ama “aşk uyuşturucu gibidir” sonucuna hızla geçmemek gerektiğini de ekler. Bedeli şu: Kitaba göre otuz yıllık evlilikte aşkın bileşenleri değişir, özlemin yerini güven, bakım ve ortak kimlik alabilir. Asıl soru, kıvılcımın gündelik hayata nasıl taşınacağı.",
              "01"),
        "S": ("Storge: Dostluk",
              "Senin aşkın yavaş yanar ama uzun sürer. Lee bu tarza storge der: Arkadaşlık ve zaman içinde gelişen yakınlık. Gösterişli başlangıçlardan çok birikmiş ortak geçmişe inanıyorsun. Kitap güveni de böyle tarif eder: Tek bir jestten değil, farklı koşullarda gözlenen davranışların birikmesinden oluşan bir sermaye. Bedeli şu: Yavaş kurulan bir bağ, hızlı ilerlemek isteyen birine ilgisizlik gibi görünebilir.",
              "24"),
        "L": ("Ludus: Oyun",
              "Sen aşkı hafif, keyifli ve bağlayıcı olmayan bir oyun gibi yaşıyorsun. Lee bu tarza ludus der: Oyunsu ve düşük bağlılıklı ilişki tarzı. Seçeneklerin açık kalmasını seviyorsun. Bedeli şu: Kitaba göre bütün kapıları açık tutmanın da fırsat maliyeti var, çünkü partnerin de ilişkinin her an değiştirilebileceğini düşünüp aynı ölçüde yatırım yapmayabilir. Kitabın deyişiyle “Özgürlük, kapıyı kapatmanın kendi kararımız olmasıdır.”",
              "26"),
        "P": ("Pragma: Akıllı seçim",
              "Sen aşkı doğru ortağı seçmek olarak görüyorsun: Değerler, hedefler, hayat planı. Lee bu tarza pragma der: Pratik ve uyumluluk odaklı aşk. Bu soğukluk değil. Kitaba göre asıl mesele hangi konuda benzerliğin gerektiğini bilmektir: Müzik zevkindeki fark kolay yönetilir, çocuk isteğindeki zıtlık çok daha temel bir çatışma yaratabilir. Bedeli şu: Kitabın uyarısıyla romantik uyum, benzerlik sayısını topladığımız bir puan değildir.",
              "09"),
        "M": ("Mania: Yoğunluk",
              "Senin aşkın yoğun: Ya hep ya hiç. Mesaj gelmediğinde huzursuzlanıyor, belirsizlikte zorlanıyorsun. Lee bu tarza mania der ve kitap onu yoğun bağımlılık ve kıskançlıkla ilişkili bir aşk biçimi olarak tarif eder. Derin hissedebilmek bir zenginlik. Bedeli şu: Kitaba göre kıskançlığın varlığı ilişkinin değerli olduğunu gösterebilir, ama şiddeti sevginin miktarını ölçmez. Kitabın sorusu: Neyi kaybetmekten korkuyoruz?",
              "19"),
        "A": ("Agape: Vermek",
              "Senin için aşk karşılık beklemeden vermek. Sevdiğinin iyiliği seninkinden önce geliyor. Lee bu tarza agape der: Özgeci ve verici aşk. Kitap bu tarzların değişmez kişilik tipleri olmadığını da hatırlatır. Bedeli şu: Kitaba göre bakım iyi yapıldığında görünmez hâle gelebilir. Kitabın ölçüsü: Bir kişinin bakım vermeyi sevmesi, bu sorumluluğun sonsuza kadar yalnız ona ait olması gerektiği anlamına gelmez.",
              "16"),
    },
}

# 10 -----------------------------------------------------------------
ICERIK["birbirinizi-fiyatlamak"] = {
    "kanca": "Ayrı ayrı çözün, sonra ikinizin aynı şeylere ne kadar değer verdiğini karşılaştırın.",
    "sorular": [
        ("Bir akşam:", ["Evde baş başa", "Arkadaşlarla dışarıda"]),
        ("Beklenmedik bir para geldi:", ["Tatile", "Birikime"]),
        ("Tartışınca:", ["Hemen konuşalım", "Soğuyunca konuşalım"]),
        ("Sevgi en çok böyle gösterilir:", ["Sözle", "Davranışla"]),
        ("Yaşanacak yer:", ["Büyükşehir", "Sakin bir kasaba"]),
        ("Ortak giderler:", ["Yarı yarıya", "Gelire göre"]),
        ("Telefonlar:", ["Şifreler paylaşılır", "Herkesin kendi alanı"]),
        ("Bayram ve tatiller:", ["Ailelerle", "İkimiz"]),
        ("Gelecek:", ["Planlı", "Akışına"]),
        ("Ev işleri:", ["Görev listesiyle", "Kim müsaitse"]),
    ],
    "seviyeler": [
        (0, "Farklı fiyat listeleri",
         "Neredeyse her konuda farklı şeylere değer veriyorsunuz. Bu bir hüküm değil. Kitaba göre aşk piyasasında eşleşme iki ayrı tercih sıralamasının kesişmesidir ve sizin kesişim alanınız bu on maddede dar görünüyor. Farklı cevap verdiğiniz maddeler, ikinizin de bakmaya değer bulabileceği bir harita."),
        (3, "Farklı para birimleri",
         "Bazı konularda aynı, bazılarında farklı şeylere değer veriyorsunuz. Kitabın para bölümündeki örnek size tanıdık gelebilir: Bir eş için tasarruf güvenlik, diğeri için yaşamın ertelenmesi olabilir. Ayrıldığınız maddeler belki tercihten çok, aynı şeye yüklediğiniz farklı anlamdan doğuyor."),
        (6, "Yakın kur",
         "Çoğu konuda aynı şeylere değer veriyorsunuz. Kitaba göre romantik uyum, benzerlik sayısını topladığımız bir puan değildir. Asıl soru, ayrıldığınız maddelerin hangisinin müzik zevki gibi kolay yönetilir, hangisinin çocuk isteği gibi temel olduğu."),
        (9, "Aynı fiyat listesi",
         "Neredeyse her şeyi aynı biçimde değerlendiriyorsunuz. Yine de kitap bir şeyi hatırlatır: Aşk piyasası vardır, ama sevgilinin fiyat etiketi yoktur. Bugünkü örtüşme yarını garanti etmez. Kitaba göre insan farklı yaşlarda aynı partner özelliklerine aynı ağırlığı vermek zorunda değildir."),
    ],
    "bolum": "05",
}
