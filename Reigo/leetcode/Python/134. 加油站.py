
import collections
from typing import  List,Optional
import copy

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n=len(gas)
        leftgas=[0]*n
        minleftgas=0
        minleftgasidx=0
        for i in range(n):
            if i>=1:
                leftgas[i]=leftgas[i-1]+gas[i]-cost[i]
                if leftgas[i]<minleftgas:
                    minleftgas=leftgas[i]
                    minleftgasidx=i
            else:
                leftgas[0]=gas[i]-cost[i]
                minleftgas=leftgas[0]
        if leftgas[n-1]<0:
            return -1
        
        return minleftgasidx+1 if minleftgasidx!=n-1 else 0
        

sol=Solution()
gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
print(sol.canCompleteCircuit(gas,cost))


# 输入: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
# 输出: 3



