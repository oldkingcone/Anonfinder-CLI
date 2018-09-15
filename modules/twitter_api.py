from utilities import utillities
import time
import re
import os
target = ""
search_level = ""


def get_target():
    global target
    return target


def get_sl():
    global search_level
    return search_level


def set_target(param):
    global target
    target = param


def set_search_level(param):
    global search_level
    search_level = param


def output(message):

    if utillities.get_cm() == '':
        time.sleep(.1)
        print('> %s' % message)
        idle()

    else:
        time.sleep(.1)
        print('>[%s] %s' % (utillities.get_cm(), message))
        idle()


def idle():

    if utillities.get_cm() != '':
        __response = input('>[%s] ' % utillities.get_cm())
        options(__response)
    else:
        __response = input('> ')
        options(__response)


def options(response):
    if response == "memes":
        try:
            command, option = re.split(response)
        except ValueError:
            output("Im sorry I didn't quite catch that")
    if response == "denk":
        output("wow thats a meme")
    if response == "wow":
        output("wooooooooooow")
    if response == "exit":
        os._exit(0)
    if response == "back":
        utillities.set_cm("")
        output("returning back to main menu.")


 
def main():
    idle()
