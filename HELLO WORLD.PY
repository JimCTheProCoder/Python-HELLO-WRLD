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
	
        self.print_char("\n")
            
class HelloWorldPrinter(Printer):
    
    def __init__(self, stdout):
        super().__init__(stdout)

    
    def print_hello(self, color: str, word: str):
        COLOR = {
            "BLACK": "\033[90m",
            "YELLOW": "\033[93m",
            "MAGENTA": "\033[95m",
            "BLUE": "\033[94m",
            "GREEN": "\033[92m",
            "RED": "\033[91m",
            "CYAN": "\033[96m",
            "WHITE": "\033[97m",
            "END": "\033[0m",
        }

        if not color.upper() in COLOR.keys():
            raise ValueError("Please give a valid color")

        super().print_string(COLOR[color.upper()] + word + COLOR["END"])
        
        
        
hello_world = HelloWorldPrinter(sys.stdout)
hello_world.print_hello("red", "hello")
