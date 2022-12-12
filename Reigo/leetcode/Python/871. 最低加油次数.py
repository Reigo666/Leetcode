import collections
from typing import  List,Optional
import copy
import heapq
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        heap=[]
        i=0
        ans=0
        while startFuel<target:
            while i<len(stations) and startFuel>=stations[i][0]:
                heapq.heappush(heap,-stations[i][1])
                i+=1
            if not heap:
                return -1
            m=heapq.heappop(heap)
            print(m)
            startFuel-=m
            ans+=1
        return ans