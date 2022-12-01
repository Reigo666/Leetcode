class Solution:
    def rob(self, nums: List[int]) -> int:
        ans=0
        n=len(nums)
        dp=[[0]*2 for _ in range(n)]


        for i in range(1,n):
            dp[i][0]=max(dp[i-1][0],dp[i-1][1])
            dp[i][1]=dp[i-1][0]+nums[i]
        print(dp)
        ans=max(dp[-1][0],dp[-1][1])
        
        dp=[[0]*2 for _ in range(n)]
        dp[0][0]=0
        dp[0][1]=nums[0]
        for i in range(1,n-1):
            dp[i][0]=max(dp[i-1][0],dp[i-1][1])
            dp[i][1]=dp[i-1][0]+nums[i]
        
        print(dp)
        ans=max(ans,nums[0])
        if len(dp)>=2:
            ans=max(ans,dp[-2][0],dp[-2][1])
        return ans
