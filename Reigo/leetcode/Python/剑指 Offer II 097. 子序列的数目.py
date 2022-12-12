class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        s=' '+s
        t=' '+t

        m=len(s)
        n=len(t)
        dp=[[0]*n for _ in range(m)]

        for i in range(1,m):
            dp[i][1]=dp[i-1][1]
            if s[i]==t[1]:
                dp[i][1]+=1
        
        #print(dp)
        for j in range(2,n):
            for i in range(j,m):
                dp[i][j]=dp[i-1][j]
                if s[i]==t[j]:
                    dp[i][j]+=dp[i-1][j-1]
        #print(dp)
        return dp[m-1][n-1]