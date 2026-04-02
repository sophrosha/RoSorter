from src.config.config import ValidateFileConfig
from src.config.validates import ConfigOptionValidate

from src.language.text_loader import TextLoader

import yaml
import os
from pathlib import Path

class Config(ValidateFileConfig, ConfigOptionValidate):
    def __init__(self, language, custom_config=None):
        self.language = language
        lang = TextLoader(language)
        self.printf = lang.printf
        self.inputf = lang.inputf

        self.custom_config = custom_config
        if os.name == 'nt':
            self.username = os.environ.get('USERNAME')
            self.home_path = Path(f"C:/Users/{self.username}")
            self.sys_path = Path("C:/Program Files")

            #self.filepath = self.home_path / "AppData/Roaming/rosorter.yaml"
            self.filepath = self.home_path / "Documents/Projects/RoSorter-1/assets/test_config.yaml" if self.custom_config is None else self.custom_config
            #self.example_config = self.sys_path / "RoSorter/src/example.yaml"
            self.example_config = self.home_path / "Documents/Projects/RoSorter-1/assets/test_config.yaml"
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