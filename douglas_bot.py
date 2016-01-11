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

import operator
ops = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.div}

welcome_count = 0


def handle(msg):
    command = ''
    print msg
    content_type, chat_type, chat_id = telepot.glance2(msg)
    print content_type, chat_type, chat_id
    if content_type == 'text':
        command = msg['text']

    name = msg['from']['first_name']

    print 'Got command: %s' % command

    if command.lower() in morning_words:
        bot.sendMessage(chat_id, "Good morning, {}!".format(name))
    elif command == u'@doguinha_bot que dia \xe9 hoje?':
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
    elif command.lower() == '@doguinha_bot eu te amo!':
        bot.sendMessage(chat_id, u"Eu tambem amo vc, {} \u2764\ufe0f".format(name))
    elif command.lower() == u'@doguinha_bot que horas s\xe3o?':
        msg = u"É muita hipocrisia da sua parte me perguntar isso {}... "\
              u"Você pode vizualisar facilmente as horas olhando para parte "\
              u"inferior direita do seu comentário."
        bot.sendMessage(chat_id, msg.format(name))
        bot.sendChatAction(chat_id, 'upload_document')
        bot.sendDocument(chat_id, "BQADAQADEwADnqxzCGp0fqkzsPC6Ag")
    elif command.lower() == u'@doguinha_bot n\xf3s te amamos!':
        msg = u"Eu amo todos vocês! \u2764\ufe0f"
        bot.sendMessage(chat_id, msg)
        bot.sendChatAction(chat_id, 'upload_document')
        bot.sendDocument(chat_id, "BQADBAADYwMAAiUcZAe1DjlP-IMGhQI")
    elif len(command.split()) == 4 and command.split()[2] in ops.keys():
        """
        please refactor with it: http://stackoverflow.com/questions/1740726/python-turn-string-into-operator
        """
        parse = command.split()
        op = parse.pop(2)
        bot.sendMessage(chat_id, u'\xae: {}'.format(ops[op](float(parse[1]), float(parse[2]))))


bot = telepot.Bot('142375463:AAFf1mMbT1O3rxOCaQ8j0hzdU_Hc5Wh4kj0')
bot.notifyOnMessage(handle)
print 'I am listening ...'

while 1:
    time.sleep(10)
