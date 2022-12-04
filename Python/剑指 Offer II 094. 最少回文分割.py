class Solution:
    def minCut(self, s: str) -> int:
        n=len(s)
        f=[[False]*n for _ in range(n)]
        
        for j in range(n):
            for i in range(j,-1,-1):
                if s[i]==s[j]:
                    if i+1<=j-1 and i+1<n and j>=1:
                        if f[i+1][j-1]:
                            f[i][j]=True
                    else:
                        f[i][j]=True
                #print(i,j,f)
        #print(f)
        if f[0][n-1]:
            return 0
        dp=[inf]*n
        
        for i in range(n):
            if f[0][i]:
                dp[i]=0
            else:
                for j in range(1,i+1):
                    if f[j][i]:
                        dp[i]=min(dp[i],dp[j-1]+1)
        #print(dp)
        return dp[n-1]
        


                