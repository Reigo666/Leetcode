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
            if l==r:
                return nums[l]
            elif l==mid:
                return min(nums[l],nums[r])
            elif nums[l]<nums[mid] and nums[mid]<nums[r]:
                return nums[l]
            elif nums[mid]<nums[l]:
                r=mid
            elif nums[mid]>nums[r]:
                l=mid+1
            elif nums[l]==nums[mid] and nums[mid]==nums[r]:
                l+=1
            else:
                if nums[l]==nums[mid]:
                    if nums[mid]>nums[r]:
                        l=mid+1
                    if nums[mid]<nums[r]:
                        r=mid-1
                elif nums[mid]==nums[r]:
                    if nums[mid]>nums[l]:
                        r=mid-1
                    if nums[mid]<nums[l]:
                        l=mid+1
                else:
                    print("error")
        return 0