class MyCalendar:

    def __init__(self):
        self.c=[]

    def book(self, start: int, end: int) -> bool:
        if not self.c:
            self.c.append([start,end])
            return True
        else:
            for i in range(len(self.c)):
                if start>=self.c[i][0] and start<self.c[i][1]:
                    return False
                if end>self.c[i][0] and end<=self.c[i][1]:
                    return False
                if start<=self.c[i][0] and end>=self.c[i][1]:
                    return False
            self.c.append([start,end])
            #print(self.c)
            return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)