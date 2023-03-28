class Solution:
    def shortestCommonSupersequence(self, s: str, t: str) -> str:
        s=' '+s
        t=' '+t
        m=len(s)
        n=len(t)


        dp=[[0]*n for _ in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                if s[i]==t[j]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])

        def backTrack(dp):
            i,j=m-1,n-1
            ans=''
            while i>=0 and j>=0:
                if i==0:
                    ans+=t[1:j+1][::-1]
                    break
                elif j==0:
                    ans+=s[1:i+1][::-1]
                    break
                else:
                    if s[i]==t[j]:
                        ans+=s[i]
                        i-=1
                        j-=1
                    else:
                        if dp[i-1][j]>=dp[i][j-1]:
                            ans+=s[i]
                            i-=1
                        else:
                            ans+=t[j]
                            j-=1
                #print(ans)
            return ans[::-1]
        #print(dp)
        ans=backTrack(dp)
        return ans

        #
#[[0, 0, 0, 0, 0, 0], 
# [0, 1, 1, 1, 1, 1], 
# [0, 1, 1, 1, 1, 1], 
# [0, 1, 1, 2, 2, 2], 
# [0, 1, 1, 2, 2, 2], 
# [0, 1, 1, 2, 3, 3]]