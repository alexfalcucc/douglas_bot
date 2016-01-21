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
import json


# Regular Expression to remove html tags r'<\/?\w+\s*[^>]*?\/?>'
pattern = re.compile(u'<\/?\w+\s*[^>]*?\/?>', re.DOTALL | re.MULTILINE | re.IGNORECASE | re.UNICODE)


def get_simsimi_reply(user_text):
    http = urllib3.PoolManager()
    api_key = "0da76951-3f0d-49be-9be3-e014f658644b"
    url = (
        "http://sandbox.api.simsimi.com/request.p"
        "?key=" + api_key + "&lc=pt&ft=1.0&text=" + urllib.quote_plus(user_text)
    )
    r = http.request('GET', url)
    status = r.status
    name = 'simsimi'
    text = r.data.strip()
    response_text = pattern.sub(" ", text)
    if response_text:
        try:
            dict_ = json.loads(response_text)
            reply_text = dict_.get('response')
        except SyntaxError:
            reply_text, status, name = get_ed_reply(user_text)
        print reply_text
        if not reply_text:
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
