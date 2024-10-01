import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        # Create an instance of SimpleCalculator
        self.calc = SimpleCalculator()

    def test_addition(self):
        result = self.calc.add(10, 5)
        self.assertAlmostEqual(result, 15)
        self.assertAlmostEqual(self.calc.add(-1, 1), 0)

    def test_subtract(self):
        result = self.calc.subtract(10, 5)
        self.assertAlmostEqual(result, 5)

    def test_multiply(self):
        result = self.calc.multiply(10, 5)
        self.assertAlmostEqual(result, 50)

    def test_divide(self):
        self.assertAlmostEqual(self.calc.divide(10, 2), 5)
        # For division by zero, handle the exception or check if None is returned
        self.assertEqual(self.calc.divide(10, 0), None)

if __name__ == "__main__":
    unittest.main()
