class Solution:
    def longestCommonSubsequence(self, t1: str, t2: str) -> int:
        m=len(t1)
        n=len(t2)
        dp=[[0]*(n+1) for _ in range(m+1)]

        t1=" "+t1
        t2=" "+t2
        for i in range(1,m+1):
            for j in range(1,n+1):
                if t1[i]==t2[j]:
                    dp[i][j]=max(dp[i][j-1],dp[i-1][j],dp[i-1][j-1]+1)
                else:
                    dp[i][j]=max(dp[i][j-1],dp[i-1][j])
        return dp[m][n]