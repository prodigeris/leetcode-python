import unittest
from sol_2025 import Trie


class TestImplementTriePrefixTree(unittest.TestCase):
    def test_example_1(self):
        trie = Trie()
        trie.insert("apple")
        self.assertTrue(trie.search("apple"))
        self.assertFalse(trie.search("app"))
        self.assertTrue(trie.startsWith("app"))
        trie.insert("app")
        self.assertTrue(trie.search("app"))


if __name__ == '__main__':
    unittest.main()
