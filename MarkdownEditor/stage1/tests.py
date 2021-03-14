from hstest.stage_test import StageTest
from hstest.test_case import TestCase
from hstest.check_result import CheckResult


class SumTest(StageTest):

    answer = [
        "# John Lennon",
        "or ***John Winston Ono Lennon***, was one of *The Beatles*.",
        "Here are the songs he wrote I like the most:",
        "* Imagine",
        "* Norwegian Wood",
        "* Come Together",
        "* In My Life",
        "* ~~Hey Jude~~ (that was *McCartney*)"
    ]

    def generate(self):
        return [
            TestCase()
        ]

    def check(self, reply, attach):
        reply = reply.strip().split('\n')
        if len(reply) != len(self.answer):
            CheckResult.wrong("Wrong answer. Please try again")

        for i, line in enumerate(reply):
            if line != self.answer[i]:
                CheckResult.wrong("Wrong answer. Please try again")

        return CheckResult.correct()


if __name__ == '__main__':
    SumTest('markdown_editor.editor').run_tests()
