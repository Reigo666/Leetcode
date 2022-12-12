# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        q=deque([root])
        ans=[]
        while q:
            maxval=-(2**31)
            for i in range(len(q)):
                node=q.popleft()
                maxval=max(maxval,node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(maxval)
        return ans