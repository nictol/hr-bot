import telebot

import config
import util

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "This is HR bot by Silvia Bobariko")
    print('start command ' + str(message.chat.id))


@bot.message_handler(commands=[config.HELP_COMMAND])
def contacts_command(message):
    util.send_answer(bot, message.chat.id, config.HELP_ANSWER_FILE, config.HELP_LOG)


@bot.message_handler(commands=['idea'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Фабрика идей! Добрый день! ' +
                     'Опишите подробнее свою идею по улучшению качеству в компании')
    print('idea command ' + str(message.chat.id))


@bot.message_handler(commands=['warning'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Добрый день! Укажите номер своего рабочего места (станка), ' +
                     'который необходимо проверить')
    print('warning command ' + str(message.chat.id))


@bot.message_handler(commands=[config.CONTACTS_COMMAND])
def contacts_command(message):
    util.send_answer(bot, message.chat.id, config.CONTACTS_ANSWER_FILE, config.CONTACTS_LOG)


@bot.message_handler(commands=['timetable'])
def timetable_command(message):
    bot.send_message(message.chat.id, 'Help Message hasn\'t implemented yet')
    print('timetable command ' + str(message.chat.id))


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    # TODO: standart answer
    bot.send_message(message.chat.id, 'Спасибо, в ближайшее время с вами свяжется бригада по ремонту')


bot.polling()
