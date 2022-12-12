from typing import List,Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        lens=len(nums)
        l=0
        for r in range(lens):
            if nums[r]!=val:
                nums[l]=nums[r]
                l+=1
        return l
sol=Solution()
nums1 = [0,1,2,2,3,0,4,2] 
val1 = 2
print(sol.removeElement(nums1,val1))

# 输入：nums = [0,1,2,2,3,0,4,2], val = 2
# 输出：5, nums = [0,1,4,0,3]
# 解释：函数应该返回新的长度 5, 并且 nums 中的前五个元素为 0, 1, 3, 0, 4。注意这五个元素可为任意顺序。你不需要考虑数组中超出新长度后面的元素。


