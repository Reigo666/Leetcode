
import collections
from typing import  List,Optional
import copy


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        dp=[[0]*n for i in range(m)]
        if obstacleGrid[m-1][n-1]==1 or obstacleGrid[0][0]==1:
            return 0
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j]==1:
                    dp[i][j]=0
                    continue
                if i==0 and j==0 and obstacleGrid[i][j]==0:
                    dp[i][j]=1
                elif j==0:
                    if obstacleGrid[i-1][j]==0:
                        dp[i][j]=dp[i-1][j]
                    else:dp[i][j]=0
                elif i==0:
                    if obstacleGrid[i][j-1]==0:
                        dp[i][j]=dp[i][j-1]
                    else:dp[i][j]=0
                else:
                    if obstacleGrid[i][j-1]==1 and obstacleGrid[i-1][j]==0:
                        dp[i][j]=dp[i-1][j]
                    elif obstacleGrid[i][j-1]==0 and obstacleGrid[i-1][j]==1:
                        dp[i][j]=dp[i][j-1]
                    elif obstacleGrid[i][j-1]==1 and obstacleGrid[i-1][j]==1:
                        dp[i][j]=0
                    else:
                        dp[i][j]=dp[i][j-1]+dp[i-1][j]
        return dp[m-1][n-1]
sol=Solution()
obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
print(sol.uniquePathsWithObstacles(obstacleGrid))


# 输入：obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
# 输出：2



