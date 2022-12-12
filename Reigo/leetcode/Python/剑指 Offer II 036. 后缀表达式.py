class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s=[]
        for token in tokens:
            if token=="+" or token=='-' or token=='*' or token=='/':
                t1=s.pop()
                t2=s.pop()
                if token=='+':
                    s.append(t1+t2)
                if token=='-':
                    s.append(t2-t1)
                if token=='*':
                    s.append(t1*t2)
                if token=='/':
                    rev=False
                    if t1<0:
                        rev=not rev
                        t1=-t1
                    if t2<0:
                        rev=not rev
                        t2=-t2
                    temp=t2//t1
                    if rev:
                        temp=-temp
                    s.append(temp)
            else:
                s.append(int(token))
            #print(s)
        return s[0]
