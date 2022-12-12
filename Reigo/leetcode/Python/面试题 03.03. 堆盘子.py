class StackOfPlates:

    def __init__(self, cap: int):
        self.stack=[]
        self.cap=cap

    def push(self, val: int) -> None:
        if self.cap==0:
            return
        cap=self.cap
        stack=self.stack
        if stack:
            if len(stack[-1])<cap:
                stack[-1].append(val)
            else:
                stack.append([val])
        else:
            stack.append([val])
        

    def pop(self) -> int:
        stack=self.stack
        #cap=self.cap
        if len(stack):
            res=stack[-1].pop()
            if len(stack[-1])==0:
                del stack[-1]
        else:
            res=-1
        return res
            

    def popAt(self, index: int) -> int:
        stack=self.stack
        if index>=len(stack):
            return -1
        res=stack[index].pop()
        if len(stack[index])==0:
            del stack[index]
        return res


# Your StackOfPlates object will be instantiated and called as such:
# obj = StackOfPlates(cap)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAt(index)