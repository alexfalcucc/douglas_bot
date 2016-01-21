#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
from utils.utils import my_shuffle
from utils.emoji import Emoji


def job(bot):
    print("Sending message...")
    msg = "#bomdia Smininos! É hora de acordar... {}".format(
        Emoji.SUN_BEHIND_CLOUD,
        Emoji.SMILING_FACE_WITH_OPEN_MOUTH)
    chat_id = '-58208727'
    bot.sendMessage(chat_id, msg)
    bot.sendChatAction(chat_id, 'upload_document')
    gifs = [
        'BQADBAADgAMAAnIdZAdIwXN1oJLFZwI',
        'BQADBAAD5gMAAuMZZAer90C0u8hN9wI',
        'BQADBAADSgMAAmAZZAc8QCM-wgy6gwI',
        'BQADBAADlQMAAosbZAcK-YB68LLP1QI',
        'BQADBAADIwMAAj8cZAfvVsu1eC6qqgI',
        'BQADBAADiAMAAsEaZAfUliUupYKU5AI',
    ]
    bot.sendDocument(chat_id, random.choice(my_shuffle(gifs)))
    print 'Sent'
