import collections
from typing import  List,Optional
import copy
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m=len(grid)
        n=len(grid[0])
        all_direct=[[0,1],[0,-1],[1,0],[-1,0]]
        def dfs(i,j):
            grid[i][j]="0"
            for direct in all_direct:
                tx,ty=i+direct[0],j+direct[1]
                if tx>=0 and tx<m and ty>=0 and ty<n and grid[tx][ty]=="1":             
                    dfs(tx,ty)
        ans=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1':
                    ans+=1
                    dfs(i,j)
        return ans