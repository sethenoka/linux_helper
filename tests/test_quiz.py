import unittest

import linux_helper
from modules import directories, misc, navigation, packages, process, search, usage
from modules.quiz import QuizQuestion, is_correct, normalize_answer, run_quiz


TOPIC_MODULES = (
    navigation,
    directories,
    search,
    usage,
    packages,
    process,
    misc,
)


def find_question(module, prompt_fragment):
    for question in module.QUESTIONS:
        if prompt_fragment in question.prompt:
            return question
    raise AssertionError(f"Question containing {prompt_fragment!r} not found in {module.__name__}")


class QuizRunnerTests(unittest.TestCase):
    def test_normalize_answer_collapses_whitespace_and_optional_sudo(self):
        self.assertEqual(normalize_answer("  sudo   apt   update  "), "apt update")

    def test_is_correct_respects_case_sensitive_commands_by_default(self):
        question = QuizQuestion(prompt="Run wireshark", accepted_answers=("wireshark &",))

        self.assertTrue(is_correct("wireshark &", question))
        self.assertFalse(is_correct("Wireshark &", question))

    def test_is_correct_can_be_case_insensitive(self):
        question = QuizQuestion(
            prompt="Interrupt a process",
            accepted_answers=("ctrl+c",),
            case_sensitive=False,
        )

        self.assertTrue(is_correct("CTRL+C", question))

    def test_run_quiz_tracks_correct_skipped_and_attempts(self):
        questions = (
            QuizQuestion(prompt="First", accepted_answers=("one",), hints=("Number one.",)),
            QuizQuestion(prompt="Second", accepted_answers=("two",)),
        )
        answers = iter(("hint", "wrong", "one", "skip"))
        output = []

        result = run_quiz(
            "Test Quiz",
            questions,
            input_func=lambda _prompt: next(answers),
            print_func=output.append,
            clear_before_start=False,
        )

        self.assertEqual(result.total, 2)
        self.assertEqual(result.correct, 1)
        self.assertEqual(result.skipped, 1)
        self.assertEqual(result.attempts, 2)


class QuizDataTests(unittest.TestCase):
    def test_all_questions_have_required_content(self):
        for module in TOPIC_MODULES:
            with self.subTest(module=module.__name__):
                self.assertTrue(module.TITLE)
                self.assertTrue(module.QUESTIONS)

                prompts = [question.prompt for question in module.QUESTIONS]
                self.assertEqual(len(prompts), len(set(prompts)))

                for question in module.QUESTIONS:
                    self.assertTrue(question.prompt.strip())
                    self.assertTrue(question.accepted_answers)
                    for answer in question.accepted_answers:
                        self.assertTrue(answer.strip())

    def test_corrected_commands_are_accepted_and_old_wrong_answers_are_rejected(self):
        recursive_delete = find_question(directories, "including its contents")
        grep_or = find_question(search, "foo or bar")
        ip_addresses = find_question(misc, "IP addresses")
        reboot = find_question(misc, "Immediately reboot")
        foreground_job = find_question(process, "job number 1")
        wireshark = find_question(process, "Wireshark")

        self.assertTrue(is_correct("rm -r foo", recursive_delete))
        self.assertFalse(is_correct("rmdir -r foo", recursive_delete))

        self.assertTrue(is_correct("grep -E 'foo|bar' bar.txt", grep_or))
        self.assertFalse(is_correct("grep 'foo|bar' bar.txt", grep_or))

        self.assertTrue(is_correct("ip addr", ip_addresses))
        self.assertFalse(is_correct("ip", ip_addresses))

        self.assertTrue(is_correct("shutdown -r now", reboot))
        self.assertFalse(is_correct("shutdown -r", reboot))

        self.assertTrue(is_correct("fg %1", foreground_job))
        self.assertFalse(is_correct("fg 1000", foreground_job))

        self.assertTrue(is_correct("wireshark &", wireshark))
        self.assertFalse(is_correct("Wireshark &", wireshark))

    def test_no_known_incorrect_answers_remain(self):
        known_bad_answers = {
            "rmdir -r foo",
            "grep 'foo|bar' bar.txt",
            "ip",
            "shutdown -r",
            "fg 1000",
            "Wireshark &",
        }

        accepted_answers = {
            answer
            for module in TOPIC_MODULES
            for question in module.QUESTIONS
            for answer in question.accepted_answers
        }

        self.assertFalse(known_bad_answers & accepted_answers)


class CliTests(unittest.TestCase):
    def test_menu_registry_matches_topic_modules(self):
        self.assertEqual(
            [entry.module_name for entry in linux_helper.MODULES],
            ["navigation", "directories", "search", "usage", "packages", "process", "misc"],
        )

    def test_module_selection_accepts_number_and_key(self):
        self.assertEqual(linux_helper.get_module("1").key, "navigation")
        self.assertEqual(linux_helper.get_module("search").module_name, "search")
        self.assertIsNone(linux_helper.get_module("not-a-module"))


if __name__ == "__main__":
    unittest.main()
