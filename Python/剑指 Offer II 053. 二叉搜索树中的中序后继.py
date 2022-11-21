# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        needFind=False
        isFind=False
        ans=None
        def inOrder(root):
            if root:
                nonlocal isFind
                nonlocal needFind
                if isFind:
                    return
                inOrder(root.left)

                if needFind:
                    nonlocal ans
                    ans=root
                    needFind=False
                    isFind=True
                    return

                if root==p:
                    needFind=True
                
                inOrder(root.right)
        
        inOrder(root)
        return ans