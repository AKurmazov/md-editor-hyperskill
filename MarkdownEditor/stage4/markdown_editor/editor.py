FORMATTING_TYPES = ['plain', 'bold', 'italic', 'header', 'ordered-list', 'unordered-list', 'link', 'inline-code', 'new-line']
SPECIAL_COMMANDS = ['!help', '!done']
MD = ""


def help():
    print('Available formatting types: ', ' '.join(FORMATTING_TYPES))
    print('Special commands: ', ' '.join(SPECIAL_COMMANDS))


def done():
    exit()


def format_header():
    global MD

    level = int(input('- Level: '))
    if level not in list(range(1, 7)):
        print('Level should be within the range from 1 to 6')
        format_header()
    else:
        text = input('- Text: ')

        MD += '#' * level + f' {text}\n'


def format_list(is_ordered):
    global MD

    items_number = int(input('- Number of rows: '))
    if items_number <= 0:
        print('The number of rows should be greater than zero')
        format_list(is_ordered)
    else:
        items = []
        for i in range(items_number):
            items.append(input(f'- Row #{i + 1}: '))

        if is_ordered:
            formatted_items = [f'{i + 1}. {items[i]}' for i in range(items_number)]
        else:
            formatted_items = list(map(lambda x: f'* {x}', items))

        MD += '\n'.join(formatted_items) + '\n'


def format_link():
    global MD

    label = input('- Label: ')
    url = input('- URL: ')

    MD += f'[{label}]({url})'


def format_plain(extra=''):
    global MD

    text = input('- Text: ')

    MD += f'{extra}{text}{extra}'


def query_input(message):
    global MD

    ftype = input(message)
    if ftype in FORMATTING_TYPES:
        if ftype == 'plain':
            format_plain()
        elif ftype == 'italic':
            format_plain(extra='*')
        elif ftype == 'bold':
            format_plain(extra='**')
        elif ftype == 'inline-code':
            format_plain(extra='`')
        elif ftype == 'header':
            format_header()
        elif ftype == 'ordered-list':
            format_list(is_ordered=True)
        elif ftype == 'unordered-list':
            format_list(is_ordered=False)
        elif ftype == 'link':
            format_link()
        elif ftype == 'new-line':
            MD += '\n'
        print(MD)
    elif ftype in SPECIAL_COMMANDS:
        if ftype == '!help':
            help()
        elif ftype == '!done':
            done()
    else:
        print('Unknown formatting type or command. Please try again')

    query_input(message)


def main():
    query_input("- Choose a formatter: ")


main()
