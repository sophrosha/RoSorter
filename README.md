# RoSorter - Сортировщик файлов по каталогам

## Премущества
- Понятная настройка в конфигурационном файле
- Создание кастомных названий для файлов
- Сортировка всех файлов указанием *
- Наличие двух языков

## TO-DO
- Создание графического интерфейса на ткинтер
- Настройка спящего режима(silent)
- Создание демона для сортировки в определенное время
- ~~Фикс ошибки копирования каталога на каталог~~ 
- cli команда -> Разрабатывается
- Поддержка Linux систем
- сборка программы -> На стадии тестирования

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
git clone https://github.com/sophrosha/RoSorter
cd RoSorter
pip install -r requirements.txt
python3 main.py
```