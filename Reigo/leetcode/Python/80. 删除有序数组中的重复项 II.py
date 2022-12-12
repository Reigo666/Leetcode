
import collections
from typing import  List,Optional
import copy

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        lenn=len(nums)
        l=1
        tempadd=1
        tempnum=nums[0]
        ans=1
        for i in range(1,lenn):
            if tempnum==nums[i]:
                tempadd+=1
                ans+=1
                if tempadd>2:
                    ans-=1
                else:
                    nums[l]=tempnum
            else:
                tempnum=nums[i]
                tempadd=1
                ans+=1
                nums[l]=tempnum
        return ans  


sol=Solution()
nums = [1,1,1,2,2,3]

print(sol.removeDuplicates(nums))

# 输入：nums = [1,1,1,2,2,3]
# 输出：5, nums = [1,1,1,1,2,2,3]
# 解释：函数应返回新长度 length = 5, 并且原数组的前五个元素被修改为 1, 1, 2, 2, 3 。 不需要考虑数组中超出新长度后面的元素。

