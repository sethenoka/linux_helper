# Python Bash Helper

Python Bash Helper is an interactive terminal quiz for learning common Linux and Bash commands used in system administration, networking, and security workflows.

## Requirements

- Python 3.9 or newer
- A terminal environment for running the quiz
- A Linux or Unix-like shell is recommended if you want to practice the commands exactly as written

## Usage

Run the interactive menu:

```bash
python3 linux_helper.py
```

List available modules:

```bash
python3 linux_helper.py --list
```

Run a single module directly:

```bash
python3 linux_helper.py search
python3 linux_helper.py packages
```

Available module keys are:

- `navigation`
- `directories`
- `search`
- `usage`
- `packages`
- `process`
- `misc`

## Adding Questions

Each topic module defines a `QUESTIONS` tuple of `QuizQuestion` objects and calls the shared runner in `modules/quiz.py`. Add new content by adding another `QuizQuestion` to the relevant module:

```python
QuizQuestion(
    prompt="Print the current directory path.",
    accepted_answers=("pwd",),
    hints=("This command stands for 'print working directory'.",),
)
```

Use multiple `accepted_answers` for common valid variations. The runner automatically handles `hint`, `skip`, whitespace normalisation, scoring, and optional `sudo` prefixes.

## Testing

Run the test suite:

```bash
python3 -m unittest
```

Run a syntax check:

```bash
python3 -m py_compile linux_helper.py modules/*.py tests/*.py
```

## Resources

- Bash Cheat Sheet: https://github.com/RehanSaeed/Bash-Cheat-Sheet
- Bash Reference Manual: https://www.gnu.org/software/bash/manual/bash.html
- Linux Command Line Tutorial: https://www.learnshell.org/

## License

MIT. See [LICENSE](LICENSE).
