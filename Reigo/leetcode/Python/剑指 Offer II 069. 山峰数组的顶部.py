class Solution:
    def peakIndexInMountainArray(self, nums: List[int]) -> int:
        l=0
        r=len(nums)

        while l<r:
            mid=(l+r)//2

            if nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
                return mid
            if nums[mid]>nums[mid+1]:
                r=mid-1
            elif nums[mid]<nums[mid+1]:
                l=mid+1
        
        return l