
import collections
from typing import  List,Optional
import copy
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def takeFirst(elem):
            return elem[0]
        intervals.sort(key=takeFirst)
        n=len(intervals)
        ans=[]
        ans.append(intervals[0])
        lastpos=0
        for i in range(1,n):
            if intervals[i][0]<=ans[lastpos][1]:
                ans[lastpos][1]=max(intervals[i][1],ans[lastpos][1])
            elif intervals[i][0]>ans[lastpos][1]:
                ans.append(intervals[i])
                lastpos+=1
        #print(intervals)
        return ans
sol=Solution()
intervals = [[2,6],[1,3],[8,10],[15,18]]

print(sol.merge(intervals))



# 输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
# 输出：[[1,6],[8,10],[15,18]]
# 解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].





