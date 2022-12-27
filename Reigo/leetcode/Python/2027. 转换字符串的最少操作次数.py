class Solution:
    def minimumMoves(self, s: str) -> int:
        l=0
        ans=0
        while l<len(s):
            if s[l]=="X":
                l+=2
                ans+=1
            l+=1
        return ans
        