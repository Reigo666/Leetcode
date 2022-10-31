import collections
from typing import  List,Optional
import copy
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n=len(nums)
        maxans=nums[0]
        imax=1
        imin=1
        for i in range(n):
            if nums[i]<0:
                imax,imin=imin,imax
            imax=max(imax*nums[i],nums[i])
            imin=min(imin*nums[i],nums[i])
            maxans=max(maxans,imax)
        return maxans
    #超时
    def maxProduct1(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[[1]*n for i in range(n)]
        maxans=nums[0]
        #dpmax=[[1]*n for i in range(n)]
        for j in range(n):
            for i in range(j,-1,-1):
                if i==j:
                    dp[i][i]=nums[i]
                    maxans=max(maxans,nums[i])
                else:
                    dp[i][j]=dp[i][j-1]*nums[j]
                    maxans=max(maxans,dp[i][j])
        return maxans
