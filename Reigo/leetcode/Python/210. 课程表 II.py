import collections
from typing import  List,Optional
import copy
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        dict=defaultdict(list)
        dictto=defaultdict(list)
        for i in range(numCourses):
            dict[i]=[]
        for i in range(len(prerequisites)):
            dict[prerequisites[i][0]].append(prerequisites[i][1])
            dictto[prerequisites[i][1]].append(prerequisites[i][0])

        #print(dict)
        #print(dictto)
        ans=[]
        while True:
            if dict=={}:
                return ans
            valid=False
            for k in dict:
                if dict[k]==[]:
                    valid=True
                    for point in dictto[k]:
                        dict[point].remove(k)
                    ans.append(k)
                    del dict[k]
                    break
            if not valid:
                return []
        return ans
        
        
