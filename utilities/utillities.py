import os
import re
import time
import platform
import modules.twitter_api as twitter
import shutil
current_module = ''
profile_name = ''
commands = ["help", "exit", "clear", "show", "list"]

help_menu = "Commands: \n" \
            "   help -  Displays the help screen.\n" \
            "   exit - Will exit out of AnonFinder. \n" \
            "   clear - to clear the screen (global command) \n" \
            "   use= - This command will select a script to use ex. use=twitter \n" \
            "   list - Lists profiles within the workspaces directory. \n" \
            "   show - displays currently selected profile to be used. \n" \
            "   mkp= - makes profile within the workspaces directory ex. mkp=filename \n" \
            "   remove - this command removes a profile ex. remove=PROFILE=profile_name \n" \
            "   set= - this command sets the profile to be used. ex. set=profile=profile_name \n" \
            "   ***This is not a terminal emulator, commands will not work here only the commands provided will.\n" \
            "   ***AnonFinder does not have multi command usage, you will have to type each command when setting" \
            " parameters. \n" \
            "   Scripts available: \n" \
            "   * Twitter as twitter        * FullContact as fullcontact \n" \
            "   * Facebook as facebook      * Have I Been Pwned as hibp \n" \
            "   * Linkedin as link          * WhitePages as wp \n" \
            "   * Google as google " \



def get_os_name():
    operating_system = platform.system()
    return operating_system


def set_info(param):
    global profile_name
    profile_name = param


def get_info():
    global profile_name
    return profile_name


def set_cm(param):
    global current_module
    current_module = param


def get_cm():
    global current_module
    return current_module


def straight(msg):
    print('* %s \r' % msg)


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
    if response in commands:
        if response == "help":
            output(help_menu)
        if response == "exit":
            os._exit(0)
        if response == "clear":
            if get_os_name() == "linux":
                os.system("clear")
                idle()
            if get_os_name() == "Windows":
                os.system("cls")
                idle()
            else:
                os.system("clear")
                idle()
        if response == "show":
            output("Selected profile is: %s" % get_info())
        if response == "list":
            dirs = os.listdir("workspaces/")
            output("Valid profiles within the workspace directory: %s" % dirs)

    else:
        if "mkp" in response:
            try:
                command, profile = re.split("=", response)
            except ValueError:
                output("Error when processing command.")
            try:
                os.mkdir("workspaces/%s" % profile)
                output("Profile folder has been created for : %s" % profile)
            except FileExistsError or PermissionError:
                output("Error when creating profile.")
        if "use" in response:
            try:
                command, option = re.split("=", response)
            except ValueError:
                output("error when processing use command")

            if option == "twitter":
                set_cm("twitter")
                while current_module == get_cm():
                    twitter.idle()
        if "set" in response:
            try:
                command, option, value = re.split("=", response)
            except ValueError:
                output("error when processing set command")
            if option == "profile":
                if os.path.exists("workspaces/%s" % value):
                    set_info(value)
                    output("%s is now the selected profile" % value)
                else:
                    output("Please use a profile that is within the workspace directory")
            else:
                output("Invalid syntax and or error when processing")
        if "remove" in response:
            try:
                command, option, value = re.split("=", response)
            except ValueError:
                output("Error when processing remove command")

            if option == "PROFILE":
                if os.path.exists("workspaces/%s/" % value):
                    try:
                        shutil.rmtree("workspaces/%s" % value)
                    except PermissionError:
                        output("invalid permissions to remove profile and its content")
                    idle()
                else:
                    output("Im sorry there was an error")
                    idle()
        if "view" in response:
            if get_info() == "":
                output("Please specify a profile by setting it with the set command.")
            else:
                try:
                    command, option, modules, value = re.split("=", response)
                except ValueError:
                    output("Error when processing the view command.")

                if option == "files":
                    content = os.listdir("workspaces/%s/%s/" % (get_info(), modules))
                    output(content)
                else:
                    pass

                if option == "data":
                    path = "workspaces/%s/%s/%s" % (get_info(), modules, value)
                    with open(path) as file:
                        for line in file.readlines():
                            straight(line)
                    idle()
                else:
                    pass



        else:
            output("Im sorry I didn't quite catch that")





