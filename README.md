# RoSorter - Сортировщик файлов по каталогам

## Премущества
- Понятная настройка в конфигурационном файле
- Создание кастомных названий для файлов
- Сортировка всех файлов указанием *
- Наличие двух языков

> [!WARNING]
> Программа готова не полностью, многий функционал отсуствует.

## Сборка
```
git clone https://github.com/sophrosha/RoSorter
cd RoSorter/packaging

# Windows
.\app_build.bat

# Linux-based
chmod +x actions_build.sh
./actions_build.sh

cd ../dist/RoSorter
```

## Установка
```
# Windows
git clone https://github.com/sophrosha/RoSorter
cd RoSorter
pip install -r requirements.txt
# Или Releases -> RoSorter-Release.exe

# Linux
# Необходим pipx, установите его с помощью вашего пакетного менеджера.
git clone https://github.com/sophrosha/RoSorter
cd RoSorter
pipx ensurepath
chmod +x packaging/actions_build.sh
./packaging/actions_build.sh
```