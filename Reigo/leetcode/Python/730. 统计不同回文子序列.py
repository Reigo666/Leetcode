class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        n=len(s)
        dp=[[0]*n for i in range(n)]
        mod=10**9+7
        for j in range(n):
            for i in range(j,-1,-1):
                if i==j:
                    dp[i][j]=1
                elif j-i==1:
                    dp[i][j]=2
                else:
                    if s[i]==s[j]:
                        left=-1
                        right=-1
                        for k in range(i+1,j):
                            if s[i]==s[k]:
                                left=k
                                break
                        if left!=-1:
                            for k in range(j-1,i,-1):
                                if s[i]==s[k]:
                                    right=k
                                    break
                        
                        if left==-1:
                            dp[i][j]=dp[i+1][j-1]*2+2
                        elif left==right:
                            dp[i][j]=dp[i+1][j-1]*2+1
                        else:
                            if right-left==1:
                                dp[i][j]=dp[i+1][j-1]*2
                            else:
                                dp[i][j]=dp[i+1][j-1]*2-dp[left+1][right-1]
                    else:
                        dp[i][j]=dp[i+1][j]+dp[i][j-1]-dp[i+1][j-1]
                    if dp[i][j]>mod:
                        dp[i][j]=dp[i][j]%mod
                    if dp[i][j]<0:
                        dp[i][j]=dp[i][j]+mod
        return dp[0][n-1]
sol=Solution()
s="ab"
print(sol.countPalindromicSubsequences(s))