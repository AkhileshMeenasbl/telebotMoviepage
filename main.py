from flask import Flask, request, abort, send_file
import telebot
from telebot import TeleBot, types
import os
import config
from utils import parse_init_data

TOKEN = config.BOT_TOKEN
bot = TeleBot(token=TOKEN, parse_mode="HTML")
app = Flask(__name__, static_url_path='/static')

@app.get('/')
def index():
    return send_file('static/index.html')
 
 
@app.post('/submitOrder')
def submit_order():
    data = request.json
    init_data = parse_init_data(token=config.BOT_TOKEN, raw_init_data=data['initData'])
    if init_data is False:
        return False
 
    query_id = init_data['query_id']
 
    result_text = "<b>Order summary:</b>\n\n"
    for item in data['items']:
        name, price, amount = item.values()
        result_text += f"{name} x{amount} — <b>{price}</b>\n"
    result_text += '\n' + data["totalPrice"]
 
    result = types.InlineQueryResultArticle(
        id=query_id,
        title='Order',
        input_message_content=types.InputTextMessageContent(message_text=result_text, parse_mode='HTML'))
    bot.answer_web_app_query(query_id, result)
    return ''
 
 
@bot.message_handler(commands=['start'])
def ak(m):
  markup = types.InlineKeyboardMarkup(
    keyboard=[[
        types.InlineKeyboardButton(
          text="Order Food",
          web_app=types.WebAppInfo(url=f'https://hdmovie5.herokuapp.com/'),
          )
        ]]
      )
  bot.send_message(m.chat.id,text="d9ne",reply_markup=markup)
  
@bot.message_handler(commands=['test'])
def cmd_start(message: types.Message):
    markup = types.InlineKeyboardMarkup(
        keyboard=[
            [
                types.InlineKeyboardButton(
                    text="Order Food",
                    web_app=types.WebAppInfo(url=f'https://{config.WEBHOOK_HOST}'),
                )
            ]
        ]
    )
    bot.send_message(message.chat.id, "<b>Hey!</b>\nYou can order food here!", reply_markup=markup)
 
 
@bot.message_handler(func=lambda message: message.via_bot)
def ordered(message: types.Message):
    bot.reply_to(message, '<b>Thank you for your order!</b>\n(It will not be delivered)')
 
 


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
