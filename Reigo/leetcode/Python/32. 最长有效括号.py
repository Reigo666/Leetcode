from typing import List,Optional

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        ans=0
        dp=[0]
        if s=="":
            return ans
        lens=len(s)
        for i in range(1,lens):
            if s[i]=='(':
                dp.append(0)
            elif s[i]==')':
                if s[i-1]=='(':
                    if i>=2:
                        dp.append(dp[i-2]+2)
                    else:
                        dp.append(2)
                if s[i-1]==')':
                    if dp[i-1]==0:
                        dp.append(0)
                    elif dp[i-1]>0:
                        if i-dp[i-1]-1>=0:
                            if s[i-dp[i-1]-1]=='(':
                                if i-dp[i-1]-2>=0:
                                    dp.append(dp[i-1]+2+dp[i-dp[i-1]-2])
                                else:
                                    dp.append(dp[i-1]+2)
                            elif s[i-dp[i-1]-1]==')':
                                dp.append(0)
                        else:
                            dp.append(0)
            if dp[i]>ans:ans=dp[i]
        #print(dp)
        return ans
        
    def longestValidParentheses1(self, s: str) -> int:
        dp=[0]*len(s)
        ans=0
        for i in range(len(s)):
            if s[i]=='(':
                continue
            elif s[i]==')':
                if i-1>=0:
                    if s[i-1]=='(':
                        if i-2>=0:
                            dp[i]=dp[i-2]+2
                        else:
                            dp[i]=2
                    elif s[i-1]==')':
                        if i-dp[i-1]-1>=0:
                            if s[i-dp[i-1]-1]=='(':
                                if i-dp[i-1]-2>=0:
                                    dp[i]=dp[i-1]+2+dp[i-dp[i-1]-2]
                                else:
                                    dp[i]=dp[i-1]+2
                        else:
                            dp[i]=0
                else:
                    dp[i]=0
        
            ans=max(ans,dp[i])
        return ans
sol=Solution()

s1 = ")()())"
s2="(()))())("
print(sol.longestValidParentheses(s2))


# 输入：s = ")()())"
# 输出：4
# 解释：最长有效括号子串是 "()()"