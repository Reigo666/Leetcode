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
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        dict=collections.defaultdict(int)
        maxsum=[]
        maxtime=0
        def findMaxSum(root: TreeNode):
            
            if root:
                
                suml=findMaxSum(root.left)
                sumr=findMaxSum(root.right)
                s=suml+sumr+root.val
                nonlocal maxtime
                nonlocal maxsum
                

                dict[s]+=1
                if dict[s]>maxtime:
                    maxsum=[s]
                    maxtime=dict[s]
                elif dict[s]==maxtime:
                    maxsum.append(s)
                return s
            else:
                return 0
        findMaxSum(root)
        return maxsum
sol=Solution()

t3=TreeNode(-3,None,None)
t2=TreeNode(2,None,None)
t1=TreeNode(5,t2,t3)
print(sol.findFrequentTreeSum(t1))