class Solution:
    def canChange(self, start: str, target: str) -> bool:
        s=[]
        t=[]

        for i,l in enumerate(start):
            if l=='_':
                continue
            else:
                s.append([l,i])
        
        for i,l in enumerate(target):
            if l=='_':
                continue
            else:
                t.append([l,i])
        
        if len(s)!=len(t):
            return False
        
        for i in range(len(s)):
            if s[i][0]!=t[i][0]:
                return False
            else:
                if s[i][0]=='L':
                    if s[i][1]<t[i][1]:
                        return False
                elif s[i][0]=='R':
                    if s[i][1]>t[i][1]:
                        return False
        
        return True