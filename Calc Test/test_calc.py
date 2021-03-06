# to run this test, download both scripts in a folder, 'cd' to the folder containing both downloaded scripts, 
# when you have changed directory to the folder, run this on your command line 'python test_calc.py', 
# make sure both scripts are in the same folder


import unittest
import calc


class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(5, 5), 10)
        self.assertEqual(calc.add(-5, 5), 0)
        self.assertEqual(calc.add(-5, -5), -10)

    def test_subtract(self):
        self.assertEqual(calc.subtract(5, 5), 0)
        self.assertEqual(calc.subtract(-5, 10), -15)
        self.assertEqual(calc.subtract(-5, -5), 0)

    def test_multiply(self):
        self.assertEqual(calc.multiply(1, 5), 5)
        self.assertEqual(calc.multiply(-5, 5), -25)
        self.assertEqual(calc.multiply(-5, -5), 25)

    def test_divide(self):
        self.assertEqual(calc.divide(5, 1), 5)
        self.assertEqual(calc.divide(-5, 10), -0.5)
        self.assertEqual(calc.divide(-5, -5), 1)

        with self.assertRaises(ValueError):
            calc.divide(10, 0)


if __name__ == '__main__':
    unittest.main()
    
    
    
   
