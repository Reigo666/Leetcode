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
    def flatten(self, root: TreeNode) -> None:
        cur=root
        while cur:
            if cur.left:
                rnode=cur.right
                cur.right=cur.left
                cur.left=None
                downnode=cur.right
                while downnode.right:
                    downnode=downnode.right
                downnode.right=rnode
            cur=cur.right
    def flatten1(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        nodelist=[]
        def preorder(root:TreeNode):
            if root:
                nodelist.append(root)
                preorder(root.left)
                preorder(root.right)
        if root:
            preorder(root)
            dummynode=TreeNode(0,None,root)
            prenode=dummynode  
            for node in nodelist:
                node.left=None
                prenode.right=node
                node.right=None
                prenode=node
            
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

print(sol.flatten(t3))

# 输入：root = [1,2,2,3,3,null,null,4,4]
# 输出：false
