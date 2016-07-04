#Test cases for calc3_Exercise file

import unittest
from calc3_Exercise import Interpreter

class TestMultipleMultiplicationDivisionExpressions(unittest.TestCase):
    def test_multipleMultiplications(self):
        interpreter = Interpreter("1*2*3*4")
        result = interpreter.expr()
        self.assertEqual(24, result)

        interpreter = Interpreter("1*2*3*40")
        result = interpreter.expr()
        self.assertEqual(240, result)

        interpreter = Interpreter("1  *22  *   32 *43")
        result = interpreter.expr()
        self.assertEqual(30272, result)

    def test_multipleDivisions(self):
        interpreter = Interpreter("1/2/3/4")
        result = interpreter.expr()
        self.assertEqual(0, result)

        interpreter = Interpreter("64/2/4/1")
        result = interpreter.expr()
        self.assertEqual(8, result)

        interpreter = Interpreter("1024  /1  /   2 /2")
        result = interpreter.expr()
        self.assertEqual(256, result)

    def test_multipleMultiplicationsDivisons(self):
        interpreter = Interpreter("1*2*3/4")
        result = interpreter.expr()
        self.assertEqual(1, result)

        interpreter = Interpreter("100/2*3 / 5")
        result = interpreter.expr()
        self.assertEqual(30, result)

        interpreter = Interpreter("10000  /1  /10   *2 /1")
        result = interpreter.expr()
        self.assertEqual(2000, result)

    def test_InvalidOperations(self):
        interpreter = Interpreter("1+2*3")
        self.assertRaises(Exception, interpreter.expr)

if __name__ == '__main__':
    unittest.main()