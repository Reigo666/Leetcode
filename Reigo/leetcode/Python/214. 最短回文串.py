import collections
from typing import  List,Optional
import copy
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        n=len(s)
        if n==0:
            return ""
        for i in range(n-1,-1,-1):
            if s[0:i+1]==s[0:i+1][::-1]:
                return s[i+1:][::-1]+s
        
        #ccbb aa bbcc
sol=Solution()
s = "aacecaaa"
print(sol.shortestPalindrome(s))              