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
    def minDepth(self, root: TreeNode) -> int:
        def calculateDepth(root:TreeNode):
            if root:
                ldepth=calculateDepth(root.left)
                rdepth=calculateDepth(root.right)
                if not ldepth and not rdepth:
                    return 1
                elif not ldepth or not rdepth:
                    return max(ldepth,rdepth)+1
                else:return min(ldepth,rdepth)+1
            else:
                return 0
        return calculateDepth(root)
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

print(sol.minDepth(t3))

# 输入：root = [1,2,2,3,3,null,null,4,4]
# 输出：false
