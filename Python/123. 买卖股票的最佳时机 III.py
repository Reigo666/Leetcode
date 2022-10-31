

import collections
from typing import  List,Optional
import copy
class Solution:
    #动态规划 O(n)
    def maxProfit(self, prices: List[int]) -> int:
        #buy1,sell1,buy2,sell2均为最大利益
        #buy2指在sell1之后对当天进行购买
        buy1=-prices[0]
        sell1=0
        buy2=-prices[0]
        sell2=0
        for i in range(1,len(prices)):
            buy1=max(buy1,-prices[i])
            sell1=max(sell1,buy1+prices[i])
            buy2=max(buy2,sell1-prices[i])
            sell2=max(sell2,buy2+prices[i])
        return sell2
    #动态规划 O(n2)超时
    def maxProfit1(self, prices: List[int]) -> int:
        n=len(prices)
        dp=[[0]*n for i in range(n)]
        for j in range(n):
            for i in range(j,-1,-1):
                if j==i:
                    dp[i][j]==0
                elif j-i==1:
                    if prices[i]<prices[j]:
                        dp[i][j]=prices[j]-prices[i]
                    else:
                        dp[i][j]==0
                else:
                    maxprofit=max(0,prices[j]-prices[i])                 
                    maxprofit=max(maxprofit,dp[i+1][j],dp[i][j-1])
                    dp[i][j]=maxprofit
        ans=0
        for k in range(0,n-1):
            ans=max(ans,dp[0][k]+dp[k+1][n-1])
        return ans
                
sol=Solution()
nums = [3,3,5,0,0,3,1,4]
print(sol.maxProfit(nums))