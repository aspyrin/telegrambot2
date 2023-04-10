from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from filters import IsPrivate
from keyboards.default import kb_menue
from loader import dp

from states import Register


@dp.message_handler(IsPrivate(), Command('register'))  # /register
async def register(message: types.Message):
    from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
    name = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=f"{message.from_user.first_name}"),
            ]
        ],
        resize_keyboard=True
    )
    await message.answer('Привет, ты начал регистрацию, \nВведи свое имя', reply_markup=name)
    await Register.test1.set()  # переводим пользователяв состояние test1


@dp.message_handler(state=Register.test1)  # ловим сообщения с состоянием test1
async def state1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(test1=answer)
    await message.answer('Сколько тебе лет?')
    await Register.test2.set()  # переводим пользователяв состояние test2


@dp.message_handler(state=Register.test2)  # ловим сообщения с состоянием test2
async def state2(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(test2=answer)
    data = await state.get_data()
    name = data.get('test1')
    years = data.get('test2')
    await message.answer(f'Регистрация успешно завершена \n'
                         f'Твое имя {name} \n'
                         f'Тебе {years} лет', reply_markup=kb_menue)
    await state.finish()  # переводим пользователяв состояние finish
