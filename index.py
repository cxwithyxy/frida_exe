import frida
import sys
from file_tools.file import get_file_string

try:
    print("frida doing with: " + sys.argv[1])
    session = frida.attach(sys.argv[1])
except BaseException as e:
    print(e)
    sys.exit()


now_script = None


def load_script():
    global now_script

    try:
        now_script.unload()
        print("unload last script")
    except Exception as e:
        pass

    try:
        script_string = get_file_string(sys.argv[2])
        script = session.create_script(script_string)
        script.load()
        now_script = script
        print("script has loaded successfully")
    except Exception as e:
        print(e)


load_script()

print("enter 'exit' for exiting")
while True:
    usr_input = input()
    if usr_input == 'exit':
        break
    if usr_input == 'load':
        load_script()

session.detach()