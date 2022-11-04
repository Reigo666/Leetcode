class Solution:
    def reachNumber(self, target: int) -> int:
        if target<0:target=-target
        l=1
        r=math.ceil(math.sqrt(2*target))

        def solve(target,l,r):
            while(l<r):
                mid=(l+r)//2
                if mid*(mid+1)==2*target:
                    return mid
                elif mid*(mid+1)>2*target:
                    r=mid
                else:
                    l=mid+1
            return l
        
        k=solve(target,l,r)
        #print(k)
        s=(1+k)*k//2
        
        dert=s-target
        print(k,s,dert)
        if dert%2==0:
            return k
        else:
            if k%2==1:
                return k+2
            else:
                return k+1