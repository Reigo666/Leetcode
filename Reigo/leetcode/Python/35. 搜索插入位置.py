from typing import List,Optional

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def left_func(target,nums):
            l=0
            r=len(nums)-1
            while l<=r:
                mid=((r-l)>>1)+l
                if nums[mid]>=target:
                    r=mid-1

                elif nums[mid]<target:
                    l=mid+1
            return l
        return left_func(target,nums)
sol=Solution()

nums1 = [1,3,5,6]
target1 = 5
print(sol.searchInsert(nums1,target1))

# 输入: nums = [1,3,5,6], target = 5
# 输出: 2