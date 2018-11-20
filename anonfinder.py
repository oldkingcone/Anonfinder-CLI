from utilities import utilities
import re
from modules import fullcontact
from modules import whitepages
import os
import shutil


class AnonFinder(utilities.Options):
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
        self.menu()

    def check(self):
        pass

    def __del__(self):
        pass

    def menu(self):
        while self.alive:
            response = self.get_input()

            if response == "exit":
                self.exit()
            else:
                pass

            if response == "help":
                self.help()
            else:
                pass

            if response == "clear":
                self.clear()
            else:
                pass

            if response == "show":
                self.output("\n Selected profile: workspaces/%s \n First Name: %s \n Last Name: %s \n Email: %s "
                            "\n Phone: %s" % (self.profile, self.first, self.last, self.email, self.phone_number))
            else:
                pass

            if "stprofile=" in response:
                try:
                    __garbage, __value = re.split('=', response)
                    self.profile = __value
                except ValueError:
                    self.output("There was an error when setting the profile")
            else:
                pass

            if response == "addkey":
                confirmed = input("> would you like to add a key? [y/n]: ")
                if confirmed == "y" or confirmed == "yes":
                    self.output("you wanted to add a key")
                else:
                    pass



AnonFinder = AnonFinder()
