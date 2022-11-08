class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l=0
        r=0

        cnt=Counter(t)
        need=set(cnt)
        ans=len(s)+3
        ansl=-1
        ansr=-1
        while r<len(s):
            if s[r] in cnt:
                cnt[s[r]]-=1
                if cnt[s[r]]==0:
                    need.remove(s[r])
            
            while len(need)==0:
                if r-l+1<ans:
                    ansl=l
                    ansr=r
                    ans=r-l+1
                
                if s[l] in cnt:
                    cnt[s[l]]+=1
                    if cnt[s[l]]==1:
                        need.add(s[l])
                l+=1
            r+=1
        
        return s[ansl:ansr+1]
