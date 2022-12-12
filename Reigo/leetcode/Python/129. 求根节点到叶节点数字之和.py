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
    def sumNumbers(self, root: TreeNode) -> int:
        def solve(root:TreeNode,val:int):
            if root:
                if not root.left and not root.right:
                    return val*10+root.val
                if root.left:
                    leftsum=solve(root.left,val*10+root.val)
                else:
                    leftsum=0
                if root.right:
                    rightsum=solve(root.right,val*10+root.val)
                else:
                    rightsum=0
                return leftsum+rightsum
            else:
                return val
        return solve(root,0)

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
                if nums[k]!=None:
                    lnode=TreeNode(nums[k],None,None)
                    q.append(lnode)
                else:
                    lnode=None
                k+=1
                r.left=lnode
                if k==lennum:
                    break

                if nums[k]!=None:
                    rnode=TreeNode(nums[k],None,None)
                    q.append(rnode)
                else:
                    rnode=None
                k+=1    
                r.right=rnode
                if k==lennum:
                    break
        return root  
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
nums = [4,9,0,5,1]
root=sol.layerCreateTree(nums)
def preorder(root:TreeNode):
    if root:
        print(root.val)
        preorder(root.left)
        preorder(root.right)
preorder(root)

print(sol.sumNumbers(root))
# 输入：root = [4,9,0,5,1]
# 输出：1026
# 解释：
# 从根到叶子节点路径 4->9->5 代表数字 495
# 从根到叶子节点路径 4->9->1 代表数字 491
# 从根到叶子节点路径 4->0 代表数字 40
# 因此，数字总和 = 495 + 491 + 40 = 1026
