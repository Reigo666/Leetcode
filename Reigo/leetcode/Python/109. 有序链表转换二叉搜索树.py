import collections
from typing import  List,Optional
import copy



# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def sortedArrayToBST(nums: List[int]) -> Optional[TreeNode]:
            def build(nums):
                if nums:
                    mid=(0+len(nums)-1)//2
                    lnode=build(nums[:mid])
                    rnode=build(nums[mid+1:])
                    root=TreeNode(nums[mid],lnode,rnode)
                    return root
                else:
                    return None
            return build(nums)
        nums=[]
        while head:
            nums.append(head.val)
            head=head.next
        return sortedArrayToBST(nums)

sol=Solution()

# root = [1,null,2,3]

t2=TreeNode(2,None,None)
t3=TreeNode(3,None,t2)
t1=TreeNode(1,t3,None)

t9=TreeNode(9,None,None)
t15=TreeNode(15,None,None)
t7=TreeNode(7,None,None)
t20=TreeNode(20,t15,t7)
t3=TreeNode(3,t9,t20)
#t4=TreeNode(4,t2,None)

nums = [-10,-3,0,5,9]
print(sol.sortedArrayToBST(nums))

# 输入：nums = [-10,-3,0,5,9]
# 输出：[0,-3,9,-10,null,5]
# 解释：[0,-10,5,null,-3,null,9] 也将被视为正确答案：
