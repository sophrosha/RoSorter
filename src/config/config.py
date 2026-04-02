import sys, os
import shutil

from typing import Callable
from pathlib import Path

class ValidateFileConfig:
    filepath: str
    printf: Callable
    example_config: Path

    def validate_config(self):
        if os.name == 'nt':
            system = os.name
            if os.path.exists(self.filepath):
                return 1
            else:
                self.printf('config_not_found')
                self.printf('config_create')
                config = self.create_config(system)
                if config == 1:
                    self.printf('config_created', self.filepath)
                    self.printf('please_set_config')
                    self.printf('exit')
                    sys.exit()
                else:
                    return None
        else:
            return None
                    
    def create_config(self, system):
        if system == 'nt':
            try:
                self.example_config.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(self.example_config, self.filepath)
                return 1
            except Exception as error:
                self.printf('fail', error)
                sys.exit()
        else:
            return None

    def contains_values(self, config):
        count = 0
        for key, _ in config.items():
            if key in {'settings', 'directories'}:
                count += 1
            else:
                self.printf('found_error_option', key)
                sys.exit()
        if count != 2:
            self.printf('missing_settings_directories')
            sys.exit()
        return None