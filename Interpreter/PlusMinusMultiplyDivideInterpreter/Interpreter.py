
from Lexer import Lexer
from TokenType import *

# grammar
# expr      :   term((PLUS|MINUS)term)*
# term      :   factor((MUL|DIV)factor)*
# factor    :   INTEGER


class Interpreter(object):
    def __init__(self, text):
        self.lexer = Lexer(text)

    def interpret(self):
        return self.expr()
        
    def expr(self):
        result = 0
    
        self.lexer.eatWhitespace()

        token = self.term()
        result = token

        self.lexer.eatWhitespace()
    
        while(self.lexer.isAddition() or self.lexer.isSubtraction()):
            operator = self.lexer.eatOperator()
            
            self.lexer.eatWhitespace()
            
            token = self.term()

            self.lexer.eatWhitespace()
            
            if operator.value == TokenType.ADD:
                result = result + token
            elif operator.value == TokenType.SUBTRACT:
                result = result - token
            else:
                raise ValueError("Parse error")

        return result
            

    def term(self):
        result = 1
    
        self.lexer.eatWhitespace()

        token = self.factor()
        result = int(token.value)

        self.lexer.eatWhitespace()

        while(self.lexer.isMultiplication() or self.lexer.isDivision()):
            operator = self.lexer.eatOperator()

            self.lexer.eatWhitespace()

            token = self.factor()

            self.lexer.eatWhitespace()

            if operator.value == TokenType.MULTIPLY:
                result = result * int(token.value)
            elif operator.value == TokenType.DIVIDE:
                result = result // int(token.value)
            else:
                raise ValueError("Parse error")

        return result

    def factor(self):
        token = self.lexer.eatInteger()
        return token





