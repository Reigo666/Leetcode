class Solution:
    def countSubstrings(self, s: str) -> int:
        ans=0
        q=deque([])
        for i in range(len(s)-1):
            q.append([i,i])
            if s[i]==s[i+1]:
                q.append([i,i+1])
        q.append([len(s)-1,len(s)-1])
        

        while q:
            ans+=len(q)
            #print(q)
            for i in range(len(q)):
                l,r=q.popleft()
                if l==0 or r==len(s)-1:
                    continue
                if s[l-1]==s[r+1]:
                    q.append([l-1,r+1])
        return ans
        
