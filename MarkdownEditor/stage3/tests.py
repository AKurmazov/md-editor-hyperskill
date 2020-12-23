from hstest.stage_test import StageTest
from hstest.test_case import TestCase
from hstest.check_result import CheckResult


class SumTest(StageTest):

    answers = [
        [
            '- Choose a formatter: > - Level: > - Text: > #### Hello World!',
            '',
            '- Choose a formatter: > - Text: > #### Hello World!',
            'Some plain text',
            '- Choose a formatter: > #### Hello World!',
            'Some plain text',
            '',
            '- Choose a formatter: > - Label: > - URL: > #### Hello World!',
            'Some plain text',
            '[Google](https://google.com)',
            '- Choose a formatter: >'
        ],
        [
            '- Choose a formatter: > - Text: > **Bold text**',
            '- Choose a formatter: > **Bold text**',
            '',
            '- Choose a formatter: > - Text: > **Bold text**',
            '*Italic text*',
            '- Choose a formatter: > **Bold text**',
            '*Italic text*',
            '',
            '- Choose a formatter: > - Text: > **Bold text**',
            '*Italic text*',
            '`code.work()`',
            '- Choose a formatter: >'
        ],
        [
            '- Choose a formatter: >'
        ]
    ]

    def generate(self):
        return [
            TestCase(
                stdin=['header', '4', 'Hello World!', 'plain', 'Some plain text',
                       'new-line', 'link', 'Google', 'https://google.com', '!done'],
                attach=0
            ),
            TestCase(
                stdin=['bold', 'Bold text', 'new-line', 'italic', 'Italic text',
                       'new-line', 'inline-code', 'code.work()', '!done'],
                attach=1
            ),
            TestCase(
                stdin=['!done'],
                attach=2
            ),
        ]

    def check(self, reply, attach):
        reply = reply.strip().split('\n')
        print(reply)
        if len(reply) != len(self.answers[attach]):
            CheckResult.wrong('Wrong answer. Please try again')

        for i, line in enumerate(reply):
            if line.strip() != self.answers[attach][i].strip():
                CheckResult.wrong('Wrong answer. Please try again')

        return CheckResult.correct()


if __name__ == '__main__':
    SumTest('markdown_editor.editor').run_tests()
