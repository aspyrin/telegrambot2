from aiogram import types
from loader import dp


@dp.message_handler(text='10')
async def buttons_test_10(message: types.Message):
    await message.answer(f'Привет, {message.from_user.full_name} \n'
                         f'Ты выбрал число {message.text}')


@dp.message_handler(text='11')
async def buttons_test_11(message: types.Message):
    await message.answer(f'Привет, {message.from_user.full_name} \n'
                         f'Ты выбрал число {message.text}')


@dp.message_handler(text='100')
async def buttons_test_100(message: types.Message):
    await message.answer(f'Привет, {message.from_user.full_name} \n'
                         f'Ты выбрал число {message.text}')
