
import collections
from multiprocessing import dummy
from typing import  List,Optional
import copy

class Solution:
    def numDecodings(self, s: str) -> int:
        lens=len(s)
        if s[0]=='0':
            return 0
        dp=[1]*lens
        for i in range(1,lens):
            letter=s[i]
            #dp[i]=dp[i-1]+dp[i-2]
            #当s[i]==0 and s[i-1]==1 or 2时dp[i]=dp[i-2] else return 0
            #当s[i]!=0 if s[i-1:i+1] valid dp[i]=dp[i-1]+dp[i-2] else dp[i]=dp[i-1]
            if s[i]=='0':
                if s[i-1]=='1' or s[i-1]=='2':
                    if i!=1:
                        dp[i]=dp[i-2]
                    elif i==1:
                        dp[i]=1
                else:
                    return 0
            elif s[i]!='0':
                if s[i-1]!='0' and int(s[i-1:i+1])<=26:
                    if i!=1:
                        dp[i]=dp[i-1]+dp[i-2]
                    elif i==1:
                        dp[1]=2
                else:
                    dp[i]=dp[i-1]
        return dp[lens-1]
sol=Solution()
s = "226"
s1="2611055971756562"
s2="2101"
print(sol.numDecodings(s1))

# 输入：s = "226"
# 输出：3
# 解释：它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。


