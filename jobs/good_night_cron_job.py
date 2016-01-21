#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
from utils.utils import my_shuffle


def job(bot):
    print("Sending message...")
    msg = "Fui!"
    chat_id = "-58208727"
    bot.sendMessage(chat_id, msg)
    bot.sendChatAction(chat_id, 'upload_document')
    gifs = [
        'BQADBAADeQMAAqwbZAeNjNm2fzVR0wI',
        'BQADBAADEgMAAnwYZAdLuk2uOkqL2gI',
        'BQADBAADSwMAAoQYZAevJ86wPaeRxwI',
        'BQADBAADuwMAAj8bZAfJzPzXdPh7jwI',
    ]
    bot.sendDocument(chat_id, random.choice(my_shuffle(gifs)))
    print 'Sent'
