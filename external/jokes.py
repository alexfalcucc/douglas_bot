#!/usr/bin/env python
# -*- coding: utf-8 -*-
import webdriverplus as webdriver
import os
import pickledb
# simulate GUI
from pyvirtualdisplay import Display
# need selenium webdriver to set the firefoxprofile
from selenium import webdriver as old_webdriver
# webdriverplus is a fork of selenium2 webdriver with added features


class Joke(object):

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
        self.urls = self.get_urls()

    def run(self):
        print "Updating..."
        jokes = []
        for url in self.urls:
            driver = self.browser.get(url)
            print driver.current_url
            for joke_element in driver.find('#main article').find('.row'):
                try:
                    vote = joke_element.find('.votes').text.split()
                    if int(vote[1]) >= 100:
                        jokes.append(joke_element.find('.joke').text)
                except AttributeError:
                    print "I am not an element."
        print jokes
        self.db.set('jokes', jokes)
        print '*'*100
        print 'Updated!'
        self.browser.close()
        self.display.stop()

    def get_urls(self):
        default_url = 'http://www.osvigaristas.com.br/piadas/curtas/'
        urls = [default_url + 'pagina{}.html'.format(i)
                for i in range(2, 51)]
        urls.append(default_url)
        return urls

    def get_jokes(self):
        return self.db.get('jokes')


if __name__ == '__main__':
    Joke(db=pickledb.load(os.environ['HOME'] + '/douglas_db/douglas.db', True)).run()
