        # [InlineKeyboardButton(text="Jadvalni to'ldirish➕", callback_data="jadval")],
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

inline_menu = InlineKeyboardMarkup(
    inline_keyboard= [

    [InlineKeyboardButton(text="Mahsulot joylash📥",callback_data="sotish"),
    InlineKeyboardButton(text="Mahsulot olish🛍",url="https://t.me/kompyuterlar_savdosi_bot"),]]
    
)

# link_b = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [InlineKeyboardButton(text="Kanal 📣", url="https://t.me/kompyuterlar_savdosi_bot")],
#         [InlineKeyboardButton(text="🔙Orqaga", callback_data="orqaga")]
#     ]
# )


sinf = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🧸 Bolalar dunyosi", callback_data="bola"),InlineKeyboardButton(text="🔑 Ko'chmas mulk", callback_data="mulk")],  
        [InlineKeyboardButton(text="🚘 Transport", callback_data="transport"),InlineKeyboardButton(text="💼 Ish", callback_data="ish")],
        [InlineKeyboardButton(text="🐶 Hayvonlar", callback_data="hayvon"),InlineKeyboardButton(text="🪑 Uy va bog'", callback_data="uybog")],     
        [InlineKeyboardButton(text="📱 Elektr jihozlari", callback_data="elektrjihoz"),InlineKeyboardButton(text="🔨 Xizmatlar", callback_data="xizmat")],    
        [InlineKeyboardButton(text="👗 Moda va stil", callback_data="modavastil"),InlineKeyboardButton(text="🆓 Tekinga berish", callback_data="tekingaberish")],    
        [InlineKeyboardButton(text="🔙Orqaga", callback_data="orqagami")]
    ]
)
    

# buyurtma = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [InlineKeyboardButton(text="🔙Orqaga", callback_data="orqaga")]
#     ]
# )

bolalar = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🩳 Bolalar kiyimi", callback_data="bolakiyimi"),InlineKeyboardButton(text="🛏 Bolalar mebeli", callback_data="bolamebeli")],  
        [InlineKeyboardButton(text="🧸 O'yinchoqlar", callback_data="uyinchoqlar"),InlineKeyboardButton(text="👟 Bolalar oyoq kiyimi", callback_data="bolaoyoqkiyim")],
        [InlineKeyboardButton(text="Boshqa bolalar mahsuloti", callback_data="bolamahsulot"),InlineKeyboardButton(text="Bolalar kolyaskasi", callback_data="bolakolyaska")],
        [InlineKeyboardButton(text="🚲 Bolalar transporti", callback_data="bolatransporti"),InlineKeyboardButton(text="🍽 Oziqlantirish", callback_data="oziqlantirish")],
        [InlineKeyboardButton(text="🏫 Maktab o'quvchilari uchun mahsulotlar",callback_data="bolamaktab"),],


        [InlineKeyboardButton(text="🔙Orqaga", callback_data="orqaga")]
    ]
)


mulk = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🕒 Sutkalik ijarasi", callback_data="sutijarasi"),InlineKeyboardButton(text="🏘 Kvartira", callback_data="kvartira")], 
        [InlineKeyboardButton(text="🏢 Xususiy uylar", callback_data="xususiyuylar"),InlineKeyboardButton(text="🏡 Yer uchastkasi", callback_data="yeruchastkasi")], 
        [InlineKeyboardButton(text="🏗 Garajlar / Turargohlar", callback_data="garaj|turargoh"),InlineKeyboardButton(text="🏬 Tijorat binolari", callback_data="tijoratbino")], 
        [InlineKeyboardButton(text="🔙Orqaga", callback_data="orqaga")]
    ]
)


avto = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🚗 Yengil avtomashinalar", callback_data="yengilavto"),InlineKeyboardButton(text="🏍 Moto", callback_data="moto")], 
        [InlineKeyboardButton(text="🛸 Boshqa transport", callback_data="boshqatransport"),InlineKeyboardButton(text="🚌 Avtobuslar", callback_data="avtobuslar")], 
        [InlineKeyboardButton(text="🚚 Yuk mashinalari", callback_data="yukmashinalari"),InlineKeyboardButton(text="🚋 Tirkamalar", callback_data="tirkamalar")], 
        [InlineKeyboardButton(text="🛻 Maxsus texnika", callback_data="maxsustexnika"),InlineKeyboardButton(text="🚜 Qishloq xo'jalik texnikasi", callback_data="qishloqavto")], 
        [InlineKeyboardButton(text="🛠 Boshqa ehtiyot qismlar", callback_data="boshqaqismlar"),InlineKeyboardButton(text="🛥 Suvtransporti", callback_data="suvtransporti")], 
        [InlineKeyboardButton(text="⚙️ Maxsus texnika uchun qismlar",callback_data="maxsustexnikaqismlari"),],
        [InlineKeyboardButton(text="🛞 Shinalar, disklar va g'ildirakla",callback_data="shina"),],
        [InlineKeyboardButton(text="🔙Orqaga", callback_data="orqaga")]
    ]
)

ish = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🛍 Chakana savdo-sotuvlar",callback_data="chakanasavdo")],
        [InlineKeyboardButton(text="🏭 Ishlab chiqarish-energetika",callback_data="ishlabchiqarish")],
        [InlineKeyboardButton(text="👩🏻‍🍳|🧑🏻‍🍳 Barlar-restoranlar",callback_data="barrestoranlar")],
        [InlineKeyboardButton(text="🚛Transport / 📍logistika / 🗄ombor",callback_data="transportlogistikaombor")],
        [InlineKeyboardButton(text="🧑🏻‍🏭 Qurilish",callback_data="qurilish")],
        [InlineKeyboardButton(text="🚐Xizmat ko'rsatish / 🧽tozalash ishlari",callback_data="xizmattozalash")],
        [InlineKeyboardButton(text="👩🏻‍🏫 Ta'lim",callback_data="talim"),InlineKeyboardButton(text="🤵🏻‍♀️ Uy xodimlari",callback_data="uyxodimi")],
        [InlineKeyboardButton(text="🔙Orqaga", callback_data="orqaga")]
    ]
)

hayvonlar = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🐶 Itlar", callback_data="itlar"),InlineKeyboardButton(text="🐱 Mushuklar", callback_data="mushuklar")], 
        [InlineKeyboardButton(text="🐟 Akvarium baliqlari", callback_data="akvariumbaliqlari"),InlineKeyboardButton(text="🐦 Qushlar", callback_data="qushlar")], 
        [InlineKeyboardButton(text="🪱 Kemiruvchi", callback_data="kemiruvchi"),InlineKeyboardButton(text="🐻‍❄️ To'qish", callback_data="toqish")], 
        [InlineKeyboardButton(text="📦 Topilmalar idorasi", callback_data="topilmalaridorasi"),InlineKeyboardButton(text="🦆 Boshqa hayvonlar", callback_data="boshqahayvonlar")], 
        [InlineKeyboardButton(text="🆓🐶 Tekinga hayvonlar", callback_data="tekingahayvonlar"),InlineKeyboardButton(text="🐮 Qishloq xo'jalik hayvonlari", callback_data="qishloqxojalikhayvonlari")], 
        [InlineKeyboardButton(text="🍗 Hayvonlar uchun mahsulotlar",callback_data="hayvonlaruchunmahsulotlar"),],
        [InlineKeyboardButton(text="🔙Orqaga", callback_data="orqaga")]
    ]
)

uyvabog = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🛏 Mebel", callback_data="mebel"),InlineKeyboardButton(text="🏕 Bog'-tomorqa", callback_data="bogtomorqa")], 
        [InlineKeyboardButton(text="🛋Interyer jihozlari", callback_data="interyerjihozlari"),InlineKeyboardButton(text="🚪 Jihozlar", callback_data="jihozlar")], 
        [InlineKeyboardButton(text="Xona o'simliklari", callback_data="xonaosimliklari"),InlineKeyboardButton(text="Bog' anjomlari", callback_data="boganjomlari")], 
        [InlineKeyboardButton(text="Oziq-ovqat / Ichimliklar", callback_data="oziqovqatichimliklar"),InlineKeyboardButton(text="Uy uchun boshqa mahsulotlar", callback_data="uyuchunboshqamahsulotlar")], 
        [InlineKeyboardButton(text="🍴 Idish-tovoq, oshxona anjomlari",callback_data="idishtovoqoshxonaanjomlari"),],
        [InlineKeyboardButton(text="Qurilish/ta‘mirlash uchun tovarlar",callback_data="qurilishtamirlashuchuntovarlar"),],
        [InlineKeyboardButton(text="Kanstovarlar-chiqim materiallari",callback_data="kanstovarlarchiqimmateriallari"),],
        [InlineKeyboardButton(text="🔙Orqaga", callback_data="orqaga")]
    ]
)

elektirjihoz = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="📱 Telefonlar", callback_data="telefonlar"),InlineKeyboardButton(text="Kompyuterlar", callback_data="kompyuterlar")],
        [InlineKeyboardButton(text="📹 Foto/ video", callback_data="fotovideo"),InlineKeyboardButton(text="Tv/ videotexnika", callback_data="tvvideotexnika")], 
        [InlineKeyboardButton(text="🎙 Audiotexnika", callback_data="audiotexnika"),InlineKeyboardButton(text="Boshqa elektronika", callback_data="boshqaelektronika")], 
        [InlineKeyboardButton(text="Uy uchun texnika", callback_data="uyuchuntexnika"),InlineKeyboardButton(text="Oshxona uchun texnika", callback_data="oshxonauchuntexnika")], 
        [InlineKeyboardButton(text="Iqlim qurilmalari", callback_data="iqlimqurilmalari"),InlineKeyboardButton(text="Yakka tartibdagi parvarish", callback_data="yakkatartibdagiparvarish")], 
        [InlineKeyboardButton(text="O'yinlar va o'yin anjomlari", callback_data="oyinlarvaoyinanjomlari"),],
        [InlineKeyboardButton(text="Aksessuarlar va komplekt jihozlar",callback_data="aksessuarlarvakomplektjihozlar"),], 
        [InlineKeyboardButton(text="🔙Orqaga", callback_data="orqaga")]
    ]
)



xizmatlar = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Ta'lim-sport", callback_data="talimsport"),InlineKeyboardButton(text="Turizm", callback_data="turizm")],
        [InlineKeyboardButton(text="Yuridik xizmatlar", callback_data="yuridikxizmatlar"),InlineKeyboardButton(text="Moliya xizmatlari", callback_data="moliyaxizmatlari")],
        [InlineKeyboardButton(text="Xomashyo-materiallar", callback_data="xomashyomateriallar"),InlineKeyboardButton(text="Hayvonlar uchun xizmatlar", callback_data="hayvonlaruchunxizmatlar")],
        [InlineKeyboardButton(text="Mahsulotlar prokati", callback_data="mahsulotlarprokati"),InlineKeyboardButton(text="Tashishlar-transport ijarasi", callback_data="tashishlartransportijarasi")],
        [InlineKeyboardButton(text="Go'zallik-salomatlik", callback_data="gozalliksalomatlik"),InlineKeyboardButton(text="Biznesni sotish", callback_data="biznesnisotish")],
        [InlineKeyboardButton(text="Avto-moto xizmatlar", callback_data="avtomotoxizmatlar"),InlineKeyboardButton(text="Boshqa xizmatlar", callback_data="boshqaxizmatlar")],
        [InlineKeyboardButton(text="Qurilmalar", callback_data="qurilmalar"),InlineKeyboardButton(text="O'yinlar-san'at-foto-video", callback_data="oyinlarsanatfotovideo")],
        [InlineKeyboardButton(text="Qurilish-ta'mirlash-xona tozalash",callback_data="qurilishtamirlashxonatozalash"),], 
        [InlineKeyboardButton(text="Enagalar-kasalga qarovchilar",callback_data="enagalarkasalgaqarovchilar"),], 
        [InlineKeyboardButton(text="Tarjimonlar xizmatlari-matnlarni terish",callback_data="tarjimonlarxizmatlarimatnlarniterish"),], 
        [InlineKeyboardButton(text="Reklama, poligrafiya, marketing, internet",callback_data="reklamapoligrafiyamarketinginternet"),], 
        [InlineKeyboardButton(text="Texnikaga xizmat ko'rsatish, ta'mirlash",callback_data="texnikagaxizmatkorsatishtamirlash"),], 
        [InlineKeyboardButton(text="🔙Orqaga", callback_data="orqaga")]
    ]
)


modavastil = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Kiyim-kechak", callback_data="kiyimkechak"),InlineKeyboardButton(text="To'y uchun", callback_data="Toyuchun")],
        [InlineKeyboardButton(text="Moda, turli-tumanliklar", callback_data="modaturlitumanliklar"),InlineKeyboardButton(text="Qo'l soatlari", callback_data="qolsoatlari")],
        [InlineKeyboardButton(text="Aksessuarlar", callback_data="aksessuarlar"),InlineKeyboardButton(text="Sovg'alar", callback_data="sovgalar")],
        [InlineKeyboardButton(text="Go'zallik-salomatlik",callback_data="gozalliksalomatlik"),], 
        [InlineKeyboardButton(text="🔙Orqaga", callback_data="orqaga")]
    ]
)













# inli1ne_menu = InlineKeyboardMarkup(
#     inline_keyboard= [

#     [InlineKeyboardButton(text="Andijon",callback_data="andijon"),
#     InlineKeyboardButton(text="Buxoro",callback_data="buxoro"),],
#     [InlineKeyboardButton(text="Farg'ona",callback_data="fargona"),
#     InlineKeyboardButton(text="Jizzax",callback_data="jizzax"),],
#     [InlineKeyboardButton(text="Xorazm",callback_data="xorazm"),
#     InlineKeyboardButton(text="Namangan",callback_data="namangan"),],
#     [InlineKeyboardButton(text="Navoiy",callback_data="navoiy"),
#     InlineKeyboardButton(text="Qashqadaryo",callback_data="qashqadaryo"),],
#     [InlineKeyboardButton(text="Qoraqalpog'iston",callback_data="qoraqalpogiston"),
#     InlineKeyboardButton(text="Samarqand",callback_data="samarqand"),],    
#     [InlineKeyboardButton(text="Sirdaryo",callback_data="sirdaryo"),
#     InlineKeyboardButton(text="Surxondaryo",callback_data="surxondaryo"),],   
#     [InlineKeyboardButton(text="Toshkent",callback_data="toshkent"),]]
# )

