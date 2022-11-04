from telegram import ReplyKeyboardRemove
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler, ConversationHandler
import names
from bot import tic, tac, start_game

CHOOSING_X, CHOOSING_O = range(2)


def start(update, context):
    update.message.reply_text('Чтобы начать игру введите: /start_game.\n'
                              'Можно ввести "stop", и игра прервется')


def interceptor(update, context):
    if update.message.text == "stop":
        update.message.reply_text(
            'Ну, вот... а так играли:(\n'
            ' Будет скучно - пиши.',
            reply_markup=ReplyKeyboardRemove()
        )
        return ConversationHandler.END
    else:
        update.message.reply_text("Что это вы ввели? Вы уверены, что число от 1 до 9?")


def main():
    updater = Updater(names.my_bot)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start_game", start_game)],

        states={
            "CHOOSING_X": [MessageHandler(Filters.regex('^(1|2|3|4|5|6|7|8|9)$'), tic)],
            "CHOOSING_O": [MessageHandler(Filters.regex('^(1|2|3|4|5|6|7|8|9)$'), tac)],
        },

        fallbacks=[MessageHandler(Filters.text, interceptor)]
    )

    dp.add_handler(conv_handler)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
