
from typing import List,Optional

class Solution:
    
    def rotate(self, matrix: List[List[int]]) -> None:
        n=len(matrix)
        for i in range(n//2):
            for j in range((n+1)//2):
                temp=matrix[i][j]
                matrix[i][j]=matrix[n-1-j][i]
                matrix[n-1-j][i]=matrix[n-1-i][n-1-j]
                matrix[n-1-i][n-1-j]=matrix[j][n-1-i]
                matrix[j][n-1-i]=temp

        
sol=Solution()
matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
nums2 = [2,2,1,1]
print(matrix1)
sol.rotate(matrix1)
print(matrix1)

# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[[7,4,1],[8,5,2],[9,6,3]]

