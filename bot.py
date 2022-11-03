import datetime
import math
from random import randint

import names
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ReplyKeyboardMarkup

STATE = None
Player_1 = '❌'
Player_2 = '⭕'
BOARD = list(range(1, 10))
WINS = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7),
        (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]


def start(update, context):
    global BOARD
    first_name = update.message.chat.first_name
    reply_keyboard = [[BOARD[0], BOARD[1], BOARD[2]],
                      [BOARD[3], BOARD[4], BOARD[5]],
                      [BOARD[6], BOARD[7], BOARD[8]]]
    markup = ReplyKeyboardMarkup(reply_keyboard)
    update.message.reply_text(f"Привет, {first_name}, поиграем в Крестики-нолики\n"
                              f"Куда ты поставишь крестик?", reply_markup=markup)
    get_token()


def get_token(update, context):
    global BOARD
    value = int(update.message.text)
    # if str(BOARD[value - 1]) in '❌⭕':
    #     update.message.reply_text('Эта клетка занята. Повторите ввод')
    BOARD[value - 1] = '❌'
    reply_keyboard = [[BOARD[0], BOARD[1], BOARD[2]],
                      [BOARD[3], BOARD[4], BOARD[5]],
                     [BOARD[6], BOARD[7], BOARD[8]]]
    markup = ReplyKeyboardMarkup(reply_keyboard)
    update.message.reply_text(f"Вы поставили крестик на {value}. \n"
                              f"Теперь ходит бот", reply_markup=markup)
    start_put_bot()

def start_put_bot(update, context):
    global STATE
    global BOARD
    STATE = Player_2
    while True:
        value = randint(1, 9)
        if str(BOARD[value - 1]) in '❌⭕':
            continue
        update.message.reply_text(f"Bot поставил ⭕ на клетку {value}")
        BOARD[value - 1] = '⭕'
        break
    reply_keyboard = [[BOARD[0], BOARD[1], BOARD[2]],
                      [BOARD[3], BOARD[4], BOARD[5]],
                      [BOARD[6], BOARD[7], BOARD[8]]]
    markup = ReplyKeyboardMarkup(reply_keyboard)
    first_name = update.message.chat.first_name
    update.message.reply_text(f" {first_name}, Куда теперь ставить?\n", reply_markup=markup)
    get_token()

def check_win(update, context):
    global WINS
    global BOARD
    for each in WINS:
        if (BOARD[each[0] - 1]) == (BOARD[each[1] - 1]) == (BOARD[each[2] - 1]):
            winner = BOARD[each[1] - 1]
            update.message.reply_text(f'Ура! 🎉 {winner} выиграл!')
    else:
        return False

def help(update, context):
    update.message.reply_text('help command received')


def error(update, context):
    update.message.reply_text('an error occured')


def main():
    TOKEN = names.my_bot

    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help))
    # dispatcher.add_handler(CommandHandler("biorhythm", biorhythm))

    dispatcher.add_handler(MessageHandler(Filters.text, get_token))

    dispatcher.add_error_handler(error)

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
