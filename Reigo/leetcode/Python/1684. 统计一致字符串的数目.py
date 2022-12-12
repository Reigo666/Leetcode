class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        seen=set(allowed)
        ans=0
        for word in words:
            flag=True
            for l in word:
                if l not in seen:
                    flag=False
                    break
            if flag:
                ans+=1
        return ans