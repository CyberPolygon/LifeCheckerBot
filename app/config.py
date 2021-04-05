import os
from telebot import TeleBot

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SQL_ROOT_PATH = os.path.join(BASE_DIR, 'app/sql')
BOT_TOKEN = os.environ.get('BOT_TOKEN')

bot = TeleBot(BOT_TOKEN)

TEAM_TAG = '[LIFE]'
DATABASE = {
    'dbname': os.environ.get('POSTGRES_DB'),
    'host': os.environ.get('POSTGRES_HOST'),
    'password': os.environ.get('POSTGRES_PASSWORD'),
    'user': os.environ.get('POSTGRES_USER')
}