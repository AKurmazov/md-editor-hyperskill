from hstest.stage_test import StageTest
from hstest.test_case import TestCase
from hstest.check_result import CheckResult


class SumTest(StageTest):

    def generate(self):
        return [
            TestCase(
                stdin=[
                    'random',
                    lambda output:
                        '!done'
                        if 'unknown formatting type or command' in output.strip().lower()
                        else CheckResult.wrong('In case of an unknown formatter the program should\
                                                return the corresponding message: "Unknown formatting type or command')
                ]
            ),
            TestCase(
                stdin=[
                    '!help',
                    self.check_help_command,
                ]
            ),
            TestCase(
                stdin=[
                    'header',
                    lambda output:
                        'ordered-list'
                        if len(output.split('\n')) == 1 and 'formatter' in output.strip().lower()
                        else CheckResult.wrong('A user should be prompted for input again,\
                                                i.e  "- Choose a formatter: > "'),
                    lambda output:
                        'unordered-list'
                        if len(output.split('\n')) == 1 and 'formatter' in output.strip().lower()
                        else CheckResult.wrong('A user should be prompted for input again,\
                                                i.e  "- Choose a formatter: > "'),
                    lambda output:
                        'link'
                        if len(output.split('\n')) == 1 and 'formatter' in output.strip().lower()
                        else CheckResult.wrong('A user should be prompted for input again,\
                                                i.e  "- Choose a formatter: > "'),
                    lambda output:
                        'inline-code'
                        if len(output.split('\n')) == 1 and 'formatter' in output.strip().lower()
                        else CheckResult.wrong('A user should be prompted for input again,\
                                                i.e  "- Choose a formatter: > "'),
                    lambda output:
                        'new-line'
                        if len(output.split('\n')) == 1 and 'formatter' in output.strip().lower()
                        else CheckResult.wrong('A user should be prompted for input again,\
                                                i.e  "- Choose a formatter: > "'),
                    lambda output:
                        '!done'
                        if len(output.split('\n')) == 1 and 'formatter' in output.strip().lower()
                        else CheckResult.wrong('A user should be prompted for input again,\
                                                i.e  "- Choose a formatter: > "')
                ]
            ),
            TestCase(
                stdin=[
                    'plain',
                    lambda output:
                        'bold'
                        if len(output.split('\n')) == 1 and 'formatter' in output.strip().lower()
                        else CheckResult.wrong('A user should be prompted for input again,\
                                                i.e  "- Choose a formatter: > "'),
                    lambda output:
                        'italic'
                        if len(output.split('\n')) == 1 and 'formatter' in output.strip().lower()
                        else CheckResult.wrong('A user should be prompted for input again,\
                                                i.e  "- Choose a formatter: > "'),
                    lambda output:
                        '!done'
                        if len(output.split('\n')) == 1 and 'formatter' in output.strip().lower()
                        else CheckResult.wrong('A user should be prompted for input again,\
                                                i.e  "- Choose a formatter: > "')
                ]
            )
        ]

    def check_help_command(self, output):
        formatters = ['plain', 'bold', 'italic', 'header', 'ordered-list', 'unordered-list',
                      'link', 'inline-code', 'new-line']
        commands = ['!help', '!done']

        output = list(map(lambda item: item.lower(), output.split('\n')))

        if len(output) != 3:
            return CheckResult.wrong('!help command should return the list of available formatting types, and \
                                    the list of special commands, on separate rows, and the prompt a user for an input')

        for formatter in formatters:
            if formatter not in output[0].split():
                return CheckResult.wrong('One or more formatting types are not present in the output of !help command')

        for command in commands:
            if command not in output[1].split():
                return CheckResult.wrong('One or more special commands are not present in the output of !help command')

        if 'formatter' not in output[2].strip():
            return CheckResult.wrong('A user should be prompted for input again, i.e  "- Choose a formatter: > "')

        return '!done'

    def check(self, reply, attach):
        return CheckResult.correct()


if __name__ == '__main__':
    SumTest('markdown_editor.editor').run_tests()
