class Solution:
    def secondHighest(self, s: str) -> int:
        first=-1
        second=-1
        for l in s:
            if l.isdigit():
                l=int(l)
                if l>first:
                    second=first
                    first=l
                elif l<first and l>second:
                    second=l
        
        return second
