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
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        ans=[]
        def findpath(root:TreeNode,target,sum,combination:List[int]):
            if not root:
                return
            sum+=root.val
            combination.append(root.val)
            if sum==target and not root.left and not root.right:
                ans.append(copy.deepcopy(combination))
                combination.pop()
                return
            findpath(root.left,target,sum,combination)
            findpath(root.right,target,sum,combination)
            combination.pop()
        findpath(root,targetSum,0,[])
        return ans
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
nums=[5,4,8,11,None,13,4,7,2,None,None,5,1]
root=sol.layerCreateTree(nums)
def preorder(root:TreeNode):
    if root:
        print(root.val)
        preorder(root.left)
        preorder(root.right)
preorder(root)
print(sol.hasPathSum(root,22))

# 输入：root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
# 输出：true
# 解释：等于目标和的根节点到叶节点路径如上图所示。
