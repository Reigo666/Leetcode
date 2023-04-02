class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        # if len(values)==3:
        #     return values[0]*values[1]*values[2]
        
        n=len(values)
        dp=[[inf]*n for _ in range(n)]
        for j in range(n):
            for i in range(j,-1,-1):
                if j-i<=1:
                    dp[i][j]=0
                    continue
                for k in range(i+1,j):
                    dp[i][j]=min(dp[i][j],dp[i][k]+values[i]*values[k]*values[j]+dp[k][j])
        
        return dp[0][n-1]
                