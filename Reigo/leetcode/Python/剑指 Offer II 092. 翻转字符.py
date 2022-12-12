class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        dp=[[0]*2 for _ in range(len(s))]
        if s[0]=='0':
            dp[0][1]=1
        elif s[0]=='1':
            dp[0][0]=1
        for i in range(1,len(s)):
            if s[i]=='0':
                dp[i][0]=dp[i-1][0]
                dp[i][1]=min(dp[i-1][0],dp[i-1][1])+1
            elif s[i]=='1':
                dp[i][0]=dp[i-1][0]+1
                dp[i][1]=min(dp[i-1][0],dp[i-1][1])
        
        return min(dp[-1])