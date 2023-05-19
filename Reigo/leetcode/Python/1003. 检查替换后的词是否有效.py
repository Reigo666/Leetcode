class Solution:
    def isValid(self, str: str) -> bool:
        s=[]
        for l in str:
            s.append(l)
            if l=='c':
                if len(s)<3:
                    return False
                c=s.pop()
                b=s.pop()
                a=s.pop()
                if a!='a' or b!='b':
                    return False
            if len(s)==1 and s[0]!='a':
                return False
            #print(s)
        if s:
            return False
        return True