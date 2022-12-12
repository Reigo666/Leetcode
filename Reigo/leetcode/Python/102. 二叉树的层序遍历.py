import collections
from typing import  List,Optional
import copy

from matplotlib.collections import Collection



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        ans=[]
        q= collections.deque([root])
        while True:
            lenq=len(q)
            if lenq==0:
                break
            lv=[]
            for i in range(lenq):
                t=q.popleft()
                lv.append(t.val)
                if t.left:
                    q.append(t.left)
                if t.right:
                    q.append(t.right)
            if lv:
                ans.append(lv)
        return ans

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

print(sol.levelOrder(t3))

# 输入：root = [3,9,20,null,null,15,7]
# 输出：[[3],[9,20],[15,7]]