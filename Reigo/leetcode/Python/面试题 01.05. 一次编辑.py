class Solution:
    #更好的方法是双指针 如果长度相等只考虑替换 如果长度不相等只考虑一次增加操作
    def oneEditAway(self, first: str, second: str) -> bool:
        len1=len(first)
        len2=len(second)
        if abs(len1-len2)>=2:
            return False
        dp=[[0]*(len2+1) for i in range(len1+1)]
        for i in range(1,len1+1):
            dp[i][0]=dp[i-1][0]+1
        for j in range(1,len2+1):
            dp[0][j]=dp[0][j-1]+1
        for i in range(1,len1+1):
            for j in range(1,len2+1):
                if first[i-1]==second[j-1]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j]=min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
        if dp[len1][len2]<=1:
            return True
        else:
            return False