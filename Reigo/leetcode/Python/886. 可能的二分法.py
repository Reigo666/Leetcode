class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        g=[[] for _ in range(n+1)]

        for ds in dislikes:
            a,b=ds
            g[a].append(b)
            g[b].append(a)
        
        print(g)
        color=[0]*(n+1)
        def dfs(u,c):
            color[u]=c

            for k in g[u]:
                if color[k]!=0:
                    if color[k]==c:
                        return False
                else:
                    if not dfs(k,3-c):
                        return False
            return True
        for i in range(1,n):
            if color[i]==0:
                if not dfs(i,1):
                    return False
            #print(color)
        return True

        
