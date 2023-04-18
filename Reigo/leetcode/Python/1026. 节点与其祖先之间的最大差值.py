# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        ans=0
        def dfs(root,minVal,maxVal):
            if root:
                nonlocal ans
                ans=max(ans,abs(minVal-root.val),abs(maxVal-root.val))
                nextma=max(root.val,maxVal)
                nextmi=min(root.val,minVal)
                dfs(root.left,nextmi,nextma)
                dfs(root.right,nextmi,nextma)
        
        dfs(root,root.val,root.val)
        return ans