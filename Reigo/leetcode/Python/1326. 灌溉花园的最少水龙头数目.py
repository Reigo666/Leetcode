class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        arr=[]
        for i in range(n+1):
            s=i-ranges[i]
            e=i+ranges[i]
            arr.append([s,e])

        arr.sort()

        epoint=0
        ans=0

        ii=0
        while ii<n+1 and epoint<n:
            findone=False
            newend=-1
            while ii<n+1 and arr[ii][0]<=epoint:
                findone=True
                newend=max(newend,arr[ii][1])
                ii+=1
            if not findone:
                return -1
            ans+=1
            epoint=newend
        return ans
