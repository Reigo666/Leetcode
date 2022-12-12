class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x:(x[1]-x[0]))
        #print(costs)
        n=len(costs)//2
        ans=0
        for i in range(n):
            ans+=costs[i][1]
        for i in range(n,len(costs)):
            ans+=costs[i][0]
        return ans


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