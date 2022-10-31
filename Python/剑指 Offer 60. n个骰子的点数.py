class Solution:
    def dicesProbability(self, n: int) -> List[float]:
        dp=[0]*(6*n+1)
        for i in range(1,7):
            dp[i]=1
        for i in range(2,n+1):
            #print(dp)
            for j in range(6*i,i-1,-1):
                dp[j]=sum(dp[max(i-1,j-6):j])
            print(dp)
        mult=1/(6**n)
        for i in range(n,6*n+1):
            dp[i]*=mult
        return dp[n:6*n+1]