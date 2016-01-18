# simulate GUI
from pyvirtualdisplay import Display
# need selenium webdriver to set the firefoxprofile
from selenium import webdriver as old_webdriver
# webdriverplus is a fork of selenium2 webdriver with added features
import webdriverplus as webdriver


class QuoteCoffee(object):
    """return the current quote coffe for the user"""
    def __init__(self):
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
        for value in values.find('td'):
            print value.text
        self.browser.close()
        self.display.stop()

if __name__ == '__main__':
    QuoteCoffee().run()
