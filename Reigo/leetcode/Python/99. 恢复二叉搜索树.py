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
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        treenodelist=[]
        def midorder(root:TreeNode)->None:
            if root:
                midorder(root.left)
                treenodelist.append(root)
                midorder(root.right)
        midorder(root)
        treenodelist.insert(0,TreeNode(treenodelist[0].val-1,None,None))
        treenodelist+=[TreeNode(treenodelist[-1].val+1,None,None)]
        lnode=treenodelist[1]
        rnode=treenodelist[-2]
        findlnode=False
        findval=-10000
        for i in range(1,len(treenodelist)-1):
            if not findlnode:  
                if treenodelist[i].val>treenodelist[i+1].val:
                    lnode=treenodelist[i]
                    findval=lnode.val
                    findlnode=True
            else:
                if findval<treenodelist[i+1].val:
                    rnode=treenodelist[i]
                    break
        lnode.val,rnode.val=rnode.val,lnode.val
        
        def midorderprint(root:TreeNode)->None:
            if root:
                midorderprint(root.left)
                print(root.val)
                midorderprint(root.right)
        midorderprint(root)
        return None
sol=Solution()

# root = [1,null,2,3]

t2=TreeNode(2,None,None)
t3=TreeNode(3,None,t2)
t1=TreeNode(1,t3,None)
#t4=TreeNode(4,t2,None)

print(sol.recoverTree(t1))

# 输入：root = [1,3,null,null,2]
# 输出：[3,1,null,null,2]
# 解释：3 不能是 1 的左孩子，因为 3 > 1 。交换 1 和 3 使二叉搜索树有效。
