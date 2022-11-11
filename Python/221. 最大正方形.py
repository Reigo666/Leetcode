class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m=len(matrix)
        n=len(matrix[0])
        dp=[[0]*n for _ in range(m)]
        ans=0
        for i in range(m):
            for j in range(n):
                if i==0 or j==0:
                    
                    if matrix[i][j]=='0':
                        dp[i][j]=0
                    else:
                        dp[i][j]=1
                        ans=max(ans,1)
                else:
                    print(i,j)
                    if matrix[i][j]=='1':
                        dp[i][j]=min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])+1
                        ans=max(ans,dp[i][j])
                    else:
                        dp[i][j]=0
            #print(dp)
        return ans*ans