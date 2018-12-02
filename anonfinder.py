from utilities import utilities
from utilities.twitter import Twitter


class Manager(utilities.Options):

    obj_names = ["twitter", "back", "fullcontact", "google", "exit"]

    def __init__(self):
        self.queue = [utilities.AnonFinder(), Twitter()]
        self.current_obj = self.fetch(0)
        self.name = self.current_obj.name
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
                    self.fetch()
                    self.name = self.current_obj.name
                else:
                    pass

                if response == "exit":
                    self.exit()
                else:
                    pass

                if "back" in response:
                    self.stow(self.current_obj)
                    self.fetch(0)
                else:
                    pass

            else:
                self.current_obj.menu(response)


manager = Manager()
