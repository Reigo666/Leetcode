import collections
from typing import  List,Optional
import copy
class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        dictrow=collections.defaultdict(int)
        dictcol=collections.defaultdict(int)
        for indice in indices:
            dictrow[indice[0]]+=1
            dictcol[indice[1]]+=1
        ans=0
        for i in range(m):
            for j in range(n):
                if (dictrow[i]+dictcol[j])%2==1:
                    ans+=1
        return ans