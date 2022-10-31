# Definition for a binary tree node.
import collections
from typing import  List,Optional
import copy

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    #遇到的问题
    #deque需要popleft
    #root.val是int 需要转换为str
    #cocollections.deque([root])中root需要加list
    #data->listd需要使用listd而不是使用data
    def serialize(self, root: TreeNode) -> str:
        if not root:
            return ""
        ans=""
        ans+=str(root.val)
        ans+=","
        q=collections.deque([root])
        while q:
            for i in range(len(q)):
                node=q.popleft()        
                if node.left:
                    q.append(node.left)
                    ans+=str(node.left.val)
                    ans+=","
                else:
                    ans+="#"
                    ans+=","
                if node.right:
                    q.append(node.right)
                    ans+=str(node.right.val)
                    ans+=","
                else:
                    ans+="#"
                    ans+=","
        ans=ans[:-1]
        #print(ans)
        return ans
        """Encodes a tree to a single string.
        """
        

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if not data or data=="":
            return None
        listd=data.split(",")
        #print(listd)
        root=TreeNode(listd[0],None,None)
        q=collections.deque([root])
        k=1
        while q:
            for i in range(len(q)):
                node=q.popleft()
                #print(k,q)
                if listd[k]!="#":
                    l=TreeNode(listd[k],None,None)
                    q.append(l)
                else:
                    l=None
                k+=1
                if listd[k]!="#":
                    r=TreeNode(listd[k],None,None)
                    q.append(r)
                else:
                    r=None
                k+=1
                node.left=l
                node.right=r
        return root


        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans