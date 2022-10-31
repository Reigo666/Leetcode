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
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def solve(root:TreeNode):
            if root:
                rootval=root.val
                if root.left:
                    ansl,ansmaxl=solve(root.left)
                else:
                    ansl,ansmaxl=0,-2**63
                if root.right:
                    ansr,ansmaxr=solve(root.right)
                else:
                    ansr,ansmaxr=0,-2**63
                return max(rootval+ansl,rootval+ansr,rootval),max(ansmaxl,ansmaxr,rootval,rootval+ansl,rootval+ansr,rootval+ansl+ansr)
            else:
                return 0,0
        return solve(root)[1]

    
    def layerCreateTree(self,nums:List[int])->TreeNode:
        if not nums:
            return None
        root=TreeNode(nums[0],None,None)
        l=[root]
        q=collections.deque(l)
        k=1
        lennum=len(nums)
        while True:
            n=len(q)
            if k==lennum:
                break
            for i in range(n):
                r=q.popleft()
                if nums[k]:
                    lnode=TreeNode(nums[k],None,None)
                    q.append(lnode)
                else:
                    lnode=None
                k+=1
                if nums[k]:
                    rnode=TreeNode(nums[k],None,None)
                    q.append(rnode)
                else:
                    rnode=None
                k+=1
                r.left=lnode
                r.right=rnode
                
        return root  

nums = [-10,9,20,None,None,15,7]
sol=Solution()
root=sol.layerCreateTree(nums)
print(sol.maxPathSum(root))
# 输入：root = [-10,9,20,null,null,15,7]
# 输出：42
# 解释：最优路径是 15 -> 20 -> 7 ，路径和为 15 + 20 + 7 = 42

