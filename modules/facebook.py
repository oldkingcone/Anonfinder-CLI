import os
import re
import platform
import sys


value_dict = {"first_name": "", "middle_name": "", "last_name": ""}
help_options = ""


def help_menu():
    output(help_options, "Facebook")


def exit_program():
    output("Thank you for using AnonFinder! <3", "Facebook")
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
            output("%s as been set to %s" % (attribute, value), "Facebook")
        else:
            output("Refer to help list for available attributes.", "Facebook")

    except ValueError or TypeError:
        output("Refer to help list on how to use set.", "Facebook")


def list_profiles():
    __profile = []

    for profile in os.listdir('workspace/'):
        __profile.append(profile)

    output(__profile, "Facebook")
    __profile.clear()


def output(msg, *prompt):
    if prompt:
        print("[%s]> %s" % (prompt[0], msg))
    else:
        print("> %s" % msg)


def run():
    pass


def main():
    output("Welcome to the Facebook module, type help to get started!", "Facebook")
    alive = True
    while alive:
        user_input = input("[Facebook]> ")

        if user_input == "back":
            alive = False
        elif user_input == "help":
            help_menu()

        elif user_input == "clear":
            clear()

        elif user_input == "list":
            list_profiles()

        elif "set" in user_input:
            set_value(user_input)

        elif user_input == "exit":
            exit_program()

        elif user_input == "run":
            run()

        else:
            output("Sorry I didn't quite understand that.", "Facebook")
