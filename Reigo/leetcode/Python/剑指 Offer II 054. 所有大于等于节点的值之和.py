# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        def calcSum(root):
            if root:
                lval=calcSum(root.left)
                rval=calcSum(root.right)
                return root.val+lval+rval
            else:
                return 0

        sum1=calcSum(root)

        def inOrder(root):
            if root:
                nonlocal sum1
                inOrder(root.left)
                cur=root.val
                root.val=sum1
                sum1-=cur
                inOrder(root.right)
        
        inOrder(root)
        return root