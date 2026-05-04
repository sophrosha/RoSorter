from src.logging.locales import LOCALES

import logging
import sys

logger = logging.getLogger(__name__)
class Logger:
    def __init__(self, locale='en-US', file_path=None):
        self.locale = locale
        self._setup_logging(file_path)

    @staticmethod
    def _setup_logging(file_path):
        if not logger.handlers:
            logger.setLevel(logging.INFO)

            c_handler = logging.StreamHandler(sys.stdout)
            logger.addHandler(c_handler)

            if file_path:
                f_handler = logging.FileHandler(file_path, encoding='utf-8')
                logger.addHandler(f_handler)

    def printf(self, code, *args):
        try:
            if args:
                message = self._get_message(code).format(*args)
            else:
                message = self._get_message(code)

            logger.info(message)
        except KeyError:
            logger.error(LOCALES['other_messages']['another_language'])

    def inputf(self, code):
        try:
            message = self._get_message(code) + ' '
            inp = input(message)

            return inp
        except KeyError:
            logger.error(LOCALES['other_messages']['another_language'])

    def code_return(self, code, *args):
        try:
            if args:
                return self._get_message(code).format(*args)
            else:
                return self._get_message(code)
        except KeyError:
            logger.error(LOCALES['other_messages']['another_language'])

    def _get_message(self, code):
        if code in LOCALES.get(self.locale, {}):
            return LOCALES[self.locale][code]
        elif code in LOCALES.get('commands', {}):
            return LOCALES['commands'][code]
        else:
            raise KeyError(f"Code {code} not found for locale {self.locale}")
