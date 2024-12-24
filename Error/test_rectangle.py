import unittest
from rectangle import calculate_area

class TestRectangle(unittest.TestCase):

    def test_area(self):
        self.assertEqual(calculate_area(5, 3), 15)  # Esto debería fallar

if __name__ == "__main__":
    unittest.main()
