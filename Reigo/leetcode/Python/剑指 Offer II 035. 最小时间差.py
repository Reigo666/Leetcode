class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def solve(s):
            hh=s[0:2]
            mm=s[-2:]
            return int(hh)*60+int(mm)
        
        for i in range(len(timePoints)):
            timePoints[i]=solve(timePoints[i])
            if timePoints[i]<=12*60:
                timePoints.append(timePoints[i]+24*60)
        
        timePoints.sort()
        ans=24*60+1
        for i in range(1,len(timePoints)):
            ans=min(ans,timePoints[i]-timePoints[i-1])
            if ans==0:
                return ans
        return ans