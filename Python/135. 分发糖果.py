
import collections
from typing import  List,Optional
import copy

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n=len(ratings)
        if n==1:
            return 1
        lefthigh=[0]*n
        righthigh=[0]*n
        lastrating=ratings[0]
        for i in range(n):
            if i==0:
                lefthigh[0]=1
            else:
                if ratings[i]>lastrating:
                    lefthigh[i]=lefthigh[i-1]+1
                else:
                    lefthigh[i]=1
                lastrating=ratings[i]
        for i in range(n-1,-1,-1):
            if i==n-1:
                righthigh[i]=1
            else:
                if ratings[i]>lastrating:
                    righthigh[i]=righthigh[i+1]+1
                else:
                    righthigh[i]=1
                lastrating=ratings[i]
        ans=0
        for i in range(n):
            ans+=max(lefthigh[i],righthigh[i])
        return ans

        
        
sol=Solution()
#ratings = [1,0,2]
ratings = [1,2,2]
print(sol.candy(ratings))



# 输入：ratings = [1,0,2]
# 输出：5


