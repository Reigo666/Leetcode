class Solution:
    def soupServings(self, n: int) -> float:
        dict={}

        def dfs(la,lb):
            if (la,lb) in dict:
                return dict[(la,lb)]
            if la<=0 and lb<=0:
                return 0.5
            if la<=0:
                return 1
            if lb<=0:
                return 0
            p1=dfs(la-100,lb)
            p2=dfs(la-75,lb-25)
            p3=dfs(la-50,lb-50)
            p4=dfs(la-25,lb-75)
            dict[(la,lb)]=0.25*(p1+p2+p3+p4)
            return 0.25*(p1+p2+p3+p4)
        if n>=5000:
            return 1
        return dfs(n,n)