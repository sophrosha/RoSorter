from src.sorter.main import Sorter
from src.config.main import Config

class CliHandlers:
    @staticmethod
    def sort(args):
        conf = Config('en-US', custom_config=args.config) if args.config else Config('en-US')
        catalogs, settings, language = conf.run()

        if settings[1]['daemon']:
            pass

        sort = Sorter(catalogs, settings, language)
        sort.main('nt')

    @staticmethod
    def gui():
        print('Under Construction')

    @staticmethod
    def create():
        print('Under Construction')