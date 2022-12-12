class Solution:
    def maximalRectangle(self, matrix: List[str]) -> int:
        m=len(matrix)
        if m==0:
            return 0
        n=len(matrix[0])
        #print(m,n)
        #return 1
        dp=[[0]*n for _ in range(m)]
        ans=0

        for i in range(m):
            for j in range(n):
                if matrix[i][j]=='1':
                    if i>=1:
                        dp[i][j]=dp[i-1][j]+1
                    else:
                        dp[i][j]=1
                
                height=dp[i][j]
                for k in range(j,-1,-1):
                    if matrix[i][j]=='0':
                        break
                    height=min(height,dp[i][k])
                    ans=max(ans,height*(j-k+1))
        
        return ans