# archivo test_rectangle.py
import unittest
from rectangle import calculate_area

class TestRectangle(unittest.TestCase):

    def test_area(self):
        # Prueba con valores normales
        self.assertEqual(calculate_area(5, 3), 15)
        self.assertEqual(calculate_area(7, 2), 14)

    def test_zero_values(self):
        # Prueba con valores cero
        self.assertEqual(calculate_area(0, 5), 0)
        self.assertEqual(calculate_area(0, 0), 0)

    def test_negative_values(self):
        # Prueba con valores negativos
        with self.assertRaises(ValueError):
            calculate_area(-1, 5)
        with self.assertRaises(ValueError):
            calculate_area(5, -3)

if __name__ == "__main__":
    unittest.main()
