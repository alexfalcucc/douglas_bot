#!/usr/bin/env python
# encoding: utf-8
#
# Robô Ed Telegram Bot
# This program is dedicated to the public domain under the CC0 license.
import urllib3


def get_ed(text):
    http = urllib3.PoolManager()
    url = 'http://www.ed.conpet.gov.br/mod_perl/bot_gateway.cgi?server=0.0.0.0%3A8085&charset_post=utf-8&charset=utf-8&pure=1&js=0&tst=1&msg=' + text
    r = http.request('GET', url)
    return r.data.strip()
