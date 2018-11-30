from utilities import utilities
import re


class Manager(utilities.Options):

    obj_names = ["twitter", "back", "fullcontact", "google"]

    def __init__(self):
        self.Obj_list = [utilities.AnonFinder(), utilities.Twitter]
        self.current_obj = self.fetch()
        self.menu()

    def stow(self, obj):
        self.Obj_list.append(obj)

    def fetch(self, *index):
        return self.Obj_list.pop(*index)

    def menu(self):
        while self.alive:
            response = self.get_input()

            if response in self.obj_names:
                if response == "twitter":
                    self.stow(self.current_obj)
                    self.fetch(1)
                else:
                    pass

                if response == "back":
                    self.stow(self.current_obj)
                    self.fetch()
                else:
                    pass

            else:
                self.current_obj.menu(response)


manager = Manager()
