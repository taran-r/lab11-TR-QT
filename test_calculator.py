# https://github.com/taran-r/lab11-TR-QT
# Partner: Taran Raj
# Partner: Quocnghia Truong
import unittest
from calculator import add, sub, div, log

class TestCalculator(unittest.TestCase):
    # Partner 2
    def test_add(self):
        self.assertTrue(add(1, 2) == 3)
        self.assertTrue(add(-1, -2) == -3)
        self.assertTrue(add(0, 0) == 0)

    def test_subtract(self):
        self.assertTrue(sub(1, -1) == 2)
        self.assertTrue(sub(-10, -1) == -9)
        self.assertTrue(sub(-10, 5) == -15)

    ######## Partner 1
    # def test_multiply(self): # 3 assertions
    #     fill in code

    # def test_divide(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self):
        self.assertTrue(log(2, 32) == 5)
        self.assertTrue(log(2, 2) == 1)
        self.assertTrue(log(2, 1) == 0)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            log(2, 0)
    
    ######## Partner 1
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    # def test_hypotenuse(self): # 3 assertions
    #     fill in code

    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()