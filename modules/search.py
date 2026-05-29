from modules.quiz import QuizQuestion, run_quiz


TITLE = "Searching the Filesystem Using Terminal"

QUESTIONS = (
    QuizQuestion(
        prompt="Find the executable file for the command wget.",
        accepted_answers=("which wget", "command -v wget"),
        hints=("which finds executables in your PATH.", "command -v is a portable shell builtin."),
    ),
    QuizQuestion(
        prompt="Find a file named foo.txt in the /opt directory using the find command.",
        accepted_answers=(
            "find /opt -iname foo.txt",
            "find /opt/ -iname foo.txt",
            "find /opt -name foo.txt",
            "find /opt/ -name foo.txt",
        ),
        hints=("-iname performs a case-insensitive search.", "find <path> -iname <name>"),
    ),
    QuizQuestion(
        prompt="Find all .txt files, not directories, in the /opt directory using find.",
        accepted_answers=(
            'find /opt -type f -iname "*.txt"',
            'find /opt/ -type f -iname "*.txt"',
            "find /opt -type f -iname *.txt",
            "find /opt/ -type f -iname *.txt",
            'find /opt -type f -name "*.txt"',
            'find /opt/ -type f -name "*.txt"',
        ),
        hints=("find has a -type argument.", 'Quote "*.txt" so the shell does not expand it first.'),
    ),
    QuizQuestion(
        prompt="Find all directories, not files, named foo in the /opt directory using find.",
        accepted_answers=(
            "find /opt -type d -iname foo",
            "find /opt/ -type d -iname foo",
            "find /opt -type d -name foo",
            "find /opt/ -type d -name foo",
        ),
        hints=("find has a -type argument.", "Use -type d to search for directories."),
    ),
    QuizQuestion(
        prompt="Search for the word foo in the file bar.txt using grep.",
        accepted_answers=("grep foo bar.txt",),
        hints=("grep takes a pattern and one or more files.",),
    ),
    QuizQuestion(
        prompt="Color instances of foo in the file bar.txt using grep.",
        accepted_answers=("grep --color=always foo bar.txt", "grep --color foo bar.txt"),
        hints=("grep takes a pattern and one or more files.", "--color highlights matching text."),
    ),
    QuizQuestion(
        prompt="Show only lines not containing foo in the file bar.txt using grep.",
        accepted_answers=("grep -v foo bar.txt",),
        hints=("grep takes a pattern and one or more files.", "-v inverts the match."),
    ),
    QuizQuestion(
        prompt="Perform a case-insensitive search for foo in the file bar.txt using grep.",
        accepted_answers=("grep -i foo bar.txt",),
        hints=("grep takes a pattern and one or more files.", "-i makes matching case-insensitive."),
    ),
    QuizQuestion(
        prompt="Return five lines of context around lines containing foo in bar.txt using grep.",
        accepted_answers=("grep -C 5 foo bar.txt", "grep -C5 foo bar.txt"),
        hints=("grep takes a pattern and one or more files.", "-C adds context around matching lines."),
    ),
    QuizQuestion(
        prompt="Search for foo or bar in the file bar.txt using grep.",
        accepted_answers=(
            "grep -E 'foo|bar' bar.txt",
            'grep -E "foo|bar" bar.txt',
            "egrep 'foo|bar' bar.txt",
            'egrep "foo|bar" bar.txt',
        ),
        hints=("Basic grep treats | literally unless extended regex is enabled.", "-E enables extended regular expressions."),
        explanation="With basic grep, 'foo|bar' is a literal pattern. grep -E makes | mean OR.",
    ),
)


def run():
    run_quiz(TITLE, QUESTIONS)
