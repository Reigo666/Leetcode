from sortedcontainers import SortedList
class ExamRoom:

    def __init__(self, n: int):
        self.sl=SortedList()
        self.n=n

    def seat(self) -> int:
        sl=self.sl
        if len(sl)==0:
            sl.add(0)
            return 0
        
        diff,idx=sl[0],0

        for x,y in pairwise(sl):
            if (y-x)//2>diff:
                idx=x+(y-x)//2
                diff=(y-x)//2
        
        if self.n-1-sl[-1]>diff:
            idx=self.n-1
        
        sl.add(idx)
        return idx



    def leave(self, p: int) -> None:
        self.sl.remove(p)

# from sortedcontainers import SortedList


# class ExamRoom:

#     def __init__(self, n: int):
#         self.sl = SortedList()  # 表示已分配的座位号（有序）
#         self.n = n

#     def seat(self) -> int:
#         # 1. 当 sl 为空时，即还没有分配座位时，分配 0 号座位
#         if not self.sl:
#             self.sl.add(0)
#             return 0

#         diff, idx = self.sl[0], 0

#         # 2.2 分配两个座位号 sl[i] 和 sl[i + 1] 之间的座位的情况：
#         #   sl[i] + (sl[i + 1] - sl[i]) // 2
#         for x, y in pairwise(self.sl):
#             if (y - x) // 2 > diff:
#                 diff = (y - x) // 2
#                 idx = x + (y - x) // 2

#         # 2.3 分配最后一个座位号 n - 1 的情况
#         if self.n - 1 - self.sl[-1] > diff:
#             diff = self.n - 1 - self.sl[-1]
#             idx = self.n - 1

#         self.sl.add(idx)
#         return idx

#     def leave(self, p: int) -> None:
#         self.sl.remove(p)


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)