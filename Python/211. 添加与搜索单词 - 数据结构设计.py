
class Node:
        def __init__(self):
            self.next={}
            self.isEnd=False
        def get(self,l:str):
            return self.next[l]

        def put(self,l:str):
            self.next[l]=Node()
        
        def contain(self,l:str):
            return l in self.next

class WordDictionary:
        
    def __init__(self):
        self.root=Node()
        self.checked=set()
        self.checkedWrong=set()

    def addWord(self, word: str) -> None:
        n=self.root
        for l in word:
            if not n.contain(l):
                n.put(l)
            n=n.get(l)
        n.isEnd=True
        self.checkedWrong=set()

    def search(self, word: str) -> bool:
        n=self.root
        if word in self.checked:
            return True
        if word in self.checkedWrong:
            return False
        return self.match(n,0,word)

    def match(self,root,k,word):
        if k==len(word):
            return root.isEnd
        if word[k]!=".":
            if not root.contain(word[k]):
                return False
            return self.match(root.get(word[k]),k+1,word)
        else:
            for node in root.next.values():
                if self.match(node,k+1,word):
                    self.checked.add(word)
                    return True
            self.checkedWrong.add(word)
        return False

# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
word="bad"
obj.addWord(word)
param_2 = obj.search("b..")
param_2 = obj.search("b..")
param_2 = obj.search("b..b")
param_2 = obj.search("b..b")
print(param_2)


