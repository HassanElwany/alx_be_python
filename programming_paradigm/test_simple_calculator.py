import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def test_add(self):
        result = SimpleCalculator.add(self, 10, 5)
        self.assertAlmostEqual(result, 15)
        self.assertAlmostEqual(SimpleCalculator.add(self, -1, 1), 0)

    def test_subtract(self):
        result = SimpleCalculator.subtract(self, 10, 5)
        self.assertAlmostEqual(result, 5)

    def test_multiply(self):
        result = SimpleCalculator.multiply(self, 10, 5)
        self.assertAlmostEqual(result, 50)

    def test_divide(self):
        self.assertAlmostEqual(SimpleCalculator.divide(self, 10, 2), 5)
        self.assertAlmostEqual(SimpleCalculator.divide(self, 10, 0), None)



if __name__ == "__main__":
    unittest.main()