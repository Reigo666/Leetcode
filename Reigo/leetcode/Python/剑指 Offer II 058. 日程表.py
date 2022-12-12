
class MyCalendar:

    def __init__(self):
        self.booked=[]

    def book(self, start: int, end: int) -> bool:
        idx=bisect.bisect_left(self.booked,end,key=lambda x:x[0])
        if idx==0 or start>=self.booked[idx-1][1]:
            self.booked.insert(idx,[start,end])
            return True
        return False



# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)