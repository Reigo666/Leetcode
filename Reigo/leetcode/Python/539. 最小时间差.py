class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def solve(s):
            hh=s[0:2]
            mm=s[-2:]
            return int(hh)*60+int(mm)
        
        h24=24*60
        for i in range(len(timePoints)):
            timePoints[i]=solve(timePoints[i])
            if timePoints[i]<720:
                timePoints.append(timePoints[i]+1440)
        timePoints.sort()
        ans=1441
        for i in range(1,len(timePoints)):
            ans=min(ans,timePoints[i]-timePoints[i-1])
            if ans==0:
                return 0
        return ans
