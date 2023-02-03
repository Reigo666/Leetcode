# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        xln=0
        xrn=0
        def dfs(root):
            if root:
                ln=dfs(root.left)
                rn=dfs(root.right)
                if root.val==x:
                    nonlocal xln,xrn
                    xln=ln
                    xrn=rn
                return ln+rn+1
            else:
                return 0
        dfs(root)
        xpn=n-1-xln-xrn
        xn=max(xln,xrn,xpn)
        return 2*xn>n-1

                
