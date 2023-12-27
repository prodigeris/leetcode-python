class Trie:

    def __init__(self):
        self.children = {}
        self.is_word = False

    def insert(self, word: str) -> None:
        char = word[0]
        if char not in self.children:
            self.children[char] = Trie()
        if len(word) == 1:
            self.children[char].is_word = True
            return
        self.children[char].insert(word[1:])
        return

    def search(self, word: str) -> bool:
        if len(word) == 0:
            return self.is_word
        if word[0] not in self.children:
            return False
        return self.children[word[0]].search(word[1:])

    def startsWith(self, prefix: str) -> bool:
        if len(prefix) == 0:
            return True
        if prefix[0] not in self.children:
            return False
        return self.children[word[0]].startsWith(prefix[1:])

# Your Trie object will be instantiated and called as such:
word = "arnas"
prefix = "a"
obj = Trie()
obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

# print(param_2)
# print(param_3)

print(obj.startsWith("tom"))

