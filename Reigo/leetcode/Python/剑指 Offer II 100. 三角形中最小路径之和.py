class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m=len(triangle[-1])

        dp=[0]*m
        dp[0]=triangle[0][0]
        for i in range(1,len(triangle)):
            for j in range(len(triangle[i])-1,-1,-1):
                if j==0:
                    dp[j]=dp[j]+triangle[i][j]
                elif j==len(triangle[i])-1:
                    dp[j]=dp[j-1]+triangle[i][j]
                else:
                    dp[j]=min(dp[j-1],dp[j])+triangle[i][j]
            #print(dp)
        return min(dp)