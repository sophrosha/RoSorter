from src.config.config import ValidateFileConfig
from src.config.validates import ConfigOptionValidate

from src.logging.logger import Logger

import yaml

class Config(ValidateFileConfig, ConfigOptionValidate):
    def __init__(self, language, custom_config=None):
        self.language = language
        lang = Logger(language)
        self.printf = lang.printf
        self.inputf = lang.inputf

        self.custom_config = custom_config
        self.setup_paths(custom_config)

    def main(self):
        catalogs = {}
        settings = {}
        config_lang = None
        with open(self.configuration, 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)

            self.contains_values(config)
            config_lang, settings = self.validate_settings(config, settings)
            catalogs = self.validate_directories(config, catalogs)
            self.validate_catalogs(catalogs)

        if config_lang:
            language = config_lang
        else:
            language = self.language

        return catalogs, settings, language
                
    def run(self):
        if not self.custom_config is None:
            self.validate_config()
        catalogs, settings, language = self.main()
        return catalogs, settings, language