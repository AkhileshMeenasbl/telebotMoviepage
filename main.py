import os
import telebot
from utils import parse_init_data
from telebot import TeleBot
from flask import Flask, request, abort, send_file

import config
from Module import Buttons,GeneralTxt

TOKEN = config.BOT_TOKEN
bot = TeleBot(token=TOKEN, parse_mode="HTML")
app = Flask(__name__, static_url_path='/static')

@bot.message_handler(commands=['start'])
def ak(m):
  bot.send_message(m.chat.id,text=GeneralTxt.Welcomemsg.format(m.chat.first_name),reply_markup=Buttons.HOME_PAGE)

@app.route('/' + "home", methods=['POST'])
def index():
  return send_file('static/index.html')


@app.route('/' + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200
 
@app.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=f"https://hdmovie5.herokuapp.com/{TOKEN}")
    return "!", 200
 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
