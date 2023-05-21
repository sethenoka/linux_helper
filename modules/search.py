import os

def run():
    print("Searching the Filesystem Using Terminal")
    print("==================\n")

    # Quiz 1
    os.system('clear')
    print("Q1: Find the file for the command wget.")
    hint_given = 0  # Track the number of hints given

    while True:
        if hint_given <2:
            answer = input("Enter your answer ('hint' for a hint, 'skip' to skip): ")
        else:
            answer = input("Enter your answer ('skip' to skip): ")

        if answer.strip().lower() == "hint":
            if hint_given < 1:
                print("Hint 1: which is a command that will find binaries on Linux.\n")
                hint_given += 1
            elif hint_given < 2:
                print("Hint 2: locate is a command that uses an index and is fast for finding files.\n")
                hint_given += 1
            else:
                print("No more hints available.\n")
        elif answer.strip() == "skip":
            print("Skipped!\n")
            break
        elif answer.strip() == "which wget":
            print("Correct!\n")
            break
        elif answer.strip() == "locate wget":
            print("Correct!\n")
            break
        else:
            print("Incorrect. Please try again.\n")

    # Quiz 2
    print("Q2: Find a file named foo.txt in the /opt/ directory using the find command.")
    hint_given = 0  # Track the number of hints given

    while True:
        if hint_given <2:
            answer = input("Enter your answer ('hint' for a hint, 'skip' to skip): ")
        else:
            answer = input("Enter your answer ('skip' to skip): ")

        if answer.strip().lower() == "hint":
            if hint_given < 1:
                print("Hint 1: -iname can be used to perform a case insensitive search.\n")
                hint_given += 1
            elif hint_given < 2:
                print("Hint 2: find <path> -iname <keyword>.\n")
                hint_given += 1
            else:
                print("No more hints available.\n")
        elif answer.strip() == "skip":
            print("Skipped!\n")
            break
        elif answer.strip() == "find /opt/ -iname foo.txt":
            print("Correct!\n")
            break
        elif answer.strip() == "find /opt -iname foo.txt":
            print("Correct!\n")
            break
        elif answer.strip() == "find /opt -name foo.txt":
            print("Correct!\n")
            break
        elif answer.strip() == "find /opt/ -name foo.txt":
            print("Correct!\n")
            break
        else:
            print("Incorrect. Please try again.\n")

    # Quiz 3
    print("Q3: Find all .txt files (not directories) in the /opt/ directory using the find command.")
    hint_given = 0  # Track the number of hints given

    while True:
        if hint_given <2:
            answer = input("Enter your answer ('hint' for a hint, 'skip' to skip): ")
        else:
            answer = input("Enter your answer ('skip' to skip): ")

        if answer.strip().lower() == "hint":
            if hint_given < 1:
                print("Hint 1: find has a -type argument.\n")
                hint_given += 1
            elif hint_given < 2:
                print("Hint 2: find <path> -type f -iname *.txt.\n")
                hint_given += 1
            else:
                print("No more hints available.\n")
        elif answer.strip() == "skip":
            print("Skipped!\n")
            break
        elif answer.strip() == "find /opt/ -type f -iname *.txt":
            print("Correct!\n")
            break
        elif answer.strip() == "find /opt -type f -iname *.txt":
            print("Correct!\n")
            break
        elif answer.strip() == "find /opt -type f -name *.txt":
            print("Correct!\n")
            break
        elif answer.strip() == "find /opt/ -type f -name *.txt":
            print("Correct!\n")
            break
        else:
            print("Incorrect. Please try again.\n")

    # Quiz 4
    print("Q4: Find all directories (not files) named foo in the /opt/ directory using the find command.")
    hint_given = 0  # Track the number of hints given

    while True:
        if hint_given <2:
            answer = input("Enter your answer ('hint' for a hint, 'skip' to skip): ")
        else:
            answer = input("Enter your answer ('skip' to skip): ")

        if answer.strip().lower() == "hint":
            if hint_given < 1:
                print("Hint 1: find has a -type argument.\n")
                hint_given += 1
            elif hint_given < 2:
                print("Hint 2: find <path> -type d -iname foo.\n")
                hint_given += 1
            else:
                print("No more hints available.\n")
        elif answer.strip() == "skip":
            print("Skipped!\n")
            break
        elif answer.strip() == "find /opt/ -type d -iname foo":
            print("Correct!\n")
            break
        elif answer.strip() == "find /opt -type d -iname foo":
            print("Correct!\n")
            break
        elif answer.strip() == "find /opt -type d -name foo":
            print("Correct!\n")
            break
        elif answer.strip() == "find /opt/ -type d -name foo":
            print("Correct!\n")
            break
        else:
            print("Incorrect. Please try again.\n")

    # Quiz 5
    print("Q5: Search for the word foo in the file bar.txt using the grep command.")
    hint_given = 0  # Track the number of hints given

    while True:
        if hint_given <2:
            answer = input("Enter your answer ('hint' for a hint, 'skip' to skip): ")
        else:
            answer = input("Enter your answer ('skip' to skip): ")

        if answer.strip().lower() == "hint":
            if hint_given < 1:
                print("Hint 1: grep takes two arguments: keyword and file.\n")
                hint_given += 1
            elif hint_given < 2:
                print("No more hints available.\n")
                hint_given += 1
            else:
                print("No more hints available.\n")
        elif answer.strip() == "skip":
            print("Skipped!\n")
            break
        elif answer.strip() == "grep foo bar.txt":
            print("Correct!\n")
            break
        else:
            print("Incorrect. Please try again.\n")

    # Quiz 6
    print("Q6: Colour instances of foo in the file bar.txt using the grep command.")
    hint_given = 0  # Track the number of hints given

    while True:
        if hint_given <2:
            answer = input("Enter your answer ('hint' for a hint, 'skip' to skip): ")
        else:
            answer = input("Enter your answer ('skip' to skip): ")

        if answer.strip().lower() == "hint":
            if hint_given < 1:
                print("Hint 1: grep takes two arguments: keyword and file.\n")
                hint_given += 1
            elif hint_given < 2:
                print("Hint 2: --color=always will highlight the matches when using grep.\n")
                hint_given += 1
            else:
                print("No more hints available.\n")
        elif answer.strip() == "skip":
            print("Skipped!\n")
            break
        elif answer.strip() == "grep --color=always foo bar.txt":
            print("Correct!\n")
            break
        else:
            print("Incorrect. Please try again.\n")

    # Quiz 7
    print("Q7: Show only lines not containing foo in the file bar.txt using the grep command.")
    hint_given = 0  # Track the number of hints given

    while True:
        if hint_given <2:
            answer = input("Enter your answer ('hint' for a hint, 'skip' to skip): ")
        else:
            answer = input("Enter your answer ('skip' to skip): ")

        if answer.strip().lower() == "hint":
            if hint_given < 1:
                print("Hint 1: grep takes two arguments: keyword and file.\n")
                hint_given += 1
            elif hint_given < 2:
                print("Hint 2: -v does an inverse or exclusive search in grep.\n")
                hint_given += 1
            else:
                print("No more hints available.\n")
        elif answer.strip() == "skip":
            print("Skipped!\n")
            break
        elif answer.strip() == "grep -v foo bar.txt":
            print("Correct!\n")
            break
        else:
            print("Incorrect. Please try again.\n")

    # Quiz 8
    print("Q8: Perform a case insensitive search for foo in the file bar.txt using the grep command.")
    hint_given = 0  # Track the number of hints given

    while True:
        if hint_given <2:
            answer = input("Enter your answer ('hint' for a hint, 'skip' to skip): ")
        else:
            answer = input("Enter your answer ('skip' to skip): ")

        if answer.strip().lower() == "hint":
            if hint_given < 1:
                print("Hint 1: grep takes two arguments: keyword and file.\n")
                hint_given += 1
            elif hint_given < 2:
                print("Hint 2: -i performs a case insensitive search in grep.\n")
                hint_given += 1
            else:
                print("No more hints available.\n")
        elif answer.strip() == "skip":
            print("Skipped!\n")
            break
        elif answer.strip() == "grep -i foo bar.txt":
            print("Correct!\n")
            break
        else:
            print("Incorrect. Please try again.\n")

    # Quiz 9
    print("Q9: Return five lines of context around lines containing foo in the file bar.txt using the grep command.")
    hint_given = 0  # Track the number of hints given

    while True:
        if hint_given <2:
            answer = input("Enter your answer ('hint' for a hint, 'skip' to skip): ")
        else:
            answer = input("Enter your answer ('skip' to skip): ")

        if answer.strip().lower() == "hint":
            if hint_given < 1:
                print("Hint 1: grep takes two arguments: keyword and file.\n")
                hint_given += 1
            elif hint_given < 2:
                print("Hint 2: -C provides additional lines of context in grep.\n")
                hint_given += 1
            else:
                print("No more hints available.\n")
        elif answer.strip() == "skip":
            print("Skipped!\n")
            break
        elif answer.strip() == "grep -C 5 foo bar.txt":
            print("Correct!\n")
            break
        else:
            print("Incorrect. Please try again.\n")

    # Quiz 10
    print("Q10: Search for foo or bar in the file bar.txt using the grep command.")
    hint_given = 0  # Track the number of hints given

    while True:
        if hint_given <2:
            answer = input("Enter your answer ('hint' for a hint, 'skip' to skip): ")
        else:
            answer = input("Enter your answer ('skip' to skip): ")

        if answer.strip().lower() == "hint":
            if hint_given < 1:
                print("Hint 1: grep takes two arguments: keyword and file.\n")
                hint_given += 1
            elif hint_given < 2:
                print("Hint 2: 'a|b' is used to indicate an or search in grep.\n")
                hint_given += 1
            else:
                print("No more hints available.\n")
        elif answer.strip() == "skip":
            print("Skipped!\n")
            break
        elif answer.strip() == "grep 'foo|bar' bar.txt":
            print("Correct!\n")
            break
        else:
            print("Incorrect. Please try again.\n")

    # Feedback
    print("Feedback")
    print("========\n")
    print("Congratulations! You have completed the Searching the Filesystem Using Terminal tutorial.")
    input("Press any key to continue.")