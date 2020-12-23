from hstest.stage_test import StageTest
from hstest.test_case import TestCase
from hstest.check_result import CheckResult


class SumTest(StageTest):

    answer = [

    ]

    def generate(self):
        return [
            TestCase(
                stdin=[],
                attach=0
            ),
            TestCase(
                stdin=[],
                attach=1
            ),
            TestCase(
                stdin=[],
                attach=2
            ),
        ]

    def check(self, reply, attach):
        reply = reply.strip().split('\n')
        if len(reply) != len(self.answer[attach]):
            CheckResult.wrong("Wrong answer. Please try again")

        for i, line in enumerate(reply):
            if line != self.answer[attach][i]:
                CheckResult.wrong("Wrong answer. Please try again")

        return CheckResult.correct()


if __name__ == '__main__':
    SumTest('markdown_editor.editor').run_tests()
