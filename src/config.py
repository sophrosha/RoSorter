import sys
import yaml
import os
import shutil
from pathlib import Path

from src.languages import LANGUAGE

'''
    Обработчик конфигурации

    Создает конфиг если его нету, 
    проверяет конфиг и дальше выдает спарсенные значения
'''

class config:
    def __init__(self, language='en_US'): # инициализация
        self.language = language
        if os.name == 'nt':
            self.username = os.environ.get('USERNAME')
            self.home_path = Path(f"C:/Users/{self.username}")
            self.sys_path = Path("C:\\Program Files")

            #self.filepath = self.home_path / "AppData/Roaming/rosorter.yaml"
            self.filepath = self.home_path / "Documents/Projects/RoSorter/src/example.yaml"
            #self.example_config = self.sys_path / "RoSorter/src/example.yaml"
            self.example_config = self.home_path / "Documents/Projects/RoSorter/src/example.yaml"
        else: # Линукс
            pass

    def validate_config(self): # валидация конфига
        if os.name == 'nt':
            username = os.environ.get("USERNAME")
            system = os.name
            if os.path.exists(self.filepath):
                return 1
            else:
                print(LANGUAGE[self.language]['config_not_found'])
                print(LANGUAGE[self.language]['config_create'])
                config = self.create_config(system)
                if config == 1:
                    print(LANGUAGE[self.language]['config_created'].format(self.filepath))
                    print(LANGUAGE[self.language]['config_please_set_config'])
                    print(LANGUAGE[self.language]['exit'])
                    sys.exit()
        else: # Линукс
            pass
                    
    def create_config(self, system):
        if system == 'nt':
            try:
                self.example_config.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(self.example_config, self.filepath)
                return 1
            except Exception as error:
                print(LANGUAGE[self.language]['fail'].format(error))
                sys.exit()
        else: # Линукс
            pass

    def parser(self):
        catalogs = {}
        settings = {}
        with open(self.filepath, 'r', encoding='utf-8') as f:
            # Защищенная загрузка конфигурации
            config = yaml.safe_load(f)

            # Проверка наличия масивов settings, directories.
            cout = 0
            for key, _ in config.items():
                if key in {'settings', 'directories'}:
                    cout += 1
                else:
                    print(LANGUAGE[self.language]['found_error_option'].format(key))
                    sys.exit()
            if cout != 2:
                print(LANGUAGE[self.language]['missing_settings_directories'])
                sys.exit()

            # Парсинг settings
            for key, value in config['settings'].items():
                if key in {'logs', 'daemon', 'timeout', 'gui', 'silent'}: 
                    settings[key] = value
                else:
                    print(LANGUAGE[self.language]['found_error_option'].format(key))
                    sys.exit()

            # Парсинг directories
            for directory in config['directories']:
                catalogs[directory] = {}
                # Проверка значений, если есть неопределенное значение то выход
                for key, value in config['directories'][directory].items():
                    if key in {'path', 'files', 'names', 'ignore'}: 
                        catalogs[directory][key] = value
                    else:
                        print(LANGUAGE[self.language]['found_error_option_dir'].format(key, directory))
                        sys.exit()
            
            # Валидация path
            for catalog in catalogs:
                if not os.path.isdir(catalogs[catalog]['path']):
                    print(LANGUAGE[self.language]['missing_directory'].format(catalogs[catalog]['path']))
                    answer = input(LANGUAGE[self.language]['create_catalog'] + ' ')
                    if answer.lower() in 'y':
                        print(LANGUAGE[self.language]['creating_catalog'])
                        os.mkdir(catalogs[catalog]['path'])
                    else:
                        print(LANGUAGE[self.language]['exit'])
                        sys.exit()
                    
        return catalogs, settings
                
    def run(self): # хранение конфигурации внутри()
        # Валидация конфигурации
        self.validate_config()
        catalogs, settings = self.parser()
        return catalogs, settings, 'en_US'