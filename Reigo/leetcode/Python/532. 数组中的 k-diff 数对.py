import collections
from typing import  List,Optional
import copy
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        def binarySearch(nums,l,r,val)->bool:
            while l<=r:
                mid=(l+r)//2
                if nums[mid]==val:
                    return True
                elif nums[mid]<val:
                    l=mid+1
                elif nums[mid]>val:
                    r=mid-1
            return False

        ans=0
        if k!=0:
            ns=set(nums)
            nums=list(ns)
            nums.sort()
            
            for i in range(len(nums)):           
                if binarySearch(nums,i+1,len(nums)-1,nums[i]+k):
                    ans+=1          
        else:
            dict={}
            for i in range(len(nums)):
                if nums[i] in dict:
                    dict[nums[i]]+=1
                    if dict[nums[i]]==2:
                        ans+=1
                else:
                    dict[nums[i]]=1
        return ans



