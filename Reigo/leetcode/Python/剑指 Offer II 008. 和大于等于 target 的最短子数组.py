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