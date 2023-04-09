from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from data import config

# Создаем переменную Бота где Bot(Token="токен нашего бота")
bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)

# Создаем переменную для хранилища машины состояний
storage = MemoryStorage()

# Создаем диспетчер
dp = Dispatcher(bot, storage=storage)
