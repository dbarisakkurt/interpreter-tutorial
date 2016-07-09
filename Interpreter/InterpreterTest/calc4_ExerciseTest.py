
#Test cases for calc4_Exercise file

import unittest
from calc4_Exercise import Interpreter
from calc4_Exercise import Lexer


class Calc4TestCases(unittest.TestCase):
    def test_multipleAddMultiply1(self):
        lexer = Lexer("1+2*4")
        interpreter = Interpreter(lexer)
        result = interpreter.expr()
        self.assertEqual(9, result)

    def test_multipleAddMultiply2(self):
        lexer = Lexer("1*2+4*5")
        interpreter = Interpreter(lexer)
        result = interpreter.expr()
        self.assertEqual(22, result)

    def test_multipleAddMultiply3(self):
        lexer = Lexer("11*2 + 4*5   ")
        interpreter = Interpreter(lexer)
        result = interpreter.expr()
        self.assertEqual(42, result)

    def test_multipleAddMultiply4(self):
        lexer = Lexer("   11*2 + 400+5   +1   ")
        interpreter = Interpreter(lexer)
        result = interpreter.expr()
        self.assertEqual(428, result)

    def test_multipleSubtractDivide1(self):
        lexer = Lexer("100/20-40")
        interpreter = Interpreter(lexer)
        result = interpreter.expr()
        self.assertEqual(-35, result)

    def test_multipleSubtractDivide2(self):
        lexer = Lexer("2+1 / 4 -5")
        interpreter = Interpreter(lexer)
        result = interpreter.expr()
        self.assertEqual(-3, result)

    def test_multipleSubtractDivide3(self):
        lexer = Lexer("10/2 -2 -3-1   ")
        interpreter = Interpreter(lexer)
        result = interpreter.expr()
        self.assertEqual(-1, result)

    def test_multipleSubtractDivide4(self):
        lexer = Lexer("   11/2 / 5-1   ")
        interpreter = Interpreter(lexer)
        result = interpreter.expr()
        self.assertEqual(0, result)

    def test_multipleSameOperations1(self):
        lexer = Lexer("   11+2 + 400+5   +11   ")
        interpreter = Interpreter(lexer)
        result = interpreter.expr()
        self.assertEqual(429, result)

    def test_multipleSameOperations2(self):
        lexer = Lexer("   100-2 - 10-5   -1     ")
        interpreter = Interpreter(lexer)
        result = interpreter.expr()
        self.assertEqual(82, result)

    def test_multipleSameOperations3(self):
        lexer = Lexer("   2*1 *     10*1*1*1   ")
        interpreter = Interpreter(lexer)
        result = interpreter.expr()
        self.assertEqual(20, result)

    def test_multipleSameOperations4(self):
        lexer = Lexer("   1024/2/2/     2   ")
        interpreter = Interpreter(lexer)
        result = interpreter.expr()
        self.assertEqual(128, result)

    def test_multipleComplexOperations1(self):
        lexer = Lexer("1+2/3-1*1024")
        interpreter = Interpreter(lexer)
        result = interpreter.expr()
        self.assertEqual(-1023, result)

    def test_multipleComplexOperations2(self):
        lexer = Lexer("100/ 2 + 5 * 2 -10")
        interpreter = Interpreter(lexer)
        result = interpreter.expr()
        self.assertEqual(50, result)

    def test_multipleComplexOperations3(self):
        lexer = Lexer("1 * 5 + 0      -3/3")
        interpreter = Interpreter(lexer)
        result = interpreter.expr()
        self.assertEqual(4, result)

    def test_multipleComplexOperations4(self):
        lexer = Lexer("5-5 * 3 +1 /2")
        interpreter = Interpreter(lexer)
        result = interpreter.expr()
        self.assertEqual(-10, result)

if __name__ == '__main__':
    unittest.main()