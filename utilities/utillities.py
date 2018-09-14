import os
import re
import time
from modules import twitter_api
current_module = ''
workspace = ''
target_name = ''
help_menu = "Command List: \n" \
            "   To show this help screen, type 'help' or 'Help' \n" \
            "   To use a module or script, type 'use= ' and after the equal sign the desired script \n"\
            "   To exit the program, type 'exit' \n"


def get_info():
    global workspace
    global target_name
    return workspace, target_name


def set_cm(param):
    global current_module
    current_module = param


def get_cm():
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
        global help_menu
        output(help_menu)
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
