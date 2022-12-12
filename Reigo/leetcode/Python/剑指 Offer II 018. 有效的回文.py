class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1=""

        for l in s:
            if l.isalpha():
                s1+=l.lower()
            elif l.isdigit():
                s1+=l

        if s1==s1[::-1]:
            return True
        return False