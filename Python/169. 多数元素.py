import collections
from typing import  List,Optional
import copy
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maxoccurrence=0
        maxoccurrencenum=-1
        n=len(nums)
        dict=collections.defaultdict(int)
        for i in range(n):
            dict[nums[i]]+=1
            if dict[nums[i]]>maxoccurrence:
                maxoccurrence=dict[nums[i]]
                maxoccurrencenum=nums[i]
                if maxoccurrence>n//2:
                    return maxoccurrencenum
        return maxoccurrencenum