class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        ans=0
        
        dp=[[1]*1001 for _ in range(len(nums))]
        for j in range(1,len(nums)):
            #i只能从前向后遍历 否则dp[j][diff]更新时需要考虑相同diff时最大的情况 正向遍历一定最大
            for i in range(j):       
                diff=nums[j]-nums[i]
                diff+=500
                # if diff<0:
                #     diff=500-diff
                dp[j][diff]=dp[i][diff]+1
                ans=max(ans,dp[j][diff])
        return ans