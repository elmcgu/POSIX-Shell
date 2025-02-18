import sys
import os
import subprocess

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

def run_exec(args):
    try:
        subprocess.run(args)
    except FileNotFoundError:
        print(f"{args[0]}: command not found")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")


def main():
    while True:
        sys.stdout.write("$ ")
        # Wait for user input
        command = input()
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
            if len(argv) != 2:
                print("Enter one argument for type command")
            elif argv[1] in builtins:
                print(f"{argv[1]} is a shell builtin")
            else:
                find_exec(argv[1])
        
        elif argv[0] == "pwd":
            cwd = os.getcwd()
            print(cwd)

        else:
            run_exec(argv)

if __name__ == "__main__":
    main()
