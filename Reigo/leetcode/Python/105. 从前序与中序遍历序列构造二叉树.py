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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def build(preorder: List[int], inorder: List[int])-> TreeNode:
            if not inorder:
                return None
            else:
                idx=inorder.index(preorder[0])
                lnode=build(preorder[1:1+idx],inorder[:idx])
                rnode=build(preorder[idx+1:],inorder[idx+1:])
                root=TreeNode(preorder[0],lnode,rnode)
                return root
        return build(preorder,inorder)
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
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
print(sol.buildTree(preorder,inorder))

# 输入：root = [3,9,20,null,null,15,7]
# 输出：[[3],[9,20],[15,7]]