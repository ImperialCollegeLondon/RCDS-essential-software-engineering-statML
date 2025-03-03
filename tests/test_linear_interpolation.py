import unittest

from linear_interpolation import linear_interpolation  # Adjust the import statement as needed

class TestLinearInterpolation(unittest.TestCase):

    def test_interpolation_within_range(self):
        self.assertAlmostEqual(linear_interpolation(0, 0, 10, 10, 5), 5)
        self.assertAlmostEqual(linear_interpolation(1, 2, 3, 4, 2), 3)
        self.assertAlmostEqual(linear_interpolation(-1, -1, 1, 1, 0), 0)

    def test_interpolation_at_boundaries(self):
        self.assertAlmostEqual(linear_interpolation(0, 0, 10, 10, 0), 0)
        self.assertAlmostEqual(linear_interpolation(0, 0, 10, 10, 10), 10)

    def test_interpolation_outside_range(self):
        with self.assertRaises(ValueError):
            linear_interpolation(0, 0, 10, 10, -1)
        with self.assertRaises(ValueError):
            linear_interpolation(0, 0, 10, 10, 11)
            def test_interpolation_with_negative_values(self):
                self.assertAlmostEqual(linear_interpolation(-10, -10, 0, 0, -5), -5)
                self.assertAlmostEqual(linear_interpolation(-10, -20, 0, 0, -5), -10)
                self.assertAlmostEqual(linear_interpolation(-5, -5, 5, 5, 0), 0)

            def test_interpolation_with_floats(self):
                self.assertAlmostEqual(linear_interpolation(0.0, 0.0, 10.0, 10.0, 5.0), 5.0)
                self.assertAlmostEqual(linear_interpolation(1.5, 2.5, 3.5, 4.5, 2.5), 3.5)
                self.assertAlmostEqual(linear_interpolation(-1.0, -1.0, 1.0, 1.0, 0.0), 0.0)

            def test_interpolation_with_same_points(self):
                self.assertAlmostEqual(linear_interpolation(1, 1, 1, 1, 1), 1)
                with self.assertRaises(ZeroDivisionError):
                    linear_interpolation(1, 1, 1, 1, 2)

            def test_interpolation_with_large_numbers(self):
                self.assertAlmostEqual(linear_interpolation(1e10, 1e10, 1e11, 1e11, 5e10), 5e10)
                self.assertAlmostEqual(linear_interpolation(1e10, 2e10, 1e11, 2e11, 5e10), 1e11)
if __name__ == '__main__':
    unittest.main()
