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
    def isBalanced(self, root: TreeNode) -> bool:
        def check(root,depth):
            if root:
                ldepth,lvalid=check(root.left,depth+1)
                if not lvalid:
                    return 0,False
                rdepth,rvalid=check(root.right,depth+1)
                if not rvalid:
                    return 0,False
                if abs(ldepth-rdepth)>=2:
                    return 0,False
                else:
                    return max(ldepth,rdepth),True
            else:
                return depth-1,True
        return check(root,1)[1]
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

print(sol.isBalanced(t3))

# 输入：root = [1,2,2,3,3,null,null,4,4]
# 输出：false
