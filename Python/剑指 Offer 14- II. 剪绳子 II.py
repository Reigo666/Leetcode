class Solution:
    def cuttingRope(self, n: int) -> int:
        if n==2:return 1
        if n==3:return 2
        if n==4:return 4
        __MOD__=1000000007
        print(3**40)
        if n%3==0:
            return 3**(n//3)%__MOD__
        if n%3==1:
            return 3**(n//3-1)*4%__MOD__
        if n%3==2:
            return 3**(n//3)*2%__MOD__