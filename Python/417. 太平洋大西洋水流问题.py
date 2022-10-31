import collections
from typing import  List,Optional
import copy
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m=len(heights)
        n=len(heights[0])
        dp=[[0]*n for i in range(m)]
        visit=[[False]*n for i in range(m)]
        if m==1 or n==1:
            if m==1:
                for j in range(n):
                    dp[0][j]=3
                    visit[0][j]=True
            elif n==1:
                for i in range(m):
                    dp[i][0]=3
                    visit[i][0]=True
        else:
            for i in range(m):
                dp[i][0]=1
                dp[i][n-1]=2
            for j in range(n):    
                dp[0][j]=1    
                dp[m-1][j]=2
            dp[0][n-1]=3
            dp[m-1][0]=3
            
            visit[0][n-1]=True
            visit[m-1][0]=True


        all_direct=[[0,1],[0,-1],[1,0],[-1,0]]
        def solvedp(i,j,tx,ty):
            if dp[tx][ty]==3:
                dp[i][j]=3
            elif dp[i][j]==3:
                pass
            elif dp[i][j]==0:
                dp[i][j]=dp[tx][ty]
            elif dp[i][j]==1:
                if dp[tx][ty]==2:
                    dp[i][j]=3
            elif dp[i][j]==2:
                if dp[tx][ty]==1:
                    dp[i][j]=3
        def dfs(i,j):   
            visit[i][j]=True
            for direct in all_direct:
                tx,ty=i+direct[0],j+direct[1]
                if tx<0 or tx>=m or ty<0 or ty>=n:
                    continue
                if visit[tx][ty]:
                    if heights[i][j]>=heights[tx][ty]:
                        solvedp(i,j,tx,ty)
                else:
                   

                    if heights[i][j]>heights[tx][ty]:
                        dfs(tx,ty)
                        solvedp(i,j,tx,ty)
                    elif heights[i][j]==heights[tx][ty]:
                        dfs(tx,ty)
                        solvedp(i,j,tx,ty)
                        visit[tx][ty]=False
                  
                
        
        anslist=[]
        for i in range(m):
            for j in range(n):
                if visit[i][j]:
                    if dp[i][j]==3:
                        anslist.append([i,j])
                else:
                    dfs(i,j)
                    if dp[i][j]==3:
                        anslist.append([i,j])
        return anslist
heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
heights1=[[2,1],[1,2]]
heights2=[[13],[4],[19],[10],[1],[11],[5],[17],[3],[10],[1],[0],[1],[4],[1],[3],[6],[13],[2],[16],[7],[6],[3],[1],[9],[9],[13],[10],[9],[10],[6],[2],[11],[17],[13],[0],[19],[7],[13],[3],[9],[2]]
sol=Solution()
print(sol.pacificAtlantic(heights2))           
# 输入: heights = [
# [1,2,2,3,5],
# [3,2,3,4,4],
# [2,4,5,3,1],
# [6,7,1,4,5],
# [5,1,1,2,4]]
# 输出: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

              
                

