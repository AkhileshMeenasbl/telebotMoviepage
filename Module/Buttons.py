import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

Movie = InlineKeyboardButton(text="🔍 Movie App",web_app=WebAppInfo(url=f'https://hdmovie5.herokuapp.com/'))
Help = InlineKeyboardButton(text="💡 Help",callback_data='CoolFonts')
About = InlineKeyboardButton(text='About ⚠️',callback_data='CoolFonts')


HOME_PAGE = InlineKeyboardMarkup([
  [BUTTON1,CoolFonts]
  ])
