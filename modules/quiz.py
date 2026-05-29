import os
import re
import subprocess
import sys
from dataclasses import dataclass, field
from typing import Callable, Iterable


PrintFunc = Callable[[str], None]
InputFunc = Callable[[str], str]


@dataclass(frozen=True)
class QuizQuestion:
    prompt: str
    accepted_answers: tuple[str, ...]
    hints: tuple[str, ...] = field(default_factory=tuple)
    explanation: str = ""
    case_sensitive: bool = True
    allow_sudo: bool = True


@dataclass(frozen=True)
class QuizResult:
    total: int
    correct: int
    skipped: int
    attempts: int


def clear_screen() -> None:
    if not sys.stdout.isatty():
        return

    command = "cls" if os.name == "nt" else "clear"
    try:
        subprocess.run([command], check=False)
    except FileNotFoundError:
        return


def normalize_answer(answer: str, *, case_sensitive: bool = True, allow_sudo: bool = True) -> str:
    normalized = re.sub(r"\s+", " ", answer.strip())

    if allow_sudo and normalized.startswith("sudo "):
        normalized = normalized[5:].strip()

    if not case_sensitive:
        normalized = normalized.lower()

    return normalized


def is_correct(answer: str, question: QuizQuestion) -> bool:
    normalized_answer = normalize_answer(
        answer,
        case_sensitive=question.case_sensitive,
        allow_sudo=question.allow_sudo,
    )

    normalized_expected = {
        normalize_answer(
            expected,
            case_sensitive=question.case_sensitive,
            allow_sudo=question.allow_sudo,
        )
        for expected in question.accepted_answers
    }

    return normalized_answer in normalized_expected


def run_quiz(
    title: str,
    questions: Iterable[QuizQuestion],
    *,
    input_func: InputFunc = input,
    print_func: PrintFunc = print,
    clear_before_start: bool = True,
) -> QuizResult:
    question_list = list(questions)

    if clear_before_start:
        clear_screen()

    print_func(title)
    print_func("=" * len(title))
    print_func("")

    correct = 0
    skipped = 0
    attempts = 0

    for index, question in enumerate(question_list, start=1):
        print_func(f"Q{index}: {question.prompt}")
        hints_used = 0

        while True:
            prompt = "Enter your answer ('hint' for a hint, 'skip' to skip): "
            if hints_used >= len(question.hints):
                prompt = "Enter your answer ('skip' to skip): "

            answer = input_func(prompt)
            command = answer.strip().lower()

            if command == "hint":
                if hints_used < len(question.hints):
                    print_func(f"Hint {hints_used + 1}: {question.hints[hints_used]}\n")
                    hints_used += 1
                else:
                    print_func("No more hints available.\n")
                continue

            if command == "skip":
                skipped += 1
                print_func("Skipped!\n")
                break

            attempts += 1

            if is_correct(answer, question):
                correct += 1
                print_func("Correct!")
                if question.explanation:
                    print_func(question.explanation)
                print_func("")
                break

            print_func("Incorrect. Please try again.\n")

    print_func("Feedback")
    print_func("========")
    print_func(f"You answered {correct} of {len(question_list)} questions correctly.")
    if skipped:
        print_func(f"You skipped {skipped} question(s).")
    print_func(f"Total attempts: {attempts}.")

    return QuizResult(
        total=len(question_list),
        correct=correct,
        skipped=skipped,
        attempts=attempts,
    )
