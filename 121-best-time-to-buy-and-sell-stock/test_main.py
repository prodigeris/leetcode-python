import unittest
from main import Solution


class TestStocks(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.maxProfit([7, 1, 5, 3, 6, 4]), 5)  # add assertion here

    def test_example_2(self):
        self.assertEqual(self.solution.maxProfit([7, 6, 4, 3, 1]), 0)  # add assertion here

    def test_example_3(self):
        self.assertEqual(self.solution.maxProfit([1, 2]), 1)  # add assertion here


if __name__ == '__main__':
    unittest.main()
