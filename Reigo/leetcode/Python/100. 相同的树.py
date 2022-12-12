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
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def check(root1:TreeNode,root2:TreeNode):
            if (root1 and not root2)or (not root1 and root2):
                return False
            elif not root1 and not root2:
                return True
            else:
                if root1.val!=root2.val:
                    return False
                lcheck=check(root1.left,root2.left)
                if not lcheck:return False
                rcheck=check(root1.right,root2.right)
                if lcheck and rcheck:
                    return True
                else:return False
        return check(p,q)
sol=Solution()

# root = [1,null,2,3]

t2=TreeNode(2,None,None)
t3=TreeNode(3,None,t2)
t1=TreeNode(1,t3,None)
#t4=TreeNode(4,t2,None)

print(sol.isSameTree(t1,t2))

# 输入：p = [1,2,3], q = [1,2,3]
# 输出：true
