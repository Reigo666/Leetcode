import collections
from typing import  List,Optional
import copy
class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        self.ws=n-len(blacklist)
        self.dict={}
        last=n-1
        for b in blacklist:
            self.dict[b]=666
        
        for b in blacklist:
            if b<self.ws:
                while last in self.dict:
                    last-=1
                self.dict[b]=last
                last-=1
        #print(self.dict)
    def pick(self) -> int:
        num=randint(0,self.ws-1)
        if num not in self.dict:
            return num
        else:
            return self.dict[num]
        

# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()