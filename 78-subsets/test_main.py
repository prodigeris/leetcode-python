import unittest
from main import Solution


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        expected = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
        result = self.solution.subsets([1, 2, 3])

        self.assertCountEqual(
            [tuple(sorted(subset)) for subset in expected],
            [tuple(sorted(subset)) for subset in result]
        )

    def test_example_2(self):
        expected = [[], [0]]
        result = self.solution.subsets([0])

        self.assertCountEqual(
            [tuple(sorted(subset)) for subset in expected],
            [tuple(sorted(subset)) for subset in result]
        )


if __name__ == '__main__':
    unittest.main()
