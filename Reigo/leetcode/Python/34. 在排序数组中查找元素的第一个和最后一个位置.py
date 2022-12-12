from typing import List,Optional

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if nums==[]:
            return [-1,-1]
        
        #找到最左面的target值
        def left_func(target,nums):
            l=0
            r=len(nums)-1
            while(l<=r):
                mid=((r-l)>>1)+l
                if nums[mid]>=target:
                    r=mid-1
                elif nums[mid]<target:
                    l=mid+1
            return l

        #找到最左面的target值
        a=left_func(target,nums)
        #找到第一个比target大的值的位置
        b=left_func(target+1,nums)
        if a!=len(nums) and nums[a]==target:
            return [a,b-1]
        else:
            return [-1,-1]
        

sol=Solution()

nums1 = [5,7,7,8,8,10]
target1 = 8
print(sol.searchRange(nums1,target1))


# 输入：nums = [5,7,7,8,8,10], target = 8
# 输出：[3,4]