class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x=int(a)+int(b)
        if x==0:
            return '0'
        ans=""
        carry=False
        #print(x)
        while x:
            #return 0
            temp=x%10
            if carry:
                carry=False
                temp+=1
            if temp>=2:
                temp-=2
                carry=True
            ans=str(temp)+ans
            x//=10
            #print(temp,x,carry)
        if carry:
            ans='1'+ans
        
        return ans
            