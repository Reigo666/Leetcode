class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        g=defaultdict(list)
        for e in edges:
            s,t=e
            g[s].append(t)
            g[t].append(s)
        
        seen=set()
        def dfs(src):
            if src==destination:
                return True

            for i in range(len(g[src])):
                if g[src][i] not in seen:
                    seen.add(g[src][i])
                    if dfs(g[src][i]):
                        return True
            
            return False
        return dfs(source)

    # 并查集
    def validPath1(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        fa=[0]*n
        for i in range(len(fa)):
            fa[i]=i
        
        def find(x):
            if fa[x]!=x:
                fa[x]=find(fa[x])
            return fa[x]
        for e in edges:
            s,t=e
            fa[find(s)]=find(t)

        return find(source)==find(destination)