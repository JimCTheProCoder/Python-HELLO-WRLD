import sys

class Printer:
    def __init__(self, stdout):
        self.out = stdout
        
    def print_char(self, character):
        self.out.write(character)
        
    def print_string(self, string):
        for character in string.split():
            self.print_char(character)
            
class HelloWorldPrinter(Printer):
    def __init__(self, stdout):
        super().__init__(stdout)
    
    def print_hello(self):
        super().print_string("hello")
        
        
        
hello_world = HelloWorldPrinter(sys.stdout)
hello_world.print_hello()
