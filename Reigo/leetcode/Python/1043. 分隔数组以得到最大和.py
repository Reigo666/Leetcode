class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        #1 15 14 1 1
        #15 15 14 14 14

        n=len(arr)
        dp=[0]*n

        dp[0]=arr[0]
        curmax=arr[0]
        for i in range(k):
            curmax=max(curmax,arr[i])
            dp[i]=curmax*(i+1)
        #print(dp)
        for i in range(k,n):
            curmax=arr[i]
            for j in range(k):
                curmax=max(curmax,arr[i-j])
                dp[i]=max(dp[i],dp[i-j-1]+curmax*(j+1))
            #print(dp)
        return dp[-1]