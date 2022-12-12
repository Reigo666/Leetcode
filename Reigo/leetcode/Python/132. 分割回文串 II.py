
import collections
from typing import  List,Optional
import copy

class Solution:
    def minCut(self, s: str) -> int:
        n=len(s)
        dp=[[False]*n for i in range(n)]
        for j in range(n):
            for i in range(j,-1,-1):
                if i==j:
                    dp[i][i]=True
                elif j-i==1:
                    if s[i]==s[j]:
                        dp[i][j]=True
                else:
                    if dp[i+1][j-1]==True and s[i]==s[j]:
                        dp[i][j]=True
        
        f=[0]*(n)
        for i in range(n):
            f[i]=i
            if dp[0][i]:
                f[i]=0
            for j in range(1,i+1):
                if dp[j][i]:
                    f[i]=min(f[i],f[j-1]+1)
        return f[n-1]


sol=Solution()
s = "aab"
print(sol.minCut(s))


# 输入：s = "aab"
# 输出：[["a","a","b"],["aa","b"]]