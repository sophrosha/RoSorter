from typing import Callable

class Applies:
    printf: Callable

    def apply_ignore(self, ignore, content_folder, catalog):
        if ignore is not None:
            self.printf('found_ignore', catalog)
            filtered_content = []
            for name, file_extension in content_folder:
                if name + file_extension in ignore:
                    self.printf('delete_ignore', name + file_extension)
                    self.printf('deleted_ignore', name + file_extension)
                else:
                    filtered_content.append((name, file_extension))
            content_folder = filtered_content
        return content_folder

    @staticmethod
    def apply_names(names, content_folder):
        if names is not None:
            content_folder = [
                (filename, fil)
                for filename, fil in content_folder
                if not any(filename in n for n in names)
            ]
        return content_folder
