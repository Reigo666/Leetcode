class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        idx=0
        for i in range(1,n+1):
            if i==1:
                idx=0
            else:
                idx=(m+idx)%i
            #print(idx)
        return idx