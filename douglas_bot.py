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


def handle(msg):
    print msg
    chat_id = msg['chat']['id']
    command = msg['text']
    name = msg['from']['first_name']

    print 'Got command: %s' % command

    if command.lower() in morning_words:
        bot.sendMessage(chat_id, "Good morning, {}!".format(name))
    elif command == '@doguinha_bot data?':
        day = datetime.datetime.now().day
        month = months.get(calendar.month_name[datetime.datetime.now().month], '')
        bot.sendMessage(chat_id, u"É dia de você calar essa boca. \n\nBrincadeira, hoje é dia {day} de {month} \U0001f605".format(day=day, month=month))

bot = telepot.Bot('142375463:AAFf1mMbT1O3rxOCaQ8j0hzdU_Hc5Wh4kj0')
bot.notifyOnMessage(handle)
print 'I am listening ...'

while 1:
    time.sleep(10)
