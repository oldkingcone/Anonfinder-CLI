from utilities import utillities
import time
import re
import os
import platform
import twitter
import json
import datetime

target = ""
key_path = "key/twitter/twitter.txt"
search_level = 0
help_screen = "Static Commands: \n " \
              "    help - Displays this screen. \n" \
              "     show - Shows current configurations for this module. \n" \
              "     back - Brings you back to the main screen to select other modules or " \
              "configure any global parameters. \n" \
              "     exit - this command is a global command will work at any point to end AnonFinder. \n" \
              "     run - this command will run the script with the current configurations that are set. \n" \
              "     Dynamic Commands: \n" \
              "     set= - This command will set any of the parameters ex. set=target=@twitter_handle. \n" \
              "     *** Parameters are case sensitive! for target use target, all lowercase. \n" \
              "     *** To set search level or search type, use sl in all lowercase.\n " \
              "     The Search Levels: \n" \
              "     0 - Basic search, it will look for the minimum amount of data for that user. \n" \
              "     1 - Medium search, it will look for basic information and " \
              "pull up the most recent 5 twitter posts. \n" \
              "     2 -  Advanced search, This search will do all of the above and pull down any media from posts " \
              "or profile pictures."
commands = ["show", "help", "exit", "back", "run", "clear"]


def get_os_name():
    os_name = platform.system()
    return os_name


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
# new methods go below this line


def fetch_key(key_type):

    path = '..\key/twitter/twitter.txt'
    file = open(key_path, "r")
    keys = file.read()
    con, cons, tk, tks = re.split('\n', keys)

    if key_type == "con":
        return con
    if key_type == "cons":
        return cons
    if key_type == "tk":
        return tk
    if key_type == "tks":
        return tks


def data_output(data):
    now = datetime.datetime.now()
    if search_0():
        # make the raw output file of the search
        day = now.day
        month = now.month
        year = now.year
        date = str('%s-%s-%s' % (year, month, day))
        file_name = 'twitter_scan-%s.json' % date
        path = '../workspace/%s' % utillities.get_info()
        pass
        # make the compiled data file based on search level



def search_0():
    api = twitter.Api()
    try:
        response = api.GetUser(screen_name=target, return_json=True)
    except Exception:
        output("Im sorry but there was an error searching for that person.")

    data = json.dumps(response, indent=4)
    data_output(data)


def search_1():
    pass


def search_2():
    pass


def run():
    # output("Running on current configurations . . .\n"
           # "Currnet Level is: %s, and Target is: %s" % (get_sl(), get_target()))

    if get_sl() == 0:
        search_0()

    else:
        output("Something went wrong :( ")


def options(response):
    if response in commands:
        if response == "help":
            output(help_screen)
        if response == "exit":
            os._exit(0)
        if response == "back":
            utillities.set_cm("")
            utillities.output("returning to main menu")
        if response == "show":
            output("Current configurations: \n"
                   "    current search level is: %s \n"
                   "    current target is: %s \n" % (get_sl(), get_target()))
        if response == "run":
            run()
        if response == "clear":
            if get_os_name() == "Windows":
                os.system('cls')
                idle()
            elif get_os_name() == "Linux":
                os.system("clear")
                idle()
            else:
                os.system("clear")
                idle()
    else:
        if "set" in response:
            try:
                command, option, value = re.split('=', response)
            except ValueError:
                output("Error when processing set command")
            if option == "target" or option == "sl":
                if option == "target":
                    set_target(value)
                    output("Target has been set to: %s" % value)
                elif option == "sl":
                    try:
                        if int(value) <= 2 & int(value) >= 0:
                            set_search_level(value)
                            output("Search level is now set to: %s " % value)
                        else:
                            output("Invalid level")
                    except ValueError:
                        output("Invalid usage")


            else:
                output("value given is not an acceptable value.")



def main():
    idle()



