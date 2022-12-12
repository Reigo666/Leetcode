class Solution:
    def divide(self, a: int, b: int) -> int:
        __MIN__=-2**31
        __MAX__=2**31-1
        rev=False
        if a<0:
            a=-a
            rev=not rev
        if b<0:
            b=-b
            rev=not rev
        
        #print(rev)
        ret=a//b
        #print(a,b,ret)
        if rev:
            ret=-ret
        #print(ret)
        if ret>__MAX__ or ret<__MIN__:
            return __MAX__
        return ret
        