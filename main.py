import re
import os
import config
import logging
import telebot
import requests
import html_to_json
from telebot import TeleBot
from bs4 import BeautifulSoup
from utils import parse_init_data
from flask import Flask, request, abort, send_file, jsonify
from Module import Buttons,GeneralTxt

logging.basicConfig(level=logging.DEBUG)

TOKEN = config.BOT_TOKEN
bot = TeleBot(token=TOKEN, parse_mode="HTML")
app = Flask(__name__, static_url_path='/static')


@bot.message_handler(commands=['start'])
def ak(m):
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
  print(MovieName)
  return f"{MovieName}"
  #return SearchMovieByName()

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
