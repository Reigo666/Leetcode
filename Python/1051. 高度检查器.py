import collections
from typing import  List,Optional
import copy
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        h1=sorted(heights)
        ans=0
        for i in range(len(h1)):
            if h1[i]!=heights[i]:
                ans+=1
        return ans
