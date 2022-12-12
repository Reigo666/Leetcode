class Solution:
    def trap(self, height: List[int]) -> int:
        height=[0]+height+[0]
        n=len(height)
        left=[0]*n
        right=[0]*n
        for i in range(1,n):
            left[i]=max(left[i-1],height[i])
        
        ans=0
        for i in range(n-2,0,-1):
            right[i]=max(right[i+1],height[i])
            temp=min(right[i+1],left[i-1])
            if temp>height[i]:
                ans+=temp-height[i]
        return ans
        



        