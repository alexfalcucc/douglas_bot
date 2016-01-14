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
    text = r.data.strip()
    reply_text = pattern.sub(" ", text)
    return reply_text if r.status == 200 else 'Desculpe, não entendi.'
