class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s=' '+s
        p=' '+p
        lens=len(s)
        lenp=len(p)
        
        def matches(i,j):
            if i==0:return False
            if p[j]=='.':
                return True
            if s[i]==p[j]:
                return True
            return False

        f=[[False]*lenp for _ in range(lens)]
        f[0][0]=True
        #print(f)
        for i in range(lens):
            for j in range(1,lenp):
                if matches(i,j):
                    f[i][j]|=f[i-1][j-1]
                else:
                    if p[j]=='*':
                        f[i][j]|=f[i][j-2]
                        if matches(i,j-1):
                            f[i][j]|=f[i-1][j]
        #print(f)
        return f[lens-1][lenp-1]
                
        