#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This it the douglas_bot's first version. So, we have to refactor it to a class skeleton.
See more at: https://github.com/nickoala/telepot/blob/master/REFERENCE.md
"""
import sys
import time
import random
import datetime
import telepot
import calendar
import operator
import schedule
# from jobs import job

__author__ = "Alexsander Falcucci"
__email__ = "alex.falcucci@gmail.com"
__maintainer__ = "Alexsander Falcucci"
__license__ = "MIT"


morning_words = [
    '@doguinha_bot morning!',
    '@doguinha_bot morning',
    '@doguinha_bot good morning!',
    '@doguinha_bot good morning',
    '@doguinha_bot bom dia',
    '@doguinha_bot bom dia!',
]

night_words = [
    '@doguinha_bot night!',
    '@doguinha_bot night',
    '@doguinha_bot good night!',
    '@doguinha_bot good night',
    '@doguinha_bot boa noite!',
    '@doguinha_bot boa noite',
]

fuck_words = [
    '@doguinha_bot fuck!',
    '@doguinha_bot fuck',
    '@doguinha_bot fuck you!',
    '@doguinha_bot fuck you',
    '@doguinha_bot fuck yourself!',
    '@doguinha_bot fuck yourself',
    '@doguinha_bot fuck u!',
    '@doguinha_bot fuck u',
]

love_words = [
    '@doguinha_bot eu te amo!',
    '@doguinha_bot eu te amo',
    '@doguinha_bot te amo!',
    '@doguinha_bot te amo',
    '@doguinha_bot i love you',
    '@doguinha_bot i love you!',
    '@doguinha_bot i lov you',
    '@doguinha_bot i lov you!',
    '@doguinha_bot lov u'
    '@doguinha_bot lov u!'
]

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
    elif command.lower() in night_words:
        bot.sendMessage(chat_id, "Good night, {}!".format(name))
    elif command == u'@doguinha_bot que dia \xe9 hoje?':
        day = datetime.datetime.now().day
        month = months.get(calendar.month_name[datetime.datetime.now().month], '')
        bot.sendMessage(
            chat_id, u"É dia de você calar essa boca. \n\nBrincadeira, hoje é dia {day} de {month} \U0001f605".format(day=day, month=month))
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
    elif command.lower() in love_words:
        msgs = [
            u"Eu tambem amo vc, {} \u2764\ufe0f".format(name),
            "Legal.",
        ]
        msg = random.choice(msgs)
        bot.sendMessage(chat_id, msg)
        if msg == "Legal.":
            bot.sendChatAction(chat_id, 'upload_document')
            bot.sendDocument(chat_id, "BQADBAADdwMAAgMdZAdPtWmOPGN1IQI")
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
    elif command.lower() in fuck_words:
        msg = [
            u"Querido, por favor! Tenha boas maneiras! Você tem que me convidar pra jantar primeiro.",
            u"Entre na fila.",
            u"Sonhando novamente, querido?",
            u"Se sentindo sozinho de novo, ha?",
            u"É só eu ou você diz isso para todos?",
            u"Sério? Agora?",
            u"Não obrigado. Eu passo.",
        ]
        bot.sendMessage(chat_id, random.choice(msg))
        # bot.sendChatAction(chat_id, 'upload_document')
        # bot.sendDocument(chat_id, "BQADBAADdwMAAgMdZAdPtWmOPGN1IQI")
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


def job():
    print("Sending message...")
    msg = "Boa noite à todos!"
    bot.sendMessage("-58208727", msg)
    bot.sendChatAction("-58208727", 'upload_document')
    bot.sendDocument("-58208727", "BQADBAADeQMAAqwbZAeNjNm2fzVR0wI")

schedule.every().day.at("00:00").do(job)
while 1:
    schedule.run_pending()
    time.sleep(10)
