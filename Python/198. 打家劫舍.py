from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[0]*(n+2)
        ans=nums[0]
        maxpre=0
        for i in range(n):
            dp[i+2]=maxpre+nums[i]
            maxpre=max(dp[i+1],maxpre)
            ans=max(ans,dp[i+2])
        return ans