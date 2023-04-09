from aiogram import Bot, Dispatcher, types
from data import config

# Создаем переменную Бота где Bot(Token="токен нашего бота")
bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)

# Создаем диспетчер
dp = Dispatcher(bot)
