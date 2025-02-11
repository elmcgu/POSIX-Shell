import sys


def main():
    # Uncomment this block to pass the first stage
    while True:
        sys.stdout.write("$ ")

        # Wait for user input
        
        command = input()
        
        if command.lower() == "exit 0":
            break

        elif command.lower().split()[0] == "echo":
            output_list = command.split()
            count = len(output_list)
            final_output = ""
            for i in range (1,count):
                final_output += f"{output_list[i]} "
            print(final_output.rstrip())

        else:
            print(f"{command}: command not found")



if __name__ == "__main__":
    main()
