class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        def checkDiff(a,b):
            diff=0
            for i in range(len(a)):
                if a[i]!=b[i]:
                    diff+=1
            return diff
        ans=[]
        for q in queries:
            for d in dictionary:
                if checkDiff(q,d)<=2:
                    ans.append(q)
                    break
        return ans