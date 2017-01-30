from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import json

updater =   Updater(token='249362685:AAF-pOpNK2yQ22JciNF0MO_7GcXJlZ3e234')
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

CMD_START = '/start'
CMD_STOP = '/stop'
CMD_HELP = '/help'
CMD_BROADCAST = '/broadcast'

CUSTOM_KEYBOARD = [
    [CMD_START],
    [CMD_STOP],
    [CMD_HELP]
]

def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="나는 Bot이다.")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

def echo(bot, update):
    reply_markup = json.dumps({
        'keyboard': CUSTOM_KEYBOARD,
        'resize_keyboard': True,
        'one_time_keyboard': False,
        'selective': True
    })
    logger.info("chat username=" + update.message.chat.username)
    bot.sendMessage(chat_id=update.message.chat_id, text=update.message.text, reply_markup=reply_markup)

echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)

def unknown(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Sorry, 이해하지 못하겠군요")

unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)

updater.start_polling()
updater.idle()






