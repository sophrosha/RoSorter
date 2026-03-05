import os
#import daemon
import pystray
import tkinter
from pathlib import Path
import sys

from src.config import config

import shutil

class sorter:
    def __init__(self, catalogs, settings): # принятие всех опции из конфига
        self.catalogs = catalogs
        self.settings = settings

    def run(self):
        self.sort(os.name)

    # Проверяем все ли на месте в конфиге и возвращаем все в переменных готовых
    def validate_options(self, catalog):
        options = {'path': True, 'files': True, 'names': False, 'ignore': False}
        added_opts = []
        for option, needed in options.items():
            if option not in self.catalogs[catalog]:
                if needed == False:
                    added_opts.append(option)
                else:
                    print(f"[RoSorter] !: Ошибка, отсуствует значение {option}. Выход")
                    sys.exit()
            elif needed == False:
                added_opts.append(option)
        path_file = self.catalogs[catalog]['path']
        files = self.catalogs[catalog]['files']
        ignore = self.catalogs[catalog]['ignore'] if 'ignore' in added_opts else None
        names = self.catalogs[catalog]['names'] if 'names' in added_opts else None
        
        return added_opts, path_file, files, ignore, names
        
    def sort(self, system): # Сортировка системы
        if system == "nt":
            # Достаем с словаря опции директории
            for catalog in self.catalogs:
                # Проверяем наличие значений и возвращаем пе
                enabled_options, path_file, files, ignore, names = self.validate_options(catalog)

                # Достаем все файлы из каталога
                files_catalogs = [os.path.splitext(n) for n in os.listdir(path_file)]
                  
                # Удаляем не валидатиевшиеся каталоги/файлы(проверяем изначально есть ли это опция)
                if ignore != None:
                    ignore_list = []
                    for name, file_extension in files_catalogs:
                        if name + file_extension in ignore:
                            files_catalogs.remove((name, file_extension))
                    
                # Проверка наличия names
                if names != None:
                    # ext, dir
                    # names: - "*": "*" # все по своим каталогам с своими названиями
                    # names: - "pdf": "*" # как второе, но оно не копирует все(а именно то что надо)
                    # names: - "*": "pdf" # копирует все в каталог
                    # names: - "*": "files/" # создает каталоги там
                    for name in names:
                        for f_ext, f_dir in name.items():
                            if '*' in f_ext and f_dir.endswith('/'):
                                pass
                            elif '*' in (f_ext and f_dir):
                                pass
                            elif '*' in f_dir:
                                pass
                            elif '*' in f_ext:
                                pass
                            break
                

                        
                break
                
        else: # Линукс
            pass
        

class daemon:
    def __init__(self): pass

class tray:
    def __init__(): pass

def main():
    conf = config()
    catalogs, settings = conf.run()
    sort = sorter(catalogs, settings)
    sort.run()
    
if __name__ == "__main__": 
    main()