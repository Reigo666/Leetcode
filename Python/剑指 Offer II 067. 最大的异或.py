class TrieNode:
    def __init__(self):
        self.next={}

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:

        root=TrieNode()
        for num in nums:
            node=root
            for i in range(30,-1,-1):
                cur=num>>i&1
                if cur not in node.next:
                    node.next[cur]=TrieNode()
                node=node.next[cur]
        pow2i=[1]*31
        for i in range(1,31):
            pow2i[i]=pow2i[i-1]*2
        maxans=0
        for num in nums:
            tempval=0
            node=root
            for i in range(30,-1,-1):
                cur=num>>i&1

                if (1-cur) in node.next:
                    tempval+=pow2i[i]
                    node=node.next[1-cur]
                else:
                    node=node.next[cur]
            
            if tempval>maxans:
                maxans=tempval
        return maxans