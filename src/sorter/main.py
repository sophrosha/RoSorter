from src.sorter.applyes import Applies
from src.sorter.copy import Copy
from src.sorter.options_validate import OptionsValidate
from src.sorter.sort import Sort

from src.logging.logger import Logger
import os
from tqdm import tqdm

class Sorter(Applies, Copy, OptionsValidate, Sort):
    def __init__(self, catalogs, settings, language):
        lang = Logger(language)
        self.printf = lang.printf
        self.code_return = lang.code_return
        
        self.catalogs = catalogs
        self.settings = settings

    # Основная функция
    def main(self):
        catalog_bar = tqdm(self.catalogs, position=1)
        for catalog in catalog_bar:
            catalog_bar.set_description(self.code_return('moving_catalog', catalog))
            path_file, files, ignore, names = self.validate_options(catalog)
            content_folder = [os.path.splitext(n) for n in os.listdir(path_file)]
            content_folder = self.apply_ignore(ignore, content_folder, catalog)
            content_folder = self.apply_names(names, content_folder)
            self.sort(content_folder, path_file, files, names)
        print("\n")
