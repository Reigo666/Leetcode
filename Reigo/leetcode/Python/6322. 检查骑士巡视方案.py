class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        all_direct=[[2,1],[2,-1],[1,2],[1,-2],[-2,-1],[-2,1],[-1,-2],[-1,2]]

        n=len(grid)
        def dfs(i,j,cur):
            if cur==n*n-1:
                return True
            for direct in all_direct:
                tx,ty=i+direct[0],j+direct[1]
                if tx>=0 and tx<n and ty>=0 and ty<n and grid[tx][ty]==cur+1:
                    if dfs(tx,ty,cur+1):
                        return True
            return False

        
        if grid[0][0]==0:
            return dfs(0,0,0)
        return False

# [[24,11,22,17,4],
#  [21,16,5,12,9],
#  [6,23,10,3,18],
#  [15,20,1,8,13],
#  [0, 7,14,19,2]]