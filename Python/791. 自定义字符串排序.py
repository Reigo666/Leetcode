class Solution:
    def customSortString(self, order: str, s: str) -> str:
        a=25
        dict=defaultdict(int)
        for l in order:
            dict[l]-=a
            a-=1
        
        sl=list(s)
        sl.sort(key=lambda x:dict[x])

        return "".join(sl)