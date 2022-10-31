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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def check(root1,root2):
            if not root1 and not root2:
                return True
            if not root1 or not root2:
                return False
            if root1.val!=root2.val:
                return False
            else:
                return check(root1.left,root2.right) and check(root1.right,root2.left)
        return check(root.left,root.right)
sol=Solution()

# root = [1,null,2,3]

t2=TreeNode(2,None,None)
t3=TreeNode(3,None,t2)
t1=TreeNode(1,t3,None)
#t4=TreeNode(4,t2,None)

print(sol.isSymmetric(t1))

# 输入：p = [1,2,3], q = [1,2,3]
# 输出：true
