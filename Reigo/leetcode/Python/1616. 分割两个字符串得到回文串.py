class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        #f ecab
        #abde f


        #abcba
        #yuiia

        def check(a,b):
            l=0
            r=len(a)-1
            while l<r and a[l]==b[r]:
                l+=1
                r-=1
            s=a[l:r+1]
            t=b[l:r+1]
            return s==s[::-1] or t==t[::-1]

        return check(a,b) or check(b,a)


        
        