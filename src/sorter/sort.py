from pathlib import Path
from tqdm import tqdm
from time import sleep
import os

from typing import Callable

class Sort:
    printf: Callable
    code_return: Callable
    copy: Callable

    def sort(self, content_folder, path_file, files, names):
        sort_bar = tqdm(content_folder, position=0)
        for filename, fil in sort_bar:
            sort_bar.set_description(self.code_return('moving_file', filename + fil))
            extension = fil.replace('.', '')
            if '*' in files and len(files) > 1:
                self.printf('some_extensions_files')
            elif '*' not in files and extension not in files:
                continue

            if any('catalog' in n for n in names):
                catalog_name = next(item for item in names if item[0] == extension)
                self.copy(filename, path_file, catalog_name[1])
            elif any(extension in n for n in names):
                catalog_name = next(item for item in names if item[0] == extension)
                self.copy(filename + fil, path_file, catalog_name[1])
            elif any('*' in n for n in names):
                if os.path.isdir(Path(path_file) / filename):
                    self.copy(filename + fil, path_file, 'catalog')
                else:
                    self.copy(filename + fil, path_file, extension)
            else:
                continue
            sleep(0.3)
