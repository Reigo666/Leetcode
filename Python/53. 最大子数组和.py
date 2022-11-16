class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans=nums[0]
        pre=0
        for num in nums:
            pre=max(num,num+pre)
            ans=max(ans,pre)
        return ans