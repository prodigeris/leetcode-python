class Trie:

    def __init__(self):
        self.children = {}
        self.is_end = False

    def insert(self, word: str) -> None:
        node = self
        for index, char in enumerate(word):
            if char in node.children:
                node = node.children[char]
            else:
                new_node = Trie()
                node.children[char] = new_node
                node = new_node
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
