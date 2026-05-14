# RoSorter — Сортировщик файлов по каталогам

## Преимущества
- Понятная настройка в конфигурационном файле
- Создание кастомных названий для файлов
- Сортировка всех файлов указанием *
- Наличие двух языков
- Наличие демона, сортирующий в определенное время файлы
- Поддержка Posix систем, Windows
- Наличие установщика

## Установка

### Готовый релиз

Для Windows можно скачать готовую сборку из раздела [Releases](https://github.com/sophrosha/RoSorter/releases).

### Установка через pipx на Linux

Необходим `pipx`, установите его с помощью вашего пакетного менеджера.

```bash
git clone https://github.com/sophrosha/RoSorter
cd RoSorter

pipx ensurepath
chmod +x packaging/setup_linux.sh
./packaging/setup_linux.sh
```

### Ручная установка из исходников

Windows:

```powershell
git clone https://github.com/sophrosha/RoSorter
cd RoSorter

python -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Linux/macOS:

```bash
git clone https://github.com/sophrosha/RoSorter
cd RoSorter

python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Тестирование

Тесты запускаются через `pytest` из активированного виртуального окружения:

```bash
pytest
```

Запуск отдельного файла с тестами:

```bash
pytest tests/test_sorter_copy.py
```

## Сборка исполняемого файла
```bash
git clone https://github.com/sophrosha/RoSorter
cd RoSorter/packaging
```

Windows:

```powershell
.\app_build.bat
```

Linux-based:

```bash
chmod +x actions_build.sh
./actions_build.sh
cd ../dist/RoSorter
```
