import utilities.utilities


class Twitter(utilities.utilities.Options):
    def __init__(self, *profile):
        self.name = "Twitter"

    def menu(self, user_input):
        if user_input == "potato":
            self.output("POTATOES")
        else:
            pass


