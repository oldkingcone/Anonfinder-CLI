from utilities import utillities
import os
import sys
import subprocess
packages = ["python-twitter"]


def clear():
    if utillities.get_os_name() == "linux":
        os.system("clear")
    if utillities.get_os_name() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def raw_out(msg):
    print('## %s ##' % msg)


def mdl_check():
    reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
    installed_packages = [r.decode().split('==')[0] for r in reqs.split()]
    for module in packages:
        if module in installed_packages:
            return True
        else:
            return False


def dir_check():

    if os.path.exists("workspaces/"):
        raw_out("Workspaces directory loaded . . .")
    else:
        raw_out("workspaces directory not found, recreating. . .")
        os.mkdir('workspaces')


def main():
    if mdl_check():
        raw_out("All packages have been detected . . .")
    else:
        raw_out("Not all package requirements were met, please install proper packages before running this again. . . ")
        sys.exit(0)

    dir_check()

    utillities.output("Welcome to Anonfinder, The CLI version, to get started type 'help'. ")
    utillities.idle()


if __name__ == '__main__':
    main()
