import twitter
import os
import re
import platform
import sys
import time

value_dict = {"twitter_handle": "", "profile": ""}
help_options = ""
key_dict = {"consumer_key": "", "consumer_secret_key": "", "access_token_key": "", "access_token_secret": ""}


def get_keys():
    temp = []
    with open('key/twitter/twitter.txt') as file:
        for block in re.split('/', file.read()):
            temp.append(block)

        for key in temp:
            value = key.split(':')
            key_dict[value[0]] = value[1]


def keys():
    __key_collection = []
    for key in key_dict:
        key_entry = input("Please enter %s: " % key)
        __key_collection.append(key_entry)

    if os.path.exists('key/twitter/twitter.txt'):
        with open('key/twitter/twitter.txt', "w+") as file:
            con = str(__key_collection[0])
            cons = str(__key_collection[1])
            at = str(__key_collection[2])
            ats = str(__key_collection[3])
            file.write('consumer_key:%s/consumer_secret_key:%s/access_token_key:%s/access_token_secret:%s' %
                       (con, cons, at, ats))
        get_keys()
    else:
        try:
            open("key/twitter/twitter.txt", "w")
        except PermissionError or FileExistsError:
            output("Error when creating key file!", "Twitter")

        with open('key/twitter/twitter.txt', "a") as file:
            con = str(__key_collection[0])
            cons = str(__key_collection[1])
            at = str(__key_collection[2])
            ats = str(__key_collection[3])
            file.write('consumer_key:%s/consumer_secret_key:%s/access_token_key:%s/access_token_secret:%s' %
                       (con, cons, at, ats))
        get_keys()


def help_menu():
    output(help_options, "Twitter")


def exit_program():
    output("Thank you for using AnonFinder! <3", "Twitter")
    sys.exit(0)


def clear():
    if platform.system() == "Linux":
        os.system("clear")
    elif platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def show():
    output(value_dict, "Twitter")


def set_value(param):
    try:
        cmd, attribute, value = re.split(' ', param)

        if attribute in value_dict:
            value_dict[attribute] = value
            output("%s as been set to %s" % (attribute, value), "Twitter")
        else:
            output("Refer to help list for available attributes.", "Twitter")

    except ValueError or TypeError:
        output("Refer to help list on how to use set.", "Twitter")


def list_profiles():
    __profile = []

    for profile in os.listdir('workspace/'):
        __profile.append(profile)

    output(__profile, "Twitter")
    __profile.clear()


def output(msg, *prompt):
    if prompt:
        print("[%s]> %s" % (prompt[0], msg))
    else:
        print("> %s" % msg)


def run():
    pass

def main():
    output("Welcome to the Twitter module, type help to get started!", "Twitter")
    try:
        get_keys()
    except FileNotFoundError or IndexError:

        output("No Key file has been found, please add your keys using the key command.", "Twitter")
    alive = True
    while alive:
        user_input = input("[Twitter]> ")

        if user_input == "back":
            alive = False

        elif user_input == "exit":
            exit_program()

        elif user_input == "list":
            list_profiles()

        elif "set" in user_input:
            set_value(user_input)

        elif user_input == "clear":
            clear()

        elif user_input == "help":
            help_menu()

        elif user_input == "show":
            show()

        elif user_input == "run":
            run()

        elif user_input == "key":
            keys()

        elif user_input == "keys":
            output(key_dict, "Twitter")
        else:
            output("Sorry I didn't quite understand that.", "Twitter")
