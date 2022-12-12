# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BSTIterator:
    midorderlist=[]
    idx=-1
    def __init__(self, root: TreeNode):
        self.idx=-1
        self.midorderlist=[]
        def generate(root: TreeNode):
            if root:
                generate(root.left)
                self.midorderlist.append(root.val)
                generate(root.right)
        generate(root)


    def next(self) -> int:
        self.idx+=1
        return self.midorderlist[self.idx]

    def hasNext(self) -> bool:
        n=len(self.midorderlist)
        if self.idx+1<n:
            return True
        return False



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()