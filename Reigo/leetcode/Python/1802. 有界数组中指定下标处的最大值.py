class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        #2,3,2,1
        #1,1,2,1
        
        def calc(l,r):
            if l<=0:
                return (1+r)*(r)//2+(1-l)
            else:
                return (l+r)*(r-l+1)//2
        def check(mid):
            lval=calc(mid-index,mid-1)
            #print(mid-n+index+1,mid-1)
            rval=calc(mid-n+index+1,mid-1)
            #print(mid,lval,rval,lval+rval+mid)
            return lval+rval+mid<=maxSum
        l=1
        r=maxSum

        cnt=20
        while l<r:
            # cnt-=1
            # if cnt==0:
            #     break
            mid=(l+r+1)//2
            #print(mid,l,r)
    
            if check(mid):
                l=mid
            else:
                r=mid-1
        
        return l