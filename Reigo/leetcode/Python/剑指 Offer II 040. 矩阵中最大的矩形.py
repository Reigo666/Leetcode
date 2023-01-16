class Solution:
    def maximalRectangle(self, matrix: List[str]) -> int:
        m=len(matrix)
        if m==0:
            return 0
        n=len(matrix[0])
        #print(m,n)
        #return 1
        dp=[[0]*n for _ in range(m)]
        ans=0

        for i in range(m):
            for j in range(n):
                if matrix[i][j]=='1':
                    if i>=1:
                        dp[i][j]=dp[i-1][j]+1
                    else:
                        dp[i][j]=1
                
                height=dp[i][j]
                for k in range(j,-1,-1):
                    if matrix[i][j]=='0':
                        break
                    height=min(height,dp[i][k])
                    ans=max(ans,height*(j-k+1))
        
        return ans
    
    def maximalRectangle1(self, matrix: List[str]) -> int:
        def solve(heights):
            heights=[0]+heights+[0]
            stack=[]
            ans=0
            for i,h in enumerate(heights):
                while stack and heights[stack[-1]]>h:
                    idx=stack.pop()
                    ans=max(ans,(i-stack[-1]-1)*heights[idx])
                stack.append(i)
            
            return ans
        
        if not matrix:
            return 0
        
        cur=[int(x) for x in list(matrix[0])]
        ans=0
        ans=max(ans,solve(cur))
        for i in range(1,len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]=='0':
                    cur[j]=0
                else:
                    cur[j]+=1
            ans=max(ans,solve(cur))
        return ans
