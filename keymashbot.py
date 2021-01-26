from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters

import random;

import dotenv
dotenv.load()
updater = Updater(token='{TOKEN}', use_context=True)

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

dispatcher = updater.dispatcher

import dictionary
import decoder
import encoder

def start(update, context):
  context.bot.send_message(chat_id=update.effective_chat.id, text="Type to encode")

def encodeBot(update, context):
  encoded = encode(update.message.text.lower())
  context.bot.send_message(chat_id=update.effective_chat.id, text=encoded)

def decodeBot(update, context):
  decoded = decode("".join(context.args))
  update.message.reply_text(decoded)


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

dispatcher.add_handler(CommandHandler("decode", decodeBot))

encode_handler = MessageHandler(Filters.text & (~Filters.command), encodeBot)
dispatcher.add_handler(encode_handler)

updater.start_polling()
