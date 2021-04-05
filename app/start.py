from telebot import TeleBot, types, logger
from app.user.decorators import register_required
from app.user.steps import start_register
from app.config import bot

logger.setLevel('INFO')


@bot.message_handler(commands=['help', 'start'])
@register_required
def get_text_messages(message):
    print('Авторизация пройдена')


@bot.callback_query_handler(func=lambda call: call.data == 'register')
def callback_register(call):
    start_register(call.message)


bot.enable_save_next_step_handlers(delay=2)
bot.load_next_step_handlers()
bot.infinity_polling(long_polling_timeout=10)