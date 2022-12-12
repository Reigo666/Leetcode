
import collections
from typing import  List,Optional
import copy
class Solution:
    #动态规划
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1)+len(s2)!=len(s3):
            return False
        if not s1 and not s2 and not s3:
            return True
        len1=len(s1)
        len2=len(s2)
        dp=[[False]*(len2+1) for i in range(len1+1)]
        dp[0][0]=True
        for i in range(1,len1+1):
            if s1[:i]==s3[:i]:
                dp[i][0]=True
        for j in range(1,len2+1):
            if s2[:j]==s3[:j]:
                dp[0][j]=True
        for i in range(1,len1+1):
            for j in range(1,len2+1):
                if dp[i-1][j]==False and dp[i][j-1]==False:
                    dp[i][j]=False
                else:
                    if dp[i-1][j]==True: 
                        if s1[i-1]==s3[i+j-1]:
                            dp[i][j]=True
                            continue
                    if dp[i][j-1]==True: 
                        if s2[j-1]==s3[i+j-1]:
                            dp[i][j]=True
                            continue
                    dp[i][j]=False
        return dp[len1][len2]
    #递归不行
    def isInterleave1(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1)+len(s2)!=len(s3):
            return False
        if not s1 and not s2 and not s3:
            return True
        def Recursion(s1,s2,s3):
            if not s1:
                if s2==s3:
                    return True
                else:return False
            if not s2:
                if s1==s3:
                    return True
                else:return False
            if s1[0]==s3[0] and s2[0]==s3[0]:
                return Recursion(s1[1:],s2,s3[1:]) or Recursion(s1,s2[1:],s3[1:])
            elif s1[0]==s3[0]:
                return Recursion(s1[1:],s2,s3[1:])
            elif s2[0]==s3[0]:
                return Recursion(s1,s2[1:],s3[1:])
            else:
                return False
        return Recursion(s1,s2,s3)
    
sol=Solution()

s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
print(sol.isInterleave(s1,s2,s3))




# 输入：s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# 输出：true


