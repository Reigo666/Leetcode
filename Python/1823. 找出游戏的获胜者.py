import collections
from typing import  List,Optional
import copy
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        l=list(range(1,n+1))
        idx=0
        while len(l)>1:
            tempk=k
            if k>len(l):
                tempk=k%len(l)
                if tempk==0:
                    tempk=len(l)
            idx+=tempk-1
            #print(idx)
            if idx>=len(l):
                idx=idx-len(l)
            print(l.pop(idx))
            if idx==len(l):
                idx=0
        return l[0]
    def findTheWinner1(self, n: int, k: int) -> int:
        q = collections.deque(range(1, n + 1))
        while len(q) > 1:
            for _ in range(k - 1):
                q.append(q.popleft())
            q.popleft()
        return q[0]

sol=Solution()
print(sol.findTheWinner1(10,6))