class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        arr=[0]*60
        ans=0
        for t in time:
            mod=t%60
            if mod==0:
                ans+=arr[mod]
            else:
                ans+=arr[60-mod]
            arr[mod]+=1
        return ans