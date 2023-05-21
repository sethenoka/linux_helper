import os

def run():
    print("Terminal Navigation")
    print("==================\n")

    # Quiz 1
    os.system('clear')
    print("Q1: Navigate to the root directory.")
    hint_given = 0  # Track the number of hints given

    while True:
        if hint_given <2:
            answer = input("Enter your answer ('hint' for a hint, 'skip' to skip): ")
        else:
            answer = input("Enter your answer ('skip' to skip): ")


        if answer.strip().lower() == "hint":
            if hint_given < 1:
                print("Hint 1: cd is short for 'change directory'.\n")
                hint_given += 1
            elif hint_given < 2:
                print("Hint 2: Use the '/' character to specify the root directory.\n")
                hint_given += 1
            else:
                print("No more hints available.\n")
        elif answer.strip() == "skip":
            print("Skipped!\n")
            break
        elif answer.strip() == "cd /":
            print("Correct!\n")
            #os.system('cd /; pwd')
            break
        else:
            print("Incorrect. Please try again.\n")

    # Quiz 2
    print("Q2: Navigate to the foo sub-directory.")
    hint_given = 0  # Track the number of hints given

    while True:
        if hint_given <2:
            answer = input("Enter your answer ('hint' for a hint, 'skip' to skip): ")
        else:
            answer = input("Enter your answer ('skip' to skip): ")


        if answer.strip().lower() == "hint":
            if hint_given < 1:
                print("Hint 1: cd is short for 'change directory'.\n")
                hint_given += 1
            elif hint_given < 2:
                print("Hint 2: Use the name of the folder to specify the sub-directory.\n")
                hint_given += 1
            else:
                print("No more hints available.\n")
        elif answer.strip() == "skip":
            print("Skipped!\n")
            break
        elif answer.strip() == "cd foo":
            print("Correct!\n")
            break
        else:
            print("Incorrect. Please try again.\n")

    # Quiz 3
    print("Q3: Navigate to the user's home directory.")
    hint_given = 0  # Track the number of hints given

    while True:
        if hint_given <2:
            answer = input("Enter your answer ('hint' for a hint, 'skip' to skip): ")
        else:
            answer = input("Enter your answer ('skip' to skip): ")


        if answer.strip().lower() == "hint":
            if hint_given < 1:
                print("Hint 1: cd is short for 'change directory'.\n")
                hint_given += 1
            elif hint_given < 2:
                print("Hint 2: ~ is a shortcut for the user's home directory.\n")
                hint_given += 1
            else:
                print("No more hints available.\n")
        elif answer.strip() == "skip":
            print("Skipped!\n")
            break
        elif answer.strip() == "cd ~":
            print("Correct!\n")
            break
        else:
            print("Incorrect. Please try again.\n")

    # Quiz 4
    print("Q4: Navigate to the previous directory.")
    hint_given = 0  # Track the number of hints given

    while True:
        if hint_given <2:
            answer = input("Enter your answer ('hint' for a hint, 'skip' to skip): ")
        else:
            answer = input("Enter your answer ('skip' to skip): ")


        if answer.strip().lower() == "hint":
            if hint_given < 1:
                print("Hint 1: cd is short for 'change directory'.\n")
                hint_given += 1
            elif hint_given < 2:
                print("Hint 2: - is a shortcut for the last directory used.\n")
                hint_given += 1
            else:
                print("No more hints available.\n")
        elif answer.strip() == "skip":
            print("Skipped!\n")
            break
        elif answer.strip() == "cd -":
            print("Correct!\n")
            break
        else:
            print("Incorrect. Please try again.\n")

    # Quiz 5
    print("Q5: Print the current directory path.")
    hint_given = 0  # Track the number of hints given

    while True:
        if hint_given <2:
            answer = input("Enter your answer ('hint' for a hint, 'skip' to skip): ")
        else:
            answer = input("Enter your answer ('skip' to skip): ")


        if answer.strip().lower() == "hint":
            if hint_given < 1:
                print("Hint 1: This command stands for 'print working directory.'\n")
                hint_given += 1
            elif hint_given < 2:
                print("Hint 2: This command outputs the full path of your current directory.\n")
                hint_given += 1
            else:
                print("No more hints available.\n")
        elif answer.strip() == "skip":
            print("Skipped!\n")
            break
        elif answer.strip() == "pwd":
            print("Correct!")
            #os.system('pwd')
            print("")
            break
        else:
            print("Incorrect. Please try again.\n")

    # Quiz 6
    print("Q6: List the contents of the current directory.")
    hint_given = 0  # Track the number of hints given

    while True:
        if hint_given <2:
            answer = input("Enter your answer ('hint' for a hint, 'skip' to skip): ")
        else:
            answer = input("Enter your answer ('skip' to skip): ")


        if answer.strip().lower() == "hint":
            if hint_given < 1:
                print("Hint 1: This command provides a simple (short) listing of the directory contents.\n")
                hint_given += 1
            else:
                print("No more hints available.\n")
        elif answer.strip() == "skip":
            print("Skipped!\n")
            break
        elif answer.strip() == "ls":
            print("Correct!\n")
            break
        else:
            print("Incorrect. Please try again.\n")

    # Quiz 7
    print("Q7: List the contents of the current directory, including hidden files.")
    hint_given = 0  # Track the number of hints given

    while True:
        if hint_given <2:
            answer = input("Enter your answer ('hint' for a hint, 'skip' to skip): ")
        else:
            answer = input("Enter your answer ('skip' to skip): ")


        if answer.strip().lower() == "hint":
            if hint_given < 1:
                print("Hint 1: -l provides a long (tabulated) listing of the directory contents.\n")
                hint_given += 1
            else:
                print("Hint 2: -a shows all files and directories, including those starting with a dot (i.e. hidden).\n")
        elif answer.strip() == "skip":
            print("Skipped!\n")
            break
        elif answer.strip() == "ls -la":
            print("Correct!\n")
            break
        else:
            print("Incorrect. Please try again.\n")

    # Quiz 8
    print("Q8: List the contents of the current directory, including human-readable size metadata.")
    hint_given = 0  # Track the number of hints given

    while True:
        if hint_given <2:
            answer = input("Enter your answer ('hint' for a hint, 'skip' to skip): ")
        else:
            answer = input("Enter your answer ('skip' to skip): ")


        if answer.strip().lower() == "hint":
            if hint_given < 1:
                print("Hint 1: -l provides a long (tabulated) listing of the directory contents.\n")
                hint_given += 1
            else:
                print("Hint 2: -h provides a listing including hidden files.\n")
        elif answer.strip() == "skip":
            print("Skipped!\n")
            break
        elif answer.strip() == "ls -lh":
            print("Correct!\n")
            break
        else:
            print("Incorrect. Please try again.\n")

    # Quiz 9
    print("Q9: List the contents of the current directory, sorted by modification time.")
    hint_given = 0  # Track the number of hints given

    while True:
        if hint_given <2:
            answer = input("Enter your answer ('hint' for a hint, 'skip' to skip): ")
        else:
            answer = input("Enter your answer ('skip' to skip): ")


        if answer.strip().lower() == "hint":
            if hint_given < 1:
                print("Hint 1: -l provides a long (tabulated) listing of the directory contents.\n")
                hint_given += 1
            else:
                print("Hint 2: -t displays the most recently modified files or directories at the top.\n")
        elif answer.strip() == "skip":
            print("Skipped!\n")
            break
        elif answer.strip() == "ls -lt":
            print("Correct!\n")
            break
        else:
            print("Incorrect. Please try again.\n")

    # Quiz 10
    print("Q10: List the file/directory tree of the current directory.")
    hint_given = 0  # Track the number of hints given

    while True:
        if hint_given <2:
            answer = input("Enter your answer ('hint' for a hint, 'skip' to skip): ")
        else:
            answer = input("Enter your answer ('skip' to skip): ")


        if answer.strip().lower() == "hint":
            if hint_given < 1:
                print("Hint 1: tree displays a hierarchical tree structure of the directory contents.\n")
                hint_given += 1
            else:
                print("No more hints available.\n")
        elif answer.strip() == "skip":
            print("Skipped!\n")
            break
        elif answer.strip() == "tree":
            print("Correct!\n")
            break
        else:
            print("Incorrect. Please try again.\n")

    # Quiz 11
    print("Q11: List only the directory tree of the current directory.")
    hint_given = 0  # Track the number of hints given

    while True:
        if hint_given <2:
            answer = input("Enter your answer ('hint' for a hint, 'skip' to skip): ")
        else:
            answer = input("Enter your answer ('skip' to skip): ")


        if answer.strip().lower() == "hint":
            if hint_given < 1:
                print("Hint 1: tree displays a hierarchical tree structure of the directory contents.\n")
                hint_given += 1
            else:
                print("Hint 2: -d displays only the directories in the tree.\n")
        elif answer.strip() == "skip":
            print("Skipped!\n")
            break
        elif answer.strip() == "tree -d":
            print("Correct!\n")
            break
        else:
            print("Incorrect. Please try again.\n")

    # Quiz 12
    print("Q12: List the size, created timestamp, and modified timestamp for foo.txt (also works for directories).")
    hint_given = 0  # Track the number of hints given

    while True:
        if hint_given <2:
            answer = input("Enter your answer ('hint' for a hint, 'skip' to skip): ")
        else:
            answer = input("Enter your answer ('skip' to skip): ")


        if answer.strip().lower() == "hint":
            if hint_given < 1:
                print("Hint 1: stat provides detailed information about a specific file or directory.\n")
                hint_given += 1
            else:
                print("Hint 2: stat displays attributes such as size, timestamps, and file type.\n")
        elif answer.strip() == "skip":
            print("Skipped!\n")
            break
        elif answer.strip() == "stat foo.txt":
            print("Correct!\n")
            break
        else:
            print("Incorrect. Please try again.\n")

    # Feedback
    print("Feedback")
    print("========\n")
    print("Congratulations! You have completed the Terminal Navigation tutorial.")
    input("Press any key to continue.")