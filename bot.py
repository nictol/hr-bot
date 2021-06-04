import telebot

import config

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "This is HR bot by Silvia Bobariko")
    print('start command ' + str(message.chat.id))


@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, "Help Message hasn\'t implemented yet")
    print('help command ' + str(message.chat.id))

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


@bot.message_handler(commands=['contacts'])
def contacts_command(message):
    bot.send_message(message.chat.id, 'Акционерное общество «Силовые машины – ЗТЛ, ЛМЗ,'
                                      'Электросила, Энергомашэкспорт» (АО «Силовые машины») \n' +
                     'Россия, 195009, Санкт-Петербург \n' + 'ул. Ватутина, д.3, Лит. А \n' +
                     '+7 (812) 346 70 37 \n' +
                     '+7 (812) 346 70 35 \n' +
                     'mail@power-m.ru \n')
    print('contacts command ' + str(message.chat.id))


@bot.message_handler(commands=['timetable'])
def timetable_command(message):
    bot.send_message(message.chat.id, 'Help Message hasn\'t implemented yet')
    print('timetable command ' + str(message.chat.id))


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(message.chat.id, 'Спасибо, в ближайшее время с вами свяжется бригада по ремонту')


bot.polling()
