import urllib.request
import json
import twitter
import os
import re
import platform
import sys


value_dict = {"twitter_handle": "", "email": "", "phone_number": ""}
help_options = ""


def request():
    req = urllib.request.Request('https://api.fullcontact.com/v3/person.enrich')
    req.add_header('Authorization', 'Bearer ')
    data = json.dumps({"twitter": "@xyz"}).encode()

    response = urllib.request.urlopen(req, data)
    data_response = json.load(response)

    for keyword in data_response:
        print(keyword)

    print(data_response.get("FullName"), data_response.get("twitter"))


def write(profile):
    file_name = "%s-%s-%s-%s" % ()
    if os.path.exists("../workspaces/FullContact/%s"):
        pass


def help_menu():
    output(help_options, "FullContact")


def exit_program():
    output("Thank you for using AnonFinder! <3", "FullContact")
    sys.exit(0)


def clear():
    if platform.system() == "Linux":
        os.system("clear")
    elif platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def show():
    output(value_dict)


def set_value(param):
    try:
        cmd, attribute, value = re.split(' ', param)

        if attribute in value_dict:
            value_dict[attribute] = value
            output("%s as been set to %s" % (attribute, value), "FullContact")
        else:
            output("Refer to help list for available attributes.", "FullContact")

    except ValueError or TypeError:
        output("Refer to help list on how to use set.", "FullContact")


def list_profiles():
    __profile = []

    for profile in os.listdir('workspace/'):
        __profile.append(profile)

    output(__profile, "FullContact")
    __profile.clear()


def output(msg, *prompt):
    if prompt:
        print("[%s]> %s" % (prompt[0], msg))
    else:
        print("> %s" % msg)


def reset():
    for attribute in value_dict:
        value_dict[attribute] = ''

    output("all fields cleared . . .")


def run():
    pass


def main():
    output("Welcome to the FullContact module, type help to get started!", "FullContact")

    alive = True
    while alive:
        user_input = input("[FullContact]> ")

        if user_input == "back":
            alive = False

        elif user_input == "exit":
            exit_program()

        elif user_input == "list":
            list_profiles()

        elif "set" in user_input:
            set_value(user_input)

        elif user_input == "clear":
            clear()

        elif user_input == "help":
            help_menu()

        elif user_input == "show":
            show()

        elif user_input == "clear_fields":
            reset()

        elif user_input == "run":
            run()

        else:
            output("Sorry I didn't quite understand that.", "FullContact")




if __name__ == '__main__':
    main()

