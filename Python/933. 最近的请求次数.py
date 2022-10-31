import collections
from typing import  List,Optional
import copy
class RecentCounter:

    def __init__(self):
        self.pinglist=collections.deque([])

    def ping(self, t: int) -> int:
        self.pinglist.append(t)
        lnum=t-3000
        while self.pinglist:
            if self.pinglist[0]>=lnum:
                break
            else:
                self.pinglist.popleft()
        return len(self.pinglist)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)