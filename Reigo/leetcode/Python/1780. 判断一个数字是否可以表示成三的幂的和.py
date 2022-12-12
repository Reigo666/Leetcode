class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        pow3=[1]*17
        for i in range(1,17):
            pow3[i]=pow3[i-1]*3
        
        for i in range(16,-1,-1):
            if n==0:
                return True
            if pow3[i]<=n:
                n-=pow3[i]
            #print(n)
        if n==0:
            return True
        return False