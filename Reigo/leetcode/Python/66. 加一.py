
import collections
from typing import  List,Optional
import copy

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1]+=1
        n=len(digits)
        i=n-1
        while i>=1:
            if digits[i]==10:
                digits[i]=0
                digits[i-1]+=1
                i-=1
            else:return digits
        if digits[0]==10:
            digits[0]=0
            digits.insert(0,1)
        return digits
sol=Solution()
digits = [1,2,3]
print(sol.plusOne(digits))
# 输入：digits = [1,2,3]
# 输出：[1,2,4]


