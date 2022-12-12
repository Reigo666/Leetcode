
import collections
from typing import  List,Optional

class Solution:
    def myPow(self, x: float, n: int) -> float:
        rev=False
        if n<0:
            rev=True
            n=-n
        def myPowdm(x,n):
            if n==0:
                return 1
            elif n==1:
                return x
            else:
                a=myPowdm(x,n//2)
                if n%2!=0:
                    return a*a*x
                else:
                    return a*a
        ans=myPowdm(x,n)
        return 1/ans if rev else ans
sol=Solution()
x = 2.00000
n = -2
print(sol.myPow(x,n))

# 输入：x = 2.00000, n = -2
# 输出：0.25000
# 解释：2-2 = 1/22 = 1/4 = 0.25



