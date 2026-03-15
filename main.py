import os
#import daemon
import pystray
import tkinter
from pathlib import Path
import sys
import locale

from src.config import Config
from src.sorter import Sorter
from src.languages import LANGUAGE

import shutil
        
class Cli:
    def __init__(self):
        pass

class Daemon:
    def __init__(self): pass

class Tray:
    def __init__(): pass

def main():
    if os.name == 'nt':
        conf = Config()
        catalogs, settings, language = conf.run()
        sort = Sorter(catalogs, settings, language=language)
        sort.main('nt')
    else: # Линукс
        pass
    
if __name__ == "__main__": 
    main()