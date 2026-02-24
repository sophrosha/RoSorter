import sys
import os
import time
#import daemon
import pystray
import yaml
import tkinter

'''
Главный сортировщик

Должен принимать параметры из config
Имеет функции sort_windows, sort_unix, validate_os,

sort_windows/sort_linux - Создает каталоги и перекидывает файлы от нужного каталога в другие каталоги которые были указаны. Возвращает истину если все прошло хорошо, либо ложь.
validate_os - Проверяет какая стоит система и возвращает вид системы. Если система не определенна то пишет ошибку и заканчивает работу

Сортировка начинается исключительно после класса конфига
'''
class sorter:
    def __init__(self): pass # принятие всех опции из конфига
    def sort_windows(self): pass # сортировка в windows
    def sort_unix(self): pass # сортировка в unix-like
    def validate_os(self): pass # валидация системы


'''
Обработчик конфигурации

Достает конфиг судя по директории(либо если нету то создает example конфигурацию)
Функции: validate_config, parser

validate_config/parser
validate_config - проверяет наличие конфига в определенном каталоге и возвращает True если он был, если он был создан автоматом то возвращает False
parser - Возвращает значения которые были указаны в словаре(для удобства обращения)
'''
class config:
    def __init__(self): pass # инициализация
    def validate_config(self): pass # валидация конфига
    def parser(self): pass # хранение конфигурации внутри()

'''
Демон

Работает в фоне(при откл времени автосортировки имеется возможность нажать кнопку сортировки в трее)
'''
class daemon:
    def __init__(self): pass

class tray:
    def __init__(): pass

from pprint import pprint
def main(): pass
if __name__ == "__main__": 
    with open('example.yaml', encoding='utf-8') as confe:
        f = yaml.safe_load(confe)
        print(f.settings.timeout)
        pprint(f)