import sys
import re
import os
import platform

# todo Figure out values and how to make linkedin requests and what data can be used!

value_dict = {}
help_options = ""


def output(msg, *prompt):
    if prompt:
        print("[%s]> %s" % (prompt[0], msg))
    else:
        print("> %s" % msg)


def list_profiles():
    __profile = []

    for profile in os.listdir('workspace/'):
        __profile.append(profile)

    output(__profile, "Linkedin")
    __profile.clear()


def set_value(param):
    try:
        cmd, attribute, value = re.split(' ', param)

        if attribute in value_dict:
            value_dict[attribute] = value
            output("%s as been set to %s" % (attribute, value), "Linkedin")
        else:
            output("Refer to help list for available attributes.", "Linkedin")

    except ValueError or TypeError:
        output("Refer to help list on how to use set.", "Linkedin")


def clear():
    if platform.system() == "Linux":
        os.system("clear")
    elif platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def exit_program():
    output("Thank you for using AnonFinder! <3", "Linkedin")
    sys.exit(0)


def help_menu():
    output(help_options, "Linkedin")


def show():
    output(value_dict, "Linkedin")


def reset():
    for attribute in value_dict:
        value_dict[attribute] = ''

    output("all fields cleared . . .", "Linkedin")


def run():
    pass


def main():
    output("Welcome to the Linkedin module, type help to get started!", "Linkedin")
    alive = True
    while alive:
        user_input = input("[Linkedin]> ")

        if user_input == "help":
            help_menu()

        elif user_input == "back":
            alive = False

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
            output("Sorry I didn't quite understand that.", "Linkedin")


if __name__ == '__main__':
    main()
