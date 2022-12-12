
import collections
from typing import  List,Optional
import copy

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==1:
            return 0
        buyinprice=prices[0]
        profit=0
        for i in range(1,len(prices)):
            if prices[i]>buyinprice:
                profit=max(profit,prices[i]-buyinprice)
            else:
                buyinprice=prices[i]
        return profit