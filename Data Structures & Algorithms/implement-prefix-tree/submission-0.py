class PrefixTree:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        ptr = self.root
        for letter in word:
            if letter not in ptr:
                ptr[letter] = {}
            ptr = ptr[letter]
                
        ptr["#"] = True

    def search(self, word: str) -> bool:
        ptr = self.root
        for letter in word:
            if letter not in ptr:
                return False
            ptr = ptr[letter]

        return "#" in ptr

    def startsWith(self, prefix: str) -> bool:
        ptr = self.root
        for letter in prefix:
            if letter not in ptr:
                return False
            ptr = ptr[letter]
        
        return True