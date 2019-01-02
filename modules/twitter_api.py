import twitter
import os
import re
import platform
import sys


value_dict = {"twitter_handle": ""}
help_options = ""


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
    output(value_dict)


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
    # todo add keys later!!
    api = twitter.Api()
    api.GetUser()


def main():
    output("Welcome to the Twitter module, type help to get started!", "Twitter")

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

        else:
            output("Sorry I didn't quite understand that.", "Twitter")


if __name__ == '__main__':
    main()
