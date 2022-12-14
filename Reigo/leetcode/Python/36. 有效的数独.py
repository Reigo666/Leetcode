from typing import List,Optional

class Solution:
    #hashmap方法 初始化每一行 每一列 每一个box中[1:9]的值为0 出现过就改为1
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row=[[0]*9 for i in range(9)]
        col=[[0]*9 for i in range(9)]
        box=[[0]*9 for i in range(9)]
        for i in range(9):
            for j in range(9):
                val=board[i][j]
                if val=='.':continue
                idx=int(val)-1
                if row[i][idx]==1 or col[j][idx]==1 or box[(i//3)*3+j//3][idx]==1:
                    return False
                row[i][idx]=1 
                col[j][idx]=1 
                box[(i//3)*3+j//3][idx]=1
        return True
sol=Solution()

board = \
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(board)
print(sol.isValidSudoku(board))

# 输入：board = 
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# 输出：false
