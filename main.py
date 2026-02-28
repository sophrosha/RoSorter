import sys
import os
import time
#import daemon
import pystray
import yaml
import tkinter
import shutil
from pathlib import Path

'''
Главный сортировщик

Должен принимать параметры из config
Имеет функции sort_windows, sort_unix, validate_os,

sort_windows/sort_linux - Создает каталоги и перекидывает файлы от нужного каталога в другие каталоги которые были указаны. Возвращает истину если все прошло хорошо, либо ложь.
validate_os - Проверяет какая стоит система и возвращает вид системы. Если система не определенна то пишет ошибку и заканчивает работу

Сортировка начинается исключительно после класса конфига
'''

class sorter:
    def __init__(self, catalogs={}, settings={}): # принятие всех опции из конфига
        self.catalogs = catalogs
        self.settings = settings

        if catalogs is None:
            pass
        elif settings is None:
            pass
        else:
            pass

    def init(self):
        self.sort(os.name)

    def sort(self, system): # Сортировка системы
        if system == "nt":
            pass
        else: # Линукс
            pass

'''
Обработчик конфигурации

Достает конфиг судя по директории(либо если нету то создает example конфигурацию)
'''
class config:
    def __init__(self): # инициализация
        if os.name == 'nt':
            self.username = os.environ.get('USERNAME')
            self.home_path = Path(f"C:/Users/{self.username}")
            self.sys_path = Path("C:\\Program Files")

            #self.filepath = self.home_path / "AppData/Roaming/rosorter.yaml"
            self.filepath = self.home_path / "Documents/Projects/RoSorter/example.yaml"
            #self.example_config = self.sys_path / "RoSorter/src/example.yaml"
            self.example_config = self.home_path / "Documents/Projects/RoSorter/example.yaml"
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
            config = yaml.safe_load(f)
            # спарсить и все перетащить в нужный список
            # так же спарсить настройки и перетащить в свой список(если что то из настроек отсуствует то добавить эти настройки в словарь но указать дефолт значение)

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
                    if key in {'path', 'files', 'names'}: 
                        catalogs[directory][key] = value
                    else:
                        print(f'[RoSorter] !: Ошибка, Найдена неверная опция: {key} в {directory}. Выход')
                        sys.exit()
        return catalogs, settings
                
    def run(self): # хранение конфигурации внутри()
        # Валидация конфигурации
        self.validate_config()
        catalogs, settings = self.parser()
        return catalogs, settings
        

'''
Демон

Работает в фоне(при откл времени автосортировки имеется возможность нажать кнопку сортировки в трее)
'''
class daemon:
    def __init__(self): pass

class tray:
    def __init__(): pass

def main():
    conf = config()
    conf.run()
    
if __name__ == "__main__": 
    main()