class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        def solve(s):
            res=[]
            if s=="0" or s[0]!='0':
                res.append(s)
            if s[-1]=='0':return res
            for i in range(1,len(s)):
                if i!=1 and s[0]=='0':
                    break
                temp=s[:i]+'.'+s[i:]
                res.append(temp)
            return res

        s=s[1:-1]
        ans=[]
        for i in range(1,len(s)):
            l=s[:i]
            r=s[i:]
            ll=solve(l)
            if len(ll)==0:
                continue
            rr=solve(r)
            if len(rr)==0:
                continue
            
            for j in range(len(ll)):
                for k in range(len(rr)):
                    temp='('+ll[j]+', '+rr[k]+')'
                    #print(rr[k])
                    ans.append(temp)
        
        return ans