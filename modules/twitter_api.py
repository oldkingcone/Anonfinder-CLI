from utilities import utillities
import time
import re
import os
current_module = "twitter"
target = ""
search_level = ""


def output(message):

    if utillities.getcm() == '':
        time.sleep(.1)
        print('> %s' % message)
        idle()

    else:
        time.sleep(.1)
        print('>/%s/ %s' % (utillities.getcm(), message))
        idle()


def idle():

    if utillities.getcm() != '':
        __response = input('>/%s/ ' % utillities.getcm())
        options(__response)
    else:
        __response = input('> ')
        options(__response)


def options(response):
    if "show" in response:

        output("you just used the show command wow and you thin is %s" % utillities.getcm())
        idle()
    if response == "exit":
        os._exit(0)
    if response == "back":
        utillities.setcm('')
        utillities.idle()



def main():
    output("Current module is now Twitter")
    idle()
