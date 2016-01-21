#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# SimSimI Telegram Bot
# This program is dedicated to the public domain under the CC0 license.
import urllib
import urllib3
import re
from utils.utils import convert_str_to_dict
from external.ed import get_ed_reply


# Regular Expression to remove html tags r'<\/?\w+\s*[^>]*?\/?>'
pattern = re.compile(u'<\/?\w+\s*[^>]*?\/?>', re.DOTALL | re.MULTILINE | re.IGNORECASE | re.UNICODE)


def get_simsimi_reply(user_text):
    http = urllib3.PoolManager()
    url = ("http://www.simsimi.com/requestChat?lc=pt&ft=1.0&req=" + urllib.quote_plus(user_text) +
           "&uid=83530944&did=0")
    r = http.request('GET', url)
    status = r.status
    name = 'simsimi'
    text = r.data.strip()
    response_text = pattern.sub(" ", text)
    if response_text:
        try:
            convert_str_to_dict(response_text)
            dict_ = convert_str_to_dict(response_text)
            reply_text = dict_.get('res').get('msg')
        except SyntaxError:
            reply_text, status, name = get_ed_reply(user_text)
        if 'I HAVE NO RESPONSE' in reply_text:
            print 'I HAVE NO RESPONSE'
            reply_text, status, name = get_ed_reply(user_text)
            print reply_text
    else:
        reply_text, status, name = get_ed_reply(user_text)
    return reply_text, status, 'simsimi'


def count_simsimi_msg(db):
    """
    Just return how many times simsimi answered.
    """
    try:
        count = db.get('simsimi_info')['qty_answed_message']
    except:
        count = 1
    return count
