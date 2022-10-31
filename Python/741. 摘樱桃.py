import collections
from typing import  List,Optional
import copy
import numpy as np

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n=len(grid)
        for i in range(n):
            grid[i].insert(0,-1)
        grid.insert(0,[-1]*(n+1)) 
        #初始化全为-1
        dp=(np.ones((2*n+1,n+1,n+1))*-1).tolist()

        dp[2][1][1]=grid[1][1]
        for k in range(3,2*n+1):
            for i1 in range(1,n+1):
                j1=k-i1
                if j1>=n+1:
                    continue
                if grid[i1][j1]==-1:
                    continue
                for i2 in range(1,n+1):
                    j2=k-i2
                    #注意越界
                    if j2>=n+1:
                        continue
                    #两个点之一 都不能从-1的地方走
                    if grid[i2][j2]==-1:
                        continue
                    else:
                        m=int(max(dp[k-1][i1-1][i2],dp[k-1][i1][i2-1],dp[k-1][i1-1][i2-1],dp[k-1][i1][i2]))
                        #如果前四种走法都不可达
                        if m<0:
                            dp[k][i1][i2]=-1
                            continue
                        dp[k][i1][i2]=m+grid[i1][j1]+grid[i2][j2]
                        if i1==i2 and grid[i1][j1]==1:
                            dp[k][i1][i2]-=1
        if dp[2*n][n][n]==-1:
            return 0
        return dp[2*n][n][n]
        print(123)
        
        
        return 0
sol=Solution()
# grid =\
# [[0, 1, -1],
#  [1, 0, -1],
#  [1, 1,  1]]
grid=\
[[1,1,-1],
 [1,-1,1],
 [-1,1,1]]

grid2 =\
 [[1,-1,1,-1,1,1,1,1,1,-1],
  [-1,1,1,-1,-1,1,1,1,1,1],
  [1,1,1,-1,1,1,1,1,1,1],
  [1,1,1,1,1,1,1,1,1,1],
  [-1,1,1,1,1,1,1,1,1,1],
  [1,-1,1,1,1,1,-1,1,1,1],
  [1,1,1,-1,1,1,-1,1,1,1],
  [1,-1,1,-1,-1,1,1,1,1,1],
  [1,1,-1,-1,1,1,1,-1,1,-1],
  [1,1,-1,1,1,1,1,1,1,1]]
print(sol.cherryPickup(grid2))
grid1 =\
[[1,1,1,1,0,0,0],
 [0,0,0,1,0,0,0],
 [0,0,0,1,0,0,1],
 [1,0,0,1,0,0,0],
 [0,0,0,1,0,0,0],
 [0,0,0,1,0,0,0],
 [0,0,0,1,1,1,1]]
