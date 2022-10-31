# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x,left,right):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        l=[]
        index=[0]
        i=[0]
        def inorder(root:TreeNode):
            if root:
                inorder(root.left)
                l.append(root)
                if root==p:
                    index[0]=i[0]
                i[0]+=1
                inorder(root.right)
        inorder(root)
        if index[0]<len(l)-1:
            return l[index[0]+1]
        else:
            return None

    def inorderSuccessor1(self, root: TreeNode, p: TreeNode) -> TreeNode:
        pre=[None]
        def inorder(root:TreeNode):
            if root:
                resl=inorder(root.left)
                if resl:
                    return resl
                if pre[0]==p:
                    return root
                pre[0]=root
                resr=inorder(root.right)
                if resr:
                    return resr
                return None
            else:
                return None
        return inorder(root)

t3=TreeNode(3,None,None)
t1=TreeNode(1,None,None)
t2=TreeNode(2,t1,t3)
sol=Solution()
res=sol.inorderSuccessor1(t2,t1)
print(res.val)