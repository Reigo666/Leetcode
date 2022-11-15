class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        s=[0]
        ans=0
        heights=[0]+heights
        for i in range(1,len(heights)):
            while s and heights[s[-1]]>heights[i]:
                idx=s.pop()
                ans=max(ans,heights[idx]*(i-s[-1]-1))
            s.append(i)
        while len(s)>1:
            idx=s.pop()
            ans=max(ans,heights[idx]*(len(heights)-s[-1]-1))
        return ans