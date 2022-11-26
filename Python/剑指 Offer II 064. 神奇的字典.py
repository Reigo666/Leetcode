class TrieNode:
    def __init__(self):
        self.next={}
        self.isEnd=False

class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root=TrieNode()

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            node=self.root
            for l in word:
                if l not in node.next:
                    node.next[l]=TrieNode()
                node=node.next[l]
            node.isEnd=True
        

    def search(self, searchWord: str) -> bool:
        def dfs(left,s,node):
            if left<0:
                return False
            if not s:
                if left==1:
                    return False
                if left==0:
                    if node.isEnd:
                        return True
                    return False
            
            for l in node.next:
                if l==s[0]:
                    if dfs(left,s[1:],node.next[l]):
                        return True
                elif l!=s[0]:
                    if dfs(left-1,s[1:],node.next[l]):
                        return True
            return False
        return dfs(1,searchWord,self.root)



# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)