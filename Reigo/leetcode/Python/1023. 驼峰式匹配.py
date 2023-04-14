class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:

        def matchOne(str,pattern):
            l=0
            for p in pattern:
                match=False
                while l<len(str):
                    if str[l]==p:
                        match=True
                        l+=1
                        break
                    if str[l]>='A' and str[l]<='Z':
                        return False
                    l+=1
                if not match:
                    return False
            while l<len(str):
                if str[l]>='A' and str[l]<='Z':
                    return False
                l+=1
            return True

        ans=[]
        for q in queries:
            ans.append(matchOne(q,pattern))
        
        return ans
        