import os

def run():
    print("Disk and Memory Usage and Statistics")
    print("==================\n")

    # Quiz 1
    os.system('clear')
    print("Q1: List the disks, their sizes, used space, and available space.")
    hint_given = 0  # Track the number of hints given

    while True:
        if hint_given <2:
            answer = input("Enter your answer ('hint' for a hint, 'skip' to skip): ")
        else:
            answer = input("Enter your answer ('skip' to skip): ")

        if answer.strip().lower() == "hint":
            if hint_given < 1:
                print("Hint 1: df is short for 'disk free'.\n")
                hint_given += 1
            elif hint_given < 2:
                print("No more hints available.\n")
                hint_given += 1
            else:
                print("No more hints available.\n")
        elif answer.strip() == "skip":
            print("Skipped!\n")
            break
        elif answer.strip() == "df":
            print("Correct!\n")
            break
        else:
            print("Incorrect. Please try again.\n")

    # Quiz 2
    print("Q2: List the disks, their sizes, used space, and available space with human-readable numbers.")
    hint_given = 0  # Track the number of hints given

    while True:
        if hint_given <2:
            answer = input("Enter your answer ('hint' for a hint, 'skip' to skip): ")
        else:
            answer = input("Enter your answer ('skip' to skip): ")

        if answer.strip().lower() == "hint":
            if hint_given < 1:
                print("Hint 1: df is short for 'disk free'.\n")
                hint_given += 1
            elif hint_given < 2:
                print("Hint 2: -h is used for human-readable data.\n")
                hint_given += 1
            else:
                print("No more hints available.\n")
        elif answer.strip() == "skip":
            print("Skipped!\n")
            break
        elif answer.strip() == "df -h":
            print("Correct!\n")
            break
        else:
            print("Incorrect. Please try again.\n")

    # Quiz 3
    print("Q3: List the file sizes of the current directory contents (including sub-directories).")
    hint_given = 0  # Track the number of hints given

    while True:
        if hint_given <2:
            answer = input("Enter your answer ('hint' for a hint, 'skip' to skip): ")
        else:
            answer = input("Enter your answer ('skip' to skip): ")

        if answer.strip().lower() == "hint":
            if hint_given < 1:
                print("Hint 1: du is short for 'disk usage'.\n")
                hint_given += 1
            elif hint_given < 2:
                print("No more hints available.\n")
                hint_given += 1
            else:
                print("No more hints available.\n")
        elif answer.strip() == "skip":
            print("Skipped!\n")
            break
        elif answer.strip() == "du":
            print("Correct!\n")
            break
        else:
            print("Incorrect. Please try again.\n")

    # Quiz 4
    print("Q4: Show the current memory usage.")
    hint_given = 0  # Track the number of hints given

    while True:
        if hint_given <2:
            answer = input("Enter your answer ('hint' for a hint, 'skip' to skip): ")
        else:
            answer = input("Enter your answer ('skip' to skip): ")

        if answer.strip().lower() == "hint":
            if hint_given < 1:
                print("Hint 1: free is used for memory statistics.\n")
                hint_given += 1
            elif hint_given < 2:
                print("No more hints available.\n")
                hint_given += 1
            else:
                print("No more hints available.\n")
        elif answer.strip() == "skip":
            print("Skipped!\n")
            break
        elif answer.strip() == "free":
            print("Correct!\n")
            break
        else:
            print("Incorrect. Please try again.\n")

    # Quiz 5
    print("Q5: Show the current memory usage, updating every 5 seconds.")
    hint_given = 0  # Track the number of hints given

    while True:
        if hint_given <2:
            answer = input("Enter your answer ('hint' for a hint, 'skip' to skip): ")
        else:
            answer = input("Enter your answer ('skip' to skip): ")

        if answer.strip().lower() == "hint":
            if hint_given < 1:
                print("Hint 1: free is used for memory statistics.\n")
                hint_given += 1
            elif hint_given < 2:
                print("Hint 2: -s is used with free for constant updates.\n")
                hint_given += 1
            else:
                print("No more hints available.\n")
        elif answer.strip() == "skip":
            print("Skipped!\n")
            break
        elif answer.strip() == "free -s 5":
            print("Correct!\n")
            break
        elif answer.strip() == "free --seconds 5":
            print("Correct!\n")
            break
        else:
            print("Incorrect. Please try again.\n")

    # Feedback
    print("Feedback")
    print("========\n")
    print("Congratulations! You have completed the Disk and Memory Usage and Statistics tutorial.")
    input("Press any key to continue.")