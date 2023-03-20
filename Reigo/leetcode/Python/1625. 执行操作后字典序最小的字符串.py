class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        vis={s}
        ans=s

        q=deque([s])
        while q:
            t=q.popleft()
            t1=list(t)
            for i in range(1,len(s),2):
                t1[i]=str((int(t1[i])+a)%10)
            t1=''.join(t1)
            t2=t[-b:]+t[:-b]

            for tt in (t1,t2):
                if tt not in vis:
                    vis.add(tt)
                    q.append(tt)

                    if tt<ans:
                        ans=tt
        
        return ans
        