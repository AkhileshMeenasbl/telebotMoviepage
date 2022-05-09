import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

BUTTON1 = InlineKeyboardButton(text="y1",web_app=WebAppInfo(url=f'https://hdmovie5.herokuapp.com/')),
CoolFonts = InlineKeyboardButton(text='Cool Fonts',callback_data='CoolFonts')

HOME_PAGE = InlineKeyboardMarkup([
  [BUTTON1,CoolFonts]
  ])
