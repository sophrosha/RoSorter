from src.language.translates import LANGUAGE

from pathlib import Path
from datetime import datetime

class TextLoader:
    def __init__(self, language='en-US', logging=False):
        self.language = language
        self.logging = logging
        self.log_messages = []

    def printf(self, code_name, *args):
        try:
            if args:
                message = LANGUAGE[self.language][code_name].format(*args)
            else:
                message = LANGUAGE[self.language][code_name]

            print(message)

            if self.logging:
                self.log_messages.append(message)
        except KeyError:
            print(LANGUAGE['other_messages']['another_language'])
    
    def inputf(self, code_name):
        try:
            message = LANGUAGE[self.language][code_name] + ' '
            inp = input(message)

            if self.logging:
                self.log_messages.append(inp)
            return inp
        except KeyError:
            print(LANGUAGE['other_messages']['another_language'])

    def code_return(self, code_name):
        try:
            return LANGUAGE[self.language][code_name]
        except KeyError:
            print(LANGUAGE['other_messages']['another_language'])

    def save_log(self, sys_path=(Path('C:\\Program Files') / 'RoSorter')):
        date = datetime.now()
        log = date.strftime("%d-%m-%Y_%H-%M-log.txt")
        with open(sys_path / log, 'w', encoding='utf-8') as f:
            for message in self.log_messages:
                print(f'writing {message}')
                f.write(f"{message}\n")