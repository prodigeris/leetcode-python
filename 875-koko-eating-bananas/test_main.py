import unittest
from main import Solution


class TestKokoEatingBananas(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(4, self.solution.minEatingSpeed([3, 6, 7, 11], 8))

    def test_example_2(self):
        self.assertEqual(30, self.solution.minEatingSpeed([30, 11, 23, 4, 20], 5))

    def test_example_3(self):
        self.assertEqual(23, self.solution.minEatingSpeed([30, 11, 23, 4, 20], 6))


if __name__ == '__main__':
    unittest.main()
