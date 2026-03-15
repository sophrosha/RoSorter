# API Документация

## main.py

### Классы
- **Cli**: Заглушка для CLI интерфейса (не реализован).
- **Daemon**: Заглушка для демона (не реализован).
- **Tray**: Заглушка для трея (не реализован).

### Функции
- **main()**: Основная функция. Определяет ОС и запускает сортировку для Windows.

## src/config.py

### Класс Config
Класс для работы с конфигурационными файлами.

#### Методы
- `__init__(language='en_US')`: Инициализация с языком.
- `validate_config()`: Проверка наличия конфиг-файла.
- `create_config(system)`: Создание конфиг-файла из примера.
- `contains_values(config)`: Проверка обязательных ключей.
- `validate_settings(config, settings)`: Валидация настроек.
- `validate_directories(config, catalogs)`: Валидация директорий.
- `validate_catalogs(catalogs)`: Проверка существования путей.
- `main()`: Парсинг конфигурации.
- `run()`: Запуск валидации и парсинга.

## src/sorter.py

### Класс Sorter
Класс для сортировки файлов.

#### Методы
- `__init__(catalogs, settings, language='ru-RU')`: Инициализация.
- `validate_options(catalog)`: Проверка опций каталога.
- `apply_ignore(ignore, content_folder, catalog)`: Применение игнора.
- `apply_names(names, content_folder)`: Применение правил имен.
- `copy(file_name, path, name_folder)`: Копирование файла.
- `sort(content_folder, path_file, files, names)`: Сортировка файлов.
- `main(system)`: Основная функция сортировки.

## src/languages.py

### LANGUAGE
Словарь с локализованными сообщениями.

#### Ключи
- `'ru-RU'`: Русские сообщения.
- `'en-US'`: Английские сообщения.

Список всех ключей см. в [languages.md](languages.md).