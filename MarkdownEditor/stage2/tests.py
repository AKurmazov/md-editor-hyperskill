from hstest.stage_test import StageTest
from hstest.test_case import TestCase
from hstest.check_result import CheckResult


class SumTest(StageTest):

    answers = [
        [
            '- Choose a formatter: > Unknown formatting type or command. Please try again',
            '- Choose a formatter: > Available formatting types:  plain bold italic header ordered-list unordered-list link inline-code new-line',
            'Special commands:  !help !done',
            '- Choose a formatter: > ' * 3
        ],
        [
            '- Choose a formatter: > ' * 9
        ],
        [
            '- Choose a formatter: > '
        ]
    ]

    def generate(self):
        return [
            TestCase(
                stdin=['nan', '!help', 'header', 'ordered-list', '!done'],
                attach=0
            ),
            TestCase(
                stdin=['plain', 'bold', 'italic', 'inline-code', 'link',
                       'header', 'unordered-list', 'ordered-list', 'new-line', '!done'],
                attach=1
            ),
            TestCase(
                stdin=['!done'],
                attach=2
            ),
        ]

    def check(self, reply, attach):
        print(reply)

        reply = reply.strip().split('\n')
        if len(reply) != len(self.answers[attach]):
            CheckResult.wrong('Wrong answer. Please try again')

        for i, line in enumerate(reply):
            if line != self.answers[attach][i]:
                CheckResult.wrong('Wrong answer. Please try again')

        return CheckResult.correct()


if __name__ == '__main__':
    SumTest('markdown_editor.editor').run_tests()
