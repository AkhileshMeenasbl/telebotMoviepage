'''from bs4 import BeautifulSoup
import requests
import re

# Download IMDB's Top 250 data
url = 'http://www.imdb.com/chart/top'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

movies = soup.select('td.titleColumn')
links = [a.attrs.get('href') for a in soup.select('td.titleColumn a')]
crew = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]
ratings = [b.attrs.get('data-value') for b in soup.select('td.posterColumn span[name=ir]')]
votes = [b.attrs.get('data-value') for b in soup.select('td.ratingColumn strong')]

imdb = []

# Store each item into dictionary (data), then put those into a list (imdb)
for index in range(0, len(movies)):
    # Seperate movie into: 'place', 'title', 'year'
    movie_string = movies[index].get_text()
    movie = (' '.join(movie_string.split()).replace('.', ''))
    movie_title = movie[len(str(index))+1:-7]
    year = re.search('\((.*?)\)', movie_string).group(1)
    place = movie[:len(str(index))-(len(movie))]
    data = {"movie_title": movie_title,
            "year": year,
            "place": place,
            "star_cast": crew[index],
            "rating": ratings[index],
            "vote": votes[index],
            "link": links[index]}
    imdb.append(data)

for item in imdb:
    print(item['link'])
'''





import os
import telebot
from utils import parse_init_data
from telebot import TeleBot
from flask import Flask, request, abort, send_file, jsonify
import imdb
import config
import json
import uuid 
import string
from Module import Buttons,GeneralTxt
import logging

logging.basicConfig(level=logging.DEBUG)
ia = imdb.IMDb()

TOKEN = config.BOT_TOKEN
bot = TeleBot(token=TOKEN, parse_mode="HTML")
app = Flask(__name__, static_url_path='/static')


@bot.message_handler(commands=['start'])
def ak(m):
  bot.send_message(m.chat.id,text=GeneralTxt.Welcomemsg.format(m.chat.first_name),reply_markup=Buttons.HOME_PAGE)

def UpdateData():
  Uniq_Id1 = uuid.uuid1()
  Uniq_Id = f"{Uniq_Id1}".replace("-","")
  file_name = f"{Uniq_Id}.json"
  Data = GetMovies()
  with open(file_name, 'w') as fp:
    json.dump(Data, fp, indent=2)
  doc = open(file_name, "rb")
  Result_Data = doc.read()
  return Result_Data
  
def GetMovies():
  Result = {}
  search = ia.search_movie("Bahubali")
  srchrslt = f"{search}"
  srchrslt1 = srchrslt[2:]
  srchrslt2 = srchrslt1[:-3]
  srchrslt3 = str(srchrslt2)
  srchrslt4 = srchrslt3.split("_>, <")
  for i in srchrslt4:
    startid = i.find("Movie id:") + len("Movie id:")
    endid = i.find("[http]")
    iid = i[startid:endid]
    ttl = i.partition("title:_")[2]
    Result[str(iid)] = str(ttl)
  return Result






@app.route('/home',methods=['POST','GET'])
def index():
  app.logger.info("akhil")
  try:
    app.logger.debug('Debug:')
    return send_file('static/index.html')
  except IndexError:
    app.logger.error('error:')

@app.route("/class",methods=['POST','GET'])
def akhil():
  return UpdateData()











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
