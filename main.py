import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

API_TOKEN = "7897232233:AAGDnmEWHJ5jtQjrOIp0NPa916P_ymLIsRg"  # Вставь сюда свой API Token из BotFather

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Я твой новый Telegram-бот!")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
