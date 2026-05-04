from src.logging.logger import Logger
from src.config.config import ValidateFileConfig
from src.config.validates import ConfigOptionValidate
from src.config.main import Config
from src.sorter.main import Sorter

import yaml
import time

class Daemon(ValidateFileConfig, ConfigOptionValidate):
    def __init__(self, custom_config=None):
        self.custom_config = custom_config
        self.lang = Logger('en-US', file_path=None)
        self.printf = self.lang.printf
        self.inputf = self.lang.inputf
        
        self.setup_paths(custom_config)
        self.validate_config()
        
    def get_timeout(self):
        try:
            with open(self.configuration, 'r', encoding='utf-8') as f:
                config = yaml.safe_load(f)
                if 'settings' in config and 'timeout' in config['settings']:
                    timeout_str = str(config['settings']['timeout'])
                    if timeout_str.endswith('m'):
                        return int(timeout_str.replace('m', '')) * 60
                    elif timeout_str.endswith('h'):
                        return int(timeout_str.replace('h', '')) * 3600
                    else:
                        try:
                            return int(timeout_str)
                        except:
                            return 3600
                else:
                    return 3600
        except Exception:
            return 3600

    def is_daemon_enabled(self):
        try:
            with open(self.configuration, 'r', encoding='utf-8') as f:
                config = yaml.safe_load(f)
                if 'settings' in config and 'daemon' in config['settings']:
                    return config['settings']['daemon']
                return False
        except Exception:
            return False

    def run(self):
        if not self.is_daemon_enabled():
            self.printf('fail', 'Daemon is disabled in config')
            return
        
        timeout = self.get_timeout()
        
        while True:
            try:
                conf = Config('en-US', custom_config=self.custom_config)
                catalogs, settings, language = conf.run()
                
                sorter = Sorter(catalogs, settings, language)
                sorter.main()
                
                self.printf('exit')
                time.sleep(timeout)
            except KeyboardInterrupt:
                self.printf('exit')
                break
            except Exception as e:
                self.printf('fail', str(e))
                time.sleep(timeout)


