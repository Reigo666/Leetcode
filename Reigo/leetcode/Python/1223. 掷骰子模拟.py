class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        t=max(rollMax)
        __MOD__=10**9+7
        dp=[[[0]*(t+1) for _ in range(6)] for __ in range(n+1)]
        for j in range(6):
            dp[1][j][1]=1
        for i in range(2,n+1):
            for j in range(6):
                for pre in range(6):
                    for k in range(rollMax[pre]+1):
                        if pre!=j:
                            dp[i][j][1]+=dp[i-1][pre][k]
                        else:
                            if k+1<=rollMax[j]:
                                dp[i][j][k+1]+=dp[i-1][pre][k]
        ans=0
        for j in range(6):
            for k in range(rollMax[j]+1):
                ans+=dp[-1][j][k]%__MOD__
        #print(dp)
        return ans%__MOD__


