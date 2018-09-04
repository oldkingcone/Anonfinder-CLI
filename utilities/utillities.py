import os
import re
import time

current_module = ''


def fetch_keys():
    pass


def output(message):
    global current_module
    if current_module == '':
        print('> %s' % message)
        time.sleep(1)
        idle()
    else:
        print('>/%s/ %s' % (current_module, message))
        idle()


def idle():
    global  current_module
    if current_module == '':
        __response = input('>/%s/ ' % current_module)
        options(__response)
    else:
        __response = input('> ')
        options(__response)


def options(response):
    if response == "Help" or response == "help":
        output("This is the help screen")
    elif "use=" in response:
        global current_module
        rand, __module = re.split('=', response)
        current_module = __module

    elif response == "exit":
        os._exit(0)
    else:
        output("Im sorry I didn't quite catch that")
