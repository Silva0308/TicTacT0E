BOT_TOKEN_FILENAME = 'token.txt'
#Доска и массив с выигрышной комбинацией
BOARD = list(range(1, 10))
WINS = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7),
        (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]
# символы, которые используются
SYMBOL_X = '❌'
SYMBOL_O = '⭕'
SYMBOL_UNDEF = '◻'

# ответы бота
ANSW_YOUR_TURN = 'Ваш ход'
ANSW_YOU_WIN = 'Вы победили'
ANSW_BOT_WIN = 'Победил бот'
ANSW_DRAW = 'Ничья'
ANSW_HELP = 'Бот для игры в крестики-нолики\n' \
            'Используйте команду /new_game для начала новой игры'

# ошибки
ALERT_CANNOT_MOVE_TO_THIS_CELL = 'Нажимать можно только на ' + SYMBOL_UNDEF