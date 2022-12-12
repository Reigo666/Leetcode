import collections
from typing import  List,Optional
import copy
class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        s+="I"
        l=0
        r=len(s)-1
        ans=[]
        for i in range(len(s)):
            if s[i]=="D":
                ans.append(r)
                r-=1
            else:
                ans.append(l)
                l+=1
        return ans