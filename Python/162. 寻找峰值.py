import collections
from typing import  List,Optional
import copy
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n=len(nums)
        l=0
        r=n-1
        while l<=r:
            if l==r:
                return l
            else:
                mid=(l+r)//2
                if nums[mid+1]>nums[mid]:
                    l=mid+1
                elif nums[mid+1]<nums[mid]:
                    r=mid
        return l
