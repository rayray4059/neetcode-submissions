class WordDictionary:

    def __init__(self):
        self.children = [None] * 26
        self.end = False

    def addWord(self, word: str) -> None:
        current = self
        for c in word:
            pos = ord(c.lower()) - 97
            if not current.children[pos]:
                current.children[pos] = WordDictionary()
            current = current.children[pos]
        current.end = True

    def search(self, word: str) -> bool:
        current = self
        def dfs(node, i):
            if i == len(word):
                return node.end
            if word[i] == ".":
                for n in node.children:
                    if n and dfs(n, i + 1):
                        return True
                return False
            pos = ord(word[i]) - 97
            if not node.children[pos]:
                return False
            return dfs(node.children[pos], i + 1)
        return dfs(current, 0)

