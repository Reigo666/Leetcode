import collections
from typing import  List,Optional
import copy
class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        ans=0
        
        if startPos>endPos:
            startPos,endPos=endPos,startPos
        dert=endPos-startPos

        if (k-dert)%2!=0:
            return 0
        
        startPos=(k-dert)//2
        endPos=startPos+dert

        dp=[[[0]*k for i in range(startPos+endPos)] for j in range(startPos+endPos)]

        print(dp)

        #dp[startPos][endPos][k]
        
        return ans%(10**9 + 7 )
        
sol=Solution()
startPos = 1
endPos = 2
k = 3
print(sol.numberOfWays(startPos,endPos,k))