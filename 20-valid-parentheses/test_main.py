import unittest
from main import Solution


class TestValidParentheses(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(True, self.solution.isValid("()"))  # add assertion here


if __name__ == '__main__':
    unittest.main()
