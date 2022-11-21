# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.root=root
        self.q=deque([])
        q=self.q
        def inOrder(root):
            if root:
                inOrder(root.left)
                q.append(root)
                inOrder(root.right)
        inOrder(root)

    def next(self) -> int:
        q=self.q
        if q:
            return q.popleft().val
        return -1

    def hasNext(self) -> bool:
        q=self.q
        if q:
            return True
        return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()