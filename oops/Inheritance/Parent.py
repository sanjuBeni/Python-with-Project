import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from StaticMethodClass import StaticMethodClass

class Class_Main:
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(StaticMethodClass.capitalize_text(self.name))

