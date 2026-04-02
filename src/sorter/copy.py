from pathlib import Path
import shutil
import os

from typing import Callable

class Copy:
    printf: Callable

    def copy(self, file_name, path, name_folder):
        path_dir = Path(path) / name_folder
        path_file = Path(path) / file_name

        if not os.path.isdir(path_dir):
            self.printf('found_error_catalog', file_name)
            os.mkdir(path_dir)
            
        try:
            shutil.move(path_file, path_dir)
        except PermissionError:
            self.printf('file_process', file_name)
            return None