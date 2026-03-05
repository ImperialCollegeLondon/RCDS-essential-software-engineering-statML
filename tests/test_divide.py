import unittest
from divide import divide

class test_divide(unittest.TestCase):
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(2, 0)
    
    def test_negative(self):
        self.assertEqual(-1, divide(2, -2))

    def test_regular(self):
        self.assertEqual(0.5, divide(1, 2))