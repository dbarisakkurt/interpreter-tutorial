from Lexer import Lexer
from Interpreter import Interpreter


def main():
    lexer = Lexer("10 + 7 * 4")
    interpreter = Interpreter(lexer)
    result = interpreter.interpret();
    print(result)
    print(result == 38)


main()