import os

import telebot
from telebot import types

from services import get_weather
from utils import get_city


TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def handle_start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton("Узнать погоду")
    markup.add(button)

    bot.send_message(
        message.chat.id,
        "Привет! Я бот для узнавания погоды. Нажми кнопку 'Узнать погоду' для получения прогноза.",
        reply_markup=markup
    )


@bot.message_handler(func=lambda message: message.text == "Узнать погоду")
def handle_weather_button(message):
    bot.send_message(message.chat.id, "Введите название города:")


@bot.message_handler(func=lambda message: True)
def handle_text(message):
    city_name = message.text

    city = get_city(city_name)

    if city:
        weather_data = get_weather(city[2], city[3])

        if weather_data:
            response_text = f"Погода в городе {city_name} на сегодня: {weather_data}"
        else:
            response_text = f"Не удалось получить данные о погоде для города {city_name}"
    else:
        response_text = f'Города "{city_name}" нету в базе городов. Проверьте правильность ввода.'
    bot.send_message(message.chat.id, response_text)


if __name__ == '__main__':
    bot.polling(none_stop=True)
