import sys
import os
from typing import Literal

class Printer:
    def __init__(self, stdout):
        self.out = stdout
        
    def print_char(self, character):
        self.out.write(character)
        
    def print_string(self, string):
        for character in string.split():
            self.print_char(character)
            
BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(8)
END = "\033[0m"
COLOR_SEQ = "\033[1;%dm"

class HelloWorldPrinter(Printer):
     
    
    def __init__(self, stdout):
        super().__init__(stdout)
       
    
    def print_hello(self, color: Literal[BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE]):
        os.system("color")
        _str = "\033[9%dm" % (30 + color) + "hello" + END
        super().print_string(_str)
        
        
        
hello_world = HelloWorldPrinter(sys.stdout)
hello_world.print_hello(RED)

