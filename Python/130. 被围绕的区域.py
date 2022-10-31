
import collections
from typing import  List,Optional
import copy

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m=len(board)
        n=len(board[0])
        all_direct=[[0,1],[0,-1],[1,0],[-1,0]]
        def change_map(i,j):
            stack=[(i,j)]
            board[i][j]='#'
            while True:
                if not stack:
                    break
                for _ in range(len(stack)):
                    sx,sy=stack.pop()
                    for direct in all_direct:
                        tx=sx+direct[0]
                        ty=sy+direct[1]
                        if tx>=0 and tx<=m-1 and ty>=0 and ty<=n-1 and board[tx][ty]=='O':
                            stack.append((tx,ty))
                            board[tx][ty]="#"
        def solve_edge(i,j):
            if board[i][j]=='O':
                change_map(i,j)
        
        for j in range(n):
            solve_edge(0,j)                     
        for j in range(n):
            solve_edge(m-1,j)        
        for i in range(m):
            solve_edge(i,0)
        for i in range(m):
            solve_edge(i,n-1)
        
        for i in range(m):
            for j in range(n):
                if board[i][j]=="#":
                    board[i][j]="O"
                elif board[i][j]=="O":
                    board[i][j]="X"
        return board


    def solve1(self, board: List[List[str]]) -> None:
        m=len(board)
        n=len(board[0])
        visit=[[False]*n for i in range(m)]
        all_direct=[[1,0],[0,1],[0,-1],[-1,0]]
        for i in range(m):
            for j in range(n):
                if visit[i][j]:
                    continue
                if board[i][j]=='X':
                    visit[i][j]=True
                    continue
                else:
                    valid=False
                    stack=[(i,j)]
                    deletestack=[(i,j)]
                    visit[i][j]=True
                    while True:
                        if not stack:
                            break
                        for k in range(len(stack)):
                            sx,sy=stack.pop()
                            if sx==0 or sx==m-1 or sy==0 or sy==n-1:
                                valid=True
                            for direct in all_direct:
                                tx=sx+direct[0]
                                ty=sy+direct[1]
                                if tx>=0 and tx<=m-1 and ty>=0 and ty<=n-1 and not visit[tx][ty] and board[tx][ty]=='O':
                                    deletestack.append((tx,ty))
                                    stack.append((tx,ty))
                                    visit[tx][ty]=True
                    if not valid:
                        for k in range(len(deletestack)):
                            x,y=deletestack.pop()
                            board[x][y]='X'
        """
        Do not return anything, modify board in-place instead.
        """
        return board
sol=Solution()
board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
board1=[["O","O","O"],["O","O","O"],["O","O","O"]]
board2=[["X","O","X","X"],["O","X","O","X"],["X","O","X","O"],["O","X","O","X"]]
board3=[["X","O","X","O","X","O"],["O","X","O","X","O","X"],["X","O","X","O","X","O"],["O","X","O","X","O","X"]]
print(sol.solve(board3))


# 输入：board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
# 输出：[["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
# 解释：被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。


