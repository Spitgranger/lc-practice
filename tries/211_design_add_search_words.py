class Node:
    def __init__(self):
        self.isWord = False
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = Node()
            cur = cur.children[char]
        cur.isWord = True

    def search(self, word: str) -> bool:
        cur = self.root
        def dfs(node, word, index):
            if index == len(word):
                return node.isWord
            if word[index] == ".":
                if index == len(word):
                    return True
                for child in node.children.values():
                    if dfs(child, word, index + 1):
                        return True
                return False
            if word[index] not in node.children:
                return False
            elif word[index] in node.children:
                node = node.children.get(word[index])
                return dfs(node, word, index + 1)
        return dfs(cur, word, 0)




# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)