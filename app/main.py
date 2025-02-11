import sys


def main():
    # Uncomment this block to pass the first stage
    while True:
        sys.stdout.write("$ ")

        # Wait for user input
        
        command = input()
        
        if command.lower() == "exit 0":
            break

        else:
            print(f"{command}: command not found")



if __name__ == "__main__":
    main()
