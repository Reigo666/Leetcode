class Solution:
    def numTilings(self, n: int) -> int:
        dp=[[0]*4 for _ in range(n+1)]
        __MOD__=10**9 + 7
        dp[0][3]=1
        for i in range(1,n+1):
            dp[i][0]=dp[i-1][3]%__MOD__
            dp[i][1]=(dp[i-1][0]+dp[i-1][2])%__MOD__
            dp[i][2]=(dp[i-1][0]+dp[i-1][1])%__MOD__
            dp[i][3]=(dp[i-1][3]+dp[i-1][0]+dp[i-1][1]+dp[i-1][2])%__MOD__
        
        return dp[n][3]%__MOD__