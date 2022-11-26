class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        l=0
        ans=[]
        while l<len(intervals):
            start,end=intervals[l]
            l+=1
            while l<len(intervals) and intervals[l][0]<=end:
                end=max(end,intervals[l][1])
                l+=1
            ans.append([start,end])
        return ans
            