import importlib, os

def print_menu():
    print("Available Modules:")
    print("1. Terminal Navigation")
    print("2. Working with Directories and Files")
    print("3. Searching in Terminal")
    print("4. Disk and Memory Usage and Statistics")
    print("5. Package Management")
    print("6. Process Management")
    print("7. Miscellaneous")
    print("8. Exit")

def run_module(module_name):
    try:
        module_path = os.path.join("modules", module_name + ".py")
        module_name = "modules." + module_name
        module = importlib.import_module(module_name)
        os.system('clear')
        module.run()
        os.system('clear')
    except ModuleNotFoundError:
        print("Error: Module not found.")
    except AttributeError:
        print("Error: Invalid module format.")

def main():
    # Introduction
    os.system('clear')
    print("Welcome to the Bash Basics tutorial!")
    print("In this tutorial, you will learn the basics of using the Bash terminal.")
    print("Let's get started!\n")

    while True:
        # Print menu
        print_menu()

        # Get user's choice
        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            run_module("navigation")    # navigating the terminal
        elif choice == "2":
            run_module("directories")   # working with directories and files
        elif choice == "3":
            run_module("search")        # find/grep, wc, sort, uniq, cut
        elif choice == "4":
            run_module("usage")         # disk and memory usage stats
        elif choice == "5":
            run_module("packages")      # apt and installing/updating/uninstalling
        elif choice == "6":
            run_module("process")       # working with processes (ID/kill)
        elif choice == "7":
            run_module("misc")          # misc (shutdown, date, ip, rsync, man)
        elif choice == "8":
            print("Exiting the program.")
            print("If you would like to learn more, please visit the following links:\n")
            print("- Bash Cheat Sheet: https://github.com/RehanSaeed/Bash-Cheat-Sheet")
            print("- Bash Reference Manual: https://www.gnu.org/software/bash/manual/bash.html")
            print("- Linux Command Line Tutorial: https://www.learnshell.org/")
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
