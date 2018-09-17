import os
import re
import time
from modules import twitter_api
current_module = ''
workspace = ''
target_name = ''
help_menu = "Commands: \n" \
            "   help -  Displays the help screen.\n" \
            "   exit - Will exit out of AnonFinder. \n" \
            "   use= - This command will select a script to use ex. use=twitter"


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
        print('>[%s] %s' % (current_module, message))
        idle()


def idle():
    global current_module
    if current_module != '':
        __response = input('>[%s] ' % current_module)
        main_menu(__response)
    else:
        __response = input('> ')
        main_menu(__response)


def main_menu(response):
    if response == "Help" or response == "help":
        global help_menu
        output(help_menu)
# This command will select and set the current module so that its passed to the correct module handler.
    if "use=" in response:
        try:
            global current_module
            rand, __module = re.split('=', response)
            if __module == "twitter" or __module == "fullcontact":
                current_module = __module
            else:
                output("oi use a real script.")
        except ValueError:
            output("Im sorry I didn't quite catch that")

        if __module == "twitter":
            while current_module == "twitter":
                twitter_api.main()
        elif __module == "fullcontact":
                pass
        else:
            output("Please use a real script.")
# This command will exit the program with a 0 code.
    elif response == "exit":
        os._exit(0)
# This will tell the user that they used an undefined command.
    else:
        output("Im sorry I didn't quite catch that")
