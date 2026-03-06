import os
#import daemon
import pystray
import tkinter
from pathlib import Path
import sys
import locale

from src.config import config
from src.languages import LANGUAGE

import shutil

class sorter:
    def __init__(self, catalogs, settings, language='ru_RU'): # принятие всех опции из конфига
        self.language = language
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
                    print(LANGUAGE[self.language]['missing_option'].format(option))
                    sys.exit()
            elif needed == False:
                added_opts.append(option)
        path_file = self.catalogs[catalog]['path']
        files = self.catalogs[catalog]['files']
        ignore = self.catalogs[catalog]['ignore'] if 'ignore' in added_opts else None
        names = self.catalogs[catalog]['names'] if 'names' in added_opts else None
        
        return added_opts, path_file, files, ignore, names
    
    def remove_ignore_files(self, ignore, files_catalogs, catalog):
        if ignore != None:
            print(LANGUAGE[self.language]['found_ignore'].format(catalog))
            for name, file_extension in files_catalogs:
                if name + file_extension in ignore:
                    print(LANGUAGE[self.language]['delete_ignore'].format(name + file_extension))
                    files_catalogs.remove((name, file_extension))
                    print(LANGUAGE[self.language]['deleted_ignore'].format(name + file_extension))
        return files_catalogs
        
    def sort(self, system): # Сортировка системы
        if system == "nt":
            # Достаем с словаря опции директории
            for catalog in self.catalogs:
                # Проверяем наличие значений и возвращаем их
                enabled_options, path_file, files, ignore, names = self.validate_options(catalog)

                # Достаем все файлы из каталога
                files_catalogs = [os.path.splitext(n) for n in os.listdir(path_file)]
                  
                # Удаляем не валидатиевшиеся каталоги/файлы(проверяем изначально есть ли это опция)
                files_catalogs = self.remove_ignore_files(ignore, files_catalogs, catalog)
                
                # 
                for name, ext in files_catalogs:
                    if '*' in files:
                        if len(files) >= 2:
                            print(LANGUAGE[self.language]['searched_some_extensions'])
                        pass
                    elif ext.replace('.', '') in files:
                        #print(name+ext)
                        pass
                    elif os.path.isdir(f'{path_file}/{name + ext}') and 'directory' in files:
                        #print(f"dir {name+ext}")
                        pass

                        
                break
                
        else: # Линукс
            pass
        

class daemon:
    def __init__(self): pass

class tray:
    def __init__(): pass

def main():
    if os.name == 'nt':
        default_lang = 'en-US'
        conf = config()
        catalogs, settings, language = conf.run()
        sort = sorter(catalogs, settings)
        sort.run()
    else: # Линукс
        pass
    
if __name__ == "__main__": 
    main()