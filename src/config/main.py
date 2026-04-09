from src.config.config import ValidateFileConfig
from src.config.validates import ConfigOptionValidate

from src.language.text_loader import TextLoader

import yaml
import os
import sys
from pathlib import Path

class Config(ValidateFileConfig, ConfigOptionValidate):
    def __init__(self, language, custom_config=None):
        self.language = language
        lang = TextLoader(language)
        self.printf = lang.printf
        self.inputf = lang.inputf

        self.custom_config = custom_config
        if os.name == 'nt':
            try:
                self.app_path = Path(os.environ.get('APPDATA'))
                self.configuration = self.app_path / "RoSorter" / "config.yaml"
                if not self.custom_config:
                    self.configuration = Path(self.custom_config)
            except FileNotFoundError:
                self.printf('file_exists')
                sys.exit()
            except NotADirectoryError:
                self.printf('not_directory')
                sys.exit()
        else:
            pass

    def main(self):
        catalogs = {}
        settings = {}
        with open(self.filepath, 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)

            self.contains_values(config)
            settings = self.validate_settings(config, settings)
            catalogs = self.validate_directories(config, catalogs)
            self.validate_catalogs(catalogs)

        language = 'en-US' if not self.language in settings else self.language
        return catalogs, settings, language
                
    def run(self):
        if not self.custom_config is None:
            self.validate_config()
        catalogs, settings, language = self.main()
        return catalogs, settings, language