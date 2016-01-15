#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random


def job(bot):
    print("Sending message...")
    msg = "É sexta-feira, POHA!"
    chat_id = "-58208727"
    bot.sendMessage(chat_id, msg)
    bot.sendChatAction(chat_id, 'upload_document')
    # gifs = [
    #     'BQADBAADeQMAAqwbZAeNjNm2fzVR0wI',
    #     'BQADBAADEgMAAnwYZAdLuk2uOkqL2gI',
    #     'BQADBAADSwMAAoQYZAevJ86wPaeRxwI',
    #     'BQADBAADuwMAAj8bZAfJzPzXdPh7jwI',
    # ]
    bot.sendDocument(chat_id, 'BQADBAADygQAAlsYZAcxL0KdDKX4GQI')
