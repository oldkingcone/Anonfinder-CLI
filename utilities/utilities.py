import os
import platform
import re
from modules import whitepages
from modules import twitter_api
from modules import fullcontact

current_module = ""


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

    @staticmethod
    def output(msg):
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


class Twitter(Options):
    def __init__(self, *profile):
        self.menu()

    def menu(self):
        pass


class AnonFinder(Options):
    depth = None
    twitter = ""
    google_query = ""
    facebook = ""
    modules = ["FaceBook", "FullContact", "Google", "HIBP", "Linkedin", "Twitter", "WhitePages"]
    phone_number = ""
    email = ""
    first = ""
    last = ""
    custom_help = "  list - Displays valid profiles to select from. \n   " \
                  "show - shows current configurations.\n   " \
                  "mkprofile=**** - Creates a profile within the workspaces directory.\n   " \
                  "stprofile=**** - sets a valid profile to be used.\n   email=**** - sets target email.\n   " \
                  "phone=**** - sets phone number.\n   name=First Last - sets target name.\n   " \
                  "use=**** - this goes into a specific module menu to run only specific scans.\n   " \
                  "REMOVE=**** - Deletes valid profiles within workspaces directory."

    def __init__(self):
        self.set_help(self.custom_help)
        self.check()
        self.output("Welcome to AnonFinder. Type 'help' to get started.")

    def check(self):
        pass

    def __del__(self):
        pass

    def menu(self, user_input):
        while self.alive:
            print("I AM WORKING")


class RunningManager:
    def __init__(self, first=None, last=None, phone=None, email=None, twitter=None, facebook=None, google=None):
        self.first = first
        self.last = last
        self.phone = phone
        self.email = email
        self.email = email
        self.twitter = twitter
        self.facebook = facebook
        self.google = google

    def run(self):
        twitter_api.auto_search()
        whitepages.auto_run()
        fullcontact.main()


