import os

modules = ['python-twitter']

print("Checking for third party modules . . .")

for module in modules:
    os.system('pip3 install %s' % module)

print("finished check . . .")
