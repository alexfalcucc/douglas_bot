#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# SimSimI Telegram Bot
# This program is dedicated to the public domain under the CC0 license.
import urllib
import urllib3
import re
from utils.utils import convert_str_to_dict

# Regular Expression to remove html tags r'<\/?\w+\s*[^>]*?\/?>'
pattern = re.compile(u'<\/?\w+\s*[^>]*?\/?>', re.DOTALL | re.MULTILINE | re.IGNORECASE | re.UNICODE)


def get_simsimi_reply(text):
    http = urllib3.PoolManager()
    url = ("http://www.simsimi.com/requestChat?lc=pt&ft=1.0&req=" + urllib.quote_plus(text) +
           "&uid=83530944&did=0")
    r = http.request('GET', url)
    text = r.data.strip()
    response_text = pattern.sub(" ", text)
    dict_ = convert_str_to_dict(response_text)
    reply_text = dict_.get('res').get('msg')
    return reply_text if r.status == 200 and 'I HAVE NO RESPONSE' not in reply_text\
        else 'Desculpe, não entendi.'
