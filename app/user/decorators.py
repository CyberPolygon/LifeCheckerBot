from app.user.processor import Processor as User
from telebot import types
from app.config import bot


def register_required(func):
    def wrapper(message):
        user = User()
        user.add_id(message.from_user.id)

        keyboard = types.InlineKeyboardMarkup()
        key_register = None
        out_message = None

        if user.is_exists and user.is_filled:
            func(message)
            return wrapper

        if not user.is_exists:
            key_register = types.InlineKeyboardButton(text='Регистрация', callback_data='register')
            out_message = 'Для работы необходимо зарегистрироваться.'

        elif user.is_exists and not user.is_filled:
            key_register = types.InlineKeyboardButton(text='Заполнить данные', callback_data='register')
            out_message = 'Для работы необходимо заполнить данные.'

        keyboard.add(key_register)
        bot.send_message(message.from_user.id, out_message, reply_markup=keyboard)
    return wrapper
