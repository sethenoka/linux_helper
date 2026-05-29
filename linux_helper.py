import argparse
import importlib
from dataclasses import dataclass
from typing import Optional, Sequence

from modules.quiz import clear_screen


LINKS = (
    "Bash Cheat Sheet: https://github.com/RehanSaeed/Bash-Cheat-Sheet",
    "Bash Reference Manual: https://www.gnu.org/software/bash/manual/bash.html",
    "Linux Command Line Tutorial: https://www.learnshell.org/",
)


@dataclass(frozen=True)
class ModuleEntry:
    key: str
    title: str
    module_name: str


MODULES = (
    ModuleEntry("navigation", "Terminal Navigation", "navigation"),
    ModuleEntry("directories", "Working with Directories and Files", "directories"),
    ModuleEntry("search", "Searching in Terminal", "search"),
    ModuleEntry("usage", "Disk and Memory Usage and Statistics", "usage"),
    ModuleEntry("packages", "Package Management", "packages"),
    ModuleEntry("process", "Process Management", "process"),
    ModuleEntry("misc", "Miscellaneous", "misc"),
)


def print_menu() -> None:
    print("Available Modules:")
    for index, entry in enumerate(MODULES, start=1):
        print(f"{index}. {entry.title} ({entry.key})")
    print(f"{len(MODULES) + 1}. Exit")


def print_goodbye() -> None:
    print("Exiting the program.")
    print("If you'd like to learn more, please visit the following links:\n")
    for link in LINKS:
        print(f"- {link}")
    print("Goodbye!")


def get_module(selection: str) -> Optional[ModuleEntry]:
    selection = selection.strip().lower()

    if selection.isdigit():
        index = int(selection)
        if 1 <= index <= len(MODULES):
            return MODULES[index - 1]
        return None

    for entry in MODULES:
        if selection in {entry.key, entry.module_name}:
            return entry

    return None


def run_module(entry: ModuleEntry, *, return_to_menu: bool = True) -> None:
    module = importlib.import_module(f"modules.{entry.module_name}")
    run = getattr(module, "run", None)

    if not callable(run):
        raise TypeError(f"modules.{entry.module_name} doesn't define a callable run()")

    clear_screen()
    run()
    if return_to_menu:
        input("Press Enter to return to the menu.")
        clear_screen()


def parse_args(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Interactive Bash basics quiz helper.")
    parser.add_argument(
        "module",
        nargs="?",
        choices=[entry.key for entry in MODULES],
        help="Run a single module directly.",
    )
    parser.add_argument("--list", action="store_true", help="List available modules and exit.")
    return parser.parse_args(argv)


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = parse_args(argv)

    if args.list:
        print_menu()
        return 0

    if args.module:
        entry = get_module(args.module)
        if entry is None:
            raise ValueError(f"Unknown module: {args.module}")
        run_module(entry, return_to_menu=False)
        return 0

    clear_screen()
    print("Welcome to the Bash Basics tutorial!")
    print("In this tutorial, you'll learn the basics of using the Bash terminal.")
    print("Let's get started!\n")

    while True:
        print_menu()
        choice = input(f"Enter your choice (1-{len(MODULES) + 1}, or a module name): ")
        normalized_choice = choice.strip().lower()

        if normalized_choice in {str(len(MODULES) + 1), "exit", "quit", "q"}:
            print_goodbye()
            return 0

        entry = get_module(choice)
        if entry is None:
            print("Invalid choice. Please try again.\n")
            continue

        run_module(entry)


if __name__ == "__main__":
    raise SystemExit(main())
