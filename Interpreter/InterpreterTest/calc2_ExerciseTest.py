#Test cases for calc2_Exercise file

import unittest
from calc2_Exercise import Interpreter

class Calc2TestCases(unittest.TestCase):
    def test_multiplyOneDigitNumber_WithOneDigitNumber_ReturnsTwentyOne(self):
        interpreter = Interpreter("3*7")
        result = interpreter.expr()
        self.assertEqual(21, result)

    def test_multiplyZero_WithZero_ReturnsZero(self):
        interpreter = Interpreter("0 * 0")
        result = interpreter.expr()
        self.assertEqual(0, result)

    def test_multiplyMultiDigitNumber_WithOneDigitNumber_ReturnsResult(self):
        interpreter = Interpreter("15*4")
        result = interpreter.expr()
        self.assertEqual(60, result)

        interpreter = Interpreter("200 *4")
        result = interpreter.expr()
        self.assertEqual(800, result)

        interpreter = Interpreter("3102 *   6")
        result = interpreter.expr()
        self.assertEqual(18612, result)

        interpreter = Interpreter("103431*9")
        result = interpreter.expr()
        self.assertEqual(930879, result)

    def test_addOneDigitNumber_ToMultiDigitNumber_ReturnsResult(self):
        interpreter = Interpreter(" 2*75 ")
        result = interpreter.expr()
        self.assertEqual(150, result)

        interpreter = Interpreter("1*754    ")
        result = interpreter.expr()
        self.assertEqual(754, result)

        interpreter = Interpreter("2 * 6000  ")
        result = interpreter.expr()
        self.assertEqual(12000, result)

        interpreter = Interpreter("8* 10000")
        result = interpreter.expr()
        self.assertEqual(80000, result)

    def test_addMultiDigitNumber_ToMultiDigitNumber_ReturnsResult(self):
        interpreter = Interpreter("10*76")
        result = interpreter.expr()
        self.assertEqual(760, result)

        interpreter = Interpreter("67*75")
        result = interpreter.expr()
        self.assertEqual(5025, result)

        interpreter = Interpreter(" 100 * 746    ")
        result = interpreter.expr()
        self.assertEqual(74600, result)

        interpreter = Interpreter("550 * 746")
        result = interpreter.expr()
        self.assertEqual(410300, result)

        interpreter = Interpreter("900 * 20")
        result = interpreter.expr()
        self.assertEqual(18000, result)

        interpreter = Interpreter("10*376")
        result = interpreter.expr()
        self.assertEqual(3760, result)

        interpreter = Interpreter("14340* 37436")
        result = interpreter.expr()
        self.assertEqual(536832240, result)

    def test_divideOneDigitNumber_ToOneDigitNumber_ReturnsResult(self):
        interpreter = Interpreter("3/7")
        result = interpreter.expr()
        self.assertEqual(0, result)

    def test_divideZero_ToZero_ReturnsZero(self):
        interpreter = Interpreter("0/0")
        self.assertRaises(ZeroDivisionError, interpreter.expr)

    def test_divideNonZero_ToZero_ReturnsZero(self):
        interpreter = Interpreter("1/0")
        self.assertRaises(ZeroDivisionError, interpreter.expr)

    def test_divideMultiDigitNumber_ToOneDigitNumber_ReturnsResult(self):
        interpreter = Interpreter("20/10")
        result = interpreter.expr()
        self.assertEqual(2, result)

        interpreter = Interpreter("140  /7")
        result = interpreter.expr()
        self.assertEqual(20, result)

        interpreter = Interpreter("3000    /4   ")
        result = interpreter.expr()
        self.assertEqual(750, result)

        interpreter = Interpreter("  100000/    10")
        result = interpreter.expr()
        self.assertEqual(10000, result)

    def test_divideOneDigitNumber_ToMultiDigitNumber_ReturnsResult(self):
        interpreter = Interpreter("5/75")
        result = interpreter.expr()
        self.assertEqual(0, result)

        interpreter = Interpreter("1/5754")
        result = interpreter.expr()
        self.assertEqual(0, result)

    def test_divideMultiDigitNumber_ToMultiDigitNumber_ReturnsResult(self):
        interpreter = Interpreter(" 70/10   ")
        result = interpreter.expr()
        self.assertEqual(7, result)

        interpreter = Interpreter(" 67 /    75  ")
        result = interpreter.expr()
        self.assertEqual(0, result)

        interpreter = Interpreter("880/ 110")
        result = interpreter.expr()
        self.assertEqual(8, result)

        interpreter = Interpreter("550 / 746")
        result = interpreter.expr()
        self.assertEqual(0, result)

        interpreter = Interpreter("900/90     ")
        result = interpreter.expr()
        self.assertEqual(10, result)

        interpreter = Interpreter("10 /376")
        result = interpreter.expr()
        self.assertEqual(0, result)

        interpreter = Interpreter("20000 / 10001")
        result = interpreter.expr()
        self.assertEqual(1, result)

    def test_multipleAdditions(self):
        interpreter = Interpreter("1+2+3+4")
        result = interpreter.expr()
        self.assertEqual(10, result)

        interpreter = Interpreter("1+2+3+40")
        result = interpreter.expr()
        self.assertEqual(46, result)

        interpreter = Interpreter("1  +22  +   32 +43")
        result = interpreter.expr()
        self.assertEqual(98, result)

    def test_multipleSubtractions(self):
        interpreter = Interpreter("1-2-3-4")
        result = interpreter.expr()
        self.assertEqual(-8, result)

        interpreter = Interpreter("1-2-3-40")
        result = interpreter.expr()
        self.assertEqual(-44, result)

        interpreter = Interpreter("1  -22  -   32 -43")
        result = interpreter.expr()
        self.assertEqual(-96, result)

    def test_multipleAdditionsSubtractions(self):
        interpreter = Interpreter("1+2-3+4")
        result = interpreter.expr()
        self.assertEqual(4, result)

        interpreter = Interpreter("1+2-3-40")
        result = interpreter.expr()
        self.assertEqual(-40, result)

        interpreter = Interpreter("1  -22  +   32 -43")
        result = interpreter.expr()
        self.assertEqual(-32, result)

if __name__ == '__main__':
    unittest.main()