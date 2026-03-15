# Sorter.py

## Класс
- Sorter(catalogs, settings, language='ru-RU')

## Функции
- __init__(catalogs, settings, language='ru-RU')
    - Инициализирует объект Sorter с каталогами, настройками и языком.

- validate_options(catalog)
    - Проверяет опции для заданного каталога.
    - Возвращает path_file, files, ignore, names.

- apply_ignore(ignore, content_folder, catalog)
    - Применяет список игнорируемых файлов к содержимому папки.

- apply_names(names, content_folder)
    - Применяет правила именования к содержимому папки.

- copy(file_name, path, name_folder)
    - Копирует файл в указанную папку.

- sort(content_folder, path_file, files, names)
    - Сортирует файлы в соответствии с правилами.

- main(system)
    - Основная функция сортировки для заданной системы (nt для Windows).