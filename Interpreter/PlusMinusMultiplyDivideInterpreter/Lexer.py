
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
        if self.pos < len(self.text) and self.text[self.pos: self.pos+1]=='+':
            token = Token(TokenType.ADD, self.text[self.pos: self.pos+1])
            self.advance()
            return token
        elif self.pos < len(self.text) and self.text[self.pos: self.pos+1]=='-':
            token = Token(TokenType.SUBTRACT, self.text[self.pos: self.pos+1])
            self.advance()
            return token
        elif self.pos < len(self.text) and self.text[self.pos: self.pos+1]=='*' or self.pos < len(self.text):
            token = Token(TokenType.MULTIPLY, self.text[self.pos: self.pos+1])
            self.advance()
            return token
        elif self.pos < len(self.text) and self.text[self.pos: self.pos+1]=='/':
            token = Token(TokenType.DIVIDE, self.text[self.pos: self.pos+1])
            self.advance()
            return token
        else:
            raise ValueError('Unknown operator')

    def isAddition(self):
        if(self.text[self.pos: self.pos+1]=='+'):
            return True

    def isSubtraction(self):
        if(self.text[self.pos: self.pos+1]=='-'):
            return True

    def isMultiplication(self):
        if(self.text[self.pos: self.pos+1]=='*'):
            return True

    def isDivision(self):
        if(self.text[self.pos: self.pos+1]=='/'):
            return True