import collections
from typing import  List,Optional
import copy
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m=len(dungeon)
        n=len(dungeon[0])
        
        needinithp=[[0]*n for i in range(m)]
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if i==m-1 and j==n-1:
                    needinithp[i][j]=max(0,-dungeon[i][j])
                elif i==m-1:
                    needinithp[i][j]=max(0,needinithp[i][j+1]-dungeon[i][j])
                elif j==n-1:
                    needinithp[i][j]=max(0,needinithp[i+1][j]-dungeon[i][j])
                else:
                    needinithp[i][j]=max(0,min(needinithp[i][j+1],needinithp[i+1][j])-dungeon[i][j])
                #+3 5
                #0
        return needinithp[0][0]+1
sol=Solution()
dungeon=[[-2,-3,3],[-5,-10,1],[10,30,-5]]

print(sol.calculateMinimumHP(dungeon))