from src.sorter.main import Sorter
from src.config.main import Config
from src.daemon import Daemon

import multiprocessing

class CliHandlers:
    def sort(self, args):
        conf = Config(self.lang.locale, custom_config=args.config) if args.config else Config(self.lang.locale)
        catalogs, settings, language = conf.run()

        if settings.get('daemon', False):
            daemon_process = multiprocessing.Process(
                target=self._run_daemon, 
                args=(args.config,)
            )
            daemon_process.daemon = True
            daemon_process.start()
            self.lang.printf('exit')
        else:
            sort = Sorter(catalogs, settings, language)
            sort.main()

    def _run_daemon(self, custom_config):
        daemon = Daemon(custom_config=custom_config)
        daemon.run()

    def gui(self, args):
        self.lang.printf('fail', 'GUI is not implemented yet')

    def create(self, args):
        self.lang.printf('fail', 'Config creation is not implemented yet')
