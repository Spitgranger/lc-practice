class Node:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        cur = self.root
        for char in word:
            if not cur.children.get(char):
                cur.children.update({char: Node()})
            cur = cur.children.get(char)
        cur.isWord = True

    def search(self, word: str) -> bool:
        cur = self.root
        for char in word:
            if not cur.children.get(char):
                return False
            cur = cur.children.get(char)
        return cur.isWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for char in prefix:
            if not cur.children.get(char):
                return False
            cur = cur.children.get(char)
        return True




# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)