import datetime

import requests
from telebot import TeleBot
from telebot.types import Message, ReplyKeyboardRemove

from config import *
from keyboards import *

bot = TeleBot(token=TOKEN, parse_mode='HTML')


@bot.message_handler(commands=['start'])
def starting(message: Message):
    user_id = message.from_user.id
    full_name = message.from_user.full_name
    bot.send_message(user_id, f"""Hi, Welcome to weather bot ! , {full_name} !""")
    send_loc(message)


def send_loc(message: Message):
    user_id = message.from_user.id
    bot.send_message(user_id, 'If you wanna know about weather in your location, please send me your location !', reply_markup=geo())


@bot.message_handler(content_types=['location'])
def get_weather(message: Message):
    user_id = message.from_user.id

    r = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?lat={message.location.latitude}&lon={message.location.longitude}&appid={open_weather_token}")
    data = r.json()

    city = data['name']
    cur_weather = data['main']['temp']
    weather_desc = data['weather'][0]['main']

    humidity = data['main']['humidity']
    pressure = data['main']['pressure']
    wind = data['wind']['speed']
    sunrise_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
    sunset_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunset'])

    bot.send_message(user_id, f"***{datetime.datetime.now().strftime('%d-%m-%Y  %H:%M')}***\n"
                              f"Weather in {city} city\nTemperature: {cur_weather} C° \n"
                              f"Humidity: {humidity}\nPressure: {pressure} mm_rt_st\nWind {wind} m/s\n"
                              f"Sunrise: {sunrise_timestamp}\nSunset: {sunset_timestamp}\n"
                              f"Have a nice day)", reply_markup=ReplyKeyboardRemove())


bot.polling(none_stop=True)
