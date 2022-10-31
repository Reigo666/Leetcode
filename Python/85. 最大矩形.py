
import collections
from typing import  List,Optional
import copy

class Solution:
    #单调栈解法
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m=len(matrix)
        n=len(matrix[0])
        height=[0]*n
        def calculateMaxRectangle(height1:List[int])->int:
            height=copy.deepcopy(height1)
            stack=[0]
            height.insert(0,0)
            height+=[0]
            n=len(height)
            lastheight=0
            ans=0
            for i in range(1,n):
                h=height[i]
                if h<lastheight:
                    idr=i
                    while lastheight>h:
                        stack.pop()
                        idl=stack[-1]
                        ans=max(ans,lastheight*(idr-idl-1))
                        lastheight=height[stack[-1]]
                    lastheight=h
                    stack.append(i)
                else:
                    lastheight=h 
                    stack.append(i)
            return ans

        ans=0
        for i in range(m):
            for j in range(n):
                if matrix[i][j]=='0':
                    height[j]=0
                else:
                    height[j]+=1
            print(height)
            ans=max(ans,calculateMaxRectangle(height))
        return ans



    #暴力解法
    def maximalRectangle2(self, matrix: List[List[str]]) -> int:
        m=len(matrix)
        n=len(matrix[0])
        dp=[[0]*(n+1) for i in range(m+1)]
        ans=0
        for i in range(1,m+1):
            for j in range(1,n+1):
                if matrix[i-1][j-1]=='0':
                    pass
                else:
                    dp[i][j]=dp[i][j-1]+1
                    row_num=1
                    tempmin=dp[i][j]
                    for k in range(i,0,-1):
                        tempmin=min(tempmin,dp[k][j])
                        if not tempmin:break
                        ans=max(ans,row_num*tempmin)
                        row_num+=1
        return ans

    #bad
    def maximalRectangle1(self, matrix: List[List[str]]) -> int:
        m=len(matrix)
        n=len(matrix[0])
        dp=[[(0,0)]*(n+1) for i in range(m+1)]
        ans=0

        for i in range(1,m+1):
            for j in range(1,n+1):
                temp=matrix[i-1][j-1]
                if matrix[i-1][j-1]=='0':
                    dp[i][j]=(0,0)
                else:
                    dx=dp[i][j-1][0]+1
                    dy=dp[i-1][j][1]+1
                    dp[i][j]=(dx,dy)
                    if dx==1 or dy==1:
                        ans=max(ans,max(dx,dy))
                    else:
                        
                        if dx<=dy:
                            tempmin=dy
                            #向左几列查看
                            for k in range(0,dx):
                                #不满足矩形条件
                                if dp[i][j-k][1]<tempmin:
                                    tempmin=dp[i][j-k][1]
                                    ans=max(ans,tempmin*(k+1))
                                else:
                                    ans=max(ans,tempmin*(k+1))
                        else:

                            tempmin=dx
                            #向下几行查看
                            for k in range(0,dy):
                                #不满足矩形条件
                                if dp[i-k][j][0]<tempmin:
                                    tempmin=dp[i-k][j][0]
                                    ans=max(ans,tempmin*(k+1))
                                else:
                                    ans=max(ans,tempmin*(k+1))
        
        return ans
        
        
    

sol=Solution()
matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
matrix1=[["0","0","1","0"],["0","0","1","0"],["0","0","1","0"],["0","0","1","1"],["0","1","1","1"],["0","1","1","1"],["1","1","1","1"]]
print(sol.maximalRectangle(matrix1))
# 输入：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# 输出：6
# 解释：最大矩形如上图所示。

