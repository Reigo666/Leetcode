class RecentCounter:

    def __init__(self):
        self.q=deque([])

    def ping(self, t: int) -> int:
        q=self.q
        while q and t-q[0]>3000:
            q.popleft()
        q.append(t)
        return len(q)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)