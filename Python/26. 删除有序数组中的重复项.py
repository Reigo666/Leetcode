from typing import List,Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if nums==[]: return 0
        l=0
        r=1
        lens=len(nums)
        while r<lens:
            if nums[l]!=nums[r]:
                nums[l+1]=nums[r]
                l+=1
            r+=1
        return l+1

sol=Solution()
nums1 = [0,0,1,1,1,2,2,3,3,4]
print(sol.removeDuplicates(nums1))
# 输入：nums = [1,1,2]
# 输出：2, nums = [1,2,_]
# 解释：函数应该返回新的长度 2 ，并且原数组 nums 的前两个元素被修改为 1, 2 。不需要考虑数组中超出新长度后面的元素。

