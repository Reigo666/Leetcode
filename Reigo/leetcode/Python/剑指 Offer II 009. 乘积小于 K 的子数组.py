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
    

    def numSubarrayProductLessThanK1(self, nums: List[int], k: int) -> int:
        l=0
        r=0
        mult=1
        ans=0

        while r<len(nums):
            mult*=nums[r]
            r+=1
            while l<r and mult>=k:
                mult//=nums[l]
                l+=1
            
            if mult<k:
                ans+=r-l
            #print(l,r