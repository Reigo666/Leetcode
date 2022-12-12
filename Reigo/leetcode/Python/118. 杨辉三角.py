
import collections
from typing import  List,Optional
import copy

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==1:
            return [[1]]
        ans=[[1]]
        for i in range(numRows-1):
            temp=[1,1]
            for j in range(len(ans[i])-1):
                temp.insert(1,ans[i][j]+ans[i][j+1])
            ans.append(temp)
        return ans
sol=Solution()
n=5
print(sol.generate(n))




# 输入：s = "babgbag", t = "bag"
# 输出：5


