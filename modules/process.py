from modules.quiz import QuizQuestion, run_quiz


TITLE = "Process Management"

QUESTIONS = (
    QuizQuestion(
        prompt="List all processes interactively.",
        accepted_answers=("top", "htop"),
        hints=("top is installed on most Linux distributions.", "htop has a friendlier interface, but may not be installed."),
    ),
    QuizQuestion(
        prompt="List all processes.",
        accepted_answers=("ps aux", "ps -ef", "ps a", "ps all"),
        hints=("ps prints process information.", "Common full listings include ps aux and ps -ef."),
    ),
    QuizQuestion(
        prompt="List the PID of all processes with the name bash.",
        accepted_answers=("pidof bash", "pgrep bash"),
        hints=("pidof prints process IDs for a specific program name.", "pgrep can also search processes by name."),
    ),
    QuizQuestion(
        prompt="Which key combination suspends a process running in the foreground?",
        accepted_answers=("ctrl+z", "control+z"),
        hints=("CTRL+Z pauses a foreground process.",),
        case_sensitive=False,
    ),
    QuizQuestion(
        prompt="Once suspended, how do you resume the paused process in the background?",
        accepted_answers=("bg",),
        hints=("bg is short for background.",),
    ),
    QuizQuestion(
        prompt="How do you bring the last background process to the foreground?",
        accepted_answers=("fg",),
        hints=("fg is short for foreground.",),
    ),
    QuizQuestion(
        prompt="Bring job number 1 to the foreground.",
        accepted_answers=("fg %1", "fg 1"),
        hints=("fg works with shell job IDs, not operating-system PIDs.", "Use jobs to see job IDs such as %1."),
        explanation="Shell job control uses job IDs like %1; PIDs are used by commands such as kill.",
    ),
    QuizQuestion(
        prompt="Execute Wireshark in the background.",
        accepted_answers=("wireshark &",),
        hints=("& backgrounds a process at launch.", "Linux command names are usually case-sensitive."),
    ),
    QuizQuestion(
        prompt="List all background jobs.",
        accepted_answers=("jobs",),
        hints=("jobs lists background jobs in the current shell.",),
    ),
    QuizQuestion(
        prompt="List all open files and the processes using them.",
        accepted_answers=("lsof",),
        hints=("lsof is short for list open files.",),
    ),
    QuizQuestion(
        prompt="Which key combination interrupts a process running in the foreground?",
        accepted_answers=("ctrl+c", "control+c"),
        hints=("CTRL+C sends an interrupt signal to a foreground process.",),
        case_sensitive=False,
    ),
    QuizQuestion(
        prompt="Gracefully shut down a process with PID 1000.",
        accepted_answers=("kill 1000", "kill -15 1000", "kill -TERM 1000"),
        hints=("kill sends signals to processes.", "The default kill signal is TERM."),
    ),
    QuizQuestion(
        prompt="Forcibly shut down a process with PID 1000.",
        accepted_answers=("kill -9 1000", "kill -KILL 1000", "kill -SIGKILL 1000"),
        hints=("kill sends signals to processes.", "-9 sends SIGKILL."),
    ),
    QuizQuestion(
        prompt="Gracefully shut down a process called foo by name.",
        accepted_answers=("pkill foo",),
        hints=("pkill sends signals to processes matched by name.",),
    ),
    QuizQuestion(
        prompt="Forcibly shut down a process called foo by name.",
        accepted_answers=("pkill -9 foo", "pkill -KILL foo", "pkill -SIGKILL foo"),
        hints=("pkill sends signals to processes matched by name.", "-9 sends SIGKILL."),
    ),
    QuizQuestion(
        prompt="Gracefully shut down all processes called foo.",
        accepted_answers=("killall foo",),
        hints=("killall sends a signal to every process with the given name.",),
    ),
)


def run():
    run_quiz(TITLE, QUESTIONS)
