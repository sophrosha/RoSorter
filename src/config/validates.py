import sys, os
from typing import Callable

class ConfigOptionValidate:
    printf: Callable
    inputf: Callable

    def validate_settings(self, config, settings):
        language = None

        for key, value in config['settings'].items():
            if key in {'logs', 'daemon', 'timeout', 'gui', 'silent'}: 
                settings[key] = value
            elif key in 'language':
                language = value
            else:
                self.printf('found_error_option', key)
                sys.exit()
        return language, settings

    def validate_directories(self, config, catalogs):
        for directory in config['directories']:
            catalogs[directory] = {}
            for key, value in config['directories'][directory].items():
                if key in {'path', 'files', 'names', 'ignore'}: 
                    catalogs[directory][key] = value
                else:
                    self.printf('found_error_option_dir', key, directory)
                    sys.exit()
        return catalogs

    def validate_catalogs(self, catalogs):
        for catalog in catalogs:
            if not os.path.isdir(catalogs[catalog]['path']):
                answer = self.inputf('create_catalog')
                if answer.lower() in 'y':
                    self.printf('creating_catalog')
                    os.mkdir(catalogs[catalog]['path'])
                else:
                    self.printf('exit')
                    sys.exit()