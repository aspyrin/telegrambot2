import logging

from aiogram import Dispatcher

from data.config import admins


async def on_startup_notify(dp: Dispatcher):
    """
    Функуия отправляет всем администраторам бота сообщение о том, что бот запущен
    :param dp:
    """
    for admin in admins:
        try:
            text = 'Бот запущен и готов к работе!'
            await dp.bot.send_message(chat_id=admin, text=text)
        except Exception as err:
            logging.exception(err)
