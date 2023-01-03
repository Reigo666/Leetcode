class Solution:
    def minimumLength(self, s: str) -> int:
        l=0
        r=len(s)-1

        while l<r:
            if s[l]!=s[r]:
                break
            cur=s[l]
            while l<=r and s[l]==cur:
                l+=1
            while l<=r and s[r]==cur:
                r-=1

        if l>r:
            return 0
        return r-l+1