#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This it's the douglas_bot's first version. So, we have to refactor it to a class skeleton.
See more at: https://github.com/nickoala/telepot/blob/master/REFERENCE.md
"""
import re
import os
import time
import random
import datetime
import telepot
import calendar
import schedule
import pickledb
import logging
import logging.handlers
from external.ed import get_ed_reply, count_ed_mgs
from external.simsimi import get_simsimi_reply, count_simsimi_msg
from utils.utils import utf8_encode, remove_bot_name, verify_text, equals_text, my_shuffle
from utils.emoji import Emoji, get_all_emojis
from utils.word_keys import *
from jobs import good_night_cron_job, its_friday
from external.quotes import get_quotes, QuoteCoffee
from external.jokes import Joke
from utils.handler_error import TlsSMTPHandler

__author__ = "Alexsander Falcucci"
__email__ = "alex.falcucci@gmail.com"
__maintainer__ = "Alexsander Falcucci"
__license__ = "MIT"

db = pickledb.load(os.environ['HOME'] + '/douglas_db/douglas.db', True)

logger = logging.getLogger()

email_info = db.get('email_info')

gm = TlsSMTPHandler(("smtp.gmail.com", 587), email_info.get('email'),
                    [email_info.get('email')], 'Error found!',
                    (email_info.get('email'), email_info.get('password'))
                    )

gm.setLevel(logging.ERROR)

logger.addHandler(gm)


def handle(msg):
    """
    Just do the actions for each command listed in the conditions.
    We have to refactor it puting all commands at a tuple or list, etc.
    The bot username will be dinamically alterable, too.
    """
    try:
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

        if names_to_check or chat_type == 'private':
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
                    msg_wel = "Eu sempre estive aqui, idiota! {}".format(Emoji.NEUTRAL_FACE)
                elif welcome_count == 1:
                    msg_wel = "Não repito. {}".format(Emoji.NEUTRAL_FACE)
                else:
                    msg_wel = "{}".format(Emoji.NEUTRAL_FACE)
                bot.sendMessage(chat_id, msg_wel)
                globals()['welcome_count'] += 1
                print globals()['welcome_count']
            elif command.lower() in love_words:
                msgs = [
                    "Eu tambem amo vc, {}! {}{}".format(name,
                                                        Emoji.BLACK_HEART_SUIT,
                                                        Emoji.BLACK_HEART_SUIT),
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
                msg = "Ah é?! Foda-se."
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
            elif verify_text(command.lower().split(), 'trans'):
                msg = command.lower().replace('trans ', '')
                if msg.split()[0] == 'pt':
                    msg = msg.replace("pt ", "", 1)
                    print msg
                    os.system('echo "{}" | trans -b -o ~/output.txt :pt'.format(msg))
                else:
                    os.system('echo "{}" | trans -b -o ~/output.txt :en'.format(msg))
                with open(os.environ['HOME'] + '/output.txt', 'r') as content_file:
                    content = content_file.read()
                bot.sendMessage(chat_id, content)
            elif command == 'cotação':
                msg = get_quotes(db, bot, chat_id)
                bot.sendMessage(chat_id, re.sub(' +', ' ', msg.replace('.', ',')))
            # jokes
            elif equals_text(joke_words, command):
                jokes = my_shuffle(Joke(db).get_jokes())
                bot.sendMessage(chat_id, random.choice(jokes))
            else:
                cnt_ed = count_ed_mgs(db)
                cnt_simsimi = count_simsimi_msg(db)
                sminino_group_id = -58208727
                on_the_music_group_id = -82861655
                limit_ed = 5 if chat_id == sminino_group_id else 1 if chat_id == on_the_music_group_id else 3
                limit_simsimi = 2 if chat_id == sminino_group_id else 5 if chat_id == on_the_music_group_id else 3
                print 'limit_ed', limit_ed
                print 'limit_simsimi', limit_simsimi
                if cnt_ed < limit_ed:
                    response, sim_status, robot_name = get_ed_reply(command)
                elif cnt_simsimi < limit_simsimi:
                    response, sim_status, robot_name = get_simsimi_reply(command)
                else:
                    response, ed_status, robot_name = get_ed_reply(command)
                    if ed_status != 200:
                        response, sim_status, robot_name = get_simsimi_reply(command)
                    q = {'qty_answed_message': 0}
                    db.set('ed_info', q)
                    db.set('simsimi_info', q)
                    db.dump()

                if verify_text(['Fui criado e program', 'O meu inventor'], response):
                    developed_by_texts = db.get('developed_by')
                    olds = [utf8_encode(text) for text in developed_by_texts['old']]
                    news = [utf8_encode(text) for text in developed_by_texts['new']]
                    if 'Fui criado e program' in response:
                        response = response.replace(
                                olds[0],
                                news[0])
                        response += ' {}'.format(Emoji.GRINNING_FACE)
                    if 'O meu inventor' in response:
                        response = response.replace(
                                olds[1],
                                news[1])
                info_sent = bot.sendMessage(chat_id, response)
                if info_sent:
                    print robot_name
                    try:
                        count_msg = db.get('{}_info'.format(robot_name))['qty_answed_message']
                        count_msg += 1
                    except:
                        count_msg = 0
                    q = {'qty_answed_message': count_msg}
                    db.set('{}_info'.format(robot_name), q)
                    db.dump()
        elif verify_text(command.lower().split(), 'kkk'*15):
                msgs = [
                    'hahaha',
                    'kkkk',
                ]
                bot.sendMessage(chat_id, random.choice(msgs))
    except Exception as e:
        print e
        logger.exception(e)


bot = telepot.Bot(db.get('TOKEN'))
bot.notifyOnMessage(handle)
print 'I am listening ...'

schedule.every().friday.at("10:00").do(its_friday.job, bot)
schedule.every().day.at("00:00").do(good_night_cron_job.job, bot)
schedule.every().day.at("17:12").do(QuoteCoffee(db).run)
while 1:
    schedule.run_pending()
    time.sleep(10)
