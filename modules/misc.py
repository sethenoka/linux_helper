import os

def run():
    print("Miscellaneous Terminal Commands")
    print("==================\n")

    # Quiz 1
    os.system('clear')
    print("Q1: Print the current date and time in the terminal.")
    hint_given = 0  # Track the number of hints given

    while True:
        if hint_given <2:
            answer = input("Enter your answer ('hint' for a hint, 'skip' to skip): ")
        else:
            answer = input("Enter your answer ('skip' to skip): ")

        if answer.strip().lower() == "hint":
            if hint_given < 1:
                print("Hint 1: date is one command that will achieve this.\n")
                hint_given += 1
            elif hint_given < 2:
                print("No more hints available.\n")
                hint_given += 1
            else:
                print("No more hints available.\n")
        elif answer.strip() == "skip":
            print("Skipped!\n")
            break
        elif answer.strip() == "date":
            print("Correct!\n")
            break
        else:
            print("Incorrect. Please try again.\n")

    # Quiz 2
    print("Q2: List the IP addresses configured on your system.")
    hint_given = 0  # Track the number of hints given

    while True:
        if hint_given <2:
            answer = input("Enter your answer ('hint' for a hint, 'skip' to skip): ")
        else:
            answer = input("Enter your answer ('skip' to skip): ")

        if answer.strip().lower() == "hint":
            if hint_given < 1:
                print("Hint 1: ifconfig will achieve this.\n")
                hint_given += 1
            elif hint_given < 2:
                print("Hint 2: ip is a better command for this.\n")
                hint_given += 1
            else:
                print("No more hints available.\n")
        elif answer.strip() == "skip":
            print("Skipped!\n")
            break
        elif answer.strip() == "ip":
            print("Correct!\n")
            break
        elif answer.strip() == "ifconfig":
            print("Correct! (but there's a better way)\n")
            break
        else:
            print("Incorrect. Please try again.\n")

    # Quiz 3
    print("Q3: Schedule a system shutdown to occur in 1 minute.")
    hint_given = 0  # Track the number of hints given

    while True:
        if hint_given <2:
            answer = input("Enter your answer ('hint' for a hint, 'skip' to skip): ")
        else:
            answer = input("Enter your answer ('skip' to skip): ")

        if answer.strip().lower() == "hint":
            if hint_given < 1:
                print("Hint 1: shutdown is the command to use.\n")
                hint_given += 1
            elif hint_given < 2:
                print("Hint 2: +1 is one way to achieve this.\n")
                hint_given += 1
            else:
                print("No more hints available.\n")
        elif answer.strip() == "skip":
            print("Skipped!\n")
            break
        elif answer.strip() == "shutdown +1":
            print("Correct!\n")
            break
        else:
            print("Incorrect. Please try again.\n")

    # Quiz 4
    print("Q4: Immediately shutdown the system.")
    hint_given = 0  # Track the number of hints given

    while True:
        if hint_given <2:
            answer = input("Enter your answer ('hint' for a hint, 'skip' to skip): ")
        else:
            answer = input("Enter your answer ('skip' to skip): ")

        if answer.strip().lower() == "hint":
            if hint_given < 1:
                print("Hint 1: shutdown is the command to use.\n")
                hint_given += 1
            elif hint_given < 2:
                print("Hint 2: now is one way to achieve this.\n")
                hint_given += 1
            else:
                print("No more hints available.\n")
        elif answer.strip() == "skip":
            print("Skipped!\n")
            break
        elif answer.strip() == "shutdown now":
            print("Correct!\n")
            break
        else:
            print("Incorrect. Please try again.\n")

    # Quiz 5
    print("Q5: Immediately reboot the system.")
    hint_given = 0  # Track the number of hints given

    while True:
        if hint_given <2:
            answer = input("Enter your answer ('hint' for a hint, 'skip' to skip): ")
        else:
            answer = input("Enter your answer ('skip' to skip): ")

        if answer.strip().lower() == "hint":
            if hint_given < 1:
                print("Hint 1: shutdown is the command to use.\n")
                hint_given += 1
            elif hint_given < 2:
                print("Hint 2: -r is one way to achieve this.\n")
                hint_given += 1
            else:
                print("No more hints available.\n")
        elif answer.strip() == "skip":
            print("Skipped!\n")
            break
        elif answer.strip() == "shutdown -r":
            print("Correct!\n")
            break
        else:
            print("Incorrect. Please try again.\n")

    # Quiz 6
    print("Q6: Cancel and scheduled reboot or shutdown the system.")
    hint_given = 0  # Track the number of hints given

    while True:
        if hint_given <2:
            answer = input("Enter your answer ('hint' for a hint, 'skip' to skip): ")
        else:
            answer = input("Enter your answer ('skip' to skip): ")

        if answer.strip().lower() == "hint":
            if hint_given < 1:
                print("Hint 1: shutdown is the command to use.\n")
                hint_given += 1
            elif hint_given < 2:
                print("Hint 2: -c is one way to achieve this.\n")
                hint_given += 1
            else:
                print("No more hints available.\n")
        elif answer.strip() == "skip":
            print("Skipped!\n")
            break
        elif answer.strip() == "shutdown -c":
            print("Correct!\n")
            break
        else:
            print("Incorrect. Please try again.\n")

    # Quiz 7
    print("Q7: Copy the directory /foo to /bar using rsync.")
    hint_given = 0  # Track the number of hints given

    while True:
        if hint_given <2:
            answer = input("Enter your answer ('hint' for a hint, 'skip' to skip): ")
        else:
            answer = input("Enter your answer ('skip' to skip): ")

        if answer.strip().lower() == "hint":
            if hint_given < 1:
                print("Hint 1: rsync takes two arguments: source and destination.\n")
                hint_given += 1
            elif hint_given < 2:
                print("No more hints available.\n")
                hint_given += 1
            else:
                print("No more hints available.\n")
        elif answer.strip() == "skip":
            print("Skipped!\n")
            break
        elif answer.strip() == "rsync /foo /bar":
            print("Correct!\n")
            break
        else:
            print("Incorrect. Please try again.\n")

    # Quiz 8
    print("Q8: Copy the directory /foo to /bar using rsync, recursively.")
    hint_given = 0  # Track the number of hints given

    while True:
        if hint_given <2:
            answer = input("Enter your answer ('hint' for a hint, 'skip' to skip): ")
        else:
            answer = input("Enter your answer ('skip' to skip): ")

        if answer.strip().lower() == "hint":
            if hint_given < 1:
                print("Hint 1: rsync takes two arguments: source and destination.\n")
                hint_given += 1
            elif hint_given < 2:
                print("Hint 2: -r is the argument to use.\n")
                hint_given += 1
            else:
                print("No more hints available.\n")
        elif answer.strip() == "skip":
            print("Skipped!\n")
            break
        elif answer.strip() == "rsync -r /foo /bar":
            print("Correct!\n")
            break
        else:
            print("Incorrect. Please try again.\n")

    # Quiz 9
    print("Q9: Copy only newer files from the directory /foo to /bar using rsync, recursively.")
    hint_given = 0  # Track the number of hints given

    while True:
        if hint_given <2:
            answer = input("Enter your answer ('hint' for a hint, 'skip' to skip): ")
        else:
            answer = input("Enter your answer ('skip' to skip): ")

        if answer.strip().lower() == "hint":
            if hint_given < 1:
                print("Hint 1: rsync takes two arguments: source and destination.\n")
                hint_given += 1
            elif hint_given < 2:
                print("Hint 2: -ru means recursive & update.\n")
                hint_given += 1
            else:
                print("No more hints available.\n")
        elif answer.strip() == "skip":
            print("Skipped!\n")
            break
        elif answer.strip() == "rsync -ru /foo /bar":
            print("Correct!\n")
            break
        else:
            print("Incorrect. Please try again.\n")

    # Quiz 10
    print("Q10: Copy only newer files from the directory /foo to /bar using rsync, recursively, with human-readable numbers.")
    hint_given = 0  # Track the number of hints given

    while True:
        if hint_given <2:
            answer = input("Enter your answer ('hint' for a hint, 'skip' to skip): ")
        else:
            answer = input("Enter your answer ('skip' to skip): ")

        if answer.strip().lower() == "hint":
            if hint_given < 1:
                print("Hint 1: rsync takes two arguments: source and destination.\n")
                hint_given += 1
            elif hint_given < 2:
                print("Hint 2: -ruh means recursive & update, with human-readable numbers.\n")
                hint_given += 1
            else:
                print("No more hints available.\n")
        elif answer.strip() == "skip":
            print("Skipped!\n")
            break
        elif answer.strip() == "rsync -ruh /foo /bar":
            print("Correct!\n")
            break
        else:
            print("Incorrect. Please try again.\n")

    # Quiz 11
    print("Q11: Copy only newer files from the directory /foo to /bar using rsync, recursively, with human-readable numbers, showing progress.")
    hint_given = 0  # Track the number of hints given

    while True:
        if hint_given <2:
            answer = input("Enter your answer ('hint' for a hint, 'skip' to skip): ")
        else:
            answer = input("Enter your answer ('skip' to skip): ")

        if answer.strip().lower() == "hint":
            if hint_given < 1:
                print("Hint 1: rsync takes two arguments: source and destination.\n")
                hint_given += 1
            elif hint_given < 2:
                print("Hint 2: -ruhP means recursive & update, with human-readable numbers, with progress information.\n")
                hint_given += 1
            else:
                print("No more hints available.\n")
        elif answer.strip() == "skip":
            print("Skipped!\n")
            break
        elif answer.strip() == "rsync -ruhP /foo /bar":
            print("Correct!\n")
            break
        else:
            print("Incorrect. Please try again.\n")

    # Quiz 12
    print("Q12: Show the manual for wget.")
    hint_given = 0  # Track the number of hints given

    while True:
        if hint_given <2:
            answer = input("Enter your answer ('hint' for a hint, 'skip' to skip): ")
        else:
            answer = input("Enter your answer ('skip' to skip): ")

        if answer.strip().lower() == "hint":
            if hint_given < 1:
                print("Hint 1: man will open the manual pages for any application that has one.\n")
                hint_given += 1
            elif hint_given < 2:
                print("No more hints available.\n")
                hint_given += 1
            else:
                print("No more hints available.\n")
        elif answer.strip() == "skip":
            print("Skipped!\n")
            break
        elif answer.strip() == "man wget":
            print("Correct!\n")
            break
        else:
            print("Incorrect. Please try again.\n")

    # Feedback
    print("Feedback")
    print("========\n")
    print("Congratulations! You have completed the Miscellaneous Terminal Commands tutorial.")
    input("Press any key to continue.")