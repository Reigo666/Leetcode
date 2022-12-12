# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(root,val):
            if root:
                lval=0
                rval=0
                if root.left:
                    lval=dfs(root.left,val*10+root.val)
                if root.right:
                    rval=dfs(root.right,val*10+root.val)
                if not root.left and not root.right:
                    return val*10+root.val
                return lval+rval
        return dfs(root,0)