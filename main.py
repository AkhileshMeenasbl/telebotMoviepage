from flask import Flask, request, abort, send_file
from telebot import TeleBot, types
import os
import config
from utils import parse_init_data

bot = TeleBot(config.BOT_TOKEN, parse_mode="HTML")
app = Flask(__name__, static_url_path='/static')

@bot.message_handler(commands=['test'])
def cmd_start(m):
  bot.send_message(m.chat.id,text="akhil")

@app.route('/' + config.BOT_TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200
 
@app.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://' + config.APPNAME + '.herokuapp.com/' + f"{config.BOT_TOKEN}")
    return "!", 200
 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
