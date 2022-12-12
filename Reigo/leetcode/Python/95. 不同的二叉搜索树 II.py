
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
    def generateTrees(self, n: int) -> List[TreeNode]:
        def generate(start,end):
            if start>end:
                return [None]
            else:
                allans=[]
                for i in range(start,end+1):
                    #左子树小，右子树大
                    lefttree=generate(start,i-1)
                    righttree=generate(i+1,end)
                    for l in lefttree:
                        for r in righttree:
                            allans.append(TreeNode(i,l,r))
                return allans
        return generate(1,n) if n else []
sol=Solution()

# root = [1,null,2,3]
t3=TreeNode(3,None,None)
t2=TreeNode(2,t3,None)
t1=TreeNode(1,None,t2)
print(sol.inorderTraversal(t1))

# 输入：n = 3
#中序输出
# 输出：[[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]





