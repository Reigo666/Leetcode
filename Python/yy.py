from typing import List
class Solution:
    def possibleBipartition(self, n: int, ds: List[List[int]]) -> bool:
        N, M = 2010, 20010
        he, e, ne, color = [-1] * N, [0] * M, [0] * M, [0] * N
        idx = 0
        def add(a, b):
            nonlocal idx
            e[idx], ne[idx], he[a] = b, he[a], idx
            idx += 1
        def dfs(u, cur):
            color[u] = cur
            i = he[u]
            while i != -1:
                j = e[i]
                if color[j] == cur:
                    return False
                if color[j] == 0 and not dfs(j, 3 - cur):
                    return False
                i = ne[i]
            return True
        for info in ds:
            a, b = info[0], info[1]
            add(a, b)
            add(b, a)
        for i in range(1, n + 1):
            if color[i] != 0:
                continue
            if not dfs(i, 1):
                return False
        return True
sol=Solution()
n = 4
dislikes = [[1,2],[1,3],[2,4]]
print(sol.possibleBipartition(n,dislikes))