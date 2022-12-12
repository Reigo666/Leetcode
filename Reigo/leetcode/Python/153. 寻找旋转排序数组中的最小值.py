import collections
from typing import  List,Optional
import copy
class Solution:
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)
        l=0
        r=n-1
        while l<=r:
            mid=(l+r)//2
            nummid=nums[mid]
            numl=nums[l]
            numr=nums[r]
            if nums[l]<=nums[mid] and nums[mid]<=nums[r]:
                return nums[l]
            elif nums[mid]>nums[r]:
                l=mid+1
            elif nums[mid]<nums[l]:
                r=mid
        return 0