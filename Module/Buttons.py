from telebot.types import InlineKeyboardMarkup,InlineKeyboardButton,WebAppInfo

STARTMENU = InlineKeyboardMarkup(
  keyboard=[[
    InlineKeyboardButton(text="y1",web_app=WebAppInfo(url=f'https://hdmovie5.herokuapp.com/')),
    InlineKeyboardButton(text="y2",web_app=WebAppInfo(url=f'https://hdmovie5.herokuapp.com/'))
    ],[
    InlineKeyboardButton(text="y3",web_app=WebAppInfo(url=f'https://hdmovie5.herokuapp.com/')),
    InlineKeyboardButton(text="y4",web_app=WebAppInfo(url=f'https://hdmovie5.herokuapp.com/'))
    ]]
  )
