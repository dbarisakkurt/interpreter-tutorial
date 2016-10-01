from Interpreter import *
import unittest


if __name__ == '__main__':
    unittest.main()

class AddSubtractMultiplyDivideTestInterpreter(unittest.TestCase):

    def test_OnlyNumber1(self):
        interpreter = Interpreter("3")
        result = interpreter.interpret();
        self.assertEqual(3, result)

    def test_OnlyNumber2(self):
        interpreter = Interpreter("         5   ")
        result = interpreter.interpret();
        self.assertEqual(5, result)

    def test_MultiplyOnly1(self):
        interpreter = Interpreter("1*2*3")
        result = interpreter.interpret();
        self.assertEqual(6, result)
    def test_MultiplyOnly2(self):
        interpreter = Interpreter("1   *  2         *3")
        result = interpreter.interpret();
        self.assertEqual(6, result)
    def test_MultiplyOnly3(self):
        interpreter = Interpreter("1*2*3*4*5")
        result = interpreter.interpret();
        self.assertEqual(120, result)
    def test_MultiplyOnly4(self):
        interpreter = Interpreter("1*2")
        result = interpreter.interpret();
        self.assertEqual(2, result)



    def test_AddOnly1(self):
        interpreter = Interpreter("1+2+3")
        result = interpreter.interpret();
        self.assertEqual(6, result)
    def test_AddyOnly2(self):
        interpreter = Interpreter("1   +2+3     ")
        result = interpreter.interpret();
        self.assertEqual(6, result)
    def test_AddOnly3(self):
        interpreter = Interpreter("1+2+3+4+5")
        result = interpreter.interpret();
        self.assertEqual(15, result)
    def test_AddOnly4(self):
        interpreter = Interpreter(" 1+2     ")
        result = interpreter.interpret();
        self.assertEqual(3, result)



    def test_SubtractOnly1(self):
        interpreter = Interpreter("101- 2 - 3  ")
        result = interpreter.interpret();
        self.assertEqual(96, result)
    def test_SubtractOnly2(self):
        interpreter = Interpreter("0  - 2-3")
        result = interpreter.interpret();
        self.assertEqual(-5, result)
    def test_SubtractOnly3(self):
        interpreter = Interpreter("1-2-3-4-5")
        result = interpreter.interpret();
        self.assertEqual(-13, result)
    def test_SubtractOnly4(self):
        interpreter = Interpreter(" 1   -                       2     ")
        result = interpreter.interpret();
        self.assertEqual(-1, result)


    def test_DivideOnly1(self):
        interpreter = Interpreter(" 100  /  2 / 5  ")
        result = interpreter.interpret();
        self.assertEqual(10, result)
    def test_DivideOnly2(self):
        interpreter = Interpreter("0/2/3")
        result = interpreter.interpret();
        self.assertEqual(0, result)
    def test_DivideOnly3(self):
        interpreter = Interpreter("1/2/3/4/5")
        result = interpreter.interpret();
        self.assertEqual(0, result)
    def test_DivideOnly4(self):
        interpreter = Interpreter("96/               2     ")
        result = interpreter.interpret();
        self.assertEqual(48, result)


    def test_Mixed1(self):
        interpreter = Interpreter(" 100  /  2 * 5  +1 -2 ")
        result = interpreter.interpret();
        self.assertEqual(249, result)
    def test_Mixed2(self):
        interpreter = Interpreter("0/2-3+1*2")
        result = interpreter.interpret();
        self.assertEqual(-1, result)
    def test_Mixed3(self):
        interpreter = Interpreter("1+2-4/4*5")
        result = interpreter.interpret();
        self.assertEqual(-2, result)
    def test_Mixed4(self):
        interpreter = Interpreter("96/               2   + 10/2 - 5/1*1  ")
        result = interpreter.interpret();
        self.assertEqual(48, result)

    def test_DivideSubtractMultiply1(self):
        interpreter = Interpreter(" 100  /  2 - 5  *1")
        result = interpreter.interpret();
        self.assertEqual(45, result)
    def test_DivideSubtractMultiply2(self):
        interpreter = Interpreter("0/2-                                    3 - 1*2")
        result = interpreter.interpret();
        self.assertEqual(-5, result)
    def test_DivideSubtractMultiply3(self):
        interpreter = Interpreter("2-4/4*5")
        result = interpreter.interpret();
        self.assertEqual(-3, result)
    def test_DivideSubtractMultiply4(self):
        interpreter = Interpreter("90/               10/3 - 5/1*1  ")
        result = interpreter.interpret();
        self.assertEqual(-2, result)

    def test_DivideAddSubtract1(self):
        interpreter = Interpreter(" 10/5  +1 -3")
        result = interpreter.interpret();
        self.assertEqual(0, result)
    def test_DivideAddSubtract2(self):
        interpreter = Interpreter("0+1+2-3/3")
        result = interpreter.interpret();
        self.assertEqual(2, result)
    def test_DivideAddSubtract3(self):
        interpreter = Interpreter("100+10/1-4")
        result = interpreter.interpret();
        self.assertEqual(106, result)
    def test_DivideAddSubtract4(self):
        interpreter = Interpreter("90 +             10/2-1")
        result = interpreter.interpret();
        self.assertEqual(94, result)
