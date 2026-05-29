from modules.quiz import QuizQuestion, run_quiz


TITLE = "Package Management"

QUESTIONS = (
    QuizQuestion(
        prompt="Refresh the repository index.",
        accepted_answers=("apt update",),
        hints=("apt manages packages on Debian-based distributions such as Kali and Ubuntu.", "apt update refreshes repository metadata."),
    ),
    QuizQuestion(
        prompt="Upgrade all upgradable packages.",
        accepted_answers=("apt upgrade",),
        hints=("apt manages packages on Debian-based distributions such as Kali and Ubuntu.", "apt upgrade installs available package upgrades."),
    ),
    QuizQuestion(
        prompt="Find the wget application/package.",
        accepted_answers=("apt search wget",),
        hints=("apt manages packages on Debian-based distributions such as Kali and Ubuntu.", "apt search finds matching packages."),
    ),
    QuizQuestion(
        prompt="List information about the wget application/package.",
        accepted_answers=("apt show wget",),
        hints=("apt manages packages on Debian-based distributions such as Kali and Ubuntu.", "apt show displays package details."),
    ),
    QuizQuestion(
        prompt="Install the latest available version of wget.",
        accepted_answers=("apt install wget",),
        hints=("apt manages packages on Debian-based distributions such as Kali and Ubuntu.", "apt install installs packages."),
    ),
    QuizQuestion(
        prompt="Remove wget from the system.",
        accepted_answers=("apt remove wget",),
        hints=("apt manages packages on Debian-based distributions such as Kali and Ubuntu.", "apt remove uninstalls packages."),
    ),
)


def run():
    run_quiz(TITLE, QUESTIONS)
