
import collections
from typing import  List,Optional
import copy

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root==None:
            return []
        ans=[]
        def midorder(root:TreeNode):
            if root:
                midorder(root.left)
                ans.append(root.val)
                midorder(root.right)
        midorder(root)
        return ans
sol=Solution()

# root = [1,null,2,3]
t3=TreeNode(3,None,None)
t2=TreeNode(2,t3,None)
t1=TreeNode(1,None,t2)
print(sol.inorderTraversal(t1))


# 输入：root = [1,null,2,3]
# 输出：[1,3,2]





