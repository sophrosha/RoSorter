import os
#import daemon
import pystray
import tkinter
from pathlib import Path
import sys
import locale

from src.config import config
from src.sorter import sorter
from src.languages import LANGUAGE

import shutil
        

class daemon:
    def __init__(self): pass

class tray:
    def __init__(): pass

def main():
    if os.name == 'nt':
        conf = config()
        catalogs, settings, language = conf.run()
        sort = sorter(catalogs, settings, language=language)
        sort.main('nt')
    else: # Линукс
        pass
    
if __name__ == "__main__": 
    main()