#https://github.com/NataliaVeltri/lab11-NV-IG/tree/main
#Partner 1: Natalia Veltri
#Partner 2: Izzie Gomez

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 1
     def test_multiply(self): # 3 assertions
        self.assertEqual(mul(2, 3), 6)
        self.assertEqual(mul(-3, -4), -12)
        self.assertEqual(mul(-4, 2), -8)

     def test_divide(self): # 3 assertions
        self.assertEqual(div(4, 2), 2)
        self.assertEqual(div(4, -2), -2)
        self.assertEqual(div(-6, -2), -3)

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
     def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code
        self.assertRaises(ValueError, log, -2)


     def test_hypotenuse(self): # 3 assertions
    #     fill in code
        self.assertAlmostEqual(hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(hypotenuse(5, 12), 13.0)
        self.assertAlmostEqual(hypotenuse(-3, -4), 5.0)



     def test_sqrt(self): # 3 assertions
        #     # Test for invalid argument, example:
        #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #     #    square_root(NUM)
        #     # Test basic function
        #     fill in code
            self.assertRaises(ValueError, square_root, -2)
            self.assertEqual(square_root(4), 2)
            self.assertEqual(square_root(16, 4))


# Do not touch this
if __name__ == "__main__":
    unittest.main()