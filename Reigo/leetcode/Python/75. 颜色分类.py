
import collections
from typing import  List,Optional
import copy

class Solution:
    def sortColors(self, nums: List[int]) -> List[int]:
        l=0
        mid=1
        r=2
        nums.insert(0,3)
        nums.insert(1,4)
        nums.insert(2,5)
        lenn=len(nums)
        for i in range(3,lenn):
            if nums[i]==0:
                nums.insert(l,0)
                l+=1
                mid+=1
                r+=1
            elif nums[i]==1:
                nums.insert(mid,1)
                mid+=1
                r+=1
            elif nums[i]==2:
                nums.insert(r,2)
                r+=1
            nums.pop(i)
            #3,4,5,0,0,1,1,2,2
        nums.pop(r)
        nums.pop(mid)
        nums.pop(l)
        
        return nums

        
sol=Solution()
nums = [2,0,2,1,1,0]
print(sol.sortColors(nums))

# 输入：nums = [2,0,2,1,1,0]
# 输出：[0,0,1,1,2,2]