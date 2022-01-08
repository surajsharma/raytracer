"""
Unit Tests for Vector Class
"""

import unittest
from vector import Vector


class TestVectors(unittest.TestCase):
    """class to test all vectors"""

    def setUp(self):
        """setup testing vactors"""
        self.v_1 = Vector(1.0, -2.0, -2.0)
        self.v_2 = Vector(3.0, 6.0, 9.0)

    def test_magnitude(self):
        """test magnitude of vactor"""
        self.assertEqual(self.v_1.magnitude(), 3)

    def test_add(self):
        """test vector addition"""
        _sum = self.v_1 + self.v_2
        self.assertEqual(getattr(_sum, "v_x"), 4.0)

    def test_sub(self):
        """test vector subtraction"""
        diff = self.v_1 - self.v_2
        self.assertEqual(getattr(diff, "v_x"), -2.0)

    def test_mul(self):
        """test vector multiplication"""
        diff = self.v_1 * 2
        self.assertEqual(getattr(diff, "v_x"), 2.0)

    def test_div(self):
        """test vector division"""
        diff = self.v_1 / 2
        self.assertEqual(getattr(diff, "v_x"), 0.5)


if __name__ == "__main__":
    unittest.main()
