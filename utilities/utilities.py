import os
import platform
import time
current_module = ""
import re

class Options:
    custom_help = ""
    base_help = "   help - Displays this screen. \n   clear - Clears the console of all output. \n   " \
                "exit - Exits AnonFinder"
    alive = True
    profile = ""

    def __init__(self):
        pass

    def get_input(self):

            if current_module != "":
                user_input = str(input(">[%s] " % current_module))
                if user_input == "":
                    self.get_input()
                else:
                    return user_input
            else:
                user_input = str(input("> "))
                if user_input == "":
                    self.get_input()
                else:
                    return user_input

    def output(self, msg):
        if current_module != "":
            print(">[%s] %s " % (current_module, msg))

        else:
            print("> %s" % msg)


    @staticmethod
    def clear():
        if platform.system() == "Linux":
            os.system("clear")
        elif platform.system() == "Windows":
            os.system("cls")
        else:
            os.system("clear")

    def set_help(self, param):
        self.custom_help = param

    def help(self):
        help_out = "Global Commands:\n%s \n  Custom Commands:\n %s \n" % (self.base_help, self.custom_help)
        self.output(help_out)

    @staticmethod
    def exit():
        os._exit(0)

    def make_profile(self, param):
        command, value = re.split("=", param)
        path = "workspaces/%s" % value
        try:
            os.mkdir(path)
            for module in self.modules:
                os.mkdir("%s/%s" % (path, module))
        except FileExistsError or PermissionError:
            self.output("There was an error creating the profile")

    def list(self):
        file = os.listdir("workspaces/")
        self.output(file)

    @staticmethod
    def r_list():
        file = os.listdir("workspaces/")
        return file





def run_manager(email, phone, name):
    """"First stage of searching, parsing through data with FullContact and WhitePages to pull further information"""


