
import collections
from multiprocessing import dummy
from typing import  List,Optional
import copy
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        nums.sort()
        def backTrack(combination,nums,curnum,add):
            if nums==[]:
                ans.append(combination)
            else:
                #上一次放了 这次可以接着放，上一次没放 需要看数字是否相同相同的话不能再放了
                if (curnum!=nums[0] and add==0) or add==1:
                    backTrack(combination+[nums[0]],nums[1:],nums[0],1)
                backTrack(combination,nums[1:],nums[0],0)
        backTrack([],nums,-2**31,0)
        return ans
sol=Solution()

nums1 = [1,2,2]
print(sol.subsetsWithDup(nums1))


# 输入：nums = [1,2,2]
# 输出：[[],[1],[1,2],[1,2,2],[2],[2,2]]


