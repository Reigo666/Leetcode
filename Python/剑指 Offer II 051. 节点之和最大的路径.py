# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:

        maxval=root.val
        def dfs(root):
            if root:
                nonlocal maxval
                lval=dfs(root.left)
                rval=dfs(root.right)

                maxval=max(maxval,lval+root.val,root.val,rval+root.val,lval+root.val+rval)
                return max(0,lval+root.val,root.val,rval+root.val)
            else:
                return 0
            
        
        dfs(root)
        return maxval