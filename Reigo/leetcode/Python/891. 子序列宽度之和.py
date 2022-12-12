class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        nums.sort()
        __MOD__=10**9+7
        ans=0
        n=len(nums)
        pow2=[0]*n
        pow2[0]=1
        for i in range(1,n):
            pow2[i]=pow2[i-1]*2%__MOD__
        for i in range(n):
            ans=(ans+(pow2[i]-pow2[n-i-1])*nums[i])%__MOD__

        return ans