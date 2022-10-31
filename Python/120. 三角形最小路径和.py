
import collections
from typing import  List,Optional
import copy

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n=len(triangle)
        pre=[0]*n
        cur=[0]*n
        pre[0]=triangle[0][0]
        for i in range(1,n):
            for j in range(len(triangle[i])):
                if j==0:
                    cur[j]=pre[j]+triangle[i][j]
                elif j==len(triangle[i])-1:
                    cur[j]=pre[j-1]+triangle[i][j]
                else:
                    cur[j]=min(pre[j-1],pre[j])+triangle[i][j]
            pre=copy.deepcopy(cur)
        return min(pre)

sol=Solution()
triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
print(sol.minimumTotal(triangle))



# 输入：triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
# 输出：11

