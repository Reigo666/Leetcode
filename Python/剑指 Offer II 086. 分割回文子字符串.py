class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n=len(s)
        f=[[False]*n for _ in range(n)]

        for j in range(n):
            for i in range(j,-1,-1):
                if i==j:
                    f[i][j]=True
                else:
                    if s[i]==s[j]:
                        if i+1==j:
                            f[i][j]=True
                        elif f[i+1][j-1]:
                            f[i][j]=True
        
        temp=[]
        ans=[]
        def backTrack(i):
            if i==len(s):
                ans.append(temp[:])
            for j in range(i,len(s)):
                if f[i][j]:
                    temp.append(s[i:j+1])
                    backTrack(j+1)
                    temp.pop()

        backTrack(0)
        return ans

                        
            