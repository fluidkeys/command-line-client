import textwrap
from termcolor import colored, cprint


class Print():
    TICK = colored('✓', 'green', attrs=['bold'])
    CROSS = colored('x', 'red', attrs=['bold'])
    BULLET = colored('*', 'yellow', attrs=[])

    @staticmethod
    def status(text):
        cprint('\n{}\n'.format(text), 'yellow', attrs=['bold'])

    @staticmethod
    def tick(text, indent=2):
        indented = Print.indent(
            '{} {}'.format(Print.TICK, text),
            indent
        )

        cprint(indented)

    @staticmethod
    def bullet(text, indent=2):
        indented = Print.indent(
            '{} {}'.format(Print.BULLET, text),
            indent
        )

        cprint(indented)

    @staticmethod
    def cross(text, indent=2):
        indented = Print.indent(
            '{} {}'.format(Print.CROSS, text),
            indent
        )

        cprint(indented)

    @staticmethod
    def normal(text, indent=2):
        cprint(Print.indent(text, indent))

    @staticmethod
    def indent(text, number_of_spaces):
        wrapped = '\n'.join(textwrap.wrap(text, 100))
        return textwrap.indent(wrapped, ' ' * number_of_spaces)

    @staticmethod
    def markdown(f):
        for line in f.readlines():
            line = line.strip()
            if line.startswith('# '):
                line = colored(line, 'green', attrs=['bold'])

            elif line.startswith('## '):
                line = colored(line, 'green', attrs=[])

            else:
                line = colored(line)

            Print.normal(line, indent=4)
