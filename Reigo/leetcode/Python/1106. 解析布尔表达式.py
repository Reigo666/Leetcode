class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        oplist=[]
        boollist=[]

        def solveExpression(s):
            #print(s)
            if s=='t' or s=='f':
                return s
            op=s[0]
            l=2
            tnum=0
            fnum=0
            while l<len(s)-1:
                if s[l]=='|' or s[l]=='&' or s[l]=='!':
                    ll=l
                    cnt=1
                    l+=2
                    while l<len(s)-1:
                        if s[l]=='(':
                            cnt+=1
                        elif s[l]==')':
                            cnt-=1
                        if cnt==0:
                            break
                        l+=1
                    #print(ll,l,"!!")
                    if solveExpression(s[ll:l+1])=='t':
                        tnum+=1
                    else:
                        fnum+=1
                elif s[l]=='t':
                    tnum+=1
                elif s[l]=='f':
                    fnum+=1
                if op=='|':
                    if tnum>=1:
                        return 't'
                elif op=='&':
                    if fnum>=1:
                        return 'f'
                l+=1
            if op=='&':
                return 't'
            elif op=='|':
                return 'f'
            elif op=='!':
                if tnum:
                    return 'f'
                else:
                    return 't'
            else:
                print("WTF")
                return "WTF"
        if solveExpression(expression)=='t':
            return True
        else:
            return False