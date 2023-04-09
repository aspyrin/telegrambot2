from aiogram import types
from aiogram.dispatcher.filters import Command

from keyboards.default import kb_menue
from loader import dp


@dp.message_handler(Command("menu"))
async def menu(message: types.Message):
    await message.answer(text="Выберите число из меню ниже", reply_markup=kb_menue)
