import argparse
from config import Config
from sorter import Sorter
from languages import Language

class Cli:
    def sort(self, args):
        lang = Language('commands')
        self.code_return = lang.code_return

        conf = Config('en-US', custom_config=args.config) if args.config else Config()
        catalogs, settings, language = conf.run()
        sort = Sorter(catalogs, settings, language)
        sort.main('nt')

    def gui(self, args):
        print('Under Construction')

    def create(self, args):
        print('Under Construction')

    def commands(self):
        command = self.parser
        subparser = command.add_subparsers(
            dest='command', required=True
        )

        sort_command = subparser.add_parser('sort', help=self.code_return('sort'))
        sort_command.add_argument('--config', help=self.code_return('another_config'), type=str)
        sort_command.set_defaults(func=self.sort)

        gui_command = subparser.add_parser('gui', help=self.code_return('gui'))
        gui_command.set_defaults(func=self.gui)

        create_command = subparser.add_parser('create', help=self.code_return('create'))
        create_command.add_argument('--config', help=self.code_return('another_config'))
        create_command.set_defaults(func=self.create)

        args = command.parse_args()
        args.func(args)

    def main(self):
        self.parser = argparse.ArgumentParser(
            description=self.code_return('help')
        )
        self.commands()