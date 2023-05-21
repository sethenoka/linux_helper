import os

def run():
    print("Working with Directories and Files")
    print("==================\n")

    # Quiz 1
    os.system('clear')
    print("Q1: Create a directory named foo.")
    hint_given = 0  # Track the number of hints given

    while True:
        if hint_given <2:
            answer = input("Enter your answer ('hint' for a hint, 'skip' to skip): ")
        else:
            answer = input("Enter your answer ('skip' to skip): ")

        if answer.strip().lower() == "hint":
            if hint_given < 1:
                print("Hint 1: mkdir is short for 'make directory'.\n")
                hint_given += 1
            elif hint_given < 2:
                print("Hint 2: Specify the folder name foo.\n")
                hint_given += 1
            else:
                print("No more hints available.\n")
        elif answer.strip() == "skip":
            print("Skipped!\n")
            break
        elif answer.strip() == "mkdir foo":
            print("Correct!\n")
            break
        else:
            print("Incorrect. Please try again.\n")

    # Quiz 2
    print("Q2: Create multiple directories named foo and bar.")
    hint_given = 0  # Track the number of hints given

    while True:
        if hint_given <2:
            answer = input("Enter your answer ('hint' for a hint, 'skip' to skip): ")
        else:
            answer = input("Enter your answer ('skip' to skip): ")

        if answer.strip().lower() == "hint":
            if hint_given < 1:
                print("Hint 1: mkdir is short for 'make directory'.\n")
                hint_given += 1
            elif hint_given < 2:
                print("Hint 2: You can specify multiple folder names in sequence (i.e. foo bar).\n")
                hint_given += 1
            else:
                print("No more hints available.\n")
        elif answer.strip() == "skip":
            print("Skipped!\n")
            break
        elif answer.strip() == "mkdir foo bar":
            print("Correct!\n")
            break
        else:
            print("Incorrect. Please try again.\n")

    # Quiz 3
    print("Q3: Create a directory foo with a sub-directory bar in a single command.")
    hint_given = 0  # Track the number of hints given

    while True:
        if hint_given <2:
            answer = input("Enter your answer ('hint' for a hint, 'skip' to skip): ")
        else:
            answer = input("Enter your answer ('skip' to skip): ")

        if answer.strip().lower() == "hint":
            if hint_given < 1:
                print("Hint 1: mkdir is short for 'make directory'.\n")
                hint_given += 1
            elif hint_given < 2:
                print("Hint 2: -p creates the parent and child folder.\n")
                hint_given += 1
            else:
                print("No more hints available.\n")
        elif answer.strip() == "skip":
            print("Skipped!\n")
            break
        elif answer.strip() == "mkdir -p foo/bar":
            print("Correct!\n")
            break
        else:
            print("Incorrect. Please try again.\n")

    # Quiz 4
    print("Q4: Delete the directory named foo including its contents.")
    hint_given = 0  # Track the number of hints given

    while True:
        if hint_given <2:
            answer = input("Enter your answer ('hint' for a hint, 'skip' to skip): ")
        else:
            answer = input("Enter your answer ('skip' to skip): ")

        if answer.strip().lower() == "hint":
            if hint_given < 1:
                print("Hint 1: rmdir is short for 'remove directory'.\n")
                hint_given += 1
            elif hint_given < 2:
                print("Hint 2: -r recurses through the parent and child folder.\n")
                hint_given += 1
            else:
                print("No more hints available.\n")
        elif answer.strip() == "skip":
            print("Skipped!\n")
            break
        elif answer.strip() == "rmdir -r foo":
            print("Correct!\n")
            break
        else:
            print("Incorrect. Please try again.\n")

    # Quiz 5
    print("Q5: Create an empty file named foo.txt.")
    hint_given = 0  # Track the number of hints given

    while True:
        if hint_given <2:
            answer = input("Enter your answer ('hint' for a hint, 'skip' to skip): ")
        else:
            answer = input("Enter your answer ('skip' to skip): ")

        if answer.strip().lower() == "hint":
            if hint_given < 1:
                print("Hint 1: touch will create a file (or update a file's metadata if it already exists).\n")
                hint_given += 1
            elif hint_given < 2:
                print("No more hints available.\n")
                hint_given += 1
            else:
                print("No more hints available.\n")
        elif answer.strip() == "skip":
            print("Skipped!\n")
            break
        elif answer.strip() == "touch foo.txt":
            print("Correct!\n")
            break
        else:
            print("Incorrect. Please try again.\n")

    # Quiz 6
    print("Q6: Write 'Hello, world!' to a file named foo.txt.")
    hint_given = 0  # Track the number of hints given

    while True:
        if hint_given <2:
            answer = input("Enter your answer ('hint' for a hint, 'skip' to skip): ")
        else:
            answer = input("Enter your answer ('skip' to skip): ")

        if answer.strip().lower() == "hint":
            if hint_given < 1:
                print("Hint 1: echo will write your input to standard output (i.e. the terminal window).\n")
                hint_given += 1
            elif hint_given < 2:
                print("Hint 2: use > to redirect your input to a file (remember to use '' to keep your string together).\n")
                hint_given += 1
            else:
                print("No more hints available.\n")
        elif answer.strip() == "skip":
            print("Skipped!\n")
            break
        elif answer.strip() == "echo 'Hello, world!' > foo.txt":
            print("Correct!\n")
            break
        else:
            print("Incorrect. Please try again.\n")

    # Quiz 7
    print("Q7: Append bar to your file named foo.txt.")
    hint_given = 0  # Track the number of hints given

    while True:
        if hint_given <2:
            answer = input("Enter your answer ('hint' for a hint, 'skip' to skip): ")
        else:
            answer = input("Enter your answer ('skip' to skip): ")

        if answer.strip().lower() == "hint":
            if hint_given < 1:
                print("Hint 1: echo will write your input to standard output (i.e. the terminal window).\n")
                hint_given += 1
            elif hint_given < 2:
                print("Hint 2: use >> to redirect your input to a file (> will overwrite, >> will append).\n")
                hint_given += 1
            else:
                print("No more hints available.\n")
        elif answer.strip() == "skip":
            print("Skipped!\n")
            break
        elif answer.strip() == "echo bar >> foo.txt":
            print("Correct!\n")
            break
        else:
            print("Incorrect. Please try again.\n")

    # Quiz 8
    print("Q8: Copy the file foo.txt to a new file, bar.txt.")
    hint_given = 0  # Track the number of hints given

    while True:
        if hint_given <2:
            answer = input("Enter your answer ('hint' for a hint, 'skip' to skip): ")
        else:
            answer = input("Enter your answer ('skip' to skip): ")

        if answer.strip().lower() == "hint":
            if hint_given < 1:
                print("Hint 1: cp is short for copy.\n")
                hint_given += 1
            elif hint_given < 2:
                print("Hint 2: cp takes two arguments: source and destination.\n")
                hint_given += 1
            else:
                print("No more hints available.\n")
        elif answer.strip() == "skip":
            print("Skipped!\n")
            break
        elif answer.strip() == "cp foo.txt bar.txt":
            print("Correct!\n")
            break
        else:
            print("Incorrect. Please try again.\n")

    # Quiz 9
    print("Q9: Instead, move the file foo.txt to bar.txt (i.e. change it's name).")
    hint_given = 0  # Track the number of hints given

    while True:
        if hint_given <2:
            answer = input("Enter your answer ('hint' for a hint, 'skip' to skip): ")
        else:
            answer = input("Enter your answer ('skip' to skip): ")

        if answer.strip().lower() == "hint":
            if hint_given < 1:
                print("Hint 1: mv is short for move.\n")
                hint_given += 1
            elif hint_given < 2:
                print("Hint 2: mv takes two arguments: source and destination.\n")
                hint_given += 1
            else:
                print("No more hints available.\n")
        elif answer.strip() == "skip":
            print("Skipped!\n")
            break
        elif answer.strip() == "mv foo.txt bar.txt":
            print("Correct!\n")
            break
        else:
            print("Incorrect. Please try again.\n")

    # Quiz 10
    print("Q10: Print all the contents of your file bar.txt to the terminal.")
    hint_given = 0  # Track the number of hints given

    while True:
        if hint_given <2:
            answer = input("Enter your answer ('hint' for a hint, 'skip' to skip): ")
        else:
            answer = input("Enter your answer ('skip' to skip): ")

        if answer.strip().lower() == "hint":
            if hint_given < 1:
                print("Hint 1: cat is short for concatenate.\n")
                hint_given += 1
            elif hint_given < 2:
                print("No more hints available.\n")
                hint_given += 1
            else:
                print("No more hints available.\n")
        elif answer.strip() == "skip":
            print("Skipped!\n")
            break
        elif answer.strip() == "cat bar.txt":
            print("Correct!\n")
            break
        else:
            print("Incorrect. Please try again.\n")

    # Quiz 11
    print("Q11: Print the contents of your file bar.txt so you can scroll through it.")
    hint_given = 0  # Track the number of hints given

    while True:
        if hint_given <2:
            answer = input("Enter your answer ('hint' for a hint, 'skip' to skip): ")
        else:
            answer = input("Enter your answer ('skip' to skip): ")

        if answer.strip().lower() == "hint":
            if hint_given < 1:
                print("Hint 1: less will give you some control over the output of your file.\n")
                hint_given += 1
            elif hint_given < 2:
                print("No more hints available.\n")
                hint_given += 1
            else:
                print("No more hints available.\n")
        elif answer.strip() == "skip":
            print("Skipped!\n")
            break
        elif answer.strip() == "less bar.txt":
            print("Correct!\n")
            break
        else:
            print("Incorrect. Please try again.\n")

    # Quiz 12
    print("Q12: Print the first 10 lines of your file bar.txt to the terminal.")
    hint_given = 0  # Track the number of hints given

    while True:
        if hint_given <2:
            answer = input("Enter your answer ('hint' for a hint, 'skip' to skip): ")
        else:
            answer = input("Enter your answer ('skip' to skip): ")

        if answer.strip().lower() == "hint":
            if hint_given < 1:
                print("Hint 1: head will print the first 10 lines of a file by default.\n")
                hint_given += 1
            elif hint_given < 2:
                print("No more hints available.\n")
                hint_given += 1
            else:
                print("No more hints available.\n")
        elif answer.strip() == "skip":
            print("Skipped!\n")
            break
        elif answer.strip() == "head bar.txt":
            print("Correct!\n")
            break
        else:
            print("Incorrect. Please try again.\n")

    # Quiz 13
    print("Q13: Print the last 10 lines of your file bar.txt to the terminal.")
    hint_given = 0  # Track the number of hints given

    while True:
        if hint_given <2:
            answer = input("Enter your answer ('hint' for a hint, 'skip' to skip): ")
        else:
            answer = input("Enter your answer ('skip' to skip): ")

        if answer.strip().lower() == "hint":
            if hint_given < 1:
                print("Hint 1: tail will print the last 10 lines of a file.\n")
                hint_given += 1
            elif hint_given < 2:
                print("No more hints available.\n")
                hint_given += 1
            else:
                print("No more hints available.\n")
        elif answer.strip() == "skip":
            print("Skipped!\n")
            break
        elif answer.strip() == "tail bar.txt":
            print("Correct!\n")
            break
        else:
            print("Incorrect. Please try again.\n")

    # Quiz 14
    print("Q14: Open your file bar.txt in a text editor.")
    hint_given = 0  # Track the number of hints given

    while True:
        if hint_given <2:
            answer = input("Enter your answer ('hint' for a hint, 'skip' to skip): ")
        else:
            answer = input("Enter your answer ('skip' to skip): ")

        if answer.strip().lower() == "hint":
            if hint_given < 1:
                print("Hint 1: nano is an easy to use text editor.\n")
                hint_given += 1
            elif hint_given < 2:
                print("No more hints available.\n")
                hint_given += 1
            else:
                print("No more hints available.\n")
        elif answer.strip() == "skip":
            print("Skipped!\n")
            break
        elif answer.strip() == "nano bar.txt":
            print("Correct!\n")
            break
        elif answer.strip() == "vim bar.txt":
            print("Correct!\n")
            break
        elif answer.strip() == "vi bar.txt":
            print("Correct!\n")
            break
        elif answer.strip() == "emacs bar.txt":
            print("Correct!\n")
            break
        elif answer.strip() == "gedit bar.txt":
            print("Correct!\n")
            break
        else:
            print("Incorrect. Please try again.\n")

    # Quiz 15
    print("Q15: Now, delete the file bar.txt.")
    hint_given = 0  # Track the number of hints given

    while True:
        if hint_given <2:
            answer = input("Enter your answer ('hint' for a hint, 'skip' to skip): ")
        else:
            answer = input("Enter your answer ('skip' to skip): ")

        if answer.strip().lower() == "hint":
            if hint_given < 1:
                print("Hint 1: rm is short for remove.\n")
                hint_given += 1
            elif hint_given < 2:
                print("No more hints available.\n")
                hint_given += 1
            else:
                print("No more hints available.\n")
        elif answer.strip() == "skip":
            print("Skipped!\n")
            break
        elif answer.strip() == "rm bar.txt":
            print("Correct!\n")
            break
        else:
            print("Incorrect. Please try again.\n")

    # Feedback
    print("Feedback")
    print("========\n")
    print("Congratulations! You have completed the Working with Directories tutorial.")
    input("Press any key to continue.")