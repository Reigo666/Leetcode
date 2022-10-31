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
    def isValidBST(self, root: TreeNode) -> bool:
        def isValid(root,l:int,r:int):
            if root:
                if root.val<=l or root.val>=r:
                    return False
                else:
                    lvalid=True
                    rvalid=True
                    if root.left:
                        lvalid=isValid(root.left,l,root.val)
                    if root.right:
                        rvalid=isValid(root.right,root.val,r)
                    return lvalid and rvalid
            return False
        return isValid(root,-2**63,2**63-1)
    def isValidBST1(self, root: TreeNode) -> bool:
        
        def isValid(root: TreeNode,lt:int,st:int):
            if root:
                isvalidleft=False
                isvalidright=False
                if root.val<=lt or root.val>=st:
                    return False
                if root.left:
                    if root.val>root.left.val:
                        isvalidleft=isValid(root.left,lt,root.val)
                    else:
                        return False
                else:
                    isvalidleft=True

                if root.right:     
                    if root.val<root.right.val:
                        isvalidright=isValid(root.right,root.val,st)
                    else:
                        return False
                else:
                    isvalidright=True

                return isvalidleft and isvalidright
            return False
        return isValid(root,-2**31,2**31-1)
               


sol=Solution()

# root = [1,null,2,3]
t3=TreeNode(3,None,None)
t1=TreeNode(1,None,None)
t2=TreeNode(2,t1,t3)

print(sol.isValidBST(t2))

# 输入：root = [5,1,4,null,null,3,6]
# 输出：false
# 解释：根节点的值是 5 ，但是右子节点的值是 4 。