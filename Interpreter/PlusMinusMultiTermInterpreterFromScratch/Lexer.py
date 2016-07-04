
from Parser import PLUS, MINUS, INTEGER
from Token import Token

class Lexer(object):
    def __init__(self, input):
        self.input = input
        self.pos = 0
        self.current_text = self.input[self.pos]

    def lex(self):
        token_list = []

        #scan all the input
        while self.pos < len(self.input):
            self.current_text = self.input[self.pos]
            
            if self.current_text == ' ' or self.current_text == '\t':
                self.pos+=1
            elif self.current_text.isdigit():
                value = ''
                while True:
                    if self.pos >= len(self.input):
                        break

                    self.current_text = self.input[self.pos]
                    if not self.current_text.isdigit():
                        break                    
                    value += self.current_text
                    self.pos += 1
                token = Token(INTEGER, value)
                token_list.append(token)
            elif self.current_text == '+':
                token = Token(PLUS, '+')
                token_list.append(token)
                self.pos += 1
            elif self.current_text == '-':
                token = Token(MINUS, '-')
                token_list.append(token)
                self.pos += 1
            else:
                raise Exception()

        return token_list