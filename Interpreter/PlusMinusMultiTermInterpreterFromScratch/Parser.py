
PLUS, MINUS, INTEGER = 'PLUS', 'MINUS', 'INTEGER'

class Parser(object):
    def __init__(self, tokens):
        self.tokens = tokens

    def parse(self):
        if len(self.tokens) == 0:
            self.error()
        elif len(self.tokens) == 1:
            if self.tokens[0].type != INTEGER:
                raise Exception()
            else:
                return int(self.tokens[0].value)
        else:
            if len(self.tokens) % 2 == 0:
                raise Exception("Always must be odd number of tokens")

            value = int(self.tokens[0].value)
            counter = 1
            while counter < len(self.tokens):
                op = self.tokens[counter]
                if op.type == PLUS:
                    value += int(self.tokens[counter+1].value)
                else:
                    value -= int(self.tokens[counter+1].value)
                counter+=2
        
            return value