class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum1=sum(nums)
        ma=max(nums)
        if sum1%2==1:
            return False
        
        if ma*2>sum1:
            return False
        
        target=sum1//2

        dp=[False]*(target+1)
        dp[0]=True

        for num in nums:
            for j in range(target,num-1,-1):
                dp[j]|=dp[j-num]
        
        return dp[target]
