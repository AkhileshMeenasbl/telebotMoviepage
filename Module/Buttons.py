import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

Movie = InlineKeyboardButton(text="🔍 Movie App",web_app=WebAppInfo(url=f'https://hdmovie5.herokuapp.com/home'))
Add2Channel = InlineKeyboardButton(text="💡 Help",url='http://t.me/yourbot?startgroup=new')
Help = InlineKeyboardButton(text="💡 Help",callback_data='CoolFonts')
About = InlineKeyboardButton(text='About ⚠️',callback_data='CoolFonts')


HOME_PAGE = InlineKeyboardMarkup([
  [Movie,Add2Channel],
  [Help,About]
  ])
