class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        cnt1=Counter(s)
        cnt2=Counter(target)
        ans=2**31
        for l in cnt2:
            if l not in cnt1:
                return 0
            ans=min(ans,cnt1[l]//cnt2[l])
        return ans
        
