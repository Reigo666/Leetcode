from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        height=[-1]+height+[-1]
        ms=[]
        ans=0
        for i in range(len(height)):
            if not ms:
                ms.append(i)
            else:
                while ms and height[ms[-1]]<=height[i]:
                    popidx=ms.pop()
                    if ms:
                        poph=height[popidx]
                        mi=min(height[ms[-1]],height[i])
                        ans+=(mi-poph)*(i-ms[-1]-1)
                ms.append(i)
        return ans

h=[2,1,0,2]  
sol=Solution()
print(sol.trap(h))