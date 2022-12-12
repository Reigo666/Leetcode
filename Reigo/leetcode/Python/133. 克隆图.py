
import collections
from typing import  List,Optional
import copy

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        lookup={}
        def dfs(node: 'Node'):
            if node not in lookup:
                
                clone=Node(node.val,[])
                lookup[node]=clone
                for n in node.neighbors:
                    clone.neighbors.append(dfs(n))
                return clone
            else:
                return lookup[node]
        return dfs(node)
sol=Solution()
n=5
print(sol.cloneGraph(n))

#1->4->3->2->1
# 输入：adjList = [[2,4],[1,3],[2,4],[1,3]]
# 输出：[[2,4],[1,3],[2,4],[1,3]]


