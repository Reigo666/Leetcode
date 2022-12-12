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
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        def leverOrder(root):
            if root:
                q=collections.deque([root])
                ans=[]
            else:
                return []
            while q:
                maxval=-2**31
                for i in range(len(q)):
                    n=q.popleft()
                    if n.val>maxval:
                        maxval=n.val
                    if n.left:
                        q.append(n.left)
                    if n.right:
                        q.append(n.right)
                ans.append(maxval)
            return ans
        return leverOrder(root)