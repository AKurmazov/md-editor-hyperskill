from hstest.stage_test import StageTest
from hstest.test_case import TestCase
from hstest.check_result import CheckResult


class SumTest(StageTest):

    def generate(self):
        return [
            TestCase(
                stdin=[
                    'header',
                    lambda output:
                        '4'
                        if 'level' in output.strip().lower()
                        else CheckResult.wrong('Header formatter should prompt a user for both level and text, i.e "- Level: > "'),
                    lambda output:
                        'Hello World!'
                        if 'text' in output.strip().lower()
                        else CheckResult.wrong('Header formatter should prompt a user for both level and text, i.e "- Text: > "'),
                    self.check_header_test1
                ]
            ),
            TestCase(
                stdin=[
                    'plain',
                    lambda output:
                        'plain text'
                        if 'text' in output.strip().lower()
                        else CheckResult.wrong('Plain formatter should prompt a user for text, i.e "- Text: > "'),
                    self.check_plain_test2,
                    lambda output:
                        'bold text'
                        if 'text' in output.strip().lower()
                        else CheckResult.wrong('Bold formatter should prompt a user for text, i.e "- Text: > "'),
                    self.check_bold_test2
                ]
            ),
            TestCase(
                stdin=[
                    'italic',
                    lambda output:
                        'italic text'
                        if 'text' in output.strip().lower()
                        else CheckResult.wrong('Italic formatter should prompt a user for text, i.e "- Text: > "'),
                    self.check_italic_test3,
                    lambda output:
                        'code.work()'
                        if 'text' in output.strip().lower()
                        else CheckResult.wrong('Inline code formatter should prompt a user for text, i.e "- Text: > "'),
                    self.check_inline_code_test3
                ]
            ),
            TestCase(
                stdin=[
                    'link',
                    lambda output:
                        'google'
                        if 'label' in output.strip().lower()
                        else CheckResult.wrong('Link formatter should prompt a user for both label and URL, i.e "- Label: > "'),
                    lambda output:
                        'https://www.google.com'
                        if 'url' in output.strip().lower()
                        else CheckResult.wrong('Link formatter should prompt a user for both label and URL, i.e "- URL: > "'),
                    self.check_link_test4,
                    self.check_new_line_test4
                ]
            )
        ]

    def check_header_test1(self, output):
        output = list(map(lambda item: item.lower(), output.split('\n')))

        if len(output) != 3:
            return CheckResult.wrong('Please remember that header formatter switches to a new line automatically')

        if output[0].strip().split() != ['####', 'hello', 'world!']:
            return CheckResult.wrong('Level 4 for header denotes as #### in markdown')

        if output[1]:
            return CheckResult.wrong('Please check whether some redundant data is printed after a header')

        if 'formatter' not in output[2].strip():
            return CheckResult.wrong('A user should be prompted for input again, i.e  "- Choose a formatter: > "')

        return '!done'

    def check_plain_test2(self, output):
        output = list(map(lambda item: item.lower(), output.split('\n')))

        if len(output) != 2:
            return CheckResult.wrong("Plain formatter should only return the given text as is, and prompt a user for a new formatter")

        if output[0] != 'plain text':
            return CheckResult.wrong('Plain formatter returns the given text as is, without any extra symbols or tags')

        if 'formatter' not in output[1].strip():
            return CheckResult.wrong('A user should be prompted for input again, i.e  "- Choose a formatter: > "')

        return 'bold'

    def check_bold_test2(self, output):
        output = list(map(lambda item: item.lower(), output.split('\n')))

        if len(output) != 2:
            return CheckResult.wrong("Bold formatter should only return the given text enclosed with '**' symbols, and prompt a user for a new formatter")

        if output[0] != 'plain text**bold text**':
            return CheckResult.wrong('Plain formatter returns the given text as is, and does not switch to a new line')

        if 'formatter' not in output[1].strip():
            return CheckResult.wrong('A user should be prompted for input again, i.e  "- Choose a formatter: > "')

        return '!done'

    def check_italic_test3(self, output):
        output = list(map(lambda item: item.lower(), output.split('\n')))

        if len(output) != 2 or output[0] != '*italic text*':
            return CheckResult.wrong("Bold formatter should only return the given text enclosed with '*' symbols, and prompt a user for a new formatter")

        if 'formatter' not in output[1].strip():
            return CheckResult.wrong('A user should be prompted for input again, i.e  "- Choose a formatter: > "')

        return 'inline-code'

    def check_inline_code_test3(self, output):
        output = list(map(lambda item: item.lower(), output.split('\n')))

        if len(output) != 2:
            return CheckResult.wrong("Inline code formatter should only return the given text enclosed with '`' (backtick) symbols, and prompt a user for a new formatter")

        if output[0] != '*italic text*`code.work()`':
            return CheckResult.wrong('Inline code formatter does not switch to a new line')

        if 'formatter' not in output[1].strip():
            return CheckResult.wrong('A user should be prompted for input again, i.e  "- Choose a formatter: > "')

        return '!done'

    def check_link_test4(self, output):
        output = list(map(lambda item: item.lower(), output.split('\n')))

        if len(output) != 2:
            return CheckResult.wrong('Link code formatter should only return the given label associated with a URL in the form [Label](URL), and prompt a user for a new formatter')

        if output[0] != '[google](https://www.google.com)':
            return CheckResult.wrong('Please recall that for the given label and URL the correct link formatter return will be [Label](URL)')

        if 'formatter' not in output[1].strip():
            return CheckResult.wrong('A user should be prompted for input again, i.e  "- Choose a formatter: > "')

        return 'new-line'

    def check_new_line_test4(self, output):
        output = list(map(lambda item: item.lower(), output.split('\n')))

        if len(output) != 3 or output[1] != '':
            return CheckResult.wrong('New-line formatter only moves the input pointer to the next line, and prompts a user for a new formatter')

        if output[0] != '[google](https://www.google.com)':
            return CheckResult.wrong('Please make sure that the markdown state is saved')

        if 'formatter' not in output[2].strip():
            return CheckResult.wrong('A user should be prompted for input again, i.e  "- Choose a formatter: > "')

        return '!done'

    def check(self, reply, attach):
        return CheckResult.correct()


if __name__ == '__main__':
    SumTest('markdown_editor.editor').run_tests()
