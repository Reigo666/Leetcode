
import collections
from typing import  List,Optional
import copy

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        lenn=len(nums)
        l=0
        r=lenn-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                return True
            elif nums[mid]==nums[l] and nums[mid]==nums[r]:
                l+=1
            elif nums[mid]>=nums[l]:
                if nums[mid]>target and target>=nums[l]:
                    r=mid-1
                else:
                    l=mid+1
            elif nums[mid]<=nums[l]:
                if nums[mid]<target and target<=nums[r]:
                    l=mid+1
                else:
                    r=mid-1
        return False


    def search1(self, nums: List[int], target: int) -> bool:
        lenn=len(nums)
        l=0
        r=lenn-1
        while l<=r:
            mid =(l+r)//2
            if nums[mid]==target:
                return True
            elif nums[mid]==nums[l] and nums[mid]==nums[r]:
                for i in range(l+1,r):
                    if nums[i]==target:
                        return True
                return False
            elif nums[mid]>=nums[l] and nums[mid]<=nums[r]:
                if nums[mid]>target:
                    r=mid-1
                else:
                    l=mid+1
            elif nums[mid]>=nums[l] and nums[mid]>=nums[r]:
                if target>=nums[l] and target<nums[mid]:
                    r=mid-1
                else:
                    l=mid+1
            elif nums[mid]<=nums[l] and nums[mid]<=nums[r]:
                if target<=nums[r] and target>nums[mid]:
                    l=mid+1
                else:
                    r=mid-1
        return False
sol=Solution()
nums = [2,5,6,0,0,1,2]
nums1 =[1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1]
target = 2

print(sol.search(nums1,target))


# 输入：nums = [2,5,6,0,0,1,2], target = 0
# 输出：true

