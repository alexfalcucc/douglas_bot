#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This it's the douglas_bot's first version. So, we have to refactor it to a class skeleton.
See more at: https://github.com/nickoala/telepot/blob/master/REFERENCE.md
"""
import sys
import os
import time
import random
import datetime
import telepot
import calendar
import operator
import schedule
from external.ed import get_ed_reply
from utils.utils import utf8_encode, remove_bot_name
from utils.emoji import Emoji, get_all_emojis
from jobs import good_night_cron_job
# from jobs import job

__author__ = "Alexsander Falcucci"
__email__ = "alex.falcucci@gmail.com"
__maintainer__ = "Alexsander Falcucci"
__license__ = "MIT"


morning_words = [
    'morning!',
    'morning',
    'good morning!',
    'good morning',
    'bom dia',
    'bom dia!',
]

night_words = [
    'night!',
    'night',
    'good night!',
    'good night',
    'boa noite!',
    'boa noite',
]

fuck_words = [
    'fuck!',
    'fuck',
    'fuck you!',
    'fuck you',
    'fuck yourself!',
    'fuck yourself',
    'fuck u!',
    'fuck u',
    'vai se fuder',
    'vai se fuder!',
    'foda-se',
    'foda-se!',
    'vsf',
]

love_words = [
    'eu te amo!',
    'eu te amo',
    'te amo!',
    'te amo',
    'i love you',
    'i love you!',
    'i lov you',
    'i lov you!',
    'lov u',
    'lov u!',
    'i lov u',
    'i lov u!'
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

ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.div,
}

welcome_count = 0

bot_names = [
    ', dog',
    'dog, ',
    ' dog,',
    'dog,',
    ' dogão',
    'dogão ',
    'doguinha',
    ' doguinha',
    'doguinha ',
    ' dog',
    'dog ',
    ' rei',
    'rei ',
    ' mestre',
    'mestre ',
    '@doguinha_bot ',
    ' @doguinha_bot',
]


def verify_text(names, text):
    return [name for name in names if name in text]


def handle(msg):
    """
    Just do the actions for each command listed in the conditions.
    We have to refactor it puting all commands at a tuple or list, etc.
    The bot username will be dinamically alterable, too.
    """
    global bot_names
    command = ''
    print msg
    content_type, chat_type, chat_id = telepot.glance2(msg)
    print content_type, chat_type, chat_id
    if content_type == 'text':
        command = utf8_encode(msg['text'].lower())

    name = utf8_encode(msg['from']['first_name'])

    print 'Got command: %s' % command

    names_to_check = verify_text(bot_names, command)
    print names_to_check

    if names_to_check:
        command = remove_bot_name(names_to_check, command)
        print command

        if command.lower() in morning_words:
            bot.sendMessage(chat_id, "Good morning, {}!".format(name))
        elif command.lower() in night_words:
            bot.sendMessage(chat_id, "Good night, {}!".format(name))
        elif command == 'que dia é hoje?':
            day = datetime.datetime.now().day
            month = months.get(calendar.month_name[datetime.datetime.now().month], '')
            bot.sendMessage(
                chat_id, "É dia de você calar essa boca. \n\nBrincadeira, hoje é dia {day} de {month} \U0001f605".format(day=day, month=month))
        elif command == 'bem vindo!':
            if welcome_count < 1:
                msg_wel = "Eu sempre estive aqui, idiota! \U0001f610"
            elif welcome_count == 1:
                msg_wel = "Não repito. \U0001f48b"
            else:
                msg_wel = "\U0001f610"
            bot.sendMessage(chat_id, msg_wel)
            globals()['welcome_count'] += 1
            print globals()['welcome_count']
        elif command.lower() in love_words:
            msgs = [
                "Eu tambem amo vc, {} \u2764\ufe0f".format(name),
                "Legal.",
            ]
            msg = random.choice(msgs)
            bot.sendMessage(chat_id, msg)
            if msg == "Legal.":
                bot.sendChatAction(chat_id, 'upload_document')
                bot.sendDocument(chat_id, "BQADBAADdwMAAgMdZAdPtWmOPGN1IQI")
        elif command.lower() == 'que horas são?':
            msg = "É muita hipocrisia da sua parte me perguntar isso {}... "\
                  "Você pode vizualisar facilmente as horas olhando para parte "\
                  "inferior direita do seu comentário."
            bot.sendMessage(chat_id, msg.format(name))
            bot.sendChatAction(chat_id, 'upload_document')
            bot.sendDocument(chat_id, "BQADAQADEwADnqxzCGp0fqkzsPC6Ag")
        elif command.lower() == 'nós te amamos!':
            msg = "Eu amo todos vocês! \u2764\ufe0f"
            bot.sendMessage(chat_id, msg)
            bot.sendChatAction(chat_id, 'upload_document')
            bot.sendDocument(chat_id, "BQADBAADYwMAAiUcZAe1DjlP-IMGhQI")
        elif command.lower() == 'é bininu binina ou binunu binino?'.lower():
            msg = "bininu."
            bot.sendMessage(chat_id, msg)
        elif command.lower() == 'qual sua idade?':
            msg = "Você sabe a idade de Deus, seu criador? Pois é, sou 1 ano mais novo que Ele."
            bot.sendMessage(chat_id, msg)
        elif command.lower() == '/emojis':
            msg1, msg2, msg3, msg4, msg5 = get_all_emojis()
            bot.sendMessage(chat_id, msg1)
            bot.sendMessage(chat_id, msg2)
            bot.sendMessage(chat_id, msg3)
            bot.sendMessage(chat_id, msg4)
            bot.sendMessage(chat_id, msg5)
        elif command.lower() in fuck_words:
            msg = [
                "Querido, por favor! Tenha boas maneiras! Você tem que me convidar pra jantar primeiro.",
                "Entre na fila.",
                "Sonhando novamente, querido?",
                "Se sentindo sozinho de novo, ha?",
                "É só eu ou você diz isso para todos?",
                "Sério? Agora?",
                "Não obrigado. Eu passo.",
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
            bot.sendMessage(chat_id, '\xae: {}'.format(ops[op](float(parse[1]), float(parse[2]))))
        else:
            ed_response = get_ed_reply(command)
            bot.sendMessage(chat_id, ed_response)
    elif verify_text(command.lower().split(), 'kkk'*15):
            msgs = [
                'hahaha',
                'kkkk',
            ]
            bot.sendMessage(chat_id, random.choice(msgs))


bot = telepot.Bot('142375463:AAFf1mMbT1O3rxOCaQ8j0hzdU_Hc5Wh4kj0')
bot.notifyOnMessage(handle)
print 'I am listening ...'

schedule.every().day.at("00:00").do(good_night_cron_job.job, bot)
while 1:
    schedule.run_pending()
    time.sleep(10)
