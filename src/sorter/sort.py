from pathlib import Path
import os

from typing import Callable

class Sort:
    printf: Callable[[str], None]
    copy: Callable[[str, str, str], None]

    def sort(self, content_folder, path_file, files, names):
        for filename, fil in content_folder:
            if '*' in files:
                if len(files) > 1:
                    self.printf('some_extensions_files')
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
                continue