class Solution:
    def validPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1
        while l<r:
            if s[l]==s[r]:
                l+=1
                r-=1
            else:
                t1=s[l:r]
                t2=s[l+1:r+1]

                if t1==t1[::-1]:
                    return True
                if t2==t2[::-1]:
                    return True
                return False
        return True