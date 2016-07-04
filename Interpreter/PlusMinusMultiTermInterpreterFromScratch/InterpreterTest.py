
import unittest
from Interpreter import Interpreter

class TestInterpreter(unittest.TestCase):

    # Add Only Tests
    def test_AddOnly1(self):
        interpreter = Interpreter("1+2+3+4")
        result = interpreter.evaluate()
        self.assertEqual(10, result)

    def test_AddOnly2(self):
        interpreter = Interpreter("21 + 543 + 33")
        result = interpreter.evaluate()
        self.assertEqual(597, result)

    def test_AddOnly3(self):
        interpreter = Interpreter("  100    + 5         +3 ")
        result = interpreter.evaluate()
        self.assertEqual(108, result)

    def test_AddOnly4(self):
        interpreter = Interpreter("11+22")
        result = interpreter.evaluate()
        self.assertEqual(33, result)

    #Subtract Only Tests
    def test_SubtractOnly1(self):
        interpreter = Interpreter("1-2-3-4")
        result = interpreter.evaluate()
        self.assertEqual(10, result)

    def test_SubtractOnly2(self):
        interpreter = Interpreter("100 - 80   - 5")
        result = interpreter.evaluate()
        self.assertEqual(15, result)

    def test_SubtractOnly3(self):
        interpreter = Interpreter("  100    - 5         -3 ")
        result = interpreter.evaluate()
        self.assertEqual(92, result)

    def test_SubtractOnly4(self):
        interpreter = Interpreter("  9999    - 10 ")
        result = interpreter.evaluate()
        self.assertEqual(9989, result)

    #Additon Subtraction Tests
    def test_SubtractOnly1(self):
        interpreter = Interpreter("1+2-3+4")
        result = interpreter.evaluate()
        self.assertEqual(4, result)

    def test_SubtractOnly2(self):
        interpreter = Interpreter("100 - 80   + 5")
        result = interpreter.evaluate()
        self.assertEqual(25, result)

    def test_SubtractOnly3(self):
        interpreter = Interpreter("  100    + 5         -3  +1 - 3")
        result = interpreter.evaluate()
        self.assertEqual(100, result)

    #Edge Cases and Fails
    def test_EdgeCase1(self):
        interpreter = Interpreter("1")
        result = interpreter.evaluate()
        self.assertEqual(1, result)

    def test_EdgeCase2(self):
        interpreter = Interpreter(" 100             ")
        result = interpreter.evaluate()
        self.assertEqual(100, result)

    def test_Fail1(self):
        interpreter = Interpreter("5+")
        self.assertRaises(Exception, interpreter.evaluate)

    def test_Fail2(self):
        interpreter = Interpreter("  3 - ")
        self.assertRaises(Exception, interpreter.evaluate)

    def test_Fail3(self):
        interpreter = Interpreter("3*5")
        self.assertRaises(Exception, interpreter.evaluate)

    def test_Fail4(self):
        interpreter = Interpreter("3/5")
        self.assertRaises(Exception, interpreter.evaluate)

if __name__ == '__main__':
    unittest.main()