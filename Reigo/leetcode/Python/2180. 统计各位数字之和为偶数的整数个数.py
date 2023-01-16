class Solution:
    def countEven(self, num: int) -> int:
        ans=0
        for i in range(2,num+1):
            x=i
            s=0
            while x:
                s+=x%10
                x//=10
            if s%2==0:
                ans+=1
        return ans