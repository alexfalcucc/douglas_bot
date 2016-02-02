#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib3
import webdriverplus as webdriver
import os
import pickledb
import json
# simulate GUI
from pyvirtualdisplay import Display
# need selenium webdriver to set the firefoxprofile
from selenium import webdriver as old_webdriver
# webdriverplus is a fork of selenium2 webdriver with added features
from utils.utils import utf8_encode


def get_quotes(db, bot, chat_id):
    coins_quotes, status = get_current_quote()
    dolar_value, euro_value = float(coins_quotes.get('dolar').get('cotacao')), float(coins_quotes.get('euro').get('cotacao'))
    dolar_rate, euro_rate = coins_quotes.get('dolar').get('variacao'), coins_quotes.get('euro').get('variacao')
    updated_at = utf8_encode(coins_quotes.get('atualizacao'))
    quote_coffee = QuoteCoffee(db).get_quote_coffee()
    values = {
        'dolar': dolar_value,
        'dolar_rate': dolar_rate,
        'euro_value': euro_value,
        'euro_rate': euro_rate,
        'coffee_value': quote_coffee.get('quote_coffee', ''),
        'quote_rate': quote_coffee.get('rate', ''),
        'updated_at': updated_at
    }
    msg = """
        Dólar: R$ {dolar}({dolar_rate})\nEuro: R$ {euro_value}({euro_rate})\nCafé Arábica 6 sc: R$ {coffee_value}\nAtualizado em {updated_at} hrs
    """
    msg = msg.format(**values)
    return msg.strip()


def get_current_quote():
    """return dolar and euro quotes"""
    http = urllib3.PoolManager()
    url = "http://developers.agenciaideias.com.br/cotacoes/json"
    r = http.request('GET', url)
    status = r.status
    str_reponse = r.data.strip()
    return json.loads(str_reponse), status


class QuoteCoffee(object):
    """return the current quote coffe for the user"""
    def __init__(self, db):
        self.db = db
        self.display = Display(visible=0, size=(1024, 768))
        # Latest Chrome on Windows
        self.fake_browser = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
        # be able to setup a firefox profile
        self.ff_profile = old_webdriver.firefox.firefox_profile.FirefoxProfile()
        # sets the download notification off
        self.ff_profile.set_preference('browser.download.manager.showWhenStarting', False)
        # sets the user agent, latest windows chrome is most common
        self.ff_profile.set_preference('general.useragent.override', self.fake_browser)
        # sets to not show annoying download panels
        # set driver
        self.display.start()
        self.browser = webdriver.WebDriver(firefox_profile=self.ff_profile)
        # sign in url
        self.url = 'http://www.noticiasagricolas.com.br/cotacoes/cafe/cafe-arabica-mercado-fisico-tipo-6-duro'

    def run(self):
        print "Updating..."
        browser = self.browser.get(self.url)

        latest_quote = browser.find('.cotacao tbody tr')
        rows = [row for row in latest_quote if 'Franca/SP' in row.text]
        values = rows[0]
        quote_query = {
            'city': values.find('td')[0].text,
            'quote_value': float(values.find('td')[1].text.replace(',', '.')),
            'rate': values.find('td')[2].text,
        }
        print quote_query
        self.db.set('coffe_quote', quote_query)
        self.browser.close()
        self.display.stop()

    def get_quote_coffee(self):
        return self.db.get('coffe_quote')

if __name__ == '__main__':
    QuoteCoffee(db=pickledb.load(os.environ['HOME'] + '/douglas_db/douglas.db', True)).run()
