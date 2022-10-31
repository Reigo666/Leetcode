import collections
from typing import  List,Optional
import copy
from itertools import pairwise
class Solution:
    #words = ["wrt","wrf","er","ett","rftt"]
    def alienOrder(self, words: List[str]) -> str:
        g = {}
        #初始化时给words[0]中所有字母初始化为空
        for c in words[0]:
            g[c] = []
        #pairwise即指words中相邻两单词组成一个元组的迭代器
        for s, t in pairwise(words):
            #每次初始化t中的未初始化的字母，这样和最初words[0]相加，即为所有的字母
            for c in t:
                g.setdefault(c, [])
            #每次比较s和t中的首字母，用zip打包成元组的形式，更容易比较
            for u, v in zip(s, t):
                if u != v:
                    g[u].append(v)
                    break
            else:
                if len(s) > len(t):
                    return ""

        VISITING, VISITED = 1, 2
        states = {}
        order = []
        def dfs(u: str) -> bool:
            states[u] = VISITING
            for v in g[u]:
                if v not in states:
                    if not dfs(v):
                        return False
                elif states[v] == VISITING:
                    return False
            order.append(u)
            states[u] = VISITED
            return True

        return ''.join(reversed(order)) if all(dfs(u) for u in g if u not in states) else ""

sol=Solution()
words = ["wrt","wrf","er","ett","rftt"]
words1=["wrt","wrf","wrg"]
words2=["abc","ac"]
words3=["ab","a"]
print(sol.alienOrder(words1))