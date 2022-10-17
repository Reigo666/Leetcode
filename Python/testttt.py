
import collections
from typing import List


from collections import defaultdict


class Solution:
    def distinctSubseqII(self, s: str) -> int:
        ansset=set()
        def backTrack(combination,left):
            if not left:
                ansset.add(combination)
                return   
            
            backTrack(combination+left[0],left[1:])
            backTrack(combination,left[1:])
        backTrack("",s)
        print(ansset)
        return len(ansset)-1
        

sol=Solution()
s="aba"
print(sol.distinctSubseqII(s))
