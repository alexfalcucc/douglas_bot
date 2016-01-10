#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import sys
import time
import random
import datetime
import telepot
import calendar

morning_words = ['@doguinha_bot morning', '@doguinha_bot good morning']

months = {
    'January': 'Janeiro',
    'February': 'Fevereiro',
    'March': 'Março',
    'April': 'Abril',
    'May': 'Maio',
    'June': 'Junho',
    'July': 'Julho',
    'August': 'Agosto',
    'September': 'Setembro',
    'October': 'Outubro',
    'November': 'Novembro',
    'December': 'Dezembro'
}

welcome_count = 0


def handle(msg):
    print msg
    chat_id = msg['chat']['id']
    command = msg['text']
    name = msg['from']['first_name']

    print 'Got command: %s' % command

    if command.lower() in morning_words:
        bot.sendMessage(chat_id, "Good morning, {}!".format(name))
    elif command == '@doguinha_bot data':
        day = datetime.datetime.now().day
        month = months.get(calendar.month_name[datetime.datetime.now().month], '')
        bot.sendMessage(chat_id, u"É dia de você calar essa boca. \n\nBrincadeira, hoje é dia {day} de {month} \U0001f605".format(day=day, month=month))
    elif command == '@doguinha_bot bem vindo!':
        if welcome_count < 1:
            msg_wel = u"Eu sempre estive aqui, idiota! \U0001f610"
        elif welcome_count == 1:
            msg_wel = u"Não repito. \U0001f48b"
        else:
            msg_wel = u"\U0001f610"
        bot.sendMessage(chat_id, msg_wel)
        globals()['welcome_count'] += 1
        print globals()['welcome_count']

bot = telepot.Bot('142375463:AAFf1mMbT1O3rxOCaQ8j0hzdU_Hc5Wh4kj0')
bot.notifyOnMessage(handle)
print 'I am listening ...'

while 1:
    time.sleep(10)
