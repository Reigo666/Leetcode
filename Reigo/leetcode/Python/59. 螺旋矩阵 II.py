
import collections
from typing import  List,Optional
import copy

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        mat=[[0]*n for i in range(n)]
        u=0
        d=n-1
        l=0
        r=n-1
        val=1
        while True:
            for j in range(l,r+1):
                mat[u][j]=val
                val+=1
            u+=1
            if(u>d):break

            for i in range(u,d+1):
                mat[i][r]=val
                val+=1
            r-=1
            if(l>r):break

            for j in range(r,l-1,-1):
                mat[d][j]=val
                val+=1
            d-=1
            if(u>d):break

            for i in range(d,u-1,-1):
                mat[i][l]=val
                val+=1
            l+=1
            if(l>r):break

        return mat


sol=Solution()
n1=3
n2=4
print(sol.generateMatrix(n2))

# 输入：n = 3
# 输出：[[1,2,3],[8,9,4],[7,6,5]]







