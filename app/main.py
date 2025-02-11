import sys

builtins =["type", "echo", "exit"]

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
            try:
                if argv[1] in builtins:
                    print(f"{argv[1]} is a shell builtin")
                else:
                    print(f"{argv[1]}: not found")
            except (IndexError, ValueError):
                print("Please pass valid argument to type command!") 


        else:
            print(f"{command}: command not found")



if __name__ == "__main__":
    main()
