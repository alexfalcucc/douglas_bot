#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random


def job(bot):
    print("Sending message...")
    msg = "Boa noite à todos!"
    bot.sendMessage("-58208727", msg)
    bot.sendChatAction("-58208727", 'upload_document')
    gifs = [
        'BQADBAADeQMAAqwbZAeNjNm2fzVR0wI',
        'BQADBAADEgMAAnwYZAdLuk2uOkqL2gI',
        'BQADBAADSwMAAoQYZAevJ86wPaeRxwI',
        'BQADBAADuwMAAj8bZAfJzPzXdPh7jwI',
    ]
    bot.sendDocument("-58208727", random.choice(gifs))
    bot.sendDocument("-58208727", random.choice(gifs))
