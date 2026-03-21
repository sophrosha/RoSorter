import shutil
from src.languages import LANGUAGE
import sys, os
from pathlib import Path

class Sorter:
    def __init__(self, catalogs, settings, language='ru-RU'):
        self.language = language
        self.catalogs = catalogs
        self.settings = settings

    # Проверяем опции, таскаем в переменные
    def validate_options(self, catalog):
        options = {'path': True, 'files': True, 'names': False, 'ignore': False}
        added_opts = []
        for option, needed in options.items():
            if option not in self.catalogs[catalog]:
                if needed == False:
                    continue
                else:
                    print(LANGUAGE[self.language]['missing_option'].format(option))
                    sys.exit()
            elif needed == False:
                added_opts.append(option)
        path_file = self.catalogs[catalog]['path']
        files = self.catalogs[catalog]['files']
        names = self.catalogs[catalog]['names'] if 'names' in added_opts else None
        ignore = self.catalogs[catalog]['ignore'] if 'ignore' in added_opts else None

        names1 = []
        for el in names:
            for key, value in el.items():
                names1.append([key, value])
        
        return path_file, files, ignore, names1
    
    # при наличии ignore убираем файлы находящиеся в ignore с списка
    def apply_ignore(self, ignore, content_folder, catalog):
        if ignore != None:
            print(LANGUAGE[self.language]['found_ignore'].format(catalog))
            for name, file_extension in content_folder:
                if name + file_extension in ignore:
                    print(LANGUAGE[self.language]['delete_ignore'].format(name + file_extension))
                    content_folder.remove((name, file_extension))
                    print(LANGUAGE[self.language]['deleted_ignore'].format(name + file_extension))
        return content_folder

    def apply_names(self, names, content_folder):
        if names != None:
            for filename, fil in content_folder:
                if any(filename in n for n in names):
                    content_folder.remove((filename, fil))
        return content_folder

    # копируем файлы
    def copy(self, file_name, path, name_folder):
        path_dir = Path(path) / name_folder
        path_file = Path(path) / file_name

        if not os.path.isdir(path_dir):
            print(f"[RoSorter] : Отсуствует каталог для {file_name}. Создаю")
            os.mkdir(path_dir)
            
        try:
            shutil.move(path_file, path_dir)
        except PermissionError as e:
            print(f"Файл занят процессом, пропуск")
            return None
    
    def sort(self, content_folder, path_file, files, names):
        for filename, fil in content_folder:
            if '*' in files:
                if len(files) > 1:
                    print("[RoSorter] ?: Найдено несколько расширений кроме *. Пропуск.")
                elif not fil.replace('.', '') in files:
                    continue

            if any('catalog' in n for n in names):
                catalog_name = next(item for item in names if item[0] == fil.replace('.', ''))
                self.copy(filename, path_file, catalog_name[1])
            elif any(fil.replace('.', '') in n for n in names):
                catalog_name = next(item for item in names if item[0] == fil.replace('.', ''))
                self.copy(filename + fil, path_file, catalog_name[1])
            elif any('*' in n for n in names):
                if os.path.isdir(Path(path_file) / (filename + fil)): # TODO
                    self.copy(filename + fil, path_file, 'catalog')
                else:
                    self.copy(filename + fil, path_file, fil.replace('.', ''))
            else:
                print(f"[RoSorter] : {filename + fil} отсуствует в names. Добавьте * для добавления всех файлов по своим каталогам")
                continue

    # Основная функция
    def main(self, system):
        if system == "nt":
            for catalog in self.catalogs:
                path_file, files, ignore, names = self.validate_options(catalog)
                content_folder = [os.path.splitext(n) for n in os.listdir(path_file)]
                content_folder = self.apply_ignore(ignore, content_folder, catalog)
                content_folder = self.apply_names(names, content_folder)
                self.sort(content_folder, path_file, files, names)
        else:
            pass