import collections
from typing import  List,Optional
import copy
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums)<2:
            return 0
        n=len(nums)
        nums.sort()
        maxgap=0
        for i in range(n-1):
            tempgap=nums[i+1]-nums[i]
            maxgap=max(maxgap,tempgap)
        return maxgap