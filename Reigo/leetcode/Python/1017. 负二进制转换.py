class Solution:
    def baseNeg2(self, n: int) -> str:
        if n==0:
            return '0'
        
        ans=''
        while n:
            mod=n%2
            ans+=str(mod)
            n=-(n//2)
        return ans[::-1]