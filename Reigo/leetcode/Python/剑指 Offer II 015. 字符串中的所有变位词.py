class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        cnt=Counter(p)
        #print(cnt)
        l=0
        r=0
        need=set(cnt)
        ans=[]
        while r<len(s):
            if s[r] in cnt:
                cnt[s[r]]-=1
                if cnt[s[r]]==0:
                    need.remove(s[r])
            r+=1

            while r-l>len(p):
                if s[l] in cnt:
                    cnt[s[l]]+=1
                    if cnt[s[l]]==1:
                        need.add(s[l])
                l+=1
            
            if len(need)==0:
                ans.append(l)
            
        
        return ans