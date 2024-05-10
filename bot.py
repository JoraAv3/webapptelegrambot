from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

# Подгружаем токен из настроек Django
bot = Bot('7005528546:AAF9hjJBlb1l5egEcGfe6FLy4Y335b_HZv0')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = InlineKeyboardMarkup()
    web_app_url = 'https://itproger.com/'
    button = InlineKeyboardButton(text='Открыть мини-приложение', web_app=WebAppInfo(url=web_app_url))
    markup.add(button)
    await message.answer('Нажмите на кнопку ниже, чтобы открыть мини-приложение:', reply_markup=markup)

if __name__ == "__main__":
    executor.start_polling(dp)
