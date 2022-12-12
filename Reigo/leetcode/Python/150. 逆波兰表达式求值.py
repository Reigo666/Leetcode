
import collections
from typing import  List,Optional
import copy

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for token in tokens:
            if token=="+" or token=="-" or token=="*" or token=="/":
                val2=stack.pop()
                val1=stack.pop()
                newval=0
                if token=='+':
                    newval=val1+val2
                elif token=='-':
                    newval=val1-val2
                elif token=='*':
                    newval=val1*val2
                elif token=='/':
                    rev=False
                    if val1<0:
                        val1=-val1
                        rev=not rev
                    if val2<0:
                        val2=-val2
                        rev=not rev
                    newval=val1//val2
                    if rev:
                        newval=-newval
                stack.append(newval)
            else:
                stack.append(int(token))
        return stack[0]

sol=Solution()
tokens = ["2","1","+","3","*"]
tokens1=["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(sol.evalRPN(tokens1))


# 输入：tokens = ["2","1","+","3","*"]
# 输出：9
# 解释：该算式转化为常见的中缀算术表达式为：((2 + 1) * 3) = 9
