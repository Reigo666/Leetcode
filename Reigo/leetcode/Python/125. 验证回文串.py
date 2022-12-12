
import collections

from typing import  List,Optional
import copy

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1
        while True:
            if r<=l:
                break
            if not s[l].isalnum():
                while not s[l].isalnum():
                    l+=1
                    if l>=r:
                        return True
            if not s[r].isalnum():
                while not s[r].isalnum():
                    r-=1
            if s[l].lower()==s[r].lower():
                l+=1
                r-=1
            else:
                return False
        return True
sol=Solution()
s="A man, a plan, a canal: Panama"
print(sol.isPalindrome(s))

# 输入: "A man, a plan, a canal: Panama"
# 输出: true
# 解释："amanaplanacanalpanama" 是回文串


