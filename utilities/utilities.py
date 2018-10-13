import os
import platform
import time
current_module = ""


class Options:
    custom_help = ""
    base_help = ""
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
        help_out = "Global commands: \n %s \n Commands: \n %s" % (self.base_help, self.custom_help)
        self.output(help_out)

    @staticmethod
    def exit():
        os._exit(0)
