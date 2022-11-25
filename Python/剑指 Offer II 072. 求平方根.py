class Solution:
    def mySqrt(self, x: int) -> int:
        def solve(x):
            l=0
            r=x

            while l<r:
                #print(l,r)
                mid=(l+r)//2
                mm=mid*mid
                m1m1=(mid+1)*(mid+1)
                if mm==x:
                    return mid
                elif m1m1==x:
                    return mid+1
                if mm>x:
                    r=mid-1
                elif m1m1<x:
                    l=mid+1
                elif mm<x and m1m1>x:
                    return mid
            return l
        return solve(x)