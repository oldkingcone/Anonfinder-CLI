from utilities import utilities

workspace = ''
target = ''


def greeting():
    output('Welcome to AnonFinder, type help to get started', 'AnonFinder')


def output(msg, *prompt):
    if prompt:
        print("[%s]> %s" % (prompt[0], msg))
    else:
        print("> %s" % msg)


def make_profile(option):
    pass


def delete_profile(option):
    pass


def run():
    pass


def use(option):
    pass


def set_value(param, option):
    pass


def exit_program():
    pass


def exclude(*option):
    pass


def help_menu():
    pass


def main():
    pass


if __name__ == '__main__':
    main()
