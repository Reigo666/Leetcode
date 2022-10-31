
import collections
from typing import  List,Optional
import copy

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        l=0
        r=m-1
        rowtemp=0
        while l<=r:
            mid=(l+r)//2
            if mid==m-1:
                rowtemp=mid
                break
            if matrix[mid][0]==target or matrix[mid+1][0]==target:
                return True
            elif matrix[mid][0]<target and matrix[mid+1][0]>target:
                  rowtemp=mid
                  break
            elif matrix[mid][0]>target:
                r=mid-1
            elif matrix[mid+1][0]<target:
                l=mid+1
        if r<l:
            return False
        l=0
        r=n-1
        while l<=r:
            mid=(l+r)//2
            if matrix[rowtemp][mid]==target:
                return True
            elif matrix[rowtemp][mid]<target:
                l=mid+1
            elif matrix[rowtemp][mid]>target:
                r=mid-1
        return False

        
sol=Solution()
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 32

matrix1 = [[1]]
target1=1

matrix2=[[1],[3]]
target2=1
print(sol.searchMatrix(matrix2,target2))

# 输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# 输出：true
