class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1)+len(s2)!=len(s3):
            return False
        s1=" "+s1
        s2=" "+s2
        s3=" "+s3
        m=len(s1)
        n=len(s2)

        dp=[[False]*n for _ in range(m)]
        dp[0][0]=True
        for i in range(1,m):
            if s1[i]==s3[i]:
                dp[i][0]=True
            else:
                break
        for i in range(1,n):
            if s2[i]==s3[i]:
                dp[0][i]=True
            else:
                break
        
        for i in range(1,m):
            for j in range(1,n):
                if s1[i]==s3[i+j]:
                    if dp[i-1][j]:
                        dp[i][j]=True
                if s2[j]==s3[i+j]:
                    if dp[i][j-1]:
                        dp[i][j]=True
        
        return dp[m-1][n-1]
