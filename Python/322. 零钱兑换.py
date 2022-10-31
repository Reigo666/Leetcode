import collections
from typing import  List,Optional
import copy
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        dp=[[0]*(amount+1) for i in range(len(coins))]
        for j in range(1,amount+1):
            if j-coins[0]>=0 and dp[0][j-coins[0]]!=-1:    
                dp[0][j]=dp[0][j-coins[0]]+1
            else:
                dp[0][j]=-1
        
        for i in range(1,len(coins)):
            for j in range(1,amount+1):
                if j-coins[i]>=0:
                    if dp[i][j-coins[i]]==-1:
                        dp[i][j]=dp[i-1][j]
                    elif dp[i][j-coins[i]]!=-1:
                        if dp[i-1][j]==-1:
                            dp[i][j]=dp[i][j-coins[i]]+1
                        else:
                            dp[i][j]=min(dp[i-1][j],dp[i][j-coins[i]]+1)
                else:
                    dp[i][j]=dp[i-1][j]
        #print(dp)
        return dp[len(coins)-1][amount]
sol=Solution()
coins=[83,186,408,419]
amount=6249
print(sol.coinChange(coins,amount))                  