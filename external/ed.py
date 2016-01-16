#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Robô Ed Telegram Bot
# This program is dedicated to the public domain under the CC0 license.
import urllib
import urllib3
import re


# Regular Expression to remove html tags r'<\/?\w+\s*[^>]*?\/?>'
pattern = re.compile(u'<\/?\w+\s*[^>]*?\/?>', re.DOTALL | re.MULTILINE | re.IGNORECASE | re.UNICODE)


def get_ed_reply(text):
    http = urllib3.PoolManager()
    url = ("http://www.ed.conpet.gov.br/mod_perl/bot_gateway.cgi?server=0.0.0.0"
           "%3A8085&charset_post=utf-8&charset=utf-8&pure=1&js=0&tst=1&msg=") + urllib.quote_plus(text)
    r = http.request('GET', url)
    status = r.status
    name = 'ed'
    text = r.data.strip()
    reply_text = pattern.sub(" ", text)
    if status != 200 or '408 Request Timeout' in reply_text:
        reply_text = "Desculpe, não entendi."
    return reply_text.lower(), status, name


def count_ed_mgs(db):
    """
    Just return how many times Ed answered.
    """
    try:
        count = db.get('ed_info')['qty_answed_message']
    except:
        count = 1
    return count
