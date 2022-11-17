# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        s=""
        if not root:
            return s
        def dfs(root):
            nonlocal s
            if root:
                s+=str(root.val)+','
                dfs(root.left)
                dfs(root.right)
            else:
                s+="None,"
        dfs(root)
        s=s[:-1]
        
        return s

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data=="":
            return None
        
        #print(data)
        l=data.split(",")
        q=deque(l)
        #print(q)
        def createTree(q):
            if not q:
                return None
            cur=q.popleft()
            if cur=="None":
                return None
            newnode=TreeNode(int(cur))
            newnode.left=createTree(q)
            newnode.right=createTree(q)
            return newnode
        return createTree(q)

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))