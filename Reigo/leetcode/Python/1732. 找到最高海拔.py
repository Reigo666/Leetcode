class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans=0
        presum=0
        for num in gain:
            presum+=num
            ans=max(ans,presum)
        return ans