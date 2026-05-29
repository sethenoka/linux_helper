from modules.quiz import QuizQuestion, run_quiz


TITLE = "Miscellaneous Terminal Commands"

QUESTIONS = (
    QuizQuestion(
        prompt="Print the current date and time in the terminal.",
        accepted_answers=("date",),
        hints=("date prints or sets the system date and time.",),
    ),
    QuizQuestion(
        prompt="List the IP addresses configured on your system.",
        accepted_answers=("ip addr", "ip a", "ip address", "ip address show", "ifconfig"),
        hints=("ifconfig can do this, but may not be installed by default.", "ip addr is the modern command for this."),
    ),
    QuizQuestion(
        prompt="Schedule a system shutdown to occur in 1 minute.",
        accepted_answers=("shutdown +1", "shutdown -h +1"),
        hints=("shutdown schedules power operations.", "+1 schedules it one minute from now."),
    ),
    QuizQuestion(
        prompt="Immediately shut down the system.",
        accepted_answers=("shutdown now", "shutdown -h now", "poweroff"),
        hints=("shutdown schedules power operations.", "now runs it immediately."),
    ),
    QuizQuestion(
        prompt="Immediately reboot the system.",
        accepted_answers=("shutdown -r now", "reboot", "systemctl reboot"),
        hints=("shutdown schedules power operations.", "-r requests a reboot, and now runs it immediately."),
    ),
    QuizQuestion(
        prompt="Cancel a scheduled reboot or shutdown.",
        accepted_answers=("shutdown -c",),
        hints=("shutdown schedules power operations.", "-c cancels a pending shutdown."),
    ),
    QuizQuestion(
        prompt="Copy the file /foo to /bar using rsync.",
        accepted_answers=("rsync /foo /bar",),
        hints=("rsync takes source and destination arguments.",),
    ),
    QuizQuestion(
        prompt="Copy the directory /foo to /bar using rsync, recursively.",
        accepted_answers=("rsync -r /foo /bar", "rsync -a /foo /bar"),
        hints=("rsync takes source and destination arguments.", "-r recursively copies directories; -a includes recursion and preserves metadata."),
    ),
    QuizQuestion(
        prompt="Copy only newer files from /foo to /bar using rsync, recursively.",
        accepted_answers=("rsync -ru /foo /bar", "rsync -a --update /foo /bar"),
        hints=("rsync takes source and destination arguments.", "-ru means recursive and update."),
    ),
    QuizQuestion(
        prompt="Copy only newer files from /foo to /bar using rsync, recursively, with human-readable numbers.",
        accepted_answers=("rsync -ruh /foo /bar", "rsync -a --update --human-readable /foo /bar"),
        hints=("rsync takes source and destination arguments.", "-ruh means recursive, update, and human-readable."),
    ),
    QuizQuestion(
        prompt="Copy only newer files from /foo to /bar using rsync, recursively, with human-readable numbers and progress.",
        accepted_answers=(
            "rsync -ruhP /foo /bar",
            "rsync -ruh --progress /foo /bar",
            "rsync -a --update --human-readable --progress /foo /bar",
        ),
        hints=("rsync takes source and destination arguments.", "-P is a shortcut for partial transfers and progress output."),
    ),
    QuizQuestion(
        prompt="Show the manual for wget.",
        accepted_answers=("man wget",),
        hints=("man opens manual pages for commands that provide them.",),
    ),
)


def run():
    run_quiz(TITLE, QUESTIONS)
