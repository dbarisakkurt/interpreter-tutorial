
from Lexer import Lexer
from Parser import Parser

class Interpreter(object):
    def __init__(self, input):
        self.input = input

    def evaluate(self):
        #lexer
        lexer = Lexer(self.input)
        token_list = lexer.lex()
    
        #parser
        parser = Parser(token_list)
        value = parser.parse()
        return value

    