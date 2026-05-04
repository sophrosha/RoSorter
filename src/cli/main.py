from src.logging.logger import Logger

from src.cli.commands import CliCommands
from src.cli.handlers import CliHandlers

import argparse
import yaml
import os
from pathlib import Path

class Cli(CliCommands, CliHandlers):
    def __init__(self):
        self.lang = self._init_logger()
        self.code_return = self.lang.code_return

    def _init_logger(self):
        lang = 'en-US'
        log_file = None
        
        config_path = self._get_config_path()
        
        if config_path and os.path.exists(config_path):
            try:
                with open(config_path, 'r', encoding='utf-8') as f:
                    config = yaml.safe_load(f)
                    if config and 'settings' in config:
                        if 'logging' in config['settings']:
                            lang = config['settings']['logging']
                        if config['settings'].get('logs', False):
                            log_dir = Path(self._get_app_path())
                            log_file = str(log_dir / 'logs.txt')
            except Exception:
                pass
        
        return Logger(lang, file_path=log_file)

    def _get_config_path(self):
        try:
            if os.name == 'nt':
                appdata_env = os.environ.get('APPDATA')
                if appdata_env:
                    return str(Path(appdata_env) / 'rosorter' / 'config.yaml')
            elif os.name == 'posix':
                user_env = os.environ.get('USER')
                if user_env:
                    home_config_dir = Path('/home') / user_env / '.config'
                    if os.path.exists(home_config_dir):
                        return str(home_config_dir / 'rosorter' / 'config.yaml')
                    else:
                        return str(Path('/etc/rosorter/config.yaml'))
        except Exception:
            pass
        return None

    def _get_app_path(self):
        try:
            if os.name == 'nt':
                appdata_env = os.environ.get('APPDATA')
                if appdata_env:
                    return Path(appdata_env) / 'rosorter'
            elif os.name == 'posix':
                user_env = os.environ.get('USER')
                if user_env:
                    home_config_dir = Path('/home') / user_env / '.config'
                    if os.path.exists(home_config_dir):
                        return home_config_dir / 'rosorter'
                    else:
                        return Path('/etc/rosorter')
        except Exception:
            pass
        return Path.home() / '.rosorter'

    def main(self):
        self.parser = argparse.ArgumentParser(
            description=self.code_return('help')
        )
        self.commands()