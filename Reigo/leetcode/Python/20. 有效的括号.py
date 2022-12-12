from typing import List


class Solution:
    #栈 判断结束时栈是否为空 pop前判断是否为空
    def isValid(self, s: str) -> bool:
        isvalid=True
        lens=len(s)
        lists=[]
        
        for i in range(lens):
            if s[i]=='('or s[i]=='{'or s[i]=='[':
                lists.append(s[i])
            else:
                if lists==[]:
                    return False
                if s[i]==')':
                    if lists.pop()!='(':
                        isvalid=False
                        break        
                elif s[i]=='}':
                    if lists.pop()!='{':
                        isvalid=False
                        break
                elif s[i]==']':
                    if lists.pop()!='[':
                        isvalid=False
                        break
        if lists!=[]:
            isvalid=False
        return isvalid
sol=Solution()

s1 = "{[]}"
s2="{]"
print(sol.isValid(s2))


# 输入：s = "{[]}"
# 输出：true