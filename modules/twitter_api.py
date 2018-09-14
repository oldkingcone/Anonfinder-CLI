from utilities import utillities
import time
import re
import os
current_module = "twitter"
target = ""
search_level = ""


def output(message):

    if utillities.get_cm() == '':
        time.sleep(.1)
        print('> %s' % message)
        idle()

    else:
        time.sleep(.1)
        print('>/%s/ %s' % (utillities.get_cm(), message))
        idle()


def idle():

    if utillities.get_cm() != '':
        __response = input('>/%s/ ' % utillities.get_cm())
        options(__response)
    else:
        __response = input('> ')
        options(__response)


def options(response):
    if "show" in response:

        output("you just used the show command wow and you thin is %s" % utillities.get_cm())
        idle()
    elif response == "exit":
        os._exit(0)
    elif response == "back":
        utillities.set_cm('')
        utillities.idle()
    elif response == "Help" or "help":
        output()
    else:
        output("Im sorry I didn't quite catch that.")


def main():
    output("Current module is now Twitter")
    idle()
