class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        dp=[[0]*(len(piles)+1) for _ in range(len(piles))]

        for i in range(len(piles)-1,-1,-1):
            for j in range(len(piles),0,-1):
                if i==len(piles)-1:
                    dp[i][j]=piles[i]
                else:
                    for k in range(1,min(2*j,len(piles))+1):
                        if i+k>=len(piles):
                            break
                        dp[i][j]=max(dp[i][j],dp[i+k][max(j,k)])
        print(dp)
        return dp[0][1]