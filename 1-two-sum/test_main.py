import unittest
from main import Solution


class TestTwoSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        self.assertEqual(self.solution.twoSum([2, 7, 11, 15], 9), [0, 1])

    def test_example2(self):
        self.assertEqual(self.solution.twoSum([3, 2, 4], 6), [1, 2])

    def test_example3(self):
        self.assertEqual(self.solution.twoSum([3, 3], 6), [0, 1])

    def test_example4(self):
        self.assertEqual(self.solution.twoSum([0, 4, 3, 0], 0), [0, 3])

    def test_example5(self):
        self.assertEqual(self.solution.twoSum([-3, 4, 3, 90], 0), [0, 2])


if __name__ == '__main__':
    unittest.main()
