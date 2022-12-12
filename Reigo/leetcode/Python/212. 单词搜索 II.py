import collections
from typing import  List,Optional
import copy
class Node:
    def __init__(self):
        self.next={}
        self.isEnd=False
    def contain(self,l:str)->bool:
        if l in self.next:
            return True
        return False
    
    def add(self,l:str):
        self.next[l]=Node()
    def get(self,l:str):
        return self.next[l]
    
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root=Node()

        for word in words:
            node=root
            for l in word:
                if not node.contain(l):
                    node.add(l)
                node=node.get(l)
            node.isEnd=True
        
        m=len(board)
        n=len(board[0])
        ans=[]
        isVisit=[[False]*n for _ in range(m)]
        #左 右 下 上
        all_direct=[[0,-1],[0,1],[1,0],[-1,0]]
        def dfs(i,j,root,combination):
            nonlocal all_direct
            nonlocal isVisit
            nonlocal ans
            
            if root.isEnd==True:
                ans.append(combination)
                root.isEnd=False

            if not root.next:
                return

            for direct in all_direct:
                dx=i+direct[0]
                dy=j+direct[1]
                if dx>=0 and dx<m and dy>=0 and dy<n and not isVisit[dx][dy]:
                    if root.contain(board[dx][dy]):
                        nextnode=root.get(board[dx][dy])
                    else:
                        continue
                    isVisit[dx][dy]=True
                    dfs(dx,dy,nextnode,combination+board[dx][dy])
                    isVisit[dx][dy]=False
        for i in range(m):
            for j in range(n):
                isVisit=[[False]*n for _ in range(m)]
                isVisit[i][j]=True
                if i==2 and j==2:
                    print(123)
                if root.contain(board[i][j]):
                    dfs(i,j,root.get(board[i][j]),board[i][j])
        return ans

sol=Solution()

board=[["a","b","c"],["a","e","d"],["a","f","g"]]
# abc
# aed
# afg
words=["gfedcbaaa"]
print(sol.findWords(board,words))