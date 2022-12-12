
import collections
from typing import  List,Optional
import copy
class Solution:
    def simplifyPath(self, path: str) -> str:
        lens=len(path)
        l=0
        ansstack=[]
        numdot=0
        while l<=lens-1:
            if path[l]=='/':
                if ansstack==[] or ansstack[-1]!='/':
                    ansstack.append('/')    
            else:
                tempstr=path[l]
                l+=1
                while l<=lens-1 and path[l]!='/':
                    tempstr+=path[l]
                    l+=1
                l-=1
                    
                if tempstr=="..":
                    if len(ansstack)>=3:
                        ansstack.pop()
                        ansstack.pop()
                elif tempstr=='.':
                    pass
                else:
                    ansstack.append(tempstr)
            l+=1
        if len(ansstack)>=2 and ansstack[-1]=='/':
            ansstack.pop()
        ansstr="".join(ansstack)
        return ansstr
sol=Solution()
path = "/a/./b/../../c/"
print(sol.simplifyPath(path))

# 输入：path = "/a/./b/../../c/"
# 输出："/c"
