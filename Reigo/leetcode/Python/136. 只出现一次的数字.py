
import collections
from typing import  List,Optional
import copy

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dict=collections.defaultdict(int)
        n=len(nums)
        for i in range(n):
            dict[nums[i]]+=1
        for key in dict.keys():
            if dict[key]==1:
                return key
        return -1
sol=Solution()
nums=[4,1,2,1,2]
print(sol.singleNumber(nums))


# 输入: [4,1,2,1,2]
# 输出: 4

