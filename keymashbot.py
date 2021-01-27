from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters

import random
import json

import dotenv
dotenv.load()
updater = Updater(token='{TOKEN}', use_context=True)

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

dispatcher = updater.dispatcher

def encode(inputText):
  # Convert to keymash list
  encodedText = [keymash[alphabet.index(x)] for x in inputText];

  # Convert to string delimited by 0s
  encodedText = '0'.join(encodedText);
  # Replace whitespaces with a random element from keymashExtra
  # then return as a string
  encodedText = ''.join([x.replace('0', random.choice(keymashExtra)) for x in encodedText])
  return encodedText;

def decode(encodedText):
  # Replace every occurrence s with . and k with -
  decodedText = encodedText.replace('s', '.').replace('k', '-');

  # If character is alphanumeric, i.e not a dit or dah, return '0'
  # .split('0') to delimit the resulting list by 0s, preserving spaces
  decodedText = "".join(['0' if x.isalnum() else x for x in decodedText]).split('0');

  # using morse[] as reference to find the corresponding index on alphabet[]
  decodedText = "".join([alphabet[morse.index(x)] for x in decodedText]);

  return decodedText

with open("dictionary.json", "r") as read_file:
    data = json.load(read_file)
    alphabet = data['alphabet']
    morse = data['morse']
    keymash = data['keymash']
    keymashExtra = data['keymashExtra']

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
