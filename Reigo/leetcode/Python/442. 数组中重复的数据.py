import collections
from typing import  List,Optional
import copy
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dict=collections.defaultdict(int)
        ans=[]
        for i in range(len(nums)):
            dict[nums[i]]+=1
            if dict[nums[i]]==2:
                ans.append(nums[i])
        return ans
