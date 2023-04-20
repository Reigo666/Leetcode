class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        months=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        prefix=[0]
        for i in range(11):
            prefix.append(prefix[-1]+months[i])
        def solve(str):
            mm=int(str[0:2])-1
            dd=int(str[-2:])
            return prefix[mm]+dd
        
        a1=solve(arriveAlice)
        a2=solve(leaveAlice)
        b1=solve(arriveBob)
        b2=solve(leaveBob)

        #print(a1,a2,b1,b2)
        if a2<b1 or a1>b2:
            return 0
        return min(a2,b2)-max(a1,b1)+1
