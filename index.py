import frida
import sys
from file_tools.file import get_file_string

try:
    print("frida doing with: " + sys.argv[1])
    session = frida.attach(sys.argv[1])
except BaseException as e:
    print(e)
    sys.exit()



def load_script():
    try:
        script_string = get_file_string(sys.argv[2])
        script = session.create_script(script_string)
        script.load()
    except BaseException as e:
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