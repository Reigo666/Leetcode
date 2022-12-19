class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sum1=0
        l=0
        r=0
        ans=len(nums)+1
        for i in range(len(nums)):
            sum1+=nums[i]
            r=i
            while l<len(nums) and sum1>=target:
                ans=min(ans,r-l+1)
                sum1-=nums[l]
                l+=1
        if ans==len(nums)+1:
            return 0
        return ans
    
    def minSubArrayLen1(self, target: int, nums: List[int]) -> int:
        l=0
        r=0
        sum1=0
        ans=len(nums)+1
        while r<len(nums):
            sum1+=nums[r]
            r+=1
            while sum1>=target:
                ans=min(ans,r-l)
                sum1-=nums[l]
                l+=1
        if ans==len(nums)+1:
            ans=0
        return ans