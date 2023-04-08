from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_menue = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="10"),
            KeyboardButton(text="11"),
        ],
        [
            KeyboardButton(text="100"),
        ],
        [
            KeyboardButton(text="Подпишись"),
            KeyboardButton(text="Любой текст"),
            KeyboardButton(text="Лайк"),
        ]
    ],
    resize_keyboard=True
)
