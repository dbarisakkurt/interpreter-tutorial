from Lexer import Lexer
from Interpreter import Interpreter


def main():
    interpreter = Interpreter("1 * 7 * 4")
    result = interpreter.interpret();
    print(result)
    print(result == 28)


main()