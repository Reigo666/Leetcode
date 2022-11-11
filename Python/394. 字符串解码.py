class Solution:
    def decodeString(self, str: str) -> str:
        s=[]
        l=0
        while l<len(str):
            if str[l].isdigit():
                num=str[l]
                l+=1
                while str[l].isdigit():
                    num+=str[l]
                    l+=1
                num=int(num)
                cnt=1
                l+=1
                ll=l
                while cnt:
                    if str[l]=='[':
                        cnt+=1
                    elif str[l]==']':
                        cnt-=1
                    l+=1
                rr=l-1
                instr=self.decodeString(str[ll:rr])
                s.append(num*instr)
            else:
                s.append(str[l])
                l+=1
        return "".join(s)
        