from telebot.types import ReplyKeyboardMarkup, KeyboardButton

# def send_loc_button():
#     markup = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
#     button = KeyboardButton(text='Send my geolocation')
#
#     markup.add(button)
#
#     return markup

def geo():
    keyboard = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_geo = KeyboardButton(text="Отправить местоположение",
    request_location=True)
    keyboard.add(button_geo)
    return keyboard