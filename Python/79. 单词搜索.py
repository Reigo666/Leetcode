
import collections
from typing import  List,Optional
import copy

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m=len(board)
        n=len(board[0])
        visit=[[0]*n for i in range(m)]

        direct=[(1,0),(0,1),(0,-1),(-1,0)]
        def backTrack(i,j,board,word):
            if word=="":
                return True
            else:
                for dir in direct:
                    tx=i+dir[0]
                    ty=j+dir[1]
                    if tx>=0 and tx<=m-1 and ty>=0 and ty<=n-1 and visit[tx][ty]==0 and board[tx][ty]==word[0]:
                        visit[tx][ty]=1
                        if backTrack(tx,ty,board,word[1:])==True:
                            return True
                        visit[tx][ty]=0
                return False
                        


        for i in range(m):
            for j in range(n):
                if board[i][j]==word[0]:
                    visit[i][j]=1
                    if backTrack(i,j,board,word[1:])==True:
                        return True
                    visit[i][j]=0
        return False
                


sol=Solution()
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
word1="SFCS"
print(sol.exist(board,word1))

# 输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# 输出：true

