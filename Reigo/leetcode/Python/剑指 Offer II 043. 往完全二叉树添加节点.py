# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter:

    def __init__(self, root: TreeNode):
        self.root=root
        self.q=deque([])
        q=self.q
        t=deque([root])
        while t:
            for i in range(len(t)):
                node=t.popleft()
                if node.left:
                    t.append(node.left)
                if node.right:
                    t.append(node.right)
                if not node.left or not node.right:
                    q.append(node)
        
                
    def insert(self, v: int) -> int:
        q=self.q
        newnode=TreeNode(v,None,None)
        
        ret=q[0].val
        if not q[0].left:
            q[0].left=newnode
        elif not q[0].right:
            q[0].right=newnode
            q.popleft()
        
        q.append(newnode)
        return ret

    def get_root(self) -> TreeNode:
        return self.root


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()