class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans=[]

        cur=[]
        def check(s):
            if len(s)>3:
                return False
            if len(s)==1:
                return True
            else:
                if s[0]=='0':
                    return False
                if int(s)<=255:
                    return True
                return False

        def backTrack(i):
            if len(cur)>4:
                return
            
            if i>=len(s):
                if len(cur)==4:
                    ans.append(".".join(cur))
                return
            
            else:
                for j in range(i,min(i+3,len(s))):
                    if check(s[i:j+1]):
                        cur.append(s[i:j+1])
                        backTrack(j+1)
                        cur.pop()
        
        backTrack(0)
        return ans