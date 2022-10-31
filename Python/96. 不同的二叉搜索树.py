import collections
from typing import  List,Optional
import copy

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def numTrees(self, n: int) -> int:
        ct=[[1]*n for i in range(n)]

        for j in range(n):
            
            for i in range(j,-1,-1):
                if i==j:
                    ct[i][i]=1
                else:
                    allnum=0
                    for k in range(i,j+1):
                        if k-1<i:
                            a=1
                        else:
                            a=ct[i][k-1]
                        if k+1>j:
                            b=1
                        else:
                            b=ct[k+1][j]
                        allnum+=a*b
                    ct[i][j]=allnum
        return ct[0][n-1]




sol=Solution()

# root = [1,null,2,3]
# t3=TreeNode(3,None,None)
# t2=TreeNode(2,t3,None)
# t1=TreeNode(1,None,t2)

n=3
print(sol.numTrees(n))

# 输入：n = 3
# 输出：5