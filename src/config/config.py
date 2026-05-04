import sys, os

from typing import Callable
from pathlib import Path

class ValidateFileConfig:
    configuration: str
    printf: Callable
    app_path: Path

    def setup_paths(self, custom_config=None):
        try:
            if os.name == 'nt':
                appdata_env = os.environ.get('APPDATA')
                if appdata_env is None:
                    self.printf('general_not_found')
                    sys.exit()
                self.app_path = Path(appdata_env) / 'rosorter'
                if not os.path.exists(self.app_path):
                    try:
                        self.app_path.mkdir(parents=True, exist_ok=True)
                    except Exception:
                        self.printf('general_not_found')
                        sys.exit()

                if custom_config:
                    if os.path.exists(custom_config):
                        self.configuration = str(custom_config)
                    else:
                        config_path = self.app_path / "config.yaml"
                        if not os.path.exists(config_path):
                            self.printf('file_exists')
                            sys.exit()
                        else:
                            self.configuration = str(config_path)
                else:
                    config_path = self.app_path / "config.yaml"
                    if not os.path.exists(config_path):
                        self.printf('file_exists')
                        sys.exit()
                    else:
                        self.configuration = str(config_path)

            elif os.name == 'posix':
                user_env = os.environ.get('USER')
                if user_env is None:
                    self.printf('user_not_found')
                    sys.exit()
                user_name = str(user_env)
                sys_app_path = Path('/etc/rosorter')
                if not os.path.exists(sys_app_path) and not custom_config:
                    self.printf('etc_not_found')
                    sys.exit()
                home_config_dir = Path('/home') / user_name / '.config'
                if not os.path.exists(home_config_dir):
                    self.printf('user_config_not_found')
                    self.printf('using_sys_config')
                    self.app_path = sys_app_path
                else:
                    self.app_path = home_config_dir / 'rosorter'
                    if not os.path.exists(self.app_path):
                        try:
                            self.app_path.mkdir(parents=True, exist_ok=True)
                        except Exception:
                            self.printf('general_not_found')
                            sys.exit()

                if custom_config:
                    if os.path.exists(custom_config):
                        self.configuration = str(Path(custom_config))
                    else:
                        self.printf('file_exists')
                        sys.exit()
                else:
                    config_path = self.app_path / 'config.yaml'
                    if not os.path.exists(config_path):
                        self.printf('file_exists')
                        sys.exit()
                    else:
                        self.configuration = str(config_path)
            else:
                self.printf('os_unsupported')
                sys.exit()
        except FileNotFoundError:
            self.printf('file_exists')
            sys.exit()
        except NotADirectoryError:
            self.printf('not_directory')
            sys.exit()

    def validate_config(self):
        if os.path.exists(self.configuration):
            return 1
        else:
            self.printf('config_not_found')
            self.printf('config_create')
            config = self.create_config()
            if config == 1:
                self.printf('config_created', self.configuration)
                self.printf('please_set_config')
                self.printf('exit')
                sys.exit()
            else:
                return None
                    
    def create_config(self):
        try:
            Path(self.configuration).parent.mkdir(parents=True, exist_ok=True)
            with open(self.configuration, 'w', encoding='utf-8') as f:
                f.write("# RoSorter config\nsettings:\n  "
                        "logging: en-US\n  logs: true\n  "
                        "daemon: false\n  timeout: 30\n  "
                        "gui: false\n  silent: false\ndirectories:\n  "
                        "# Add your directories here\n")
            self.printf('created_config', self.configuration)
            sys.exit()
        except Exception as error:
            self.printf('fail', error)
            sys.exit()

    def contains_values(self, config):
        count = 0
        for key, _ in config.items():
            if key in {'settings', 'directories'}:
                count += 1
            else:
                self.printf('found_error_option', key)
                sys.exit()
        if count != 2:
            self.printf('missing_settings_directories')
            sys.exit()
        return None