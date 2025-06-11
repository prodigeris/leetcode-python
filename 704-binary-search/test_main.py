import unittest
from main import Solution


class TestBinarySearch(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(4, self.solution.search([-1, 0, 3, 5, 9, 12], 9))

    def test_example_2(self):
        self.assertEqual(-1, self.solution.search([-1, 0, 3, 5, 9, 12], 2))

    def test_example_3(self):
        self.assertEqual(-1, self.solution.search([-1, 0, 3, 5, 9, 12], 13))


if __name__ == '__main__':
    unittest.main()
