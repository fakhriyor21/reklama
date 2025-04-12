from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ParseMode

API_TOKEN = '7642625328:AAE4XPbr5afok8jkPTuU1afu6_Dn5daA0hg'  # <-- Bu yerga o‘z bot tokeningizni yozing

bot = Bot(token=API_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(bot)

# 📌 Tugmalar va ularning tegishli kanallari
buttons = [
    {"text": "𝑲𝒂𝒏𝒂𝒍𝒍𝒂𝒓𝒊𝒎𝒊𝒛 ♻️", "url": "https://t.me/Kalbim_iffati_1"},
    {"text": "𝑹𝒆𝒌𝒍𝒂𝒎𝒂 𝑻𝒂𝒓𝒊𝒇 💸𝑹𝒆𝒌𝒍𝒂𝒎𝒂 𝒐𝒕𝒛𝒊v 💞", "url": "https://t.me/Reklama_tariflarimizz"},
    {"text": "🦋 𝑳𝒐𝒈𝒐 / 𝑯𝒆𝒍𝒑 𝒕𝒆𝒙𝒕 / 𝑺𝒕𝒐𝒓𝒊𝒆𝒔 🦋", "url": "https://t.me/Text_yasash_xizmati"},
    {"text": "♻️𝑷𝒓𝒆𝒎𝒊𝒖𝒎 𝒗𝒂 𝑩𝒐𝒐𝒔𝒕 𝒉𝒊𝒛𝒎𝒂𝒕𝒊 🔔", "url": "https://t.me/Xavfsiz_Premium"},
    {"text": "📞 𝑨𝒅𝒎𝒊𝒏 𝒃𝒊𝒍𝒂𝒏 𝒃𝒐𝒈‘𝒍𝒂𝒏𝒊𝒔𝒉", "url": "https://t.me/Kalbim_iffati_bot"},
    {"text": "ℹ️ 𝑴𝒂‘𝒍𝒖𝒎𝒐𝒕", "callback_data": "info"}
]

# 📌 Tugmalarni tartibga solgan holda chiqarish
def get_main_menu():
    keyboard = InlineKeyboardMarkup()
    for idx, button in enumerate(buttons, 1):
        if 'url' in button:
            keyboard.add(InlineKeyboardButton(f"{idx}. {button['text']}", url=button['url']))
        elif 'callback_data' in button:
            keyboard.add(InlineKeyboardButton(f"{idx}. {button['text']}", callback_data=button['callback_data']))
    return keyboard

# 📍 /start komandasi
@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await message.answer(
        "👋 <b>Salom!</b> Quyidagilardan birini tanlang:",
        reply_markup=get_main_menu()
    )

# 📍 Callback tugma bosilganda (ℹ️ 𝑴𝒂‘𝒍𝒖𝒎𝒐𝒕)
@dp.callback_query_handler(lambda c: c.data == 'info')
async def info_handler(callback_query: types.CallbackQuery):
    info_text = """
    <b>ℹ️ Bot haqida:</b>

    Ushbu bot sizga reklama xizmatlari, kompaniya xizmati va boshqa turdagi ma'lumotlarni taqdim etadi. Bot orqali turli kanallarga o'tish imkoniyati mavjud. 

    Quyidagi xizmatlardan foydalanishingiz mumkin:
    1. <b>Reklama tariflari</b>: Kanal va boshqa reklama xizmati haqidagi tariflar.
    2. <b>Kanalga qo‘shilish</b>: Turli kanallarimizga kirishingiz mumkin.
    3. <b>Admin bilan bog‘lanish</b>: Admin bilan to‘g‘ridan-to‘g‘ri bog‘lanish imkoniyati.

    Agar sizga boshqa savollar bo'lsa, admin bilan bog'lanishingiz mumkin.
    """
    await callback_query.message.answer(info_text)
    await callback_query.answer()

# 🚀 Botni ishga tushirish
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
