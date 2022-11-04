from random import randint

from telegram.ext import ConversationHandler

from telegram import ReplyKeyboardMarkup

BOARD = list(range(1, 10))


def keyboard():
    my_keyboard = ReplyKeyboardMarkup([["1", "2", "3"],
                                       ["4", "5", "6"],
                                       ["7", "8", "9"]
                                       ])
    return my_keyboard


def draw_board(update, context):
    global BOARD
    update.message.reply_text(f"| {BOARD[0]} | {BOARD[1]} | {BOARD[2]} |\n"
                              f"| {BOARD[3]} | {BOARD[4]} | {BOARD[5]} |\n"
                              f"| {BOARD[6]} | {BOARD[7]} | {BOARD[8]} |",
                              reply_markup=keyboard())


def start_game(update, context):
    global BOARD
    update.message.reply_text('Отсюда начнется игра:')
    draw_board(update, context)
    update.message.reply_text(f"Куда поставим ❌?")
    return "CHOOSING_X"


def check_win():
    global BOARD
    WINS = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in WINS:
        if BOARD[each[0]] == BOARD[each[1]] == BOARD[each[2]]:
            return BOARD[each[0]]
    counter = 0
    for i in BOARD:
        if type(i) == int:
            continue
        else:
            counter += 1
    if counter == 9:
        return counter
    else:
        return False


def tic(update, context):
    global BOARD
    player_answer = int(update.message.text)
    if str(BOARD[player_answer - 1]) not in "❌⭕":
        BOARD[player_answer - 1] = "❌"
        draw_board(update, context)
    else:
        update.message.reply_text("Эта клеточка уже занята,выберите другую")
        return f"CHOOSING_X"
    tmp = check_win()
    if type(tmp) == str:
        update.message.reply_text(f"{tmp} выиграл!")
        return ConversationHandler.END
    elif type(tmp) == int:
        update.message.reply_text("Ничья!")
        return ConversationHandler.END
    else:
        update.message.reply_text(f"Теперь ⭕ поставит бот. \n"
                                  f"Нажмите на любую цифру, чтобы он сделал ход")
    return "CHOOSING_O"


def tac(update, context):
    global BOARD
    while True:
        value = randint(1, 9)
        if str(BOARD[value - 1]) in '❌⭕':
                continue
        update.message.reply_text(f"Bot поставил ⭕ на клетку {value}")
        BOARD[value - 1] = '⭕'
        draw_board(update, context)
        break
    tmp = check_win()
    if type(tmp) == str:
        update.message.reply_text(f"{tmp} выиграл!")
        return ConversationHandler.END
    else:
        update.message.reply_text(f"Куда поставим X?")
    return "CHOOSING_X"
