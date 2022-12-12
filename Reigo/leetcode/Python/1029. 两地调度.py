class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n=len(costs)//2
        dp=[[inf]*(n+1) for _ in range(n+1)]

        dp[0][0]=0
        for i in range(len(costs)):
            for j in range(i+2):
                if j>n:
                    continue
                k=i+1-j
                if k>n:
                    continue
                #print(j,k)
                if k==0:
                    dp[j][k]=min(dp[j][k],dp[j-1][k]+costs[i][0])
                elif j==0:
                    dp[j][k]=min(dp[j][k],dp[j][k-1]+costs[i][1])
                else:
                    dp[j][k]=min(dp[j][k-1]+costs[i][1],dp[j-1][k]+costs[i][0])
            #print(dp)
        return dp[n][n]


        # def dfs(costs,allcost,lefta,leftb):
        #     nonlocal ans
        #     if allcost>ans:
        #         return
        #     if len(costs)==0:
        #         ans=min(ans,allcost)
        #         return
        #     if lefta:
        #         dfs(costs[1:],allcost+costs[0][0],lefta-1,leftb)
        #     if leftb:
        #         dfs(costs[1:],allcost+costs[0][1],lefta,leftb-1)
        # n=len(costs)//2
        # ans=0
        # for i in range(n):
        #     ans+=costs[i][0]
        # for i in range(n,len(costs)):
        #     ans+=costs[i][1]
        # dfs(costs,0,n,n)
        # return ans