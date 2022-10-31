import collections
from typing import  List,Optional
import copy
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n=len(nums)
        l=0
        r=0
        tempmult=nums[0]
        ans=0
        while r<n:
            if tempmult<k:
                ans+=r-l+1
                r+=1
                if r>=n:
                    break
                tempmult*=nums[r]
            else:
                tempmult//=nums[l]
                l+=1
                if l>r:
                    r=l
                    if r<n:
                        tempmult=nums[r]
        return ans
                