import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

BUTTON1 = InlineKeyboardButton(text="y1",web_app=WebAppInfo(url=f'https://hdmovie5.herokuapp.com/')),
BUTTON2 = InlineKeyboardButton(text="y2",web_app=WebAppInfo(url=f'https://hdmovie5.herokuapp.com/'))
BUTTON3 = InlineKeyboardButton(text="y3",web_app=WebAppInfo(url=f'https://hdmovie5.herokuapp.com/')),
BUTTON4 = InlineKeyboardButton(text="y4",web_app=WebAppInfo(url=f'https://hdmovie5.herokuapp.com/'))

CoolFonts = InlineKeyboardButton(text='Cool Fonts',callback_data='CoolFonts')
DecorateText = InlineKeyboardButton(text='Decorate Text',callback_data='DecorateText')
 
 

HOME_PAGE = InlineKeyboardMarkup([
  [BUTTON1,DecorateText]
  ])
