import os


def fetch_keys():
    pass


def output(message):
    print('> %s' % message)
    idle()

def idle():
    __response = input('>')
    options(__response)


def options(response):
    if response == "Help" or response == "help":
        output("This is the help screen")
    elif response == "exit()":
        os._exit(0)
    else:
        output("Im sorry I didn't quite catch that")
