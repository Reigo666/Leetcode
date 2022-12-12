class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.sum=0
        self.cap=size
        self.q=deque([])

    def next(self, val: int) -> float:
        q=self.q
        if len(q)<self.cap:
            self.sum+=val
            q.append(val)
        else:
            self.sum+=val
            self.sum-=q.popleft()
            q.append(val)
        return self.sum/len(q)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)