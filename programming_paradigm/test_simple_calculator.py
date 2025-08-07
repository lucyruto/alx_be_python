import unittest
from simple_calculator.py import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)

    def test_subtraction(self):
        """Test the addition method."""
        self.assertEqual(self.calc.subtract(3, 1), 2)
        self.assertEqual(self.calc.subtract(-1, -1), 0)

    def test_multiplication(self):
        """Test the addition method."""
        self.assertEqual(self.calc.multiply(3, 1), 3)
        self.assertEqual(self.calc.multiply(-1, -3), 3)

    def test_division(self):
        """Test the addition method."""
        self.assertEqual(self.calc.divide(6, 2), 3)
        self.assertEqual(self.calc.divide(8, 4), 2)
        self.assertEqual(self.calc.divide(2, 0.5), 4)


if __name__="__main__":
    unittest.main()