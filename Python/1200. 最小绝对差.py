import collections
from typing import  List,Optional
import copy
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        mingap=2**31-1
        ans=[]
        for i in range(len(arr)-1):
            if abs(arr[i]-arr[i+1])<mingap:
                ans=[[arr[i],arr[i+1]]]
                mingap=abs(arr[i]-arr[i+1])
            elif abs(arr[i]-arr[i+1])==mingap:
                ans.append([arr[i],arr[i+1]])
        return ans