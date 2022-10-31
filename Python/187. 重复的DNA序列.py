import collections
from typing import  List,Optional
import copy
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n=len(s)
        if n<=10:
            return []
        dict=collections.defaultdict(int)
        ans=[]
        for i in range(n-10+1):
            temps=s[0+i:10+i]
            dict[temps]+=1
            if dict[temps]==2:
                ans.append(temps)
        return ans
         
