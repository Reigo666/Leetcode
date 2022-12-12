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
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def build(inorder,postorder):
            if inorder:
                rootval=postorder[-1]
                idx=inorder.index(rootval)
                lnode=build(inorder[:idx],postorder[:idx])
                rnode=build(inorder[idx+1:],postorder[idx:-1])
                root=TreeNode(postorder[-1],lnode,rnode)
                return root
            else:
                return None
        
        return build(inorder,postorder)
    
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
inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
root=sol.buildTree(inorder,postorder)
def preorder(root):
    if root:
        print(root.val)
        preorder(root.left)
        preorder(root.right)
preorder(root)
# 输入：inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
# 输出：[3,9,20,null,null,15,7]

