from modules import twitter
from modules import fullcontact
from modules import whitepages
from modules import facebook
from modules import linked_in
import sys
import re
import os
import platform
import shutil
from utilities import utilities

exclusion_list = []
module_list = ["twitter", "fullcontact", "whitepages", "linkedin", "facebook"]
value_dict = {"first_name": "", "last_name": "", "twitter": ""}
help_options = """help        displays this screen.
  make        creates a profile based on desired name, usage: 'make [PROFILE NAME]'.
  delete      deletes target profile, usage: 'delete [PROFILE NAME]'.
  run         runs queries based on information given.
  set         sets search fields, usage 'set [ATTRIBUTE] [VALUE]'.
  show        displays current search fields.
  clear       clears console or terminal of output.
  exit        exits program.
  exclude     excludes certain modules from run script to remove nonexistent bloat data, usage: 'exclude [MODULE]'.
  final       creates final report based off of scans already within target profile, usage: 'final [PROFILE]'.
  list        lists all valid profiles within workspace directory.
  about       Shows information about AnonFinder.
  
  Available attributes:
    First name as 'first_name'
    Last name as 'last_name'
    Twitter as twitter_handle
    
  Available modules:
    Twitter as 'twitter'
    FullContact as 'fullcontact'
    Whitepages as 'whitepages'
    Linkedin as linkedin
    Facebook as facebook
    
  Modules coming soon!(these modules require a paid key to access data)
    Whitepages
"""


def greeting():
    output('Welcome to AnonFinder, type help to get started.')


def output(msg, *prompt):
    if prompt:
        print("[%s]> %s" % (prompt[0], msg))
    else:
        print("> %s" % msg)


def make_profile(option):
    try:
        cmd, profile = re.split(' ', option)

        try:
            os.mkdir('workspace/%s' % profile)
            try:
                for module in module_list:
                    os.mkdir("workspace/%s/%s" % (profile, module))
            except FileExistsError or PermissionError:
                output("Error when creating folders for module output!")
            output("%s profile has been created!" % profile)
        except FileExistsError or PermissionError:
            output("Failed to create profile directory %s!" % profile)

    except ValueError or TypeError:
        output("Refer to help list on how to use make.")


def delete_profile(option):
    try:
        cmd, profile = re.split(' ', option)
        confirmation = input("> Are you sure you want to delete %s? [y/n]" % profile)

        if confirmation == "y" or confirmation == "yes":
            if os.path.isdir('workspace/%s/' % profile):
                output("Deleting profile . . .")
                try:
                    shutil.rmtree('workspace/%s/' % profile)
                except FileNotFoundError or PermissionError:
                    output("Error when deleting %s's profile!")
            else:
                output("No such profile exists!")
        else:
            output("No profiles will be deleted.")

    except ValueError or TypeError:
        output("Refer to help list on how to use delete")


def final(param):
    pass


def run():
    profile = utilities.Profile()
    profile.First_name = value_dict["first_name"]
    profile.Last_name = value_dict["last_name"]
    profile.Twitter = value_dict["twitter"]
    # todo plan out how profile objects attributes will be assigned and algorithm on data discovery.


def list_profiles():
    __profile = []

    for profile in os.listdir('workspace/'):
        __profile.append(profile)

    output(__profile)
    __profile.clear()


def use(option):
    try:
        cmd, module = re.split(' ', option)

        if module in module_list:
            if module == "twitter":
                twitter.main()
            elif module == "fullcontact":
                fullcontact.main()
            elif module == "whitepages":
                whitepages.main()
            elif module == "linkedin":
                linked_in.main()
            elif module == "facebook":
                facebook.main()

        else:
            output("%s is not a valid module, please refer to the help list for available modules." % module)

    except ValueError or TypeError:
        output("Refer to help list on how to use 'use'.")


def set_value(param):
    try:
        cmd, attribute, value = re.split(' ', param)

        if attribute in value_dict:
            value_dict[attribute] = value
            output("%s as been set to %s" % (attribute, value))
        else:
            output("Refer to help list for available attributes.")

    except ValueError or TypeError:
        output("Refer to help list on how to use set.")


def clear():
    if platform.system() == "Linux":
        os.system("clear")
    elif platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def exit_program():
    output("Thank you for using AnonFinder! <3")
    sys.exit(0)


def exclude(option):
    for arg in re.split(' ', option):
        if arg in module_list:
            exclusion_list.append(arg)
        else:
            pass


def help_menu():
    output(help_options)


def show():
    output(value_dict)


def reset():
    for attribute in value_dict:
        value_dict[attribute] = ''

    output("all fields cleared . . .")


def main():
    greeting()
    alive = True

    while alive:
        user_input = input("> ")

        if user_input == "exit":
            exit_program()

        elif "exclude" in user_input:
            exclude(user_input)

        elif user_input == "help":
            help_menu()

        elif user_input == "run":
            run()

        elif "delete" in user_input:
            delete_profile(user_input)

        elif "set" in user_input:
            set_value(user_input)

        elif "make" in user_input:
            make_profile(user_input)

        elif user_input == "clear":
            clear()

        elif user_input == "list":
            list_profiles()

        elif user_input == "final":
            final(user_input)

        elif user_input == "show":
            show()

        elif "use" in user_input:
            use(user_input)

        elif user_input == "clear_fields":
            reset()

        else:
            output("Sorry I didn't quite understand that.")


if __name__ == '__main__':
    main()
