
import collections
from typing import  List,Optional
import copy

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_dict={}
        maxlength=0
        for num in nums:
            if num not in hash_dict:
                left=hash_dict.get(num-1,0)
                right=hash_dict.get(num+1,0)
                temp_length=1+left+right
                maxlength=max(maxlength,temp_length)

                #更新边缘
                hash_dict[num]=temp_length
                hash_dict[num+right]=temp_length
                hash_dict[num-left]=temp_length
            
        return maxlength



sol=Solution()
nums = [100,4,200,1,3,2]
print(sol.longestConsecutive(nums))

# 输入：nums = [100,4,200,1,3,2]
# 输出：4
# 解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。

