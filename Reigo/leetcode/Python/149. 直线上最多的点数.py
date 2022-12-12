
import collections
from typing import  List,Optional
import copy

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n=len(points)
        maxans=1
        def gcd(a,b):
            return a if b==0 else gcd(b,a%b)
        for i in range(n):
            hashmap={}
            sx,sy=points[i][0],points[i][1]
            for j in range(i+1,n):
                tx,ty=points[j][0],points[j][1]
                dx=tx-sx
                dy=ty-sy
                if dx==0:
                    num=hashmap.get('infmax',1)
                    hashmap['infmax']=num+1
                    maxans=max(maxans,num+1)
                elif dy==0:
                    num=hashmap.get(0,1)
                    hashmap[0]=num+1
                    maxans=max(maxans,num+1)
                else:
                    gcdxy=gcd(dx,dy)
                    dx//=gcdxy
                    dy//=gcdxy
                    temp=dy/dx
                    num=hashmap.get(temp,1)
                    hashmap[temp]=num+1
                    maxans=max(maxans,num+1)
        return maxans
sol=Solution()
points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
print(sol.maxPoints(points))

# 输入：points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
# 输出：4

