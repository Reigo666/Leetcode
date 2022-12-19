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