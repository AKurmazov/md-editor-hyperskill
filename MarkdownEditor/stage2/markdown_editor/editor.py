FORMATTING_TYPES = ['plain', 'bold', 'italic', 'header', 'ordered-list', 'unordered-list', 'link', 'inline-code', 'new-line']
SPECIAL_COMMANDS = ['!help', '!done']
MD = ""


def help():
    print('Available formatting types: ', ' '.join(FORMATTING_TYPES))
    print('Special commands: ', ' '.join(SPECIAL_COMMANDS))


def done():
    exit()


def query_input(message):
    global MD

    ftype = input(message)
    if ftype in FORMATTING_TYPES:
        if ftype == 'plain':
            pass
        elif ftype == 'italic':
            pass
        elif ftype == 'bold':
            pass
        elif ftype == 'inline-code':
            pass
        elif ftype == 'header':
            pass
        elif ftype == 'ordered-list':
            pass
        elif ftype == 'unordered-list':
            pass
        elif ftype == 'link':
            pass
        elif ftype == 'new-line':
            pass
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
