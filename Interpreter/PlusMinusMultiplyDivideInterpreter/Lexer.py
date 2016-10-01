
from Token import Token
from TokenType import *

class Lexer(object):
    def __init__(self, text):
        self.text = text
        self.pos = 0

    def advance(self):
        if self.pos < len(self.text):
            self.pos += 1

    def eatInteger(self):
        start = self.pos
        while self.pos < len(self.text) and self.text[self.pos].isdigit():
            self.advance()
        return Token(TokenType.INTEGER, self.text[start:self.pos])

    def eatWhitespace(self):
        while self.pos < len(self.text) and self.text[self.pos].isspace():
            self.advance()
    
    def eatOperator(self):
        if self.pos < len(self.text) and self.isAddition():
            token = Token(TokenType.ADD, self.text[self.pos])
            self.advance()
            return token
        elif self.pos < len(self.text) and self.isSubtraction():
            token = Token(TokenType.SUBTRACT, self.text[self.pos])
            self.advance()
            return token
        elif self.pos < len(self.text) and self.isMultiplication():
            token = Token(TokenType.MULTIPLY, self.text[self.pos])
            self.advance()
            return token
        elif self.pos < len(self.text) and self.isDivision():
            token = Token(TokenType.DIVIDE, self.text[self.pos])
            self.advance()
            return token
        else:
            raise ValueError('Unknown operator')

    def isAddition(self):
        if(self.pos < len(self.text) and self.text[self.pos]==TokenType.ADD):
            return True
        return False

    def isSubtraction(self):
        if(self.pos < len(self.text) and self.text[self.pos]==TokenType.SUBTRACT):
            return True
        return False

    def isMultiplication(self):
        if(self.pos < len(self.text) and self.text[self.pos]==TokenType.MULTIPLY):
            return True
        return False

    def isDivision(self):
        if(self.pos < len(self.text) and self.text[self.pos]==TokenType.DIVIDE):
            return True
        return False