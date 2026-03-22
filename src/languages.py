LANGUAGE = {
    'other_messages': {
        'another_language': '[RoSorter] : Language is invalid. please set one of the languages on README.md.'
    },
    'commands' : {
        'help': 'A sorter with config created in Python',
        'sort': 'Start sorting with config',
        'gui': 'Open window program for setting config',
        'create': 'Create new config file',
        'another_config': 'Select another config'
    },
    'ru-RU': {
        'mission_option': '[RoSorter] !: Ошибка, отсуствует значение {}. Выход',
        'found_ignore': '[RoSorter] : Найден ignore в {}, убираем файлы.',
        'delete_ignore': '[RoSorter] : Убираем {}',
        'deleted_ignore': '[RoSorter] : {} Убран.',
        'searched_some_extensions': '[RoSorter] ?: Найдено несколько расширений в files при указанном *. Пропуск остальных расширений.',
        'config_not_found': '[RoSorter] : Не найден файл конфигурации',
        'config_create': '[RoSorter] : Создаю файл конфигурации',
        'config_created': '[RoSorter] : Создана конфигурация! Расположение: {}',
        'please_set_config': '[RoSorter] : Настройте пожалуйста конфигурацию под себя!',
        'exit': '[RoSorter] : Выход!',
        'fail': '[RoSorter] : Произошла ошибка! Код: {}',
        'found_error_option': '[RoSorter] !: Ошибка, Найдена неверная опция: {}. Выход!',
        'missing_settings_directories': '[RoSorter] !: Ошибка, отсуствует settings или directories. Выход!',
        'found_error_option_dir': '[RoSorter] !: Ошибка, Найдена неверная опция: {} в {}. Выход!',
        'missing_directory': '[RoSorter] !: Ошибка, не существует данного каталога в {}',
        'create_catalog': '[RoSorter] : Создать каталог? Y/n >',
        'creating_catalog': '[RoSorter] : Создаю каталог',
        'found_language': '[RoSorted] : Найден язык: {}, ставим',
        'found_error_catalog': '[RoSorter] : Отсуствует каталог для {}. Создаю',
        'file_process': '[RoSorter] : Файл занят процессом, пропуск.',
        'some_extensions_files': '[RoSorter] ?: Найдено несколько расширений кроме *. Пропуск.',
        'succes_sorting': '[RoSorter] : Успешно отсортировано {}!'
    },
    'en-US': {
        'mission_option': '[RoSorter] !: Error, missing option {}. Exit',
        'found_ignore': '[RoSorter] : found ignore in {}, deleting files.',
        'delete_ignore': '[RoSorter] : delete {}',
        'deleted_ignore': '[RoSorter] : {} deteled.',
        'searched_some_extensions': '[RoSorter] ?: Multiple extensions found in files with * specified. Skipping other extensions.',
        'config_not_found': '[RoSorter] : Not found configuration file',
        'config_create': '[RoSorter] : Creating configuration file',
        'config_created': '[RoSorter] : File configuration created! Path: {}',
        'please_set_config': '[RoSorter] : Please customize the config for yourself!',
        'exit': '[RoSorter] : Exit!',
        'fail': '[RoSorter] : Error occurepted! Code error: {}',
        'found_error_option': '[RoSorter] !: Error, found fail option: {}. Exit!',
        'missing_settings_directories': '[RoSorter] !: Error, missing settings or directories. Exit!',
        'found_error_option_dir': '[RoSorter] !: Error, found fail option: {} in {}. Exit!',
        'missing_directory': '[RoSorter] !: Error, not found catalog on {}',
        'create_catalog': '[RoSorter] : Create catalog? Y/n > ',
        'creating_catalog': '[RoSorter] : Creating catalog',
        'found_language': '[RoSorted] : Found language: {}, setting',
        'found_error_catalog': '[RoSorter] : Directory for {} is missing. Creating',
        'file_process': '[RoSorter] : File is busy with process, skip.',
        'some_extensions_files': '[RoSorter] ?: Several extensions were found except *. Skip.',
        'succes_sorting': '[RoSorter] : Successfully sorted {}!'
    }
}

class Language:
    def __init__(self, language='en-US'):
        self.language = language

    def printf(self, code_name, *args):
        try:
            if args:
                print(LANGUAGE[self.language][code_name].format(*args))
            else:
                print(LANGUAGE[self.language][code_name])
        except KeyError:
            print(LANGUAGE['other_messages']['another_language'])
    
    def inputf(self, code_name):
        try:
            input(LANGUAGE[self.language][code_name])
        except KeyError:
            print(LANGUAGE['other_messages']['another_language'])

    def code_return(self, code_name):
        return LANGUAGE[self.language][code_name]