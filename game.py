import os
import random
import sys

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters

import names as n
import logging

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)


def getToken():
    token = ''
    if os.path.isfile(n.BOT_TOKEN_FILENAME):
        f = open(n.BOT_TOKEN_FILENAME, "r")
        token = f.read()
        f.close()
    else:
        print(
            "Пожалуйста, создайте в папке проекта файл 'token.txt' и поместите туда токен для работы телеграм бота  и запустите скрипт заново")
        sys.exit()  # завершить работу скрипта
    return token
def check():
    for each in n.WINS:
        if (n.BOARD[each[0] - 1]) == (n.BOARD[each[1] - 1]) == (n.BOARD[each[2] - 1]):
            return n.BOARD[each[1] - 1]
    else:
        return False
