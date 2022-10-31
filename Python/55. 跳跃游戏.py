
import collections
from typing import  List,Optional
import copy
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        if n==1:
            return True
        if nums[0]==0:
            return False
        l=1
        r=nums[0]
        while True:
            maxr=nums[0]
            for i in range(l,r+1):
                if nums[i]+i>maxr:
                    maxr=nums[i]+i
            if maxr>=n:
                return True
            if r==maxr:
                return False
            l=r+1
            r=maxr


    def canJump1(self, nums: List[int]) -> bool:
        n=len(nums)
        if n==1:
            return True
        canjump=[0]*n
        minpos=n-1
        for i in range(n-2,-1,-1):
            if minpos-i<=nums[i]:
                minpos=i
        return False if minpos else True

sol=Solution()
nums = [2,3,1,1,4]
nums1 = [3,2,1,0,4]
print(sol.canJump(nums))



# 输入：nums = [2,3,0,1,4]
# 输出：true
# 解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。



