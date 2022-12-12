
import collections
from typing import  List,Optional
import copy

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        lenn=len(heights)
        maxheight=0
        for i in range(lenn):
            if i==0:
                stack.append(i)
                maxheight=heights[i]
            else:
                nowheight=heights[i]
                if stack and nowheight<heights[stack[-1]]:
                    while stack and heights[stack[-1]]>nowheight:
                        #idx是栈顶索引
                        h=heights[stack.pop()]
                        idx=stack[-1] if stack else -1
                        maxheight=max(maxheight,(i-idx-1)*h) 
                stack.append(i)
                if i==lenn-1:
                    idr=lenn
                    while stack:
                        h=heights[stack.pop()]
                        idl=stack[-1] if stack else -1
                        maxheight=max(maxheight,(idr-idl-1)*h) 
        return maxheight

    def calculateMaxRectangle(self,height:List[int])->int:
            stack=[0]
            height.insert(0,0)
            height+=[0]
            n=len(height)
            lastheight=0
            ans=0
            for i in range(1,n):
                h=height[i]
                if h<lastheight:
                    idr=i
                    while lastheight>h:
                        stack.pop()
                        idl=stack[-1]
                        ans=max(ans,lastheight*(idr-idl-1))
                        lastheight=height[stack[-1]]
                    lastheight=h
                    stack.append(i)
                else:
                    lastheight=h 
                    stack.append(i)
            return ans

        
sol=Solution()
heights = [2,1,5,6,2,3]
print(sol.largestRectangleArea(heights))
print(sol.calculateMaxRectangle(heights))

# 输入：heights = [2,1,5,6,2,3]
# 输出：10
# 解释：最大的矩形为图中红色区域，面积为 10
