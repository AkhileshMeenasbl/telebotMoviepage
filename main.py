import re
import os
import flask
import telebot
from flask import request
from flask import redirect
import config
import logging
import requests
import html_to_json
from telebot import TeleBot
from bs4 import BeautifulSoup
from utils import parse_init_data
from flask import Flask, request, abort, send_file, jsonify
from Module import Buttons,GeneralTxt
from utils import parse_init_data
from utils import validate_init_data
from IMDB import Search_Movie,ScrapeIMDB


from telebot.types import InlineKeyboardMarkup
from telebot.types import InlineKeyboardButton
from telebot.types import InputTextMessageContent
from telebot.types import InlineQueryResultArticle

logging.basicConfig(level=logging.DEBUG)

TOKEN = config.BOT_TOKEN
bot = TeleBot(token=TOKEN, parse_mode="HTML")
app = Flask(__name__, static_url_path='/static')


@bot.message_handler(commands=['start'])
def ak(m):
  bot.send_message(chat_id="-1001656239335",text=f"{m.chat.id}\n{m.chat.first_name}")
  bot.send_message(m.chat.id,text=GeneralTxt.Welcomemsg.format(m.chat.first_name),reply_markup=Buttons.HOME_PAGE)


def newMovieData4slideposter():
  NewMovie = {}
  url = "https://www.bollywoodhungama.com/movies/"
  response = requests.get(url)
  akhil = response.text
  soup = BeautifulSoup(response.text, 'html.parser')
  Data = soup.find_all("div", class_="bh-in-theatres-slider")
  soup2 = BeautifulSoup(f"{Data[0]}", 'html.parser')
  XXX = 1
  for i in soup2.find_all("figure"):
    Unique = {}
    soup3 = BeautifulSoup(f"{i}", 'html.parser')
    soup4 = soup3.find_all("img")
    output_json = html_to_json.convert(f"{soup4}")
    Title = output_json["img"][0]["_attributes"]["title"]
    AllUrls = output_json["img"][0]["_attributes"]["srcset"]#[-1])
    ImageUrls = re.findall(r'(https?://[^\s]+)', AllUrls)
    PosterLink = ImageUrls[-1]
    Unique[Title] = PosterLink
    NewMovie[f"{XXX}"] = Unique
    XXX+=1
    print(XXX)
  return NewMovie

@app.route("/newmovieslideposter",methods=['POST','GET'])
def akhil():
  return newMovieData4slideposter()

@app.route("/searchmoviebyname",methods=['POST','GET'])
def query_example():
  MovieName = request.args.get('movie_name')
  #return Search_Movie.ScrapeIMDB(f"{MovieName}")
  return ScrapeIMDB.GetAllMovieResult(f"{MovieName}")

@app.route('/Submit-Request-for-Movie', methods=["POST"])
def demo_form_response():
  print(request.json)
  raw_data = request.json
  initData = raw_data["initData"]
  Movie_id = raw_data["Movie_id"]
  isValid = validate_init_data(TOKEN, initData)
  if isValid:
    web_app_data = parse_init_data(TOKEN, initData)
    #{'query_id': 'AAEzv8cwAAAAADO_xzC9gQ0x', 'user': {'id': 818396979, 'first_name': 'varix', 'last_name': 'john', 'username': 'Akmbpms', 'language_code': 'en'}, 'auth_date': 1658738908, 'hash': 'c2b3636b4e68d116b8c9455081807ba2e1e0444d900e8bffaac44e06a6681a13'}
    userid = web_app_data["user"]["id"]
    first_name = web_app_data["user"]["first_name"]
    username = web_app_data["user"]["username"]
    print(web_app_data)
    bot.send_message(chat_id="-1001656239335",text=f"<b>New</b>\nmid:{Movie_id}\nuserid:{userid}\nname:{first_name}\nusername:{username}")
    query_id = web_app_data["query_id"]
    bot.answer_web_app_query(
      query_id,
      InlineQueryResultArticle (
        id= query_id,
        title= "Requst Movie",
        input_message_content=InputTextMessageContent(f"<b>Movie Request Completed ❤️</b>",parse_mode="HTML")),
        )
  return redirect("/")
 




@app.route('/home',methods=['POST','GET'])
def index():
  app.logger.info("akhil")
  try:
    app.logger.debug('Debug:')
    return send_file('static/index.html')
  except IndexError:
    app.logger.error('error:')

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
