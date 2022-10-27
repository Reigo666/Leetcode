from collections import deque
from typing import List


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        suma=[0]
        for i in range(len(nums)):
            suma.append(suma[i]+nums[i])
        
        q=deque([])
        ans=10**6
        for i in range(len(nums)):
            if nums[i]>=k:
                return 1
            if not q:
                q.append(i)
            else:
                r=i
                while len(q):
                    l=q[0]
                    val=suma[r+1]-suma[l]
                    if val>=k:
                        q.popleft()
                        ans=min(ans,r-l+1)
                    else:
                        break
            
                while len(q):
                    if suma[q[-1]]>=suma[i]:
                        q.pop()
                    else:
                        break
                q.append(i)
        if ans==10**6:
            return -1
        return ans
sol=Solution()
nums=[-11,-15,76,41,-41,68,41,12,73,-8]
k=50
print(sol.shortestSubarray(nums,k))