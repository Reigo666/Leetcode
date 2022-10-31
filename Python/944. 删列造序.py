import collections
from typing import  List,Optional
import copy
class Solution:
    #直接模拟即可 判断每列
    def minDeletionSize(self, strs: List[str]) -> int:
        dict={}
        ans=set()
        for i in range(len(strs)):
            for j in range(len(strs[0])):
                if j in ans:
                    continue
                if j not in dict:
                    dict[j]=strs[i][j]
                else:
                    lastletter=dict[j]
                    if ord(lastletter)>ord(strs[i][j]):
                        ans.add(j)
                        continue
                    else:
                        dict[j]=strs[i][j]
        return len(ans)
