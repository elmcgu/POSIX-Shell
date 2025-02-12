import sys
import os

builtins =["type", "echo", "exit"]

def find_exec(command):
    paths = os.getenv("PATH", "").split(os.pathsep)
    for dir in paths:
        exec_path = os.path.join(dir,command)
        if os.path.isfile(exec_path):
            print(f"{command} is {exec_path}")
            break
    else:
        print(f"{command}: not found")


def main():
    while True:
        sys.stdout.write("$ ")
        # Wait for user input
        command = input().lower()
        argv = command.split()

        if not command:
            continue

        elif command == "exit 0":
            break

        elif argv[0] == "echo":
            count = len(argv)
            final_output = ""
            for i in range (1,count):
                final_output += f"{argv[i]} "
            print(final_output.rstrip())
        
        elif argv[0] == "type":
            if argv[1] in builtins and len(argv) == 2:
                print(f"{argv[1]} is a shell builtin")
            elif len(argv) == 2:
                find_exec(argv[1])
            else:
                print("Enter 1 argument for type command")

        else:
            print(f"{command}: command not found")

if __name__ == "__main__":
    main()
