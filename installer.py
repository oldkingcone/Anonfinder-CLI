import os

modules = ['python-twitter']
key_directories = ["twitter", "facebook", "linkedin", "fullcontact"]

print("Checking for third party modules . . .")

for module in modules:
    os.system('pip3 install %s' % module)

print("finished check . . .")

print("creating required directories")

try:
    os.mkdir("workspace/")
except FileExistsError or PermissionError:
    pass

try:
    os.mkdir("key/")
except FileExistsError or PermissionError:
    pass

for module in key_directories:
    try:
        os.mkdir("key/%s/" % module)
    except FileExistsError or PermissionError:
        pass
