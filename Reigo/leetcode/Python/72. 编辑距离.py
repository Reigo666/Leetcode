
import collections
from typing import  List,Optional
import copy
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len1=len(word1)
        len2=len(word2)
        if not len1 or not len2:
            return max(len1,len2)
        dp=[[0]*(len2+1) for i in range(len1+1)]
        word1=" "+word1
        word2=" "+word2
        for i in range(1,len2+1):
            dp[0][i]=i
        for i in range(1,len1+1):
            dp[i][0]=i
        for i in range(1,len1+1):
            for j in range(1,len2+1):
                if word1[i]==word2[j]:
                    dp[i][j]=dp[i-1][j-1]
                elif word1[i]!=word2[j]:
                    dp[i][j]=min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])+1
        return dp[len1][len2]

sol=Solution()
word1 = "intention"
word2 = "execution"
word3=""
word4=""
print(sol.minDistance(word3,word4))

# 输入：word1 = "intention", word2 = "execution"
# 输出：5
# 解释：
# intention -> inention (删除 't')
# inention -> enention (将 'i' 替换为 'e')
# enention -> exention (将 'n' 替换为 'x')
# exention -> exection (将 'n' 替换为 'c')
# exection -> execution (插入 'u')

