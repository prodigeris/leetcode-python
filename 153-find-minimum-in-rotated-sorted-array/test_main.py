import unittest
from main import Solution


class TestMinRotated(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(1, self.solution.findMin([3, 4, 5, 1, 2]))

    def test_example_2(self):
        self.assertEqual(0, self.solution.findMin([4, 5, 6, 7, 0, 1, 2]))

    def test_example_3(self):
        self.assertEqual(11, self.solution.findMin([11, 13, 15, 17]))
