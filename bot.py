from aiogram.enums import ParseMode
from aiogram import Bot,Dispatcher
from aiogram.filters import CommandStart,Command
from aiogram import F
from aiogram.types import Message,CallbackQuery
from data import config
import asyncio
import logging
import sys
import sqlite3
from menucommands.set_bot_commands  import set_default_commands
from baza.sqlite import Database
from filters.admin import IsBotAdminFilter
from filters.check_sub_channel import IsCheckSubChannels
from keyboard_buttons import admin_keyboard, keyboard_button
from aiogram.fsm.context import FSMContext
from middlewares.throttling import ThrottlingMiddleware #new
from states.reklama import Adverts, Users, Info
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from buttonlar import inline_menu,sinf,bolalar,mulk,avto,ish,hayvonlar,uyvabog,elektirjihoz,xizmatlar,modavastil
import time 
import re 
from keyboard_buttons.phonenum import phone
from aiogram.types import ReplyKeyboardRemove

#salom

ADMINS = config.ADMINS
TOKEN = config.BOT_TOKEN
CHANNELS = config.CHANNELS
ADMINS_GROUP = config.ADMINS_GROUP

dp = Dispatcher()



@dp.message(CommandStart())
async def start_command(message: Message, state: FSMContext):
    telegram_id = message.from_user.id
    user = db.get_user(telegram_id=telegram_id)
    
    if user is None:
        await message.answer("Assalomu alaykum, Ismingizni kiriting")
        await state.set_state(Users.first_name)
    else:
        await message.answer("Bizning kompyuter savdo botimizga xush kelibsiz💻", reply_markup=inline_menu)

@dp.message(Command("admin"),IsBotAdminFilter(ADMINS))
async def is_admin(message:Message):
    await message.answer(text="Admin menu",reply_markup=admin_keyboard.admin_button)


@dp.message(F.text=="Foydalanuvchilar soni",IsBotAdminFilter(ADMINS))
async def users_count(message:Message):
    counts = db.count_users()
    text = f"Botimizda {counts[0]} ta foydalanuvchi bor"
    await message.answer(text=text)

@dp.message(F.text=="Reklama yuborish",IsBotAdminFilter(ADMINS))
async def advert_dp(message:Message,state:FSMContext):
    await state.set_state(Adverts.adverts)
    await message.answer(text="Reklama yuborishingiz mumkin !")

@dp.message(Adverts.adverts)
async def send_advert(message:Message,state:FSMContext):
    
    message_id = message.message_id
    from_chat_id = message.from_user.id
    users = db.all_users_id()
    count = 0
    for user in users:
        try:
            await bot.copy_message(chat_id=user[0],from_chat_id=from_chat_id,message_id=message_id)
            count += 1
        except:
            pass
        time.sleep(0.01)
    
    await message.answer(f"Reklama {count}ta foydalanuvchiga yuborildi")
    await state.clear()




#-----------------------------------------------------------------


@dp.message(Users.first_name)
async def get_first_name(message: Message, state: FSMContext):
    pattern = "^[A-z0-9_-]{3,15}$"
    if re.match(pattern, message.text):
        first_name = message.text
        await state.update_data(first_name=first_name)
        await state.set_state(Users.phone_number)
        await message.answer("Raqamingizni kiriting", reply_markup=phone)
    else:
        await message.answer("Iltimos, ismingizni to'g'ri kiriting")



@dp.message(Users.phone_number)
async def get_phone_number(message: Message, state: FSMContext):
    phone_number = message.contact.phone_number
    print(phone_number)
    data = await state.get_data()
    full_name = data.get("first_name")
    telegram_id = message.from_user.id
    
    db.add_user(full_name=full_name, telegram_id=telegram_id, phone_number=phone_number)
    
#-----------------------------------------------------------------------viloyat-------------------------




#-----------------------------------------viloyat-------------------------------viloyat----------------------


#     await state.set_state(Users.age)
#     text = f"Yoshingizni kiriting!"
#     await message.reply(text=text)
    
#     # else:
#     #     await message.reply(text="telefon nomeringizni noto'g'ri kiritdingiz")


# @dp.message(Users.age)
# async def age(message: Message, state: FSMContext):
    # data = await state.get_data()    
    # id = message.from_user.id3
    # my_photo = data.get("photo") 
    # first_name = data.get("first_name")
    # last_name = data.get("last_name")
    # phone_number = data.get("phone_number")
    # address = data.get("address")
    # email = data.get("email")
    # photo = data.get("photo")
    # country = data.get("country")
    # city = data.get("city")
    # planet = data.get("city")
    # house_number = data.get("house_number")

    # text = f"<b>Ariza</b>\nIsmi: {first_name}\nFamilyasi: {last_name}\nTel: {phone_number}\nManzil: {address}\nGmail: {email}\nMamalakat: {country}\nShahar: {city}\nSayyora: {planet}\nUy raqami: {house_number}"
    print('salom dunyo!!!!!!!')
    

    # await bot.send_photo(ADMINS[0],photo=my_photo,caption=text)
    # print(first_name,last_name,phone_number,address,)
    

    await state.clear()
    text = f"Siz muvaffaqiyatli tarzda ro'yhatdan o'tdingiz🎉"
    await message.answer(text=text, reply_markup=ReplyKeyboardRemove())

    await message.answer('Siz asosiy menudasiz', reply_markup=inline_menu)
#1-1-1-1-1--1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1--1-1-1-1-1-1-1-1-1--1-1-1-1-1-1-1-1-1-1--1-1-1-1-1-1-1-1-1--1-1-1-1

# @dp.callback_query(F.data=="buyurtma")
# async def buyurtma(callback:CallbackQuery):
#     text = "Hozircha sizda buyurtmalar yo'q"
#     # await callback.message.delete()
#     await callback.message.answer(text = text, reply_markup=buyurtma)


# @dp.callback_query(F.data=="sotibolish")
# async def sotibolish(callback:CallbackQuery):
#     text = "Kompyuterni sotib olmoqchi bo'lsangiz ushbu kanaldan sotib olishingiz mumkin\n\n👇👇👇"
#     await callback.message.delete()
#     await callback.message.answer(text = text, reply_markup=link_b)

# @dp.callback_query(F.data=="kanal")

@dp.callback_query(F.data=="sotish")
async def sotish(callback:CallbackQuery):
    text = "Sinf"
    # await callback.message.delete()
    await callback.message.edit_text(text=text,reply_markup=sinf)

@dp.callback_query(F.data=="bola")
async def sotish(callback:CallbackQuery, state: FSMContext):
    text = "Bolalar dunyosi"
    await state.update_data(heshteg = "Bolalar_dunyosi")
    await callback.message.edit_text(text=text,reply_markup=bolalar)

@dp.callback_query(F.data=="orqaga")
async def orqaga(callback:CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text = 'Siz sinfdasiz', reply_markup=sinf)

@dp.callback_query(F.data=="mulk")
async def sotish(callback:CallbackQuery, state: FSMContext):
    text = "Bolalar dunyosi"
    await state.update_data(heshteg = "Mulk")
    await callback.message.edit_text(text=text,reply_markup=mulk)

@dp.callback_query(F.data=="transport")
async def sotish(callback:CallbackQuery, state: FSMContext):
    text = "Transportlar"
    await state.update_data(heshteg = "Transportlar")
    await callback.message.edit_text(text=text,reply_markup=avto)

@dp.callback_query(F.data=="orqagami")
async def orqaga(callback:CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text = 'Siz asosiy menudasiz', reply_markup=inline_menu)

@dp.callback_query(F.data=="ish")
async def sotish(callback:CallbackQuery, state: FSMContext):
    text = "Ish"
    await state.update_data(heshteg = "Ish")
    await callback.message.edit_text(text=text,reply_markup=ish)



@dp.callback_query(F.data=="hayvon")
async def sotish(callback:CallbackQuery, state: FSMContext):
    text = "Hayvonlar"
    await state.update_data(heshteg = "Hayvonlar")
    await callback.message.edit_text(text=text,reply_markup=hayvonlar)

@dp.callback_query(F.data=="uybog")
async def sotish(callback:CallbackQuery, state: FSMContext):
    text = "Uy va bog'"
    await state.update_data(heshteg = "Uy_va_bog")
    await callback.message.edit_text(text=text,reply_markup=uyvabog)

@dp.callback_query(F.data=="elektrjihoz")
async def sotish(callback:CallbackQuery, state: FSMContext):
    text = "Elektir Jihoz"
    await state.update_data(heshteg = "Elektir_jihozlar'")
    await callback.message.edit_text(text=text,reply_markup=elektirjihoz)

@dp.callback_query(F.data=="xizmat")
async def sotish(callback:CallbackQuery, state: FSMContext):
    text = "Xizmatlar"
    await state.update_data(heshteg = "Xizmatlar")
    await callback.message.edit_text(text=text,reply_markup=xizmatlar)

@dp.callback_query(F.data=="modavastil")
async def sotish(callback:CallbackQuery, state: FSMContext):
    text = "Moda va Still"
    await state.update_data(heshteg = "Moda_va_Still")
    await callback.message.edit_text(text=text,reply_markup=modavastil)
#________________________________________________jadval________________________-------------------------------------------------------------
@dp.callback_query(F.data=="bolakiyimi")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await callback.message.answer(text= "Rasmini yuboring")
    await state.update_data(heshtegim = "Bolalar_kiyimi")
    await state.set_state(Info.pic)

@dp.callback_query(F.data=="uyinchoqlar")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await state.update_data(heshtegim = "Uyinchoqlar")
    await callback.message.answer(text= "Rasmini yuboring")
    await state.set_state(Info.pic)

@dp.callback_query(F.data=="bolamahsulot")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await state.update_data(heshtegim = "Boshqa_bolalar_mahsuloti")
    await callback.message.answer(text= "Rasmini yuboring")
    await state.set_state(Info.pic)

@dp.callback_query(F.data=="bolatransporti")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await state.update_data(heshtegim = "Bolalar_transporti")
    await callback.message.answer(text= "Rasmini yuboring")
    await state.set_state(Info.pic)

@dp.callback_query(F.data=="bolamaktab")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await state.update_data(heshtegim = "Maktab_oquvchilari_uchun_mahsulotlar")
    await callback.message.answer(text= "Rasmini yuboring")
    await state.set_state(Info.pic)

@dp.callback_query(F.data=="bolamebeli")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await state.update_data(heshtegim = "Bolalar_mebeli")
    await callback.message.answer(text= "Rasmini yuboring")
    await state.set_state(Info.pic)

@dp.callback_query(F.data=="bolaoyoqkiyim")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await state.update_data(heshtegim = "Bolalar_oyoq_kiyimi")
    await callback.message.answer(text= "Rasmini yuboring")
    await state.set_state(Info.pic)

@dp.callback_query(F.data=="bolakolyaska")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await state.update_data(heshtegim = "Bolalar_kolyaskasi")
    await callback.message.answer(text= "Rasmini yuboring")
    await state.set_state(Info.pic)

@dp.callback_query(F.data=="oziqlantirish")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await state.update_data(heshtegim = "Oziqlantirish")
    await callback.message.answer(text= "Rasmini yuboring")
    await state.set_state(Info.pic)

@dp.callback_query(F.data=="sutijarasi")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await state.update_data(heshtegim = "Sutkalik_ijarasi")
    await callback.message.answer(text= "Rasmini yuboring")
    await state.set_state(Info.pic)

@dp.callback_query(F.data=="xususiyuylar")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await state.update_data(heshtegim = "Xususiy_uylar")
    await callback.message.answer(text= "Rasmini yuboring")
    await state.set_state(Info.pic)

@dp.callback_query(F.data=="garaj|turargoh")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await state.update_data(heshtegim = "Garajlar_Turargohlar")
    await callback.message.answer(text= "Rasmini yuboring")
    await state.set_state(Info.pic)

@dp.callback_query(F.data=="kvartira")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await state.update_data(heshtegim = "Kvartira")
    await callback.message.answer(text= "Rasmini yuboring")
    await state.set_state(Info.pic)

@dp.callback_query(F.data=="yeruchastkasi")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await state.update_data(heshtegim = "Yer_uchastkasi")
    await callback.message.answer(text= "Rasmini yuboring")
    await state.set_state(Info.pic)

@dp.callback_query(F.data=="tijoratbino")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await state.update_data(heshtegim = "Tijorat_binolari")
    await callback.message.answer(text= "Rasmini yuboring")
    await state.set_state(Info.pic)

@dp.callback_query(F.data=="yengilavto")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await state.update_data(heshtegim = "Yengil_avtomashinalar")
    await callback.message.answer(text= "Rasmini yuboring")
    await state.set_state(Info.pic)

@dp.callback_query(F.data=="boshqatransport")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await state.update_data(heshtegim = "Boshqa_transport")
    await callback.message.answer(text= "Rasmini yuboring")
    await state.set_state(Info.pic)

@dp.callback_query(F.data=="yukmashinalari")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await state.update_data(heshtegim = "Yuk_mashinalari")
    await callback.message.answer(text= "Rasmini yuboring")
    await state.set_state(Info.pic)

@dp.callback_query(F.data=="maxsustexnika")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await state.update_data(heshtegim = "Maxsus_texnika")
    await callback.message.answer(text= "Rasmini yuboring")
    await state.set_state(Info.pic)

@dp.callback_query(F.data=="boshqaqismlar")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await state.update_data(heshtegim = "Boshqa_ehtiyot_qismlar")
    await callback.message.answer(text= "Rasmini yuboring")
    await state.set_state(Info.pic)

@dp.callback_query(F.data=="maxsustexnikaqismlari")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await state.update_data(heshtegim = "Maxsus_texnika_uchun_qismlar")
    await callback.message.answer(text= "Rasmini yuboring")
    await state.set_state(Info.pic)

@dp.callback_query(F.data=="shina")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await state.update_data(heshtegim = "Shinalar_disklar_va_gildirakla")
    await callback.message.answer(text= "Rasmini yuboring")
    await state.set_state(Info.pic)

@dp.callback_query(F.data=="moto")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await state.update_data(heshtegim = "Moto")
    await callback.message.answer(text= "Rasmini yuboring")
    await state.set_state(Info.pic)

@dp.callback_query(F.data=="avtobuslar")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await state.update_data(heshtegim = "Avtobuslar")
    await callback.message.answer(text= "Rasmini yuboring")
    await state.set_state(Info.pic)

@dp.callback_query(F.data=="tirkamalar")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await state.update_data(heshtegim = "Tirkamalar")
    await callback.message.answer(text= "Rasmini yuboring")
    await state.set_state(Info.pic)

@dp.callback_query(F.data=="qishloqavto")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await state.update_data(heshtegim = "Qishloq_xojalik_texnikasi")
    await callback.message.answer(text= "Rasmini yuboring")
    await state.set_state(Info.pic)

@dp.callback_query(F.data=="suvtransporti")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await state.update_data(heshtegim = "Suvtransporti")
    await callback.message.answer(text= "Rasmini yuboring")
    await state.set_state(Info.pic)

@dp.callback_query(F.data=="chakanasavdo")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await state.update_data(heshtegim = "Chakana_savdo_sotuvlar")
    await callback.message.answer(text= "Rasmini yuboring")
    await state.set_state(Info.pic)

@dp.callback_query(F.data=="ishlabchiqarish")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await state.update_data(heshtegim = "Ishlab_chiqarish_energetika")
    await callback.message.answer(text= "Rasmini yuboring")
    await state.set_state(Info.pic)

@dp.callback_query(F.data=="barrestoranlar")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await state.update_data(heshtegim = "Barlar_restoranlar")
    await callback.message.answer(text= "Rasmini yuboring")
    await state.set_state(Info.pic)

@dp.callback_query(F.data=="transportlogistikaombor")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await state.update_data(heshtegim = "Transport_logistika_ombor")
    await callback.message.answer(text= "Rasmini yuboring")
    await state.set_state(Info.pic)

@dp.callback_query(F.data=="qurilish")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await state.update_data(heshtegim = "Qurilish")
    await callback.message.answer(text= "Rasmini yuboring")
    await state.set_state(Info.pic)

@dp.callback_query(F.data=="xizmattozalash")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await state.update_data(heshtegim = "Xizmat_korsatish_tozalash_ishlari")
    await callback.message.answer(text= "Rasmini yuboring")
    await state.set_state(Info.pic)

@dp.callback_query(F.data=="talim")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await state.update_data(heshtegim = "Talim")
    await callback.message.answer(text= "Rasmini yuboring")
    await state.set_state(Info.pic)

@dp.callback_query(F.data=="uyxodimi")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await state.update_data(heshtegim = "Uy_xodimlari")
    await callback.message.answer(text= "Rasmini yuboring")
    await state.set_state(Info.pic)


@dp.callback_query(F.data=="itlar")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await state.update_data(heshtegim = "Itlar")
    await callback.message.answer(text= "Rasmini yuboring")
    await state.set_state(Info.pic)

@dp.callback_query(F.data=="akvariumbaliqlari")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await state.update_data(heshtegim = "Akvarium_baliqlari")
    await callback.message.answer(text= "Rasmini yuboring")
    await state.set_state(Info.pic)

@dp.callback_query(F.data=="kemiruvchi")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await state.update_data(heshtegim = "Kemiruvchi")
    await callback.message.answer(text= "Rasmini yuboring")
    await state.set_state(Info.pic)

@dp.callback_query(F.data=="topilmalaridorasi")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await state.update_data(heshtegim = "Topilmalar_idorasi")
    await callback.message.answer(text= "Rasmini yuboring")
    await state.set_state(Info.pic)

@dp.callback_query(F.data=="tekingahayvonlar")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await state.update_data(heshtegim = "Tekinga_hayvonlar")    
    await callback.message.answer(text= "Rasmini yuboring")
    await state.set_state(Info.pic)

@dp.callback_query(F.data=="hayvonlaruchunmahsulotlar")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await state.update_data(heshtegim = "Hayvonlar_uchun_mahsulotlar")
    await callback.message.answer(text= "Rasmini yuboring")
    await state.set_state(Info.pic)

@dp.callback_query(F.data=="mushuklar")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await state.update_data(heshtegim = "Mushuklar")
    await callback.message.answer(text= "Rasmini yuboring")
    await state.set_state(Info.pic)

@dp.callback_query(F.data=="qushlar")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await state.update_data(heshtegim = "Qushlar")
    await callback.message.answer(text= "Rasmini yuboring")
    await state.set_state(Info.pic)

@dp.callback_query(F.data=="toqish")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await state.update_data(heshtegim = "Toqish")
    await callback.message.answer(text= "Rasmini yuboring")
    await state.set_state(Info.pic)

@dp.callback_query(F.data=="boshqahayvonlar")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await state.update_data(heshtegim = "Boshqa_hayvonlar")
    await callback.message.answer(text= "Rasmini yuboring")
    await state.set_state(Info.pic)

@dp.callback_query(F.data=="qishloqxojalikhayvonlari")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await state.update_data(heshtegim = "Qishloq_xojalik_hayvonlari")
    await callback.message.answer(text= "Rasmini yuboring")
    await state.set_state(Info.pic)

@dp.callback_query(F.data=="mebel")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await state.update_data(heshtegim = "Mebel")
    await callback.message.answer(text= "Rasmini yuboring")
    await state.set_state(Info.pic)

@dp.callback_query(F.data=="interyerjihozlari")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await state.update_data(heshtegim = "Interyer_jihozlari")
    await callback.message.answer(text= "Rasmini yuboring")
    await state.set_state(Info.pic)

@dp.callback_query(F.data=="xonaosimliklari")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await state.update_data(heshtegim = "Xona_osimliklari")
    await callback.message.answer(text= "Rasmini yuboring")
    await state.set_state(Info.pic)

@dp.callback_query(F.data=="oziqovqatichimliklar")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await state.update_data(heshtegim = "Oziq_ovqat_Ichimliklar")
    await callback.message.answer(text= "Rasmini yuboring")
    await state.set_state(Info.pic)

@dp.callback_query(F.data=="idishtovoqoshxonaanjomlari")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await state.update_data(heshtegim = "Idish_tovoq_oshxona_anjomlari")
    await callback.message.answer(text= "Rasmini yuboring")
    await state.set_state(Info.pic)

@dp.callback_query(F.data=="qurilishtamirlashuchuntovarlar")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await state.update_data(heshtegim = "Qurilish_tamirlash_uchun_tovarlar")
    await callback.message.answer(text= "Rasmini yuboring")
    await state.set_state(Info.pic)

@dp.callback_query(F.data=="kanstovarlarchiqimmateriallari")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await state.update_data(heshtegim = "Kanstovarlar_chiqim_materiallari")
    await callback.message.answer(text= "Rasmini yuboring")
    await state.set_state(Info.pic)

@dp.callback_query(F.data=="bogtomorqa")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await state.update_data(heshtegim = "Bog_tomorqa")
    await callback.message.answer(text= "Rasmini yuboring")
    await state.set_state(Info.pic)

@dp.callback_query(F.data=="jihozlar")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await state.update_data(heshtegim = "Jihozlar")
    await callback.message.answer(text= "Rasmini yuboring")
    await state.set_state(Info.pic)

@dp.callback_query(F.data=="boganjomlari")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await state.update_data(heshtegim = "Bog_anjomlari")
    await callback.message.answer(text= "Rasmini yuboring")
    await state.set_state(Info.pic)

@dp.callback_query(F.data=="uyuchunboshqamahsulotlar")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await state.update_data(heshtegim = "Uy_uchun_boshqa_mahsulotlar")
    await callback.message.answer(text= "Rasmini yuboring")
    await state.set_state(Info.pic)

@dp.callback_query(F.data=="telefonlar")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await state.update_data(heshtegim = "Telefonlar")
    await callback.message.answer(text= "Rasmini yuboring")
    await state.set_state(Info.pic)

@dp.callback_query(F.data=="fotovideo")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await state.update_data(heshtegim = "Foto_video")
    await callback.message.answer(text= "Rasmini yuboring")
    await state.set_state(Info.pic)

@dp.callback_query(F.data=="audiotexnika")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await state.update_data(heshtegim = "Audiotexnika")
    await callback.message.answer(text= "Rasmini yuboring")
    await state.set_state(Info.pic)

@dp.callback_query(F.data=="uyuchuntexnika")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await state.update_data(heshtegim = "Uy_uchun_texnika")
    await callback.message.answer(text= "Rasmini yuboring")
    await state.set_state(Info.pic)

@dp.callback_query(F.data=="iqlimqurilmalari")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await state.update_data(heshtegim = "Iqlim_qurilmalari")
    await callback.message.answer(text= "Rasmini yuboring")
    await state.set_state(Info.pic)

@dp.callback_query(F.data=="oyinlarvaoyinanjomlari")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await state.update_data(heshtegim = "Oyinlar_va_oyin_anjomlari")
    await callback.message.answer(text= "Rasmini yuboring")
    await state.set_state(Info.pic)

@dp.callback_query(F.data=="aksessuarlarvakomplektjihozlar")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await state.update_data(heshtegim = "Aksessuarlar_va_komplekt_jihozlar")
    await callback.message.answer(text= "Rasmini yuboring")
    await state.set_state(Info.pic)

@dp.callback_query(F.data=="kompyuterlar")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await state.update_data(heshtegim = "Kompyuterlar")
    await callback.message.answer(text= "Rasmini yuboring")
    await state.set_state(Info.pic)

@dp.callback_query(F.data=="tvvideotexnika")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await state.update_data(heshtegim = "Tv_videotexnika")
    await callback.message.answer(text= "Rasmini yuboring")
    await state.set_state(Info.pic)

@dp.callback_query(F.data=="boshqaelektronika")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await state.update_data(heshtegim = "Boshqa_elektronika")
    await callback.message.answer(text= "Rasmini yuboring")
    await state.set_state(Info.pic)

@dp.callback_query(F.data=="yakkatartibdagiparvarish")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await state.update_data(heshtegim = "Yakka_tartibdagi_parvarish")
    await callback.message.answer(text= "Rasmini yuboring")
    await state.set_state(Info.pic)

@dp.callback_query(F.data=="oshxonauchuntexnika")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await state.update_data(heshtegim = "Oshxona_uchun_texnika")
    await callback.message.answer(text= "Rasmini yuboring")
    await state.set_state(Info.pic)

@dp.callback_query(F.data=="talimsport")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await state.update_data(heshtegim = "Talim_sport")
    await callback.message.answer(text= "Rasmini yuboring")
    await state.set_state(Info.pic)

@dp.callback_query(F.data=="yuridikxizmatlar")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await state.update_data(heshtegim = "Yuridik_xizmatlar")
    await callback.message.answer(text= "Rasmini yuboring")
    await state.set_state(Info.pic)

@dp.callback_query(F.data=="xomashyomateriallar")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await state.update_data(heshtegim = "Xomashyo_materiallar")
    await callback.message.answer(text= "Rasmini yuboring")
    await state.set_state(Info.pic)

@dp.callback_query(F.data=="mahsulotlarprokati")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await state.update_data(heshtegim = "Mahsulotlar_prokati")
    await callback.message.answer(text= "Rasmini yuboring")
    await state.set_state(Info.pic)

@dp.callback_query(F.data=="gozalliksalomatlik")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await state.update_data(heshtegim = "Gozallik_salomatlik")
    await callback.message.answer(text= "Rasmini yuboring")
    await state.set_state(Info.pic)

@dp.callback_query(F.data=="avtomotoxizmatlar")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await state.update_data(heshtegim = "Avto_moto_xizmatlar")
    await callback.message.answer(text= "Rasmini yuboring")
    await state.set_state(Info.pic)

@dp.callback_query(F.data=="qurilmalar")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await state.update_data(heshtegim = "Qurilmalar")
    await callback.message.answer(text= "Rasmini yuboring")
    await state.set_state(Info.pic)

@dp.callback_query(F.data=="qurilishtamirlashxonatozalash")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await state.update_data(heshtegim = "Qurilish_tamirlash_xona_tozalash")
    await callback.message.answer(text= "Rasmini yuboring")
    await state.set_state(Info.pic)

@dp.callback_query(F.data=="enagalarkasalgaqarovchilar")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await state.update_data(heshtegim = "Enagalar_kasalga_qarovchilar")
    await callback.message.answer(text= "Rasmini yuboring")
    await state.set_state(Info.pic)

@dp.callback_query(F.data=="tarjimonlarxizmatlarimatnlarniterish")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await state.update_data(heshtegim = "Tarjimonlar_xizmatlari_atnlarni_terish")
    await callback.message.answer(text= "Rasmini yuboring")
    await state.set_state(Info.pic)

@dp.callback_query(F.data=="reklamapoligrafiyamarketinginternet")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await state.update_data(heshtegim = "Reklama_poligrafiya_marketing_internet")
    await callback.message.answer(text= "Rasmini yuboring")
    await state.set_state(Info.pic)

@dp.callback_query(F.data=="texnikagaxizmatkorsatishtamirlash")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await state.update_data(heshtegim = "Texnikaga_xizmat_korsatish_tamirlash")
    await callback.message.answer(text= "Rasmini yuboring")
    await state.set_state(Info.pic)

@dp.callback_query(F.data=="turizm")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await state.update_data(heshtegim = "Turizm")
    await callback.message.answer(text= "Rasmini yuboring")
    await state.set_state(Info.pic)

@dp.callback_query(F.data=="moliyaxizmatlari")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await state.update_data(heshtegim = "Jihozlar")
    await callback.message.answer(text= "Rasmini yuboring")
    await state.set_state(Info.pic)

@dp.callback_query(F.data=="hayvonlaruchunxizmatlar")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await state.update_data(heshtegim = "Hayvonlar_uchun_xizmatlar")
    await callback.message.answer(text= "Rasmini yuboring")
    await state.set_state(Info.pic)

@dp.callback_query(F.data=="tashishlartransportijarasi")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await state.update_data(heshtegim = "Tashishlar_transport_ijarasi")
    await callback.message.answer(text= "Rasmini yuboring")
    await state.set_state(Info.pic)

@dp.callback_query(F.data=="biznesnisotish")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await state.update_data(heshtegim = "Biznesni_sotish")
    await callback.message.answer(text= "Rasmini yuboring")
    await state.set_state(Info.pic)

@dp.callback_query(F.data=="boshqaxizmatlar")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await state.update_data(heshtegim = "Boshqa_xizmatlar")
    await callback.message.answer(text= "Rasmini yuboring")
    await state.set_state(Info.pic)

@dp.callback_query(F.data=="oyinlarsanatfotovideo")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await state.update_data(heshtegim = "Oyinlar_sanat_foto_video")
    await callback.message.answer(text= "Rasmini yuboring")
    await state.set_state(Info.pic)

@dp.callback_query(F.data=="kiyimkechak")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await state.update_data(heshtegim = "Kiyim_kechak")
    await callback.message.answer(text= "Rasmini yuboring")
    await state.set_state(Info.pic)

@dp.callback_query(F.data=="modaturlitumanliklar")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await state.update_data(heshtegim = "Moda_turli_tumanliklar")
    await callback.message.answer(text= "Rasmini yuboring")
    await state.set_state(Info.pic)

@dp.callback_query(F.data=="aksessuarlar")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await state.update_data(heshtegim = "Aksessuarlar")
    await callback.message.answer(text= "Rasmini yuboring")
    await state.set_state(Info.pic)

@dp.callback_query(F.data=="gozalliksalomatlik")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await state.update_data(heshtegim = "Gozallik_salomatlik")
    await callback.message.answer(text= "Rasmini yuboring")
    await state.set_state(Info.pic)

@dp.callback_query(F.data=="Toyuchun")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await state.update_data(heshtegim = "Toy_uchun")
    await callback.message.answer(text= "Rasmini yuboring")
    await state.set_state(Info.pic)

@dp.callback_query(F.data=="qolsoatlari")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await state.update_data(heshtegim = "Qol_soatlari")
    await callback.message.answer(text= "Rasmini yuboring")
    await state.set_state(Info.pic)

@dp.callback_query(F.data=="sovgalar")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await state.update_data(heshtegim = "Sovgalar")
    await callback.message.answer(text= "Rasmini yuboring")
    await state.set_state(Info.pic)
#------------------------------------------------------------------

@dp.callback_query(F.data=="tekingaberish")
async def tekingaberish(callback:CallbackQuery, state:FSMContext):
    await callback.message.answer(text= "Rasmini yuboring")
    await state.set_state(Info.pic)

@dp.message(F.photo, Info.pic)
async def info_ads_pic(message: Message, state: FSMContext):
    pic = message.photo[-1].file_id
    await state.update_data(pic=pic)
    await message.answer("Ma'lumot kiriting!")
    await state.set_state(Info.model)

@dp.message(F.text, Info.model)
async def info_ads_model(message: Message, state: FSMContext):
    model = message.text
    await state.update_data(model=model)
    await message.answer("Xolatini kiriting")
    await state.set_state(Info.protsessor)

@dp.message(F.text, Info.protsessor)
async def info_ads_protsessor(message: Message, state: FSMContext):
    protsessor = message.text
    await state.update_data(protsessor=protsessor)
    await message.answer("Narxini kiriting")
    await state.set_state(Info.price)

@dp.message(F.text, Info.price)
async def info_ads_price(message: Message, state: FSMContext):
    price = message.text
    await state.update_data(price=price)
    await message.answer("☎️ Telefon raqamingizni kiriting!")
    await state.set_state(Info.phone_number)

@dp.message(F.text, Info.phone_number)
async def info_ads_phone_number(message: Message, state: FSMContext):
    phone_number = message.text
    await state.update_data(phone_number=phone_number)
    await message.answer("Manzilini kiriting!")
    await state.set_state(Info.location)

@dp.message(F.text, Info.location)
async def info_ads_location(message: Message, state: FSMContext):
    location = message.text
    data = await state.get_data()
    pic = data.get("pic")
    model = data.get("model")
    price = data.get("price")
    protsessor = data.get("protsessor")
    phone_number = data.get("phone_number")
    heshteg = data.get("heshteg")
    heshtegim = data.get("heshtegim")
    text = f"#{heshteg},\n#{heshtegim},\n#{location},\nTavsif: {model}\nXolati: {protsessor}\n💵 Narxi: {price}\n☎️ Telefon raqam: {phone_number}\n👤 Username: <a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a>"
    

    await bot.send_photo(chat_id=CHANNELS[0], photo=pic, caption=text, reply_markup=keyboard_button.confirmation, parse_mode='HTML')
    await message.answer("E'loningiz adminga yuborildi! \nAdmin ko'rib chiqib kanalga e'loningizni yuboradi.")
    await state.clear()



@dp.message(Info.location)
async def info_ads_location_del(message: Message):
    await message.answer(text="Manzilni to'g'ri kiriting!")
    await message.delete()

# Finish________________________________--jadval offff_____________________________________________________________________________________________________________________
@dp.callback_query(F.data=="False")
async def confirmation (callback_query: CallbackQuery):
    await callback_query.message.delete()
@dp.callback_query(F.data=="True")
async def confirmation (callback_query: CallbackQuery):
    rasm = callback_query.message.photo[-1].file_id
    text = callback_query.message.caption 
    await bot.send_photo(chat_id=ADMINS_GROUP[0], photo=rasm, caption=text)
    await callback_query.message.delete()







#--------------------
@dp.callback_query(F.data=="orqaga")
async def orqaga(callback:CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text = 'Siz asosiy menudasiz', reply_markup=inline_menu)







#-----------------------------------------------------------------------------------------1-1-1-1-1-1-1-1-1-1-1-1-1--1-1-1-1-1-1-1-1-1-1-1

@dp.startup()
async def on_startup_notify(bot: Bot):
    for admin in ADMINS:
        try:
            await bot.send_message(chat_id=int(admin),text="Bot ishga tushdi")
        except Exception as err:
            logging.exception(err)

#bot ishga tushganini xabarini yuborish
@dp.shutdown()
async def off_startup_notify(bot: Bot):
    for admin in ADMINS:
        try:
            await bot.send_message(chat_id=int(admin),text="Bot ishdan to'xtadi!")
        except Exception as err:
            logging.exception(err)



async def main() -> None:
    global bot,db
    bot = Bot(TOKEN)
    db = Database(path_to_db="main.db")
    db.create_table_users()
    await set_default_commands(bot)
    dp.message.middleware(ThrottlingMiddleware(slow_mode_delay=0.5))
    await dp.start_polling(bot)
    




if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)

    asyncio.run(main())

    
