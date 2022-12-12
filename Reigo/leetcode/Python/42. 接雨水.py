
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        lens=len(height)
        #初始化每一列左最高高度
        max_left=[]
        for i in range(lens):
            if i==0:
                max_left.append(0)
            else:
                max_left.append(max(max_left[i-1],height[i-1]))

        #初始化每一列右最高高度
        max_right=[0]*lens
        for i in range(lens-1,-1,-1):
            if i!=lens-1: 
                max_right[i]=(max(max_right[i+1],height[i+1]))

        ans=0
        for i in range(1,lens-1):
            if max_left[i]>height[i] and max_right[i]>height[i]:
                ans+=min(max_left[i],max_right[i])-height[i]
        
        return ans