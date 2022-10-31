import collections
from typing import  List,Optional
import copy
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=0
        r=len(numbers)-1
        while l<r:
            if numbers[l]+numbers[r]==target:
                return [l+1,r+1]
            else:
                if numbers[l]+numbers[r]>target:
                    r-=1
                elif numbers[l]+numbers[r]<target:
                    l+=1
        return [-1,-1]