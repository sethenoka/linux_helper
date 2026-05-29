from modules.quiz import QuizQuestion, run_quiz


TITLE = "Terminal Navigation"

QUESTIONS = (
    QuizQuestion(
        prompt="Navigate to the root directory.",
        accepted_answers=("cd /",),
        hints=("cd is short for 'change directory'.", "Use '/' to specify the root directory."),
        explanation="The root directory is the top of the Linux filesystem.",
    ),
    QuizQuestion(
        prompt="Navigate to the foo sub-directory.",
        accepted_answers=("cd foo",),
        hints=("cd is short for 'change directory'.", "Use the folder name to specify a sub-directory."),
    ),
    QuizQuestion(
        prompt="Navigate to the user's home directory.",
        accepted_answers=("cd ~", "cd"),
        hints=("cd is short for 'change directory'.", "~ is a shortcut for the user's home directory."),
        explanation="Running cd with no path also returns you to your home directory.",
    ),
    QuizQuestion(
        prompt="Navigate to the previous directory.",
        accepted_answers=("cd -",),
        hints=("cd is short for 'change directory'.", "- is a shortcut for the last directory used."),
    ),
    QuizQuestion(
        prompt="Print the current directory path.",
        accepted_answers=("pwd",),
        hints=("This command stands for 'print working directory'.",),
    ),
    QuizQuestion(
        prompt="List the contents of the current directory.",
        accepted_answers=("ls",),
        hints=("This command provides a simple listing of directory contents.",),
    ),
    QuizQuestion(
        prompt="List the contents of the current directory, including hidden files.",
        accepted_answers=("ls -la", "ls -al", "ls -a"),
        hints=("-a shows all files and directories, including hidden dotfiles.",),
    ),
    QuizQuestion(
        prompt="List the contents of the current directory with human-readable size metadata.",
        accepted_answers=("ls -lh", "ls -hl"),
        hints=("-l provides a long listing.", "-h makes file sizes human-readable."),
    ),
    QuizQuestion(
        prompt="List the contents of the current directory, sorted by modification time.",
        accepted_answers=("ls -lt", "ls -tl"),
        hints=("-l provides a long listing.", "-t sorts by modification time."),
    ),
    QuizQuestion(
        prompt="List the file/directory tree of the current directory.",
        accepted_answers=("tree",),
        hints=("tree displays a hierarchical view of directory contents.",),
    ),
    QuizQuestion(
        prompt="List only the directory tree of the current directory.",
        accepted_answers=("tree -d",),
        hints=("tree displays a hierarchical view of directory contents.", "-d displays only directories."),
    ),
    QuizQuestion(
        prompt="List the size, created timestamp, and modified timestamp for foo.txt.",
        accepted_answers=("stat foo.txt",),
        hints=("stat provides detailed information about a file or directory.",),
    ),
)


def run():
    run_quiz(TITLE, QUESTIONS)
