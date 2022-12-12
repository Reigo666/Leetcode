from typing import List,Optional

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        #ishave=[0] * 5 * (10**5)
        #print(ishave)
        lens=len(nums)
        ishave=[0]*(lens+2)
        for i in range(lens):
            val=nums[i]
            if val>0 and val<=lens:
                ishave[val]=1
        for i in range(1,lens+2):
            if ishave[i]==0:
                return i
        return 1

sol=Solution()

nums1=[3,4,-1,1]
nums2=[1,2,0]
print(sol.firstMissingPositive(nums2))

# 输入：nums = [3,4,-1,1]
# 输出：2