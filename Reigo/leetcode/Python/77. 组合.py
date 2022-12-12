
import collections
from typing import  List,Optional
import copy


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans=[]
        def backTrack(temp:List[int],numlist:List[int],k):
            if k==0:
                ans.append(copy.deepcopy(temp))
            elif numlist==[]:
                return
            else:
                for i,num in enumerate(numlist):
                    temp.append(num)
                    if len(numlist[i+1:])>=k-1:
                        backTrack(temp,numlist[i+1:],k-1)
                    temp.pop()
        backTrack([],list(range(1,n+1)),k)
        return ans
sol=Solution()
n = 4
k = 2
print(sol.combine(n,k))

# 输入：n = 4, k = 2
# 输出：
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]