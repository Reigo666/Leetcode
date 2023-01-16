class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        dict={}
        for kn in knowledge:
            k,v=kn
            dict[k]=v

        ans=""
        r=0
        while r<len(s):
            if s[r]!='(':
                ans+=s[r]
            else:
                templ=r
                while s[r]!=')':
                    r+=1
                if s[templ+1:r] in dict:
                    ans+=dict[s[templ+1:r]]
                else:
                    ans+='?'
            r+=1
        return ans
