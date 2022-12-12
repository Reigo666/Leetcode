class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:

        def changeToGroup(s):
            ret=[]
            l=0
            while l<len(s):
                cur=s[l]
                cnt=1
                l+=1
                while l<len(s) and s[l]==cur:
                    cnt+=1
                    l+=1
                ret.append([cur,cnt])
            return ret

        a=changeToGroup(s)
        ans=0
        for word in words:
            b=changeToGroup(word)
            isValid=True
            if len(a)!=len(b):
                continue
            for i in range(len(a)):
                if a[i][0]!=b[i][0]:
                    isValid=False
                    break
                if a[i][1]!=b[i][1]:
                    if a[i][1]<b[i][1]:
                        isValid=False
                        break
                    elif a[i][1]>b[i][1]:
                        if a[i][1]==2:
                            isValid=False
                            break
            if isValid:
                ans+=1
        return ans