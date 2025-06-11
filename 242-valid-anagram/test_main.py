import unittest
from main import Solution



class TestIsAnagram(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        self.assertTrue(self.solution.isAnagram("anagram", "nagaram"))

    def test_example2(self):
        self.assertFalse(self.solution.isAnagram("rat", "car"))


if __name__ == "__main__":
    unittest.main()
