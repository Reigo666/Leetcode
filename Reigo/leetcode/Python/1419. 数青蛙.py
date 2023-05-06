class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        c,r,o,a,k=0,0,0,0,0
        ans=-1
        for ch in croakOfFrogs:
            if ch=='c':
                c+=1
            elif ch=='r':
                if r==c:
                    return -1
                r+=1
            elif ch=='o':
                if o==r:
                    return -1
                o+=1
            elif ch=='a':
                if a==o:
                    return -1
                a+=1
            elif ch=='k':
                if k==a:
                    return -1
                k+=1
                c-=1
                r-=1
                o-=1
                a-=1
                k-=1
            ans=max(ans,c)
            #print(c,r,o,a,k)
        if c:
            return -1
        if ans==0:
            return -1
        return ans