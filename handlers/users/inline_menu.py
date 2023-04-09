from aiogram import types
from aiogram.types import CallbackQuery

from keyboards.default import kb_test
from keyboards.inline import ikb_menu, ikb_menu2

from loader import dp


@dp.message_handler(text="Инлайн меню")
async def show_inline_menu(message: types.Message):
    """
    отобразить инлайн меню1
    """
    await message.answer("Инлайн кнопки ниже", reply_markup=ikb_menu)


@dp.callback_query_handler(text="Сообщение")
async def send_message(call: CallbackQuery):
    """
    заменить нижнее меню на меню тест
    """
    await call.message.answer(text="Кнопки заменены", reply_markup=kb_test)


@dp.callback_query_handler(text="alert")
async def send_alert(call: CallbackQuery):
    """
    отправить всплывающее сообщение
    """
    await call.answer(text="Всплывающее сообщение!!!", show_alert=True)


@dp.callback_query_handler(text="Кнопки2")
async def send_change_inline_menu(call: CallbackQuery):
    """
    заменить инлайн меню1 на инлайн меню2
    """
    await call.message.edit_reply_markup(ikb_menu2)
