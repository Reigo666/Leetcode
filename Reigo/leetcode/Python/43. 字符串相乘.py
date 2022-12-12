from typing import List,Optional

class Solution:
    
    def multiply(self, num1: str, num2: str) -> str:
        if num1=="0" or num2=="0":
            return "0"
        len1=len(num1)
        len2=len(num2)

        if len1<len2:
            num1,num2=num2,num1
            len1,len2=len2,len1
        
        ansstr="0"
        for i in range(len2):
            temp=self.stringMulLetter(num1,num2[len2-i-1])+"0"*i
            ansstr=self.stringAddString(ansstr,temp)
        return ansstr
    
    def stringMulLetter(self, num1: str, num2: str):
        ans=[]
        for i,digit in enumerate(num1):
            ans.append(int(digit)*int(num2))
        
        ans=ans[::-1]
        ans=self.carryCalc(ans)

        ans=ans[::-1]
        return "".join(str(x) for x in ans)

    def stringAddString(self, num1: str, num2: str):
        num1=num1[::-1]
        num2=num2[::-1]
        len1=len(num1)
        len2=len(num2)
        if len1<len2:
            num1+='0'*(len2-len1)
        else:
            num2+='0'*(len1-len2)
        
        s1= [int(x) for x in num1]
        s2= [int(x) for x in num2]
        ans=[]
        for i in range(len(num1)):
            ans.append(s1[i]+s2[i])
        
        ans=self.carryCalc(ans)
        ans=ans[::-1]

        return "".join(str(x) for x in ans)

    def carryCalc(self,ans:List[int]):
        carry=0
        for i,val in enumerate(ans):
            val+=carry
            carry=val//10
            ans[i]=val%10
        if carry:
            ans.append(carry)
        return ans
sol=Solution()

num1 = "123"
num2 = "456"
print(sol.multiply(num1,num2))


# 输入: num1 = "123", num2 = "456"
# 输出: "56088"

