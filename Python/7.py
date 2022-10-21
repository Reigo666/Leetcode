from math import inf
class StockSpanner:
    def __init__(self):
        self.stack = [(-1, inf)]
        self.idx = -1

    def next(self, price: int) -> int:
        self.idx += 1
        while price >= self.stack[-1][1]:
            self.stack.pop()
        self.stack.append((self.idx, price))
        return self.idx - self.stack[-2][0]
        
S = StockSpanner()
print(S.next(100))
print(S.next(80)) 
print(S.next(60))  
print(S.next(70)) 
print(S.next(60)) 
print(S.next(75)) 
print(S.next(85))

