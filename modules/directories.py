from modules.quiz import QuizQuestion, run_quiz


TITLE = "Working with Directories and Files"

QUESTIONS = (
    QuizQuestion(
        prompt="Create a directory named foo.",
        accepted_answers=("mkdir foo",),
        hints=("mkdir is short for 'make directory'.", "Specify the directory name foo."),
    ),
    QuizQuestion(
        prompt="Create multiple directories named foo and bar.",
        accepted_answers=("mkdir foo bar",),
        hints=("mkdir is short for 'make directory'.", "You can provide multiple directory names."),
    ),
    QuizQuestion(
        prompt="Create a directory foo with a sub-directory bar in a single command.",
        accepted_answers=("mkdir -p foo/bar",),
        hints=("mkdir is short for 'make directory'.", "-p creates missing parent directories."),
    ),
    QuizQuestion(
        prompt="Delete the directory named foo including its contents.",
        accepted_answers=("rm -r foo", "rm -rf foo"),
        hints=("rm is short for 'remove'.", "-r recursively removes a directory and its contents."),
        explanation="rmdir only removes empty directories; rm -r handles non-empty directories.",
    ),
    QuizQuestion(
        prompt="Create an empty file named foo.txt.",
        accepted_answers=("touch foo.txt",),
        hints=("touch creates a file or updates an existing file's timestamps.",),
    ),
    QuizQuestion(
        prompt="Write 'Hello, world!' to a file named foo.txt.",
        accepted_answers=(
            "echo 'Hello, world!' > foo.txt",
            'echo "Hello, world!" > foo.txt',
        ),
        hints=("echo writes text to standard output.", "> redirects output to a file and overwrites it."),
    ),
    QuizQuestion(
        prompt="Append bar to your file named foo.txt.",
        accepted_answers=("echo bar >> foo.txt", "echo 'bar' >> foo.txt", 'echo "bar" >> foo.txt'),
        hints=("echo writes text to standard output.", ">> redirects output to a file and appends it."),
    ),
    QuizQuestion(
        prompt="Copy the file foo.txt to a new file, bar.txt.",
        accepted_answers=("cp foo.txt bar.txt",),
        hints=("cp is short for copy.", "cp takes source and destination arguments."),
    ),
    QuizQuestion(
        prompt="Move the file foo.txt to bar.txt, changing its name.",
        accepted_answers=("mv foo.txt bar.txt",),
        hints=("mv is short for move.", "mv takes source and destination arguments."),
    ),
    QuizQuestion(
        prompt="Print all the contents of your file bar.txt to the terminal.",
        accepted_answers=("cat bar.txt",),
        hints=("cat is short for concatenate.",),
    ),
    QuizQuestion(
        prompt="Print the contents of your file bar.txt so you can scroll through it.",
        accepted_answers=("less bar.txt", "more bar.txt"),
        hints=("less opens file output in a pager.",),
    ),
    QuizQuestion(
        prompt="Print the first 10 lines of your file bar.txt to the terminal.",
        accepted_answers=("head bar.txt", "head -n 10 bar.txt"),
        hints=("head prints the first 10 lines of a file by default.",),
    ),
    QuizQuestion(
        prompt="Print the last 10 lines of your file bar.txt to the terminal.",
        accepted_answers=("tail bar.txt", "tail -n 10 bar.txt"),
        hints=("tail prints the last 10 lines of a file by default.",),
    ),
    QuizQuestion(
        prompt="Open your file bar.txt in a text editor.",
        accepted_answers=(
            "nano bar.txt",
            "vim bar.txt",
            "vi bar.txt",
            "emacs bar.txt",
            "gedit bar.txt",
        ),
        hints=("nano is a common beginner-friendly terminal text editor.",),
    ),
    QuizQuestion(
        prompt="Delete the file bar.txt.",
        accepted_answers=("rm bar.txt",),
        hints=("rm is short for remove.",),
    ),
)


def run():
    run_quiz(TITLE, QUESTIONS)
