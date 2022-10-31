import collections
from typing import  List,Optional
import copy
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        days=len(prices)
        if days==0 or days==1 or k==0:
            return 0
        dpbuy=[-prices[0]]*k
        dpsell=[0]*k
        for i in range(days):
            for j in range(k):
                if j==0:
                    dpbuy[j]=max(dpbuy[j],-prices[i])
                    dpsell[j]=max(dpsell[j],dpbuy[j]+prices[i])
                else:
                    dpbuy[j]=max(dpbuy[j],dpsell[j-1]-prices[i])
                    dpsell[j]=max(dpsell[j],dpbuy[j]+prices[i])
        return dpsell[k-1]
