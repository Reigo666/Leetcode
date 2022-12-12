class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)<len(s1):
            return False
        cnt=Counter(s1)
        #print(cnt)

        l=0
        r=len(s1)
        need=set(cnt)
        for i in range(len(s1)):
            if s2[i] in cnt:
                cnt[s2[i]]-=1
                if cnt[s2[i]]==0:
                    need.remove(s2[i])
        if len(need)==0:
            return True

        while r<len(s2):
            if s2[r] in cnt:
                cnt[s2[r]]-=1
                if cnt[s2[r]]==0:
                    need.remove(s2[r])
            if s2[l] in cnt:
                cnt[s2[l]]+=1
                if cnt[s2[l]]==1:
                    need.add(s2[l])
            l+=1
            r+=1
            if len(need)==0:
                return True
        return False