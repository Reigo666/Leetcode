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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def calculateDepth(root,tempdepth):
            if root:
                maxl=calculateDepth(root.left,tempdepth+1)
                maxr=calculateDepth(root.right,tempdepth+1)
                return max(maxl,maxr)
            else:return tempdepth-1
        return calculateDepth(root,1)

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

print(sol.maxDepth(t3))

# 输入：root = [3,9,20,null,null,15,7]
# 输出：[[3],[9,20],[15,7]]