import collections
from typing import  List,Optional
import copy
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        r=0
        sum=nums[0]
        ans=2**31-1
        while l<len(nums):
            if sum<target:
                r+=1
                if r>=len(nums):
                    break
                sum+=nums[r]
            elif sum>=target:
                ans=min(ans,r-l+1)
                if ans==1:
                    return 1
                sum-=nums[l]
                l+=1
        if ans==(2**31-1):
            return 0
        return ans      
