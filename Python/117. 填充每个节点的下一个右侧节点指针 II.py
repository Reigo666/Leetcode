
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

import collections
from typing import  List,Optional
import copy

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        q=collections.deque([root])
        while True:
            if not q:
                break
            pre=None
            for i in range(len(q)):
                node=q.popleft()
                if not node.left and not node.right:
                    continue
                
                if node.left:
                    
                    if pre:
                        pre.next=node.left
                    if node.right:
                        pre=node.right
                    else:
                        pre=node.left
                else:
                    
                    if pre:
                        pre.next=node.right
                    pre=node.right
                
                if node.left and node.right:
                    node.left.next=node.right

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return root
