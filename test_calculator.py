# https://github.com/taran-r/lab11-TR-QT
# Partner: Taran Raj
# Partner: Quocnghia Truong
import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    # Partner 2
    def test_add(self):
        self.assertTrue(add(1, 2) == 3)
        self.assertTrue(add(-1, -2) == -3)
        self.assertTrue(add(0, 0) == 0)

    def test_subtract(self):
        self.assertTrue(subtract(1, -1) == 2)
        self.assertTrue(subtract(-10, -1) == -9)
        self.assertTrue(subtract(-10, 5) == -15)

    # Partner 1
    def test_multiply(self): # 3 assertions
        self.assertTrue(mul(5, 5) == 25)
        self.assertTrue(mul(-10, -1) == 10)
        self.assertFalse(mul(-5, 10) == 50)

    def test_divide(self): # 3 assertions
         self.assertFalse(div(5, 10) == 10)
         self.assertTrue(div(10, 200) == 20)
         self.assertTrue(div(-5, 50) == -10)

    ######## Partner 2
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self):
        self.assertTrue(logarithm(2, 32) == 5)
        self.assertTrue(logarithm(2, 2) == 1)
        self.assertTrue(logarithm(2, 1) == 0)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(2, 0)
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
        with self.assertRaises(ValueError):
            logarithm(0, 5)
    #     fill in code

    def test_hypotenuse(self): # 3 assertions
        self.assertTrue(hypotenuse(3, 4) == 5.0)
        self.assertTrue(hypotenuse(5, 12) == 13.0)
        self.assertTrue(hypotenuse(8, 15) == 17.0)

    def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
        with self.assertRaises(ValueError):
            square_root(-9)
        with self.assertRaises(TypeError):
            square_root("hello world")
        with self.assertRaises(ValueError):
            square_root(-21)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()