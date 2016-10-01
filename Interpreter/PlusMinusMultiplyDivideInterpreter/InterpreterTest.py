from Interpreter import *
import unittest


if __name__ == '__main__':
    unittest.main()

class AddSubtractMultiplyDivideTestInterpreter(unittest.TestCase):

    # Add Only Tests
    def test_MultiplyOnly1(self):
        lexer = Lexer("1*2*3")
        interpreter = Interpreter(lexer)
        result = interpreter.interpret();
        self.assertEqual(6, result)