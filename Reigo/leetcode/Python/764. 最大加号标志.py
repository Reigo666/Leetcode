class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        dp=[[n]*n for _ in range(n)]
        banned=set(map(tuple,mines))
        print(banned)
        for i in range(n):
            cnt=0
            for j in range(n):
                if (i,j) in banned:
                    cnt=0
                else:
                    cnt+=1
                dp[i][j]=min(dp[i][j],cnt)
            cnt=0
            for j in range(n-1,-1,-1):
                if (i,j) in banned:
                    cnt=0
                else:
                    cnt+=1
                dp[i][j]=min(dp[i][j],cnt)
            
        ans=0
        for j in range(n):
            cnt=0
            for i in range(n):
                if (i,j) in banned:
                    cnt=0
                else:
                    cnt+=1
                dp[i][j]=min(dp[i][j],cnt)
            cnt=0
            for i in range(n-1,-1,-1):
                if (i,j) in banned:
                    cnt=0
                else:
                    cnt+=1
                dp[i][j]=min(dp[i][j],cnt)
                ans=max(ans,dp[i][j])
        #print(dp)
        return ans