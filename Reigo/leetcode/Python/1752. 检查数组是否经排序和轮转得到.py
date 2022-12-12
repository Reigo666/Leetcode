class Solution:
    def check(self, nums: List[int]) -> bool:
        l=1

        premin=nums[0]
        while l<len(nums):
            while l<len(nums) and nums[l]>=nums[l-1]:
                l+=1
            #print(l,len(nums))
            if l==len(nums):
                return True
            
            while l<len(nums)-1 and nums[l]<=premin and nums[l]<=nums[l+1]:
                l+=1
            
            if l!=len(nums)-1:
                return False
            
            if nums[l]>premin:
                return False
            
            return True
        return True