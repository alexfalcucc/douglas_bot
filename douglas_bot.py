import sys
import time
import random
import datetime
import telepot


def handle(msg):
    print msg
    chat_id = msg['chat']['id']
    command = msg['text']
    name = msg['from']['first_name']

    print 'Got command: %s' % command

    if command == '@doguinha_bot morning':
        bot.sendMessage(chat_id, "Good morning, {}!".format(name))
    elif command == '/time':
        bot.sendMessage(chat_id, str(datetime.datetime.now()))

bot = telepot.Bot('142375463:AAFf1mMbT1O3rxOCaQ8j0hzdU_Hc5Wh4kj0')
bot.notifyOnMessage(handle)
print 'I am listening ...'

while 1:
    time.sleep(10)
