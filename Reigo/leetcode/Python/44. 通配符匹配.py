from typing import List,Optional

class Solution:
    #动态规划
    def isMatch(self, s: str, p: str) -> bool:
        lenp=len(p)
        lens=len(s)
        
        newp=""
        for i in range(lenp):
            if i>=1:
                if p[i]=="*" and p[i-1]=='*':
                    continue
            newp+=p[i]
        #print(newp)
        p=newp
        lenp=len(p)
        
        dp=[[False]*(lens+1) for _ in range(lenp+1)]
        dp[0][0]=True
        #print(dp)
        for i in range(1,lenp+1):
            for j in range(0,lens+1):
                if j>=1:
                    if p[i-1]=='*':
                        if dp[i-1][j]==True or dp[i][j-1]==True:
                            dp[i][j]=True
                    elif p[i-1]=='?':
                        if dp[i-1][j-1]==True:
                            dp[i][j]=True
                    else:
                        if p[i-1]==s[j-1] and dp[i-1][j-1]==True:
                            dp[i][j]=True
                elif j==0:
                    if p[i-1]=='*':
                        if dp[i-1][j]==True:
                            dp[i][j]=True
                #print(dp)

        return dp[lenp][lens]
sol=Solution()

s1 = "adceb"
p1 = "*a*b"

s2 = "acdcb"
p2 = "a*c?b"

s3 = "babaaababaabababbbbbbaabaabbabababbaababbaaabbbaaab"
p3 = "***bba**a*bbba**aab**b"

s4="abbaabbbbababaababababbabbbaaaabbbbaaabbbabaabbbbbabbbbabbabbaaabaaaabbbbbbaaabbabbbbababbbaaabbabbabb"
p4="***b**a*a*b***b*a*b*bbb**baa*bba**b**bb***b*a*aab*a**"

print(sol.isMatch(s4,p4))

# 输入:
# s = "adceb"
# p = "*a*b"
# 输出: true
# 解释: 第一个 '*' 可以匹配空字符串, 第二个 '*' 可以匹配字符串 "dce".

# 输入:
# s = "acdcb"
# p = "a*c?b"
# 输出: false

