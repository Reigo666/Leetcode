from math import inf
from typing import List


class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        factory.sort()
        robot.sort()
        
        m=len(factory)
        n=len(robot)

        dp=[[inf]*(n+1) for _ in range(m+1)]


        def cost(i,j,k):
            if k==0:
                return 0
            pos=factory[i][0]
            res=0
            for p in range(k):
                res+=abs(pos-robot[j-p])
            #print(i,j,k,res)
            return res
        for i in range(len(factory)):
            pos,limit=factory[i]
            for j in range(len(robot)):
                if j==0:
                    dp[i][j]=0
                temp=0
                for k in range(min(j+1+1,limit+1)):
                    dp[i+1][j+1]=min(dp[i+1][j+1],dp[i][j-k+1]+temp)
                    temp+=abs(pos-robot[j-k])
                    #print(dp)
        return dp[m][n]

sol=Solution()
robot=[0,4,6]
factory=[[2,2],[6,2]]
print(sol.minimumTotalDistance(robot,factory))
