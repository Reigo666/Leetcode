class TrieNode():
    def __init__(self):
        self.next={}
        self.val=0

class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root=TrieNode()
        self.dict={}
        


    def insert(self, key: str, val: int) -> None:
        dict=self.dict
        indict=key in dict
        node=self.root
        diff=0
        if indict:
            diff=dict[key]-val
        for l in key:
            if l not in node.next:
                node.next[l]=TrieNode()
            node=node.next[l]
            if not indict:
                node.val+=val
            else:
                node.val-=diff
        dict[key]=val

    def sum(self, prefix: str) -> int:
        node=self.root
        for l in prefix:
            if l not in node.next:
                return 0
            node=node.next[l]
        return node.val
        



# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)