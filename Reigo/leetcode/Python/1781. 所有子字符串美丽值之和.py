class Solution:
    def beautySum(self, s: str) -> int:
        ans=0
        for i in range(len(s)):
            ma=0
            mi=inf
            cnt=Counter()
            for j in range(i,len(s)):
                cnt[s[j]]+=1
                ma=max(ma,cnt[s[j]])
                mi=min(cnt.values())
                ans+=ma-mi
                #print(ans,ma,mi)
        return ans