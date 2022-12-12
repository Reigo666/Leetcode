
import collections
from typing import  List,Optional
import copy
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans=[]
        map=['.'*n]*n
        #print(map)
        colmap=[False]*n
        rdiagmap=[False]*(2*n-1)
        ldiagmap=[False]*(2*n-1)

        def backTrack(map,colmap,rdiagmap,ldiagmap,row,n):
            if row==n:
                ans.append(copy.deepcopy(map))
            else:
                #在row这一行 尝试在每一列加入queen
                for j in range(n):
                    if colmap[j] or ldiagmap[n-1-row+j] or rdiagmap[row+j]:
                        continue
                    else:
                        colmap[j],ldiagmap[n-1-row+j] , rdiagmap[row+j]=True,True,True
                        map[row]=map[row][:j]+"Q"+map[row][j+1:]
                        #print(map)
                        backTrack(map,colmap,rdiagmap,ldiagmap,row+1,n)
                        map[row]=map[row][:j]+"."+map[row][j+1:]
                        colmap[j],ldiagmap[n-1-row+j] , rdiagmap[row+j]=False,False,False
        
        backTrack(map,colmap,rdiagmap,ldiagmap,0,n)
        return ans
sol=Solution()
n = 4
print(sol.solveNQueens(n))



# 输入：n = 4
# 输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# 解释：如上图所示，4 皇后问题存在两个不同的解法。




