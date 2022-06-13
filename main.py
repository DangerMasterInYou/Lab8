import telebot
from telebot import types

bot = telebot.TeleBot('5411415563:AAG5AM8t3t5YTvXhehaib3Q5fptjNGawbaY')

@bot.message_handler(commands = ['start'])

def start(message):
    mess = f'Привет, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
    bot.send_message(message.chat.id, mess, parse_mode = 'html')
# gyu
@bot.message_handler(content_types = ['text'])
def user_text(message):
    if message.text == 'Hello':
        bot.send_message(message.chat.id, f'Hello {message.from_user.first_name}', parse_mode='html')
    elif message.text == 'id':
        bot.send_message(message.chat.id, f'Your id: {message.from_user.id}', parse_mode='html')
    elif message.text == 'text':
        doc = open('ТЗ.txt', 'rb')
        bot.send_document(message.chat.id, doc)
    else:
        bot.send_message(message.chat.id, "I don't understand you", parse_mode='html')

@bot.message_handler(content_types = ['photo'])
def user_photo(message):
    bot.send_message(message.chat.id, 'Cool photo')

@bot.message_handler(commands = ['web'])
def web(message):
    markup = types.In
    bot.send_message(message.chat.id, 'Cool photo')

bot.polling(non_stop = True)


