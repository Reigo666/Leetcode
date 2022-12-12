import collections
from typing import  List,Optional
import copy
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bfs = collections.deque()
        bfs.append((start, 0))
        bankset = set(bank)
        if start in bank:
            bankset.remove(start)
        while bfs:
            gene, step = bfs.popleft()
            if gene == end:
                return step
            for i in range(len(gene)):
                for x in "ACGT":
                    newGene = gene[:i] + x + gene[i+1:]
                    if newGene in bankset:
                        bfs.append((newGene, step + 1))
                        bankset.remove(newGene)
        return -1


start="AACCGGTT"
end="AAACGGTA"
bank=["AACCGATT","AACCGATA","AAACGATA","AAACGGTA"]     

sol=Solution()
print(sol.minMutation(start,end,bank))        