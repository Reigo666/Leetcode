
import collections
from typing import  List,Optional
import copy


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex==0:
            return [1]
        elif rowIndex==1:
            return [1,1]
        temp=[1,1]
        cur=temp
        for i in range(rowIndex-1):
            cur=[1,1]
            for j in range(len(temp)-1):         
                cur.insert(-1,temp[j]+temp[j+1])
            temp=cur     
        return temp
sol=Solution()
n=5
print(sol.getRow(n))




# 输入：s = "babgbag", t = "bag"
# 输出：5


