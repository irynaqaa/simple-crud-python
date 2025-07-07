import os
import sys
from PyInstaller import __main__

if __name__ == "__main__":
    sys._MEIPASS = os.path.abspath(os.path.dirname(__file__))
    __main__.run()
