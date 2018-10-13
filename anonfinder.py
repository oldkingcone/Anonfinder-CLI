from utilities import utilities
import re


class AnonFinder(utilities.Options):
    phone_number = ""
    email = ""
    name = ""
    def __init__(self):
        self.check()
        self.menu()

    def check(self):
        pass

    def menu(self):
        while self.alive:
            response = self.get_input()

            if response == "help":
                self.output("OI IT WORKED")
            elif response == "exit":
                self.exit()
            elif response == "clear":
                self.clear()
            elif response == "show":
                self.output("Phone: %s \n  email: %s \n  name: %s" % (self.phone_number, self.email, self.name))
            elif "phone=" in response:
                command, value = re.split("=", response)
                if len(value) == 10:
                    try:
                        checker = int(value)
                        self.phone_number = value
                    except ValueError:
                        self.output("Please use only Digit values")
                else:
                    self.output("Please make sure you use a full US number")
            elif "email=" in response:

                if "@" in response and ".com":
                    self.email = response


AnonFinder = AnonFinder()
