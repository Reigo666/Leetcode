class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
class Solution:
    def queryString(self, s: str, n: int) -> bool:
        #1
        #10
        #11
        #100
        #101
        #110
        #111 7
        #1000 8
        bits=floor(log(n,2))+1
        #print(bits)
        
        root=TreeNode(-1)

        for i in range(len(s)):
            if s[i]=='0':
                continue
            root.val=1
            node=root
            for j in range(i+1,min(i+bits,len(s))):
                if s[j]=='0':
                    if not node.left:
                        node.left=TreeNode(0)
                    node=node.left
                elif s[j]=='1':
                    if not node.right:
                        node.right=TreeNode(1)
                    node=node.right
        if root.val==-1:
            return False
        q=deque([[root,1]])
        while q:
            for i in range(len(q)):
                node,val=q.popleft()
                if node.left:
                    q.append([node.left,val*2])
                else:
                    if val*2<=n:
                        return False
                if node.right:
                    q.append([node.right,val*2+1])
                else:
                    if val*2+1<=n:
                        return False
        return True
                
        