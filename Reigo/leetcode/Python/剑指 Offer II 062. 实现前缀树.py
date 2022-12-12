class TrieNode:
    def __init__(self):
        self.next={}
        self.isEnd=False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root=TrieNode()


    def insert(self, word: str) -> None:

        """
        Inserts a word into the trie.
        """
        node=self.root
        for l in word:
            if l not in node.next:
                node.next[l]=TrieNode()
            node=node.next[l]
        node.isEnd=True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node=self.root
        for l in word:
            if l not in node.next:
                return False
            node=node.next[l]
        if node.isEnd:
            return True
        return False


    def startsWith(self, prefix: str) -> bool:
        node=self.root
        for l in prefix:
            if l not in node.next:
                return False
            node=node.next[l]
        return True
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)