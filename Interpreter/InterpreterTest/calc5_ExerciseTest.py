#Test cases for calc5_Exercise file

import unittest
from calc5_Exercise import Interpreter
from calc5_Exercise import Lexer


class Calc5TestCases(unittest.TestCase):
    def test_multipleOperations1(self):
        lexer = Lexer("(14 + 2) * 3 - 6 / 2")
        interpreter = Interpreter(lexer)
        result = interpreter.expr()
        self.assertEqual(45, result)

    def test_multipleOperations2(self):
        lexer = Lexer("     (20 - 2) *(6-4)/2")
        interpreter = Interpreter(lexer)
        result = interpreter.expr()
        self.assertEqual(18, result)

    def test_multipleOperations3(self):
        lexer = Lexer("(14 + (2 + 3)) * 3 - 6 / 2")
        interpreter = Interpreter(lexer)
        result = interpreter.expr()
        self.assertEqual(54, result)

    def test_multipleOperations4(self):
        lexer = Lexer("((((14 + 2)))) * 3 - 6 / 2")
        interpreter = Interpreter(lexer)
        result = interpreter.expr()
        self.assertEqual(45, result)

    def test_multipleOperations5(self):
        lexer = Lexer("3 * (2 + (4 * 5)) / 2")
        interpreter = Interpreter(lexer)
        result = interpreter.expr()
        self.assertEqual(33, result)

    def test_multipleOperations6(self):
        lexer = Lexer("(14 + 2) * (3 - 6) / 2")
        interpreter = Interpreter(lexer)
        result = interpreter.expr()
        self.assertEqual(-24, result)

    def test_multipleOperations7(self):
        lexer = Lexer("(14 + 2) * (3 - 6 / 2)")
        interpreter = Interpreter(lexer)
        result = interpreter.expr()
        self.assertEqual(0, result)

    def test_multipleOperations8(self):
        lexer = Lexer("(100) * 3 - 6 / 2")
        interpreter = Interpreter(lexer)
        result = interpreter.expr()
        self.assertEqual(297, result)

    def test_multipleOperations9(self):
        lexer = Lexer("(1024 - 2 +2     ) / (2 / 2)")
        interpreter = Interpreter(lexer)
        result = interpreter.expr()
        self.assertEqual(1024, result)

    def test_multipleOperations10(self):
        lexer = Lexer("14 + 2 * (3 - 6 / 2")
        interpreter = Interpreter(lexer)
        self.assertRaises(Exception, interpreter.expr)

    def test_multipleOperations11(self):
        lexer = Lexer("14 + 2 * 3 - 6 / 2")
        interpreter = Interpreter(lexer)
        result = interpreter.expr()
        self.assertEqual(17, result)

    def test_multipleOperations12(self):
        lexer = Lexer("14+2*3-6")
        interpreter = Interpreter(lexer)
        result = interpreter.expr()
        self.assertEqual(14, result)

if __name__ == '__main__':
    unittest.main()