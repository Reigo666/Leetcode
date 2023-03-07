class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        
        # print(type(set()))
        # print(isinstance(set(),set))
        #print('a'.isalpha())
        def setMultiply(a,b):
            c=set()
            for str1 in a:
                for str2 in b:
                    c.add(str1+str2)
            return c
        
        s=[]
        
        for ch in expression:
            if ch=='{' or ch==',':
                s.append(ch)
            elif ch=='}':
                temp=set()
                while s and s[-1]!='{':
                    top=s.pop()
                    #top是集合
                    if top!=',':
                        temp|=top
                #消除左大括号
                s.pop()
                if s and isinstance(s[-1],set):
                    top=s.pop()
                    temp=setMultiply(top,temp)
                s.append(temp)

            else:#'a'
                temp=set()
                temp.add(ch)
                if s and isinstance(s[-1],set):
                    top=s.pop()
                    temp=setMultiply(top,temp)
                s.append(temp)
        #print(s)
        return sorted(list(s[-1]))