# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        arr=[]
        def inOrder(root):
            if root:
                inOrder(root.left)
                arr.append(root)
                inOrder(root.right)
        
        inOrder(root)
        if not arr:
            return None
        for i in range(len(arr)-1):
            arr[i].left=None
            arr[i].right=arr[i+1]
        
        arr[-1].left=None
        arr[-1].right=None

        return arr[0]
        