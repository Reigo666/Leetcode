class MinStack:
    stack=[]
    minval=None
    def __init__(self):
        self.stack=[]
        self.minval=None

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minval==None:
            self.minval=val
        else:
            if val<self.minval:
                self.minval=val
    def pop(self) -> None:
        val=self.stack.pop()
        if self.minval==val:
            n=len(self.stack)
            if n==0:
                self.minval=None
                return
            minval=self.stack[0]
            for i in range(1,n):
                minval=min(minval,self.stack[i])
            self.minval=minval
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minval



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()