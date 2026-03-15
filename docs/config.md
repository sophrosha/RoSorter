# Config.py

## Класс
- Config(language='en_US')

## Функции
- __init__(language='en_US')
    - Инициализирует объект Config с указанным языком.
    - Определяет пути для Windows (home_path, sys_path, filepath, example_config).

- validate_config()
    - Проверяет наличие конфигурационного файла.
    - Если файл не найден, предлагает создать его на основе примера.

- create_config(system)
    - Копирует пример конфигурации в пользовательский каталог.

- contains_values(config)
    - Проверяет, содержит ли конфиг обязательные ключи 'settings' и 'directories'.

- validate_settings(config, settings)
    - Валидирует настройки из конфига.
    - Поддерживаемые ключи: logs, daemon, timeout, gui, silent, language.

- validate_directories(config, catalogs)
    - Валидирует директории из конфига.
    - Поддерживаемые ключи для каждой директории: path, files, names, ignore.

- validate_catalogs(catalogs)
    - Проверяет существование путей директорий.
    - Предлагает создать отсутствующие каталоги.

- main()
    - Основная функция парсинга конфигурации.
    - Загружает YAML, валидирует и возвращает catalogs, settings, language.

- run()
    - Запускает валидацию конфига и парсинг.
    - Возвращает catalogs, settings, language.

## Формат конфигурационного файла
Конфигурационный файл должен быть в формате YAML. Пример см. в `src/example.yaml`.

### Settings
- `logs`: Включить логи (true/false).
- `daemon`: Включить демон (true/false).
- `timeout`: Время сортировки (например, "60m").
- `gui`: Использовать GUI (true/false).
- `silent`: Тихий режим (true/false).
- `language`: Язык ("ru-RU" или "en-US").

### Directories
Словарь директорий для сортировки.
- `path`: Путь к директории.
- `files`: Список расширений файлов для обработки (или "*" для всех).
- `names`: Правила именования каталогов (список словарей, например, "- 'pdf': 'Docs'").
- `ignore`: Список игнорируемых файлов (опционально).