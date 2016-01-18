#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib3
import webdriverplus as webdriver
import os
import pickledb
# simulate GUI
from pyvirtualdisplay import Display
# need selenium webdriver to set the firefoxprofile
from selenium import webdriver as old_webdriver
# webdriverplus is a fork of selenium2 webdriver with added features
from utils.utils import convert_str_to_dict


def get_quotes(db, bot, chat_id):
    coins_quotes, status = get_current_quote()
    dolar_value, euro_value = float(coins_quotes.get('dolar').get('cotacao')), float(coins_quotes.get('euro').get('cotacao'))
    dolar_var, euro_var = coins_quotes.get('dolar').get('variacao'), coins_quotes.get('euro').get('variacao')
    updated_at = coins_quotes.get('atualizacao')
    quote_coffee = QuoteCoffee(db).get_quote_coffee()
    msg = """
    Dólar: R$ %.2f (%s)\nEuro: R$ %.2f (%s)\nCafé Arábica 6 Sc: R$ %.2f (%s)\nAtualizado em %s hrs
    """ % (dolar_value, dolar_var, euro_value, euro_var,
           quote_coffee.get('quote_value', ''),
           quote_coffee.get('rate', ''),
           updated_at.replace('\/', '-').replace('  -', 'às'),)
    return msg


def get_current_quote():
    """return dolar and euro quotes"""
    http = urllib3.PoolManager()
    url = "http://developers.agenciaideias.com.br/cotacoes/json"
    r = http.request('GET', url)
    status = r.status
    str_reponse = r.data.strip()
    dict_reponse = convert_str_to_dict(str_reponse)
    return dict_reponse, status


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
        browser = self.browser.get(self.url)

        latest_quote = browser.find('.cotacao tbody tr')
        rows = [row for row in latest_quote if 'Franca/SP' in row.text]
        values = rows[0]
        quote_query = {
            'city': values.find('td')[0].text,
            'quote_value': float(values.find('td')[1].text.replace(',', '.')),
            'rate': values.find('td')[2].text,
        }
        self.db.set('coffe_quote', quote_query)
        self.browser.close()
        self.display.stop()

    def get_quote_coffee(self):
        return self.db.get('coffe_quote')

if __name__ == '__main__':
    QuoteCoffee(db=pickledb.load(os.environ['HOME'] + '/douglas_db/douglas.db', True)).run()
