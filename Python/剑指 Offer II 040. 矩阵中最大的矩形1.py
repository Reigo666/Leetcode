class Solution:
    def maximalRectangle(self, matrix: List[str]) -> int:
        #找左侧第一个比自己小的 和右侧第一个比自己小的
        def solve(heights):
            s=[]
            heights=[0]+heights
            ans=0
            for i in range(len(heights)):
                while s and heights[s[-1]]>heights[i]:
                    idx=s.pop()
                    ans=max(ans,heights[idx]*(i-s[-1]-1))
                s.append(i)

            r=len(heights)
            while len(s)>1:
                idx=s.pop()
                ans=max(ans,heights[idx]*(r-s[-1]-1))
            return ans
            
        
        m=len(matrix)
        if m==0:
            return 0
        n=len(matrix[0])

        up=[[0]*n for _ in range(m)]
        ans=0
        for i in range(m):
            for j in range(n):
                if matrix[i][j]=='1':
                    if i>=1:
                        up[i][j]=up[i-1][j]+1
                    elif i==0:
                        up[i][j]=1
            ans=max(ans,solve(up[i]))
            #print(up[i])
        return ans