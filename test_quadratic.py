import unittest
from quadratic import quadratic_solver

class test_quadratic(unittest.TestCase):
    def test_zero_discriminant(self):
        self.assertListEqual(quadratic_solver(1, 2, 1), [-1])

    def test_two_roots(self):
        self.assertIn(1, quadratic_solver(-1, 0, 1))
        self.assertIn(-1, quadratic_solver(-1, 0, 1))
        self.assertEqual(len(quadratic_solver(-1, 0, 1)), 2)

    def test_zero_a_b(self):
        # This syntax checks if the ValueError is raised where it is expected
        with self.assertRaises(ValueError):
            quadratic_solver(0, 0, 1)

    def test_zero_a(self):
        self.assertListEqual(quadratic_solver(0, 1, 1), [-1])