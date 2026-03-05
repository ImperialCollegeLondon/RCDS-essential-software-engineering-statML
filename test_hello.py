import unittest
from hello import addition

class test_hello(unittest.TestCase):
    def test_output(self):
        self.assertEqual(addition(1,2), 3)