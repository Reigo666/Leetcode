# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        need=set()
        def dfs(root):
            if root:
                if dfs(root.left):
                    return True
                if root.val in need:
                    return True
                need.add(k-root.val)

                if dfs(root.right):
                    return True
                
                return False
            
            else:
                return False
        
        return dfs(root)