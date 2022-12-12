
import collections
from typing import  List,Optional
import copy

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        lena=len(a)
        lenb=len(b)
        #a是大的
        if lena<lenb:
            a,b=b,a
            lena,lenb=lenb,lena
        b='0'*(lena-lenb)+b
        lista=list(a)
        listb=list(b)
        ans=''
        add=0
        for i in range(lena-1,-1,-1):
            temp=int(lista[i])+int(listb[i])+add 
            if temp>=2:
                ans+=str(temp-2)
                add=1
            else:
                add=0
                ans+=(str(temp))
        if add==1:
            ans+='1'
        return ans[::-1]
sol=Solution()
a = "11"
b = "1"
print(sol.addBinary(a,b))
# 输入: a = "11", b = "1"
# 输出: "100"

