# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:

        def dfs(root):
            if root:
                solve(root,root.val)
                dfs(root.left)
                dfs(root.right)
            
        ans=0
        def solve(root,val):
            nonlocal ans
            if val==targetSum:
                ans+=1
            if root.left:
                solve(root.left,val+root.left.val)
            if root.right:
                solve(root.right,val+root.right.val)
        
        dfs(root)
        return ans
    
    def pathSum1(self, root: TreeNode, targetSum: int) -> int:
        prefix=defaultdict(int)
        prefix[0]=1
        def dfs(root,cur):
            if root:
                cur+=root.val
                res=0
                res+=prefix[cur-targetSum]
                prefix[cur]+=1
                res+=dfs(root.left,cur)
                res+=dfs(root.right,cur)
                prefix[cur]-=1

                return res
            return 0
        
        return dfs(root,0)