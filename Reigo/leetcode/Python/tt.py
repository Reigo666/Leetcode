# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        lastval=None
        def dfs(root):
            if root:
                if not dfs(root.left):
                    return False
                nonlocal lastval
                print(lastval)
                if not lastval:
                    lastval=root.val
                else:
                    if root.val<=lastval:
                        return False
                lastval=root.val
                if not dfs(root.right):
                    return False
                return True
            else:
                return True
        return dfs(root)
    
t1=TreeNode(0)
t2=TreeNode(-1)
t1.right=t2
sol=Solution()
print(sol.isValidBST(t1))