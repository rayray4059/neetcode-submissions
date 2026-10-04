class PrefixTree:

    def __init__(self):
        self.children = [None] * 26
        self.end = False

    def insert(self, word: str) -> None:
        current = self
        for c in word:
            pos = ord(c.lower()) - 97
            if not current.children[pos]:
                current.children[pos] = PrefixTree()
            current = current.children[pos]
        current.end = True

    def search(self, word: str) -> bool:
        current = self
        for c in word:
            pos = ord(c.lower()) - 97
            if not current.children[pos]: 
                return False
            current = current.children[pos]        
        return current.end
        

    def startsWith(self, prefix: str) -> bool:
        current = self
        for c in prefix:
            pos = ord(c.lower()) - 97
            if not current.children[pos]: 
                return False
            current = current.children[pos]
        return True
        