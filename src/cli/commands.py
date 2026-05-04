from argparse import ArgumentParser
from typing import Callable

class CliCommands:
    parser: ArgumentParser
    code_return: Callable
    sort: Callable
    gui: Callable
    create: Callable

    def commands(self):
        command = self.parser
        subparser = command.add_subparsers(
            dest='command', required=True
        )

        sort_command = subparser.add_parser('sort', help=self.code_return('sort'))
        sort_command.add_argument('--config', help=self.code_return('another_config'), type=str)
        sort_command.set_defaults(func=self.sort)

        create_command = subparser.add_parser('create', help=self.code_return('create'))
        create_command.set_defaults(func=self.create)

        args = command.parse_args()
        args.func(args)