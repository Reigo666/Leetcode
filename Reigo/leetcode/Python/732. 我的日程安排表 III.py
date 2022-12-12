class MyCalendarThree:

    def __init__(self):
        self.c=[]

    def book(self, start: int, end: int) -> int:
        self.c.append([start,end])
        self.c=sorted(self.c,key=lambda x: (x[0],x[1]))
        temp=1
        maxans=1
        for i in range(1,len(self.c)):
            ln=self.c[i][0]
            temp=1
            for j in range(0,i):
                if ln>=self.c[j][0] and ln<self.c[j][1]:
                    temp+=1
            maxans=max(maxans,temp)
        self.c=sorted(self.c,key=lambda x: (x[1],x[0]))
        for i in range(0,len(self.c)-1):
            rn=self.c[i][1]
            temp=1
            for j in range(i+1,len(self.c)):
                if rn>self.c[j][0] and rn<=self.c[j][1]:
                    temp+=1
            maxans=max(maxans,temp)
        return maxans

obj = MyCalendarThree()
a=[[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
for i in range(1,len(a)):
    param_1 = obj.book(a[i][0],a[i][1])
    print(param_1)
