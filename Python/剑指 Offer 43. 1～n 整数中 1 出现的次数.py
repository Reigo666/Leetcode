class Solution:
    def countDigitOne(self, n: int) -> int:
        mult=9
        l=1
        r=1

        if 1<=n<=9:return 1

        bit=-1
        ans=0
        temp=10
        while n>=temp:
            bit+=1
            l=10**bit
            r=l*2-1

            k=n//temp
            a=n%temp

            ans+=(r-l+1)*k
            if a>=l and a<=r:
                ans+=a-l+1
            elif a>=r:
                ans+=r-l+1
            temp*=10
        #print(ans)
        a=n%temp
        bit+=1  
        l=10**bit
        r=l*2-1
        if a>=l and a<=r:
            ans+=a-l+1
        elif a>=r:
            ans+=r-l+1
        return ans