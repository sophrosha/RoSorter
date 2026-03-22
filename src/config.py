import sys
import yaml
import os
import shutil
from pathlib import Path

from src.languages import Language

class Config:
    def __init__(self, language, custom_config=None):
        lang = Language(language)
        self.printf = lang.printf
        self.inputf = lang.inputf

        self.custom_config = custom_config
        if os.name == 'nt':
            self.username = os.environ.get('USERNAME')
            self.home_path = Path(f"C:/Users/{self.username}")
            self.sys_path = Path("C:/Program Files")

            #self.filepath = self.home_path / "AppData/Roaming/rosorter.yaml"
            self.filepath = self.home_path / "Documents/Projects/RoSorter-1/assets/example.yaml" if self.custom_config == None else self.custom_config
            #self.example_config = self.sys_path / "RoSorter/src/example.yaml"
            self.example_config = self.home_path / "Documents/Projects/RoSorter-1/assets/example.yaml"
        else:
            pass

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
            pass
                    
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
            pass

    def contains_values(self, config):
        cout = 0
        for key, _ in config.items():
            if key in {'settings', 'directories'}:
                cout += 1
            else:
                self.printf('found_error_option', key)
                sys.exit()
        if cout != 2:
            self.printf('missing_settings_directories')
            sys.exit()
        return None

    def validate_settings(self, config, settings):
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
            # Проверка значений, если есть неопределенное значение то выход
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

    def main(self):
        catalogs = {}
        settings = {}
        with open(self.filepath, 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)

            self.contains_values(config)
            settings = self.validate_settings(config, settings)
            catalogs = self.validate_directories(config, catalogs)
            self.validate_catalogs(catalogs)
        
        if not self.language in settings:
            language = 'en-US'

        return catalogs, settings, language
                
    def run(self):
        if not self.custom_config == None:
            self.validate_config()
        catalogs, settings, language = self.main()
        return catalogs, settings, language