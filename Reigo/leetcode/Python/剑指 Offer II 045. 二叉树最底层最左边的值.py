# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        q=deque([root])
        firstnode=None
        while q:
            firstnode=None
            for i in range(len(q)):
                node=q.popleft()
                if not firstnode:
                    firstnode=node
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
        return firstnode.val
                