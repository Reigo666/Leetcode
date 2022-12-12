class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        prefix=[nums[0]]
        for i in range(1,len(nums)):
            prefix.append(prefix[i-1]+nums[i])
        
        #print(prefix)

        n=len(nums)

        dp=[[0]*(k+1) for _ in range(n)]
    
        for i in range(n):
            dp[i][1]=prefix[i]/(i+1)
        
        #print(dp)
        for i in range(n):
            for j in range(2,k+1):
                for x in range(i):
                    dp[i][j]=max(dp[i][j],dp[x][j-1]+(prefix[i]-prefix[x])/(i-x))
        
        #print(dp)
        return dp[n-1][k]