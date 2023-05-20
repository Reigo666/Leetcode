# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        ans=0
        # def dfs(root):
        #     if root:
        #         cur=root.val
        #         leftmin,leftmax,leftsum=cur,cur-1,0
        #         rightmin,rightmax,rightsum=cur+1,cur,0
        #         if root.left:
        #             leftmin,leftmax,leftsum=dfs(root.left)
        #         if root.right:
        #             rightmin,rightmax,rightsum=dfs(root.right)

        #         print(cur,leftmin,leftmax,leftsum,rightmin,rightmax,rightsum)

        #         if leftmin==None:
        #             return None,None,None
        #         if cur<=leftmax:
        #             return None,None,None
        #         if rightmin==None:
        #             return None,None,None
        #         if cur>=rightmin:
        #             return None,None,None
        #         #print(cur,leftmin,leftmax,leftsum,rightmin,rightmax,rightsum)
        #         nonlocal ans
        #         ans=max(ans,leftsum+rightsum+cur)
        #         return leftmin,rightmax,leftsum+rightsum+cur
        def dfs(root):
            if root:
                cur=root.val
                leftmin,leftmax,leftsum=dfs(root.left)
                rightmin,rightmax,rightsum=dfs(root.right)

                #print(cur,leftmin,leftmax,leftsum,rightmin,rightmax,rightsum)

                if cur<=leftmax or cur>=rightmin:
                    return -inf,inf,0

                #print(cur,leftmin,leftmax,leftsum,rightmin,rightmax,rightsum)
                nonlocal ans
                ans=max(ans,leftsum+rightsum+cur)
                return min(cur,leftmin),max(cur,rightmax),leftsum+rightsum+cur
            else:
                return inf,-inf,0
        dfs(root)
        return ans