
#Test cases for calc1_Exercise file

import unittest
from calc1_Exercise import Interpreter


class Calc1TestCases(unittest.TestCase):

    def test_addOneDigitNumber_ToOneDigitNumber_ReturnsTen(self):
        interpreter = Interpreter("3+7")
        result = interpreter.expr()
        self.assertEqual(10, result)

    def test_addZero_ToZero_ReturnsZero(self):
        interpreter = Interpreter("0+0")
        result = interpreter.expr()
        self.assertEqual(0, result)

    def test_addMultiDigitNumber_ToOneDigitNumber_ReturnsResult(self):
        interpreter = Interpreter("16+9")
        result = interpreter.expr()
        self.assertEqual(25, result)

        interpreter = Interpreter("133+7")
        result = interpreter.expr()
        self.assertEqual(140, result)

        interpreter = Interpreter("3133+4")
        result = interpreter.expr()
        self.assertEqual(3137, result)

        interpreter = Interpreter("103431+9")
        result = interpreter.expr()
        self.assertEqual(103440, result)

    def test_addOneDigitNumber_ToMultiDigitNumber_ReturnsResult(self):
        interpreter = Interpreter("5+75")
        result = interpreter.expr()
        self.assertEqual(80, result)

        interpreter = Interpreter("1+754")
        result = interpreter.expr()
        self.assertEqual(755, result)

        interpreter = Interpreter("2+6754")
        result = interpreter.expr()
        self.assertEqual(6756, result)

        interpreter = Interpreter("8+74354")
        result = interpreter.expr()
        self.assertEqual(74362, result)

    def test_addMultiDigitNumber_ToMultiDigitNumber_ReturnsResult(self):
        interpreter = Interpreter("10+76")
        result = interpreter.expr()
        self.assertEqual(86, result)

        interpreter = Interpreter("67+75")
        result = interpreter.expr()
        self.assertEqual(142, result)

        interpreter = Interpreter("100+746")
        result = interpreter.expr()
        self.assertEqual(846, result)

        interpreter = Interpreter("550+746")
        result = interpreter.expr()
        self.assertEqual(1296, result)

        interpreter = Interpreter("990+76")
        result = interpreter.expr()
        self.assertEqual(1066, result)

        interpreter = Interpreter("10+376")
        result = interpreter.expr()
        self.assertEqual(386, result)

        interpreter = Interpreter("14340+37436")
        result = interpreter.expr()
        self.assertEqual(51776, result)

    def test_subtractOneDigitNumber_FromOneDigitNumber_ReturnsSix(self):
        interpreter = Interpreter("7-1")
        result = interpreter.expr()
        self.assertEqual(6, result)

    def test_subtractZero_FromZero_ReturnsZero(self):
        interpreter = Interpreter("0-0")
        result = interpreter.expr()
        self.assertEqual(0, result)

    def test_subtractMultiDigitNumber_FromOneDigitNumber_ReturnsResult(self):
        interpreter = Interpreter("5-34")
        result = interpreter.expr()
        self.assertEqual(-29, result)

        interpreter = Interpreter("3-546")
        result = interpreter.expr()
        self.assertEqual(-543, result)

        interpreter = Interpreter("4-5454")
        result = interpreter.expr()
        self.assertEqual(-5450, result)

        interpreter = Interpreter("9-434356")
        result = interpreter.expr()
        self.assertEqual(-434347, result)

    def test_subtractOneDigitNumber_FromMultiDigitNumber_ReturnsResult(self):
        interpreter = Interpreter("75-5")
        result = interpreter.expr()
        self.assertEqual(70, result)

        interpreter = Interpreter("754-1")
        result = interpreter.expr()
        self.assertEqual(753, result)

        interpreter = Interpreter("6754-2")
        result = interpreter.expr()
        self.assertEqual(6752, result)

        interpreter = Interpreter("74354-8")
        result = interpreter.expr()
        self.assertEqual(74346, result)

    def test_subtractMultiDigitNumber_FromMultiDigitNumber_ReturnsResult(self):
        interpreter = Interpreter("10-76")
        result = interpreter.expr()
        self.assertEqual(-66, result)

        interpreter = Interpreter("75-67")
        result = interpreter.expr()
        self.assertEqual(8, result)

        interpreter = Interpreter("100-746")
        result = interpreter.expr()
        self.assertEqual(-646, result)

        interpreter = Interpreter("550-246")
        result = interpreter.expr()
        self.assertEqual(304, result)

        interpreter = Interpreter("990-76")
        result = interpreter.expr()
        self.assertEqual(914, result)

        interpreter = Interpreter("10-376")
        result = interpreter.expr()
        self.assertEqual(-366, result)

        interpreter = Interpreter("14340-37436")
        result = interpreter.expr()
        self.assertEqual(-23096, result)

    def test_InputHasWhiteSpace_AddNumbers_ReturnsResult(self):
        interpreter = Interpreter(" 3 + 7 ")
        result = interpreter.expr()
        self.assertEqual(10, result)

        interpreter = Interpreter("    3 +    7 ")
        result = interpreter.expr()
        self.assertEqual(10, result)

        interpreter = Interpreter(" 3+7 ")
        result = interpreter.expr()
        self.assertEqual(10, result)

        interpreter = Interpreter("3                 +7")
        result = interpreter.expr()
        self.assertEqual(10, result)

        interpreter = Interpreter("3+    7")
        result = interpreter.expr()
        self.assertEqual(10, result)

        interpreter = Interpreter(" 3    +       7")
        result = interpreter.expr()
        self.assertEqual(10, result)

        interpreter = Interpreter(" 3+7         ")
        result = interpreter.expr()
        self.assertEqual(10, result)

    def test_InputHasWhiteSpace_SubtractNumbers_ReturnsResult(self):
        interpreter = Interpreter(" 3 - 7 ")
        result = interpreter.expr()
        self.assertEqual(-4, result)

        interpreter = Interpreter("    3 -   7 ")
        result = interpreter.expr()
        self.assertEqual(-4, result)

        interpreter = Interpreter(" 3-7 ")
        result = interpreter.expr()
        self.assertEqual(-4, result)

        interpreter = Interpreter("3                 -3547")
        result = interpreter.expr()
        self.assertEqual(-3544, result)

        interpreter = Interpreter("543-    7")
        result = interpreter.expr()
        self.assertEqual(536, result)

        interpreter = Interpreter(" 30    -       7")
        result = interpreter.expr()
        self.assertEqual(23, result)

        interpreter = Interpreter(" 3-71         ")
        result = interpreter.expr()
        self.assertEqual(-68, result)

        interpreter = Interpreter(" 3000-4000         ")
        result = interpreter.expr()
        self.assertEqual(-1000, result)

if __name__ == '__main__':
    unittest.main()

