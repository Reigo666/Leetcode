
import collections
from typing import  List,Optional
import copy


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m=len(matrix)
        n=len(matrix[0])
        colarr=[1]*n
        rowarr=[1]*m
        for i in range(m):
            rowvis=0
            for j in range(n):
                if matrix[i][j]==0:
                    if rowvis==0:
                        rowarr[i]=0
                        rowvis=1
                    colarr[j]=0
        
        for i in range(m):
            if rowarr[i]==0:
                for j in range(n):
                    matrix[i][j]=0
        for j in range(n):
            if colarr[j]==0:
                for i in range(m):
                    matrix[i][j]=0
                    
sol=Solution()
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
print(sol.setZeroes(matrix))

# 输入：matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# 输出：[[0,0,0,0],[0,4,5,0],[0,3,1,0]]

