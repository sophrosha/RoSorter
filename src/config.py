import sys
import yaml
import os
import shutil
from pathlib import Path

'''
    Обработчик конфигурации

    Создает конфиг если его нету, 
    проверяет конфиг и дальше выдает спарсенные значения
'''

class config:
    def __init__(self): # инициализация
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
                print("[RoSorter] : Не найден файл конфигурации")
                print("[RoSorter] : Создаю файл конфигурации")
                config = self.create_config(system)
                if config == 1:
                    print(f"[RoSorter] : Создана конфигурация! Расположение: {self.filepath}")
                    print("[RoSorter] : Настройте пожалуйста конфигурацию под себя!")
                    print('[RoSorter] : Выход!')
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
                print(f"[RoSorter] : Произошла ошибка! Код: {error}")
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
                    print(f'[RoSorter] !: Ошибка, Найдена неверная опция: {key}. Выход')
                    sys.exit()
            if cout != 2:
                print(f'[RoSorter] !: Ошибка, отсуствует settings или directories. Выход')
                sys.exit()

            # Парсинг settings
            for key, value in config['settings'].items():
                if key in {'logs', 'daemon', 'timeout', 'gui', 'silent'}: 
                    settings[key] = value
                else:
                    print(f'[RoSorter] !: Ошибка, Найдена неверная опция: {key}. Выход')
                    sys.exit()

            # Парсинг directories
            for directory in config['directories']:
                catalogs[directory] = {}
                # Проверка значений, если есть неопределенное значение то выход
                for key, value in config['directories'][directory].items():
                    if key in {'path', 'files', 'names', 'ignore'}: 
                        catalogs[directory][key] = value
                    else:
                        print(f'[RoSorter] !: Ошибка, Найдена неверная опция: {key} в {directory}. Выход')
                        sys.exit()
            
            # Валидация path
            for catalog in catalogs:
                if not os.path.isdir(catalogs[catalog]['path']):
                    print("[RoSorter] !: Ошибка, не существует данного каталога в {}".format(catalogs[catalog]['path']))
                    answer = input("[RoSorter] : Создать каталог? (Y/n) > ")
                    if answer.lower() in 'y':
                        print("[RoSorter] : Создаю каталог")
                        os.mkdir(catalogs[catalog]['path'])
                    else:
                        print("[RoSorter] : Выход!")
                        sys.exit()
                    
        return catalogs, settings
                
    def run(self): # хранение конфигурации внутри()
        # Валидация конфигурации
        self.validate_config()
        catalogs, settings = self.parser()
        return catalogs, settings