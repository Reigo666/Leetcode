
import collections
from typing import  List,Optional
import copy


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        lenn=len(nums)
        ans=[]
        def backTrack(temp:List[int],nums,i,limit):
            if i>=limit:
                ans.append(copy.deepcopy(temp))
            else:
                backTrack(temp,nums,i+1,limit)
                temp.append(nums[i])
                backTrack(temp,nums,i+1,limit)
                temp.pop()
        backTrack([],nums,0,lenn)
        return ans


sol=Solution()
nums = [1,2,3]
print(sol.subsets(nums))

# 输入：nums = [1,2,3]
# 输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]s