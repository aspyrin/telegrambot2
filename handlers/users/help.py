from aiogram import types
from loader import dp
from utils.misc import rate_limit


@rate_limit(limit=5)
@dp.message_handler(text='/help')
async def command_help(message: types.Message):
    await message.answer(f'Привет, {message.from_user.full_name} \n'
                         f'Тебе нужна помощь?')
