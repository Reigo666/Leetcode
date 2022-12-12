class Solution:
    def trailingZeroes(self, n: int) -> int:
        num=0
        ans=0
        while num<=n:
            if num!=0:
                ans+=1
                temp=num
                while temp//5%5==0:
                    ans+=1
                    temp=temp//5
            num+=5
        return ans