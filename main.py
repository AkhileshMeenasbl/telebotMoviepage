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

TOKEN = config.BOT_TOKEN
bot = TeleBot(token=TOKEN, parse_mode="HTML")
app = Flask(__name__, static_url_path='/static')

ia = imdb.IMDb()

@bot.message_handler(commands=['start'])
def ak(m):
  bot.send_message(m.chat.id,text=GeneralTxt.Welcomemsg.format(m.chat.first_name),reply_markup=Buttons.HOME_PAGE)

def getChatId(m):
  print () 

def UpdateData():
  Uniq_Id1 = uuid.uuid1()
  Uniq_Id = f"{Uniq_Id1}".replace("-","")
  file_name = f"{Uniq_Id}.json"
  Data = GetMovies()
  print(Data)
  with open(file_name, 'w') as fp:
    json.dump(Data, fp, indent=2)
  pass
  return Data
  
def GetMovies():
  #[<Movie id:4549714[http] title:_"Bahubali" (2008)_>, <Movie id:2631186[http] title:_Baahubali: The Beginning (2015)_>, <Movie id:4849438[http] title:_Baahubali 2: The Conclusion (2017)_>, <Movie id:13452374[http] title:_"Bahubali" Episode #1.70 (2009)_>, <Movie id:6940950[http] title:_"Bahubali" Episode #1.1 (2008)_>, <Movie id:5216536[http] title:_Hum Bahubali (2008)_>, <Movie id:6575210[http] title:_"Hubahu" (2002)_>, <Movie id:5523460[http] title:_"Baahubali: The Lost Legends" (2017)_>, <Movie id:7618900[http
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
  
def html():  # Also allows you to set your own <head></head> etc
  search = ia.search_movie("Bahubali")
  Text = f"{search}"
  print(Text)
  return '<html><head>custom head stuff here</head><body>' + Text + '</body></html>'

@app.route('/home',methods=['POST','GET'])
def index():
  return send_file('static/index.html')

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
