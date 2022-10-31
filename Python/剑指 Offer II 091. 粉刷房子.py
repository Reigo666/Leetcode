import collections
from typing import  List,Optional
import copy
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        dp=[[2**31-1]*len(costs[0]) for i in range(len(costs))]
        for color in range(3):
            dp[0][color]=costs[0][color]
        for i in range(1,len(costs)):
            for color in range(3):
                for selcolor in range(3):
                    if selcolor!=color:
                        dp[i][color]=min(dp[i][color],dp[i-1][selcolor]+costs[i][color])
        return min(dp[len(costs)-1][0],dp[len(costs)-1][1],dp[len(costs)-1][2])