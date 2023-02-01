class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        visit=[[False]*len(grid) for _ in range(len(grid))]
        for i in range(len(grid)):
            if grid[i][i]==0:
                return False
            visit[i][i]=True
        
        for i in range(len(grid)):
            if grid[i][len(grid)-i-1]==0:
                return False
            visit[i][len(grid)-i-1]=True
        
        #print(visit)

        for i in range(len(grid)):
            for j in range(len(grid)):
                if not visit[i][j] and grid[i][j]!=0:
                    #print(i,j,grid[i][j])
                    return False
        
        return True