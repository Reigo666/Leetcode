import collections
from typing import  List,Optional
import copy
class Solution:
    #双旋转
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k=k%n
        if k==0:
            return
        ans=nums[::-1]
        print(nums[0:k][::-1])
        ans=ans[0:k][::-1]+ans[k:][::-1]
        for i in range(n):
            nums[i]=ans[i]
        print(nums)
    def rotate1(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k=k%n
        if k==0:
            return
        for i in range(k):
            num=nums.pop()
            nums.insert(0,num)