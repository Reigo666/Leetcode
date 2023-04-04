# import List from typing
from typing import List
from math import inf
class Solution:
    def mergeStones(self, stones: List[int], K: int) -> int:
        #k=2 2,3,4,5,6
        #k=3 3,5,7,9
        #k=4 4,7,10
        #K=5 5 9
        n=len(stones)
        if (n-1)%(K-1)!=0:
            return -1
        #(j-i)%(K-1)==0

        presum=[0]
        for i in range(n):
            presum.append(presum[-1]+stones[i])

        #i到j最多能分成K堆
        dp=[[[inf]*(K+1) for _ in range(n)] for __ in range(n)]

        #初始化 自己分成1堆需要0的花费
        for i in range(n):
            dp[i][i][1]=0
        
        #目标数 dp[0][n-1][1] 将0到n-1分成1堆需要的花费
        #分成1堆之前的一步为将i到j的K堆合并为1堆 即dp[i][j][1]=dp[i][j][K]+sum(i,j)
        #dp[i][j][K]用min(dp[i][h][1]+dp[h+1][j])可计算

        #从i到j
        for j in range(n):
            for i in range(j-1,-1,-1):
                for k in range(2,min(K+1,j-i+2)):
                    #(i,h)成1堆 每次要加K-1
                    for h in range(i,j,K-1):
                        dp[i][j][k]=min(dp[i][j][k],dp[i][h][1]+dp[h+1][j][k-1])
                
                #print(dp[i][j][K])
                if (j-i)%(K-1)==0:
                    dp[i][j][1]=dp[i][j][K]+presum[j+1]-presum[i]
            #print(dp)
        #print(dp[1][2][2])
        for i in range(n-1):
            print(i,i+1,2,dp[i][i+1][2])
        print(dp[0][4][1])
        return dp[0][n-1][1]
    

sol=Solution()
stones=[1,2,3,4,5,6,7]
K=3
print(sol.mergeStones(stones,K))