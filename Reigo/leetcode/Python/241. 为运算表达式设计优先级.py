import collections
from typing import  List,Optional
import copy
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        num=[]
        op=[]
        ans=[]
        k=0
        while k<len(expression):
            tempnum=""
            while k<len(expression) and expression[k].isdigit():
                tempnum+=expression[k]
                k+=1
            num.append(tempnum)
            
            if k==len(expression):
                break
            op.append(expression[k])
            k+=1
        def calculate(a,op,b)->int:
            numa=int(a)
            numb=int(b)
            if op=="+":
                return int(numa+numb)
            elif op=="-":
                return int(numa-numb)
            elif op=="*":
                return int(numa*numb)
        
        #print(num)
        #print(op)

        dp=[[list()]*(len(num)) for _ in range(len(num))]
        for i in range(len(num)):
            dp[i][i]=[int(num[i])]
        #print(dp)
        for j in range(len(num)):
            for i in range(j,-1,-1):
                if i==j:
                    continue
                dp[i][j]=[]
                for k in range(i,j):
                    for numa in dp[i][k]:
                        for numb in dp[k+1][j]:
                            dp[i][j].append(calculate(numa,op[k],numb))
                #print(dp[i][j])
        return dp[0][len(num)-1]
