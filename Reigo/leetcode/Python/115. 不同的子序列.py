
import collections
from typing import  List,Optional
import copy

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if not t:
            return 1
        m=len(t)
        n=len(s)
        dp=[[0]*(n+1) for i in range(m+1)]
        for j in range(n+1):
            dp[0][j]=1
        for i in range(1,m+1):
            for j in range(1,n+1):
                if t[i-1]==s[j-1]:
                    dp[i][j]=dp[i-1][j-1]+dp[i][j-1]
                else:
                    dp[i][j]=dp[i][j-1]
        return dp[m][n]
        
sol=Solution()

s = "babgbag"
t = "bag"
print(sol.numDistinct(s,t))




# 输入：s = "babgbag", t = "bag"
# 输出：5


