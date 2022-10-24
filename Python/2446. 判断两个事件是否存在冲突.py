class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        def solve(s):
            return int(s[0:2])*60+int(s[-2:])
        a=solve(event1[0])
        b=solve(event1[1])
        c=solve(event2[0])
        d=solve(event2[1])

        if b<c or d<a:
            return False
        return True