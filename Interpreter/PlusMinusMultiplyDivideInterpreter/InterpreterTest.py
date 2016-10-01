from Interpreter import *
import unittest


if __name__ == '__main__':
    unittest.main()

class AddSubtractMultiplyDivideTestInterpreter(unittest.TestCase):

    def test_MultiplyOnly1(self):
        interpreter = Interpreter("1*2*3")
        result = interpreter.interpret();
        self.assertEqual(6, result)