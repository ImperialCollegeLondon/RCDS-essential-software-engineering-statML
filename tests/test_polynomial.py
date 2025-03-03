import unittest
from polynomial import Polynomial

class TestPolynomial(unittest.TestCase):

    def test_initialization(self):
        p = Polynomial([1, 2, 3])
        self.assertEqual(p.coefficients, [1, 2, 3])

    def test_repr(self):
        p = Polynomial([1, 0, 3])
        self.assertEqual(repr(p), "1*x^0 + 3*x^2")

    def test_addition(self):
        p1 = Polynomial([1, 2, 3])
        p2 = Polynomial([3, 2, 1])
        p3 = p1 + p2
        self.assertEqual(p3.coefficients, [4, 4, 4])

    def test_subtraction(self):
        p1 = Polynomial([5, 4, 3])
        p2 = Polynomial([3, 2, 1])
        p3 = p1 - p2
        self.assertEqual(p3.coefficients, [2, 2, 2])

    def test_multiplication(self):
        p1 = Polynomial([1, 2])
        p2 = Polynomial([1, 2])
        p3 = p1 * p2
        self.assertEqual(p3.coefficients, [1, 4, 4])

    def test_evaluate(self):
        p = Polynomial([1, 2, 3])
        self.assertEqual(p.evaluate(0), 1)
        self.assertEqual(p.evaluate(1), 6)
        self.assertEqual(p.evaluate(2), 17)
        def test_repr(self):
            p = Polynomial([1, 0, 3])
            self.assertEqual(repr(p), "1 + 3*x^2")
if __name__ == '__main__':
    class TestPolynomial(unittest.TestCase):

        def test_initialization(self):
            p = Polynomial([1, 2, 3])
            self.assertEqual(p.coefficients, [1, 2, 3])

        def test_repr(self):
            p = Polynomial([1, 0, 3])
            self.assertEqual(repr(p), "1 + 3*x^2")

        def test_addition(self):
            p1 = Polynomial([1, 2, 3])
            p2 = Polynomial([3, 2, 1])
            p3 = p1 + p2
            self.assertEqual(p3.coefficients, [4, 4, 4])

        def test_subtraction(self):
            p1 = Polynomial([5, 4, 3])
            p2 = Polynomial([3, 2, 1])
            p3 = p1 - p2
            self.assertEqual(p3.coefficients, [2, 2, 2])

        def test_multiplication(self):
            p1 = Polynomial([1, 2])
            p2 = Polynomial([1, 2])
            p3 = p1 * p2
            self.assertEqual(p3.coefficients, [1, 4, 4])

        def test_evaluate(self):
            p = Polynomial([1, 2, 3])
            self.assertEqual(p.evaluate(0), 1)
            self.assertEqual(p.evaluate(1), 6)
            self.assertEqual(p.evaluate(2), 17)

    if __name__ == '__main__':
        unittest.main()
    unittest.main()