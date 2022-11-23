class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        def solve(x):
            sum1=0
            while x:
                sum1+=x%10
                x//=10
            return sum1
        maxnum=-1
        maxidx=-1
        dict=defaultdict(int)
        for i in range(lowLimit,highLimit+1):
            boxidx=solve(i)
            dict[boxidx]+=1

            if dict[boxidx]>maxnum:
                maxidx=boxidx
                maxnum=dict[boxidx]
        
        return maxnum
        
