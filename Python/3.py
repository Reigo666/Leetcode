# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        def rootSum(root: TreeNode, sum: int):
            if not root:
                return 0
            else:
                ret=0
                print(root.val,sum)
                if sum<root.val:
                    return 0
                if sum==root.val:
                    return 1

                ret+=rootSum(root.left,sum-root.val)
                ret+=rootSum(root.right,sum-root.val)
                return ret

        ret=0
        if root:
            ret=rootSum(root,sum)
            print(ret)
            ret+=self.pathSum(root.left,sum)
            ret+=self.pathSum(root.right,sum)
        return ret

sol=Solution()
n1=TreeNode(-2)
n2=TreeNode(-3)

n1.left=None
n1.right=n2

n4=TreeNode(2)


# [-2,null,-3]
# -5

sum=-5
print(sol.pathSum(n1,sum))