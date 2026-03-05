import unittest
from linear_interpolation import linear_interpolation


class test_linear_interpolation(unittest.TestCase):
    def test_middle_value(self):
        # interpolation halfway between the points should give average of y
        self.assertEqual(linear_interpolation(0, 0, 10, 10, 5), 5)

    def test_endpoints(self):
        # x exactly at the endpoints should return the corresponding y
        self.assertEqual(linear_interpolation(1, 2, 3, 4, 1), 2)
        self.assertEqual(linear_interpolation(1, 2, 3, 4, 3), 4)

    def test_out_of_range_low(self):
        with self.assertRaises(ValueError):
            linear_interpolation(0, 0, 1, 1, -0.1)

    def test_out_of_range_high(self):
        with self.assertRaises(ValueError):
            linear_interpolation(0, 0, 1, 1, 1.1)

    def test_vertical_line(self):
        # x1 == x2 should lead to a ZeroDivisionError when computing gradient
        with self.assertRaises(ZeroDivisionError):
            linear_interpolation(1, 1, 1, 2, 1)
