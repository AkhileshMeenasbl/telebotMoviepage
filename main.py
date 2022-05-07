from flask import Flask, request, abort, send_file
import telebot
from telebot import TeleBot, types
import os
import json
import config
from utils import parse_init_data

TOKEN = config.BOT_TOKEN
bot = TeleBot(token=TOKEN)
app = Flask(__name__)

@bot.message_handler(commands=['test'])
def cmd_start(m):
  bot.send_message(m.chat.id,text="akhil")

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
