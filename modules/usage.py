from modules.quiz import QuizQuestion, run_quiz


TITLE = "Disk and Memory Usage and Statistics"

QUESTIONS = (
    QuizQuestion(
        prompt="List disks, their sizes, used space, and available space.",
        accepted_answers=("df",),
        hints=("df is short for 'disk free'.",),
    ),
    QuizQuestion(
        prompt="List disks, their sizes, used space, and available space with human-readable numbers.",
        accepted_answers=("df -h",),
        hints=("df is short for 'disk free'.", "-h shows human-readable sizes."),
    ),
    QuizQuestion(
        prompt="List file sizes for the current directory contents, including sub-directories.",
        accepted_answers=("du",),
        hints=("du is short for 'disk usage'.",),
    ),
    QuizQuestion(
        prompt="Show current memory usage.",
        accepted_answers=("free",),
        hints=("free shows memory usage statistics.",),
    ),
    QuizQuestion(
        prompt="Show current memory usage, updating every 5 seconds.",
        accepted_answers=("free -s 5", "free --seconds 5"),
        hints=("free shows memory usage statistics.", "-s repeats output every given number of seconds."),
    ),
)


def run():
    run_quiz(TITLE, QUESTIONS)
