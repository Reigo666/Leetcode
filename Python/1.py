# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def checkSubTree(self, t1: TreeNode, t2: TreeNode) -> bool:
        #repeat=set()
        idx=0
        seen={}
        nodedict={}
        ans=False
        def dfs(root:TreeNode,findmode=False):
            if root:
                lidx=dfs(root.left)
                if lidx==-1:
                    return -1
                ridx=dfs(root.right)
                if ridx==-1:
                    return -1
                comb=(root.val,lidx,ridx)
                if findmode:
                    nonlocal t2rootcomb
                    nonlocal ans
                    print(comb)
                    if comb==t2rootcomb:
                        ans=True
                        return -1
                if comb in seen:
                    return seen[comb]
                else:
                    nonlocal idx
                    idx+=1
                    seen[comb]=idx
                    nodedict[root]=comb
                    return idx     
            else:
                return 0
        dfs(t2,False)
        t2rootcomb=nodedict[t2]
        print(t2rootcomb,seen[t2rootcomb])
        dfs(t1,True)
        return ans

sol=Solution()
n1=TreeNode(1)
n2=TreeNode(2)
n3=TreeNode(3)
n1.left=n2
n1.right=n3

n4=TreeNode(2)

t1 = [1, 2, 3]
t2 = [2]
print(sol.checkSubTree(n1,n4))