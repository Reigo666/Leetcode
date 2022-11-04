class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l=0
        r=0
        mult=1
        ans=0
        for i in range(len(nums)):
            r=i
            mult*=nums[r]
            while l<len(nums) and mult>=k:
                mult//=nums[l]
                l+=1
            if r>=l:
                ans+=r-l+1
        return ans
                