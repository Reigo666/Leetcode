from typing import List,Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle=="":return 0
        lenl=len(haystack)
        lenr=len(needle)
        for l in range(lenl):
            if l+lenr-1<lenl:
                if haystack[l:l+lenr]==needle:
                    return l
            else:return -1
        return -1
sol=Solution()
haystack = "hello"
needle = "ll"
print(sol.strStr(haystack,needle))

# 输入：haystack = "hello", needle = "ll"
# 输出：2


