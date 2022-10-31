class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans=0
        for s in columnTitle:
            ans*=26
            ans+=ord(s)-ord('A')+1
        return ans