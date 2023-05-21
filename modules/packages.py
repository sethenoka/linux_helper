import os

def run():
    print("Package Management")
    print("==================\n")

    # Quiz 1
    os.system('clear')
    print("Q1: Refresh the repository index.")
    hint_given = 0  # Track the number of hints given

    while True:
        if hint_given <2:
            answer = input("Enter your answer ('hint' for a hint, 'skip' to skip): ")
        else:
            answer = input("Enter your answer ('skip' to skip): ")

        if answer.strip().lower() == "hint":
            if hint_given < 1:
                print("Hint 1: apt is the package manager used to manage applications in Kali.\n")
                hint_given += 1
            elif hint_given < 2:
                print("Hint 2: apt has an update argument for updating the repository index.\n")
                hint_given += 1
            else:
                print("No more hints available.\n")
        elif answer.strip() == "skip":
            print("Skipped!\n")
            break
        elif answer.strip() == "apt update":
            print("Correct!\n")
            break
        else:
            print("Incorrect. Please try again.\n")

    # Quiz 2
    print("Q2: Upgrade all upgradable packages.")
    hint_given = 0  # Track the number of hints given

    while True:
        if hint_given <2:
            answer = input("Enter your answer ('hint' for a hint, 'skip' to skip): ")
        else:
            answer = input("Enter your answer ('skip' to skip): ")

        if answer.strip().lower() == "hint":
            if hint_given < 1:
                print("Hint 1: apt is the package manager used to manage applications in Kali.\n")
                hint_given += 1
            elif hint_given < 2:
                print("Hint 2: apt has an upgrade argument for upgrading applications.\n")
                hint_given += 1
            else:
                print("No more hints available.\n")
        elif answer.strip() == "skip":
            print("Skipped!\n")
            break
        elif answer.strip() == "apt upgrade":
            print("Correct!\n")
            break
        else:
            print("Incorrect. Please try again.\n")

    # Quiz 3
    print("Q3: Find the wget application/package.")
    hint_given = 0  # Track the number of hints given

    while True:
        if hint_given <2:
            answer = input("Enter your answer ('hint' for a hint, 'skip' to skip): ")
        else:
            answer = input("Enter your answer ('skip' to skip): ")

        if answer.strip().lower() == "hint":
            if hint_given < 1:
                print("Hint 1: apt is the package manager used to manage applications in Kali.\n")
                hint_given += 1
            elif hint_given < 2:
                print("Hint 2: apt has a search argument for finding application packages to install.\n")
                hint_given += 1
            else:
                print("No more hints available.\n")
        elif answer.strip() == "skip":
            print("Skipped!\n")
            break
        elif answer.strip() == "apt search wget":
            print("Correct!\n")
            break
        else:
            print("Incorrect. Please try again.\n")

    # Quiz 4
    print("Q4: List information about the wget application/package.")
    hint_given = 0  # Track the number of hints given

    while True:
        if hint_given <2:
            answer = input("Enter your answer ('hint' for a hint, 'skip' to skip): ")
        else:
            answer = input("Enter your answer ('skip' to skip): ")

        if answer.strip().lower() == "hint":
            if hint_given < 1:
                print("Hint 1: apt is the package manager used to manage applications in Kali.\n")
                hint_given += 1
            elif hint_given < 2:
                print("Hint 2: apt has a show argument for finding application packages to install.\n")
                hint_given += 1
            else:
                print("No more hints available.\n")
        elif answer.strip() == "skip":
            print("Skipped!\n")
            break
        elif answer.strip() == "apt show wget":
            print("Correct!\n")
            break
        else:
            print("Incorrect. Please try again.\n")

    # Quiz 5
    print("Q5: Install the latest version of wget.")
    hint_given = 0  # Track the number of hints given

    while True:
        if hint_given <2:
            answer = input("Enter your answer ('hint' for a hint, 'skip' to skip): ")
        else:
            answer = input("Enter your answer ('skip' to skip): ")

        if answer.strip().lower() == "hint":
            if hint_given < 1:
                print("Hint 1: apt is the package manager used to manage applications in Kali.\n")
                hint_given += 1
            elif hint_given < 2:
                print("Hint 2: apt has an install argument for finding application packages to install.\n")
                hint_given += 1
            else:
                print("No more hints available.\n")
        elif answer.strip() == "skip":
            print("Skipped!\n")
            break
        elif answer.strip() == "apt install wget":
            print("Correct!\n")
            break
        else:
            print("Incorrect. Please try again.\n")

    # Quiz 6
    print("Q6: Remove wget from the system.")
    hint_given = 0  # Track the number of hints given

    while True:
        if hint_given <2:
            answer = input("Enter your answer ('hint' for a hint, 'skip' to skip): ")
        else:
            answer = input("Enter your answer ('skip' to skip): ")

        if answer.strip().lower() == "hint":
            if hint_given < 1:
                print("Hint 1: apt is the package manager used to manage applications in Kali.\n")
                hint_given += 1
            elif hint_given < 2:
                print("Hint 2: apt has a remove argument for finding application packages to install.\n")
                hint_given += 1
            else:
                print("No more hints available.\n")
        elif answer.strip() == "skip":
            print("Skipped!\n")
            break
        elif answer.strip() == "apt remove wget":
            print("Correct!\n")
            break
        else:
            print("Incorrect. Please try again.\n")

    # Feedback
    print("Feedback")
    print("========\n")
    print("Congratulations! You have completed the Package Management tutorial.")
    input("Press any key to continue.")