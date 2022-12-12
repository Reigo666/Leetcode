class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def check(n,k):
            if n==1:
                return 0
            if n==2:
                if k==1:
                    return 0
                if k==2:
                    return 1
            if k>(2**(n-2)):
                if check(n-1,k-2**(n-2)):
                    return 0
                else:
                    return 1
            else:
                return check(n-1,k)
        return check(n,k)