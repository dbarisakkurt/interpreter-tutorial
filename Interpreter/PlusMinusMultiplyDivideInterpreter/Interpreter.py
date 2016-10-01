
from Lexer import Lexer
from TokenType import *

# grammar
# expr      :   term((PLUS|MINUS)term)*
# term      :   factor((MUL|DIV)factor)*
# factor    :   INTEGER


class Interpreter(object):
    def __init__(self, lexer):
        self.lexer = lexer

    def interpret(self):
        return self.expr()
        
    def expr(self):
        result = 0
        token = self.term()
        result = token

        self.lexer.eatWhitespace()
    
        while(self.lexer.isAddition() or self.lexer.isSubtraction()):
            operator = self.lexer.eatOperator()
            self.lexer.eatWhitespace()
            token = self.term()
            
            if operator.value == '+':
                result = result + token
            else:
                result = result - token

        return result
            

    def term(self):
        result = 1
        token = self.factor()
        result = int(token.value)

        self.lexer.eatWhitespace()

        while(self.lexer.isMultiplication() or self.lexer.isDivision()):
            operator = self.lexer.eatOperator()
            self.lexer.eatWhitespace()
            token = self.factor()

            if operator.value == '*':
                result = result * int(token.value)
            else:
                result = result / int(token.value)

        return result

    def factor(self):
        token = self.lexer.eatInteger()
        return token





