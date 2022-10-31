
import collections
from typing import  List,Optional
import copy

from pandas import Interval
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        index=len(s)-1
        ans=0
        while s[index]==' ':
            index-=1
        while s[index]!=' ':
            index-=1
            ans+=1
        return ans



sol=Solution()
s = "Hello World  "
print(sol.lengthOfLastWord(s))

# 输入：s = "Hello World"
# 输出：5
# 解释：最后一个单词是“World”，长度为5。





