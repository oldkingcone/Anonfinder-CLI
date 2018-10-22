from utilities import utilities
import re
from modules import fullcontact
from modules import whitepages
import os
import shutil


class AnonFinder(utilities.Options):
    modules = ["FaceBook", "FullContact", "Google", "HIBP", "Linkedin", "Twitter", "WhitePages"]
    phone_number = ""
    email = ""
    name = ""
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

            if response == "help":
                self.help()
            if response == "exit":
                self.exit()
            if response == "clear":
                self.clear()
            if response == "show":
                self.output("Profile: %s \n  Phone: %s \n  email: %s \n  name: %s" %
                            (self.profile, self.phone_number, self.email, self.name))
            if "phone=" in response:
                command, value = re.split("=", response)
                if len(value) == 10:
                    self.phone_number = value
                else:
                    self.output("Something went wrong when setting the phone number")

            if "email=" in response:
                if "@" in response and ".com":
                    command, value = re.split("=", response)
                    self.email = value
                else:
                    self.output("There was an error setting the email")
                    """This section will go into specific modules and perform specific scans"""

            if "use=" in response:
                __command, __value = re.split("=", response)
                if response == "twitter":
                    del self
            else:
                pass
            if "name=" in response:
                command, value = re.split("=", response)
                first, last = re.split(" ", value)
                name = "%s %s" % (first, last)
                self.name = name

            if response == "run":
                self.output("Running search with current configurations. . .")
                utilities.run_manager(self.email, self.phone_number, self.name)

            if "mkprofile=" in response:
                self.make_profile(response)

            if "stprofile=" in response:
                command, value = re.split("=", response)
                if value in self.r_list():
                    self.profile = value
                else:
                    self.output("Please use a profile within the workspace directory, use the list command to view "
                                "profiles.")
            if response == "list":
                self.list()

            if "REMOVE=" in response:
                command, value = re.split("=", response)
                answer = input("> Are you sure you want to delete %s ?[y/n]" % value)
                if answer == "y" or "yes":
                    self.output("Okay deleting %s and all its data . . ." % value)
                    try:
                        shutil.rmtree("workspaces/%s" % value)
                    except FileNotFoundError or PermissionError:
                        pass
                else:
                    pass


AnonFinder = AnonFinder()
