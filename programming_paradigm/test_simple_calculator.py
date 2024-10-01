import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        # Create an instance of SimpleCalculator
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(-1, 1), 0)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(2, 1), 1)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(4,2), 8)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        # For division by zero, handle the exception or check if None is returned
        self.assertEqual(self.calc.divide(10, 0), None)

if __name__ == "__main__":
    unittest.main()
