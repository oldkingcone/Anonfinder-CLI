import os
import re
import time
from modules import twitter_api
current_module = ''


def setcm(param):
    global current_module
    current_module = param


def getcm():
    global current_module
    return current_module


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
        idle()
# This command will select and set the current module so that its passed to the correct module handler.
    elif "use=" in response:
        global current_module
        rand, __module = re.split('=', response)
        current_module = __module
        if __module == "twitter":
            while current_module == "twitter":
                twitter_api.main()
        elif __module == "fullcontact":
                pass
# This command will exit the program with a 0 code.
    elif response == "exit":
        os._exit(0)
# This will tell the user that they used an undefined command.
    else:
        output("Im sorry I didn't quite catch that")
        idle()
