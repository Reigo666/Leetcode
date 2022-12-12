
import collections
from typing import  List,Optional
import copy

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        dp=[1]
        for i in range(1,n):
            dp.append(dp[i-1]*i)
        numlist=list(range(1,n+1))


        ansstr=''
        groupnum=k
        for i in range(n-1,-1,-1):
            ansstr+=str(numlist.pop((groupnum-1)//dp[i]))
            groupnum%=dp[i]
            if groupnum==0:groupnum=dp[i]

        return ansstr
sol=Solution()
n1 = 4
k1 = 12
print(sol.getPermutation(n1,k1))

# 输入：n = 3, k = 3
# 输出："213"





