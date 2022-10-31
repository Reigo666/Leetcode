
import collections
from typing import  List,Optional
import copy

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n=len(s)
        dp=[[False]*n for i in range(n)]
        for j in range(n):
            for i in range(j,-1,-1):
                if i==j:
                    dp[i][j]=True
                elif j-i==1:
                    if s[i]==s[j]:
                        dp[i][j]=True
                else:
                    if s[i]==s[j] and dp[i+1][j-1]==True:
                        dp[i][j]=True
        ans=[]
        def backTrack(combination,l,r):
            if l>r:
                ans.append(copy.deepcopy(combination))
            else:
                for j in range(l,r+1):
                    if dp[l][j]:
                        combination.append(s[l:j+1])
                        backTrack(combination,j+1,r)
                        combination.pop()
        backTrack([],0,n-1)
        return ans
sol=Solution()
s = "aab"
print(sol.partition(s))


# 输入：s = "aab"
# 输出：[["a","a","b"],["aa","b"]]