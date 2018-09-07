import os
import re
import time
from modules import twitter_api
current_module = ''


def fetch_keys():
    pass


def output(message):
    global current_module
    if current_module == '':
        time.sleep(.1)
        print('> %s' % message)
        idle()
    else:
        time.sleep(.1)
        print('>/%s/ %s' % (current_module, message))
        idle()


def idle():
    global current_module
    if current_module != '':
        __response = input('>/%s/ ' % current_module)
        main_menu(__response)
    else:
        __response = input('> ')
        main_menu(__response)


def main_menu(response):
    if response == "Help" or response == "help":
        output("This is the help screen")

    elif "use=" in response:
        global current_module
        rand, __module = re.split('=', response)
        current_module = __module
        output('Module %s is now selected')
        if __module == "twitter":
            twitter_api.options()
        elif __module == "fullcontact":
            pass



    elif response == "exit":
        os._exit(0)
    else:
        output("Im sorry I didn't quite catch that")
