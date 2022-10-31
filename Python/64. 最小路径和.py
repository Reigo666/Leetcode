
import collections
from typing import  List,Optional
import copy


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])

        dp=[[0]*n for i in range(m)]
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    dp[0][0]=grid[i][j]
                elif i==0:
                    dp[i][j]=dp[i][j-1]+grid[i][j]
                elif j==0:
                    dp[i][j]=dp[i-1][j]+grid[i][j]
                else:
                    dp[i][j]=min(dp[i-1][j],dp[i][j-1])+grid[i][j]
        return dp[m-1][n-1]
sol=Solution()
grid = [[1,3,1],[1,5,1],[4,2,1]]
print(sol.minPathSum(grid))

# 输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
# 输出：7


