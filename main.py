import telebot
import requests
import json
import time
from telebot import types

bot = telebot.TeleBot('1610823383:AAEnLQ25DCWEeqZxCKs-DqV6ugFaIVb0Ih0')

a = False
d = {}

def fun():
    return requests.get('https://blockchain.info/ru/ticker').text

def menu1():
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('Проверить, измененился ли курс')
    keyboard.row('Выводить курс каждые 5 минут')
    keyboard.row('RUB', 'USD', 'EUR')
    return keyboard

def menu2():
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('Проверить RUB', 'Проверить USD', 'Проверить EUR')
    keyboard.row('Вернуться в главное меню')
    return keyboard

def menu3():
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('Рубль', 'Доллар', 'Евро')
    keyboard.row('Остановить')
    keyboard.row('Вернуться в главное меню')
    return keyboard

@bot.message_handler(content_types=['text'])

def get_text_messages(message):
    if message.text.lower() == "привет":
        bot.send_message(message.chat.id,
                         "Привет, чем я могу тебе помочь? Могу рассказать о курсе валюты в интересующей тебя валюте.",
                         reply_markup=menu1())

    if message.text.lower() == "проверить, измененился ли курс":
        bot.send_message(message.chat.id, "В какой валюте ты хочешь проверить курс биткоина?", reply_markup=menu2())

    if message.text.lower() == "rub":
        global d
        d = json.loads(fun())
        bot.send_message(message.chat.id, d['RUB']['sell'])

    if message.text.lower() == "usd":
        d = json.loads(fun())
        bot.send_message(message.chat.id, d['USD']['sell'])

    if message.text.lower() == "eur":
        d = json.loads(fun())
        bot.send_message(message.chat.id, d['EUR']['sell'])

    if message.text.lower() == "проверить rub":
        if d == json.loads(fun()):
            bot.send_message(message.chat.id, "Курс не изменился")
        else:
            bot.send_message(message.chat.id, "Курс изменился", reply_markup=menu2)

    if message.text.lower() == "проверить usd":
        if d == json.loads(fun()):
            bot.send_message(message.chat.id, "Курс не изменился")
        else:
            bot.send_message(message.chat.id, "Курс изменился", reply_markup=menu2)

    if message.text.lower() == "проверить eur":
        if d == json.loads(fun()):
            bot.send_message(message.chat.id, "Курс не изменился")
        else:
            bot.send_message(message.chat.id, "Курс изменился", reply_markup=menu2)

    if message.text.lower() == "рубль":
        global a
        a = True
        while a:
            d = json.loads(fun())
            bot.send_message(message.chat.id, d['RUB']['sell'])
            time.sleep(5)

    if message.text.lower() == "доллар":
        a = True
        while a:
            d = json.loads(fun())
            bot.send_message(message.chat.id, d['USD']['sell'])
            time.sleep(5)

    if message.text.lower() == "евро":
        a = True
        while a:
            d = json.loads(fun())
            bot.send_message(message.chat.id, d['EUR']['sell'])
            time.sleep(5)

    if message.text.lower() == "выводить курс каждые 5 минут":
        bot.send_message(message.chat.id, "В какой валюте выводить курс биткоина?", reply_markup=menu3())

    if message.text.lower() == "вернуться в главное меню":
        bot.send_message(message.chat.id, "Выбери действие", reply_markup=menu1())

    if message.text.lower() == "остановить":
        a = False

    if message.text.lower() == "пока":
        bot.send_message(message.chat.id, "До встречи!")

bot.polling(none_stop=True, interval=0)
