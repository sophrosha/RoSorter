import sys

from typing import Callable, Optional

class OptionsValidate:
    printf: Callable
    catalogs: dict
    names: Optional

    def validate_options(self, catalog):
        options = {'path': True, 'files': True, 'names': False, 'ignore': False}
        added_opts = []
        for option, needed in options.items():
            if option not in self.catalogs[catalog]:
                if not needed:
                    continue
                else:
                    self.printf('missing_option', option)
                    sys.exit()
            elif not needed:
                added_opts.append(option)
        path_file = self.catalogs[catalog]['path']
        files = self.catalogs[catalog]['files']
        names = self.catalogs[catalog]['names'] if 'names' in added_opts else None
        ignore = self.catalogs[catalog]['ignore'] if 'ignore' in added_opts else None

        names1 = []
        if isinstance(names, list):
            for el in names:
                for key, value in el.items():
                    names1.append([key, value])
        
        return path_file, files, ignore, names1