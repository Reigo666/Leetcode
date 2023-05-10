class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        n=1
        for i in range(k):
            if n%k==0:
                return i+1
            n=(n*10+1)%k

        return -1