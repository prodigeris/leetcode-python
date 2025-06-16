import unittest

from sol2025 import KthLargest


class TestKthLargest(unittest.TestCase):
    def test_example_1(self):
        kth = KthLargest(3, [4, 5, 8, 2])
        self.assertEqual(4, kth.add(3))
        self.assertEqual(5, kth.add(5))
        self.assertEqual(5, kth.add(10))
        self.assertEqual(8, kth.add(9))
        self.assertEqual(8, kth.add(4))

    def test_example_2(self):
        kth = KthLargest(1, [])
        self.assertEqual(-3, kth.add(-3))
        self.assertEqual(-2, kth.add(-2))
        self.assertEqual(-2, kth.add(-4))
        self.assertEqual(0, kth.add(0))
        self.assertEqual(4, kth.add(4))


if __name__ == '__main__':
    unittest.main()
